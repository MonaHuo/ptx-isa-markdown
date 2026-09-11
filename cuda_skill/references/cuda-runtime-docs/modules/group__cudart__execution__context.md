<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/group__CUDART__EXECUTION__CONTEXT.html

#  6.16. Execution Context Management

This section describes the execution context management functions of the CUDA runtime application programming interface.

##  6.16.1. Overview

A CUDA execution context cudaExecutionContext_t serves as an abstraction for the contexts exposed by the CUDA Runtime, specifically green contexts and the primary context, and provides a unified programming model and API interface for contexts in the Runtime.

There are two primary ways today to obtain an execution context:

  * cudaDeviceGetExecutionCtx: Returns the execution context that corresponds to the primary context of the specified device.

  * cudaGreenCtxCreate: Creates a green context with the specified resources and returns an execution context.

Once you have an execution context at hand, you can perform context-level operations via the CUDA Runtime APIs. This includes:

  * Submitting work via streams created with cudaExecutionCtxStreamCreate.

  * Querying context via cudaExecutionCtxGetDevResource, cudaExecutionCtxGetDevice, etc.

  * Synchronizing and tracking context-level operations via cudaExecutionCtxSynchronize, cudaExecutionCtxRecordEvent, cudaExecutionCtxWaitEvent.

  * Performing context-level graph node operations via cudaGraphAddNode by specifying the context in `nodeParams`. Note that individual node creation APIs, such as cudaGraphAddKernelNode, do not support specifying an execution context.

Note: The above APIs take in an explicit cudaExecutionContext_t handle and ignores the context that is current to the calling thread. This enables explicit context-based programming without relying on thread-local state. If no context is specified, the APIs return cudaErrorInvalidValue.

Note: Developers should treat cudaExecutionContext_t as an opaque handle and avoid assumptions about its underlying representation. The CUDA Runtime does not provide a way to convert this handle into driver-level contexts, such as ::CUcontext or ::CUgreenCtx.

##  6.16.2. Lifetime of CUDA Resources

The lifetime of CUDA resources (memory, streams, events, modules, etc) is not tied to the lifetime of the execution context. Their lifetime is tied to the device against which they were created. As such, usage of cudaDeviceReset() should be avoided to persist the lifetime of these resources.

##  6.16.3. APIs Operating on Current Context

The CUDA runtime does not provide a way to set an execution context as current. Since, the majority of the runtime APIs operate on the current context, we document below how the developer can work with these APIs.

###  6.16.3.1. APIs Operating on Device Resources

To work with these APIs (for example, cudaMalloc, cudaEventCreate, etc), developers are expected to call cudaSetDevice() prior to invoking them. Doing so does not impact functional correctness as these APIs operate on resources that are device-wide. If users have a context handle at hand, they can get the device handle from the context handle using cudaExecutionCtxGetDevice().

###  6.16.3.2. APIs Operating on Context Resources

These APIs (for example, cudaLaunchKernel, cudaMemcpyAsync, cudaMemsetAsync, etc) take in a stream and resources are inferred from the context bound to the stream at creation. See cudaExecutionCtxStreamCreate for more details. Developers are expected to use the stream-based APIs for context awareness and always pass an explicit stream handle to ensure context-awareness, and avoid reliance on the default NULL stream, which implicitly binds to the current context.

##  6.16.4. Green Contexts

Green contexts are a lightweight alternative to traditional contexts, that can be used to select a subset of device resources. This allows the developer to, for example, select SMs from distinct spatial partitions of the GPU and target them via CUDA stream operations, kernel launches, etc.

Here are the broad initial steps to follow to get started:

  * (1) Start with an initial set of resources. For SM resources, they can be fetched via cudaDeviceGetDevResource. In case of workqueues, a new configuration can be used or an existing one queried via the cudaDeviceGetDevResource API.

  * (2) Modify these resources by either partitioning them (in case of SMs) or changing the configuration (in case of workqueues). To partition SMs, we recommend cudaDevSmResourceSplit. Changing the workqueue configuration can be done directly in place.

  * (3) Finalize the specification of resources by creating a descriptor via cudaDevResourceGenerateDesc.

  * (4) Create a green context via cudaGreenCtxCreate. This provisions the resource, such as workqueues (until this step it was only a configuration specification).

  * (5) Create a stream via cudaExecutionCtxStreamCreate, and use it throughout your application.

**SMs**

There are two possible partition operations - with cudaDevSmResourceSplitByCount the partitions created have to follow default SM count granularity requirements, so it will often be rounded up and aligned to a default value. On the other hand, cudaDevSmResourceSplit is explicit and allows for creation of non-equal groups. It will not round up automatically - instead it is the developer’s responsibility to query and set the correct values. These requirements can be queried with cudaDeviceGetDevResource to determine the alignment granularity (sm.smCoscheduledAlignment). A general guideline on the default values for each compute architecture:

  * On Compute Architecture 7.X, 8.X, and all Tegra SoC:

    * The smCount must be a multiple of 2.

    * The alignment (and default value of coscheduledSmCount) is 2.

  * On Compute Architecture 9.0+:

    * The smCount must be a multiple of 8, or coscheduledSmCount if provided.

    * The alignment (and default value of coscheduledSmCount) is 8. While the maximum value for coscheduled SM count is 32 on all Compute Architecture 9.0+, it’s recommended to follow cluster size requirements. The portable cluster size and the max cluster size should be used in order to benefit from this co-scheduling.

**Workqueues**

For `cudaDevResourceTypeWorkqueueConfig`, the resource specifies the expected maximum number of concurrent stream-ordered workloads via the `wqConcurrencyLimit` field. The `sharingScope` field determines how workqueue resources are shared:

  * `cudaDevWorkqueueConfigScopeDeviceCtx:` Use all shared workqueue resources across all contexts (default driver behavior).

  * `cudaDevWorkqueueConfigScopeGreenCtxBalanced:` When possible, use non-overlapping workqueue resources with other balanced green contexts.

The maximum concurrency limit depends on ::CUDA_DEVICE_MAX_CONNECTIONS and can be queried from the device via cudaDeviceGetDevResource. Configurations may exceed this concurrency limit, but the driver will not guarantee that work submission remains non-overlapping.

For `cudaDevResourceTypeWorkqueue`, the resource represents a pre-existing workqueue that can be retrieved from existing execution contexts. This allows reusing workqueue resources across different execution contexts.

**On Concurrency**

Even if the green contexts have disjoint SM partitions, it is not guaranteed that the kernels launched in them will run concurrently or have forward progress guarantees. This is due to other resources that could cause a dependency. Using a combination of disjoint SMs and `cudaDevWorkqueueConfigScopeGreenCtxBalanced` workqueue configurations can provide the best chance of avoiding interference. More resources will be added in the future to provide stronger guarantees.

Additionally, there are two known scenarios, where its possible for the workload to run on more SMs than was provisioned (but never less).

  * On Volta+ MPS: When `CUDA_MPS_ACTIVE_THREAD_PERCENTAGE` is used, the set of SMs that are used for running kernels can be scaled up to the value of SMs used for the MPS client.

  * On Compute Architecture 9.x: When a module with dynamic parallelism (CDP) is loaded, all future kernels running under green contexts may use and share an additional set of 2 SMs.

**Memory Copy Operations**

Green context restrictions apply to memory copy operations only when the copy is performed using a green context. For cross-device copies, green context restrictions may not be applied.

##  6.16.5. Functions

`` __host__ cudaError_t cudaDevResourceGenerateDesc(cudaDevResourceDesc_t *phDesc, cudaDevResource *resources, unsigned int nbResources) ``

Generate a resource descriptor.

Generates a single resource descriptor with the set of resources specified in `resources`. The generated resource descriptor is necessary for the creation of green contexts via the cudaGreenCtxCreate API. Resources of the same type can be passed in, provided they meet the requirements as noted below.

A successful API call must have:

  * A valid output pointer for the `phDesc` descriptor as well as a valid array of `resources` pointers, with the array size passed in `nbResources`. If multiple resources are provided in `resources`, the device they came from must be the same, otherwise cudaErrorInvalidResourceConfiguration is returned. If multiple resources are provided in `resources` and they are of type cudaDevResourceTypeSm, they must be outputs (whether `result` or `remaining`) from the same split API instance and have the same smCoscheduledAlignment values, otherwise cudaErrorInvalidResourceConfiguration is returned.

Note: The API is not supported on 32-bit platforms.

See also

::cuDevResourceGenerateDesc, cudaDeviceGetDevResource, cudaExecutionCtxGetDevResource, cudaDevSmResourceSplit, cudaGreenCtxCreate

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **phDesc** – - Output descriptor

  * **resources** – - Array of resources to be included in the descriptor

  * **nbResources** – - Number of resources passed in `resources`

Returns

cudaSuccess, cudaErrorInvalidValue, cudaErrorNotPermitted, cudaErrorInvalidResourceType, cudaErrorInvalidResourceConfiguration, cudaErrorNotSupported, ::cudaErrorOutOfMemory, cudaErrorCudartUnloading, cudaErrorInitializationError

`` __host__ cudaError_t cudaDevSmResourceSplit(cudaDevResource *result, unsigned int nbGroups, const cudaDevResource *input, cudaDevResource *remainder, unsigned int flags, cudaDevSmResourceGroupParams *groupParams) ``

Splits a `cudaDevResourceTypeSm` resource into structured groups.

This API will split a resource of cudaDevResourceTypeSm into `nbGroups` structured device resource groups (the `result` array), as well as an optional `remainder`, according to a set of requirements specified in the `groupParams` array. The term “structured” is a trait that specifies the `result` has SMs that are co-scheduled together. This co-scheduling can be specified via the `coscheduledSmCount` field of the `groupParams` structure, while the `smCount` will specify how many SMs are required in total for that result. The remainder is always “unstructured”, it does not have any set guarantees with respect to co-scheduling and those properties will need to either be queried via the occupancy set of APIs or further split into structured groups by this API.

The API has a discovery mode for use cases where it is difficult to know ahead of time what the SM count should be. Discovery happens when the `smCount` field of a given `groupParams` array entry is set to 0 - the smCount will be filled in by the API with the derived SM count according to the provided `groupParams` fields and constraints. Discovery can be used with both a valid result array and with a NULL `result` pointer value. The latter is useful in situations where the smCount will end up being zero, which is an invalid value to create a result entry with, but allowed for discovery purposes when the `result` is NULL.

The `groupParams` array is evaluated from index 0 to `nbGroups` \- 1. For each index in the `groupParams` array, the API will evaluate which SMs may be a good fit based on constraints and assign those SMs to `result`. This evaluation order is important to consider when using discovery mode, as it helps discover the remaining SMs.

For a valid call:

  * `result` should point to a `cudaDevResource` array of size `nbGroups`, or alternatively, may be NULL, if the developer wishes for only the groupParams entries to be updated

  * `input` should be a valid cudaDevResourceTypeSm resource that originates from querying the execution context, or device.

  * The `remainder` group may be NULL.

  * There are no API `flags` at this time, so the value passed in should be 0.

  * A cudaDevSmResourceGroupParams array of size `nbGroups`. Each entry must be zero-initialized.

    * `smCount:` must be either 0 or in the range of [2,inputSmCount] where inputSmCount is the amount of SMs the `input` resource has. `smCount` must be a multiple of 2, as well as a multiple of `coscheduledSmCount`. When assigning SMs to a group (and if results are expected by having the `result` parameter set), `smCount` cannot end up with 0 or a value less than `coscheduledSmCount` otherwise cudaErrorInvalidResourceConfiguration will be returned.

    * `coscheduledSmCount:` allows grouping SMs together in order to be able to launch clusters on Compute Architecture 9.0+. The default value may be queried from the device’s cudaDevResourceTypeSm resource (8 on Compute Architecture 9.0+ and 2 otherwise). The maximum is 32 on Compute Architecture 9.0+ and 2 otherwise.

    * `preferredCoscheduledSmCount:` Attempts to merge `coscheduledSmCount` groups into larger groups, in order to make use of `preferredClusterDimensions` on Compute Architecture 10.0+. The default value is set to `coscheduledSmCount`.

    * `flags:`

      * `cudaDevSmResourceGroupBackfill:` Treats constraints as a hint, ignoring them if necessary to reach the requested `smCount`. Lets `smCount` be a non-multiple of `coscheduledSmCount`, filling the difference between SM count and already assigned co-scheduled groupings with other SMs. This lets any resulting group behave similar to the `remainder` group for example. When used with `cudaDevSmResourceGroupLocalityDomainId`, backfill fills up to the requested `smCount` using the target locality domain first, then SMs not attributed to any locality domain, then SMs from other locality domains. If no SMs can be found in the requested locality domain, cudaErrorInvalidResourceConfiguration is returned.

**Example params and their effect:**

A groupParams array element is defined in the following order:

```cpp
{ .smCount, .coscheduledSmCount, .preferredCoscheduledSmCount, .flags, \/\* .reserved \*\/ }
```

```cpp
// Example 1
// Will discover how many SMs there are, that are co-scheduled in groups of smCoscheduledAlignment.
// The rest is placed in the optional remainder.
cudaDevSmResourceGroupParams params { 0, 0, 0, 0 };
```

```cpp
// Example 2
// Assuming the device has 10+ SMs, the result will have 10 SMs that are co-scheduled in groups of 2 SMs.
// The rest is placed in the optional remainder.
cudaDevSmResourceGroupParams params { 10, 2, 0, 0};
// Setting the coscheduledSmCount to 2 guarantees that we can always have a valid result
// as long as the SM count is less than or equal to the input resource SM count.
```

```cpp
// Example 3
// A single piece is split-off, but instead of assigning the rest to the remainder, a second group contains everything else
// This assumes the device has 10+ SMs (8 of which are coscheduled in groups of 4),
// otherwise the second group could end up with 0 SMs, which is not allowed.
cudaDevSmResourceGroupParams params { {8, 4, 0, 0}, {0, 2, 0, cudaDevSmResourceGroupBackfill } }
```

The difference between a catch-all param group as the last entry and the remainder is in two aspects:

  * The remainder may be NULL / _TYPE_INVALID (if there are no SMs remaining), while a result group must always be valid.

  * The remainder does not have a structure, while the result group will always need to adhere to a structure of coscheduledSmCount (even if its just 2), and therefore must always have enough coscheduled SMs to cover that requirement (even with the `cudaDevSmResourceGroupBackfill` flag enabled).

Splitting an input into N groups, can be accomplished by repeatedly splitting off 1 group and re-splitting the remainder (a bisect operation). However, it’s recommended to accomplish this with a single call wherever possible.

See also

::cuDevSmResourceSplit, cudaDeviceGetDevResource, cudaExecutionCtxGetDevResource, cudaDevResourceGenerateDesc

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **result** – - Output array of `cudaDevResource` resources. Can be NULL, alongside an smCount of 0, for discovery purpose.

  * **nbGroups** – - Specifies the number of groups in `result` and `groupParams`

  * **input** – - Input SM resource to be split. Must be a valid `cudaDevResourceTypeSm` resource.

  * **remainder** – - If splitting the input resource leaves any SMs, the remainder is placed in here.

  * **flags** – - Flags specifying how the API should behave. The value should be 0 for now.

  * **groupParams** – - Description of how the SMs should be split and assigned to the corresponding result entry.

Returns

cudaSuccess, cudaErrorInvalidValue, cudaErrorNotPermitted, cudaErrorInvalidResourceType, cudaErrorInvalidResourceConfiguration, cudaErrorNotSupported, cudaErrorCudartUnloading, cudaErrorInitializationError

`` __host__ cudaError_t cudaDevSmResourceSplitByCount(cudaDevResource *result, unsigned int *nbGroups, const cudaDevResource *input, cudaDevResource *remaining, unsigned int flags, unsigned int minCount) ``

Splits `cudaDevResourceTypeSm` resources.

Splits `cudaDevResourceTypeSm` resources into `nbGroups`, adhering to the minimum SM count specified in `minCount` and the usage flags in `flags`. If `result` is NULL, the API simulates a split and provides the amount of groups that would be created in `nbGroups`. Otherwise, `nbGroups` must point to the amount of elements in `result` and on return, the API will overwrite `nbGroups` with the amount actually created. The groups are written to the array in `result`. `nbGroups` can be less than the total amount if a smaller number of groups is needed.

This API is used to spatially partition the input resource. The input resource needs to come from one of cudaDeviceGetDevResource, or cudaExecutionCtxGetDevResource. A limitation of the API is that the output results cannot be split again without first creating a descriptor and a green context with that descriptor.

When creating the groups, the API will take into account the performance and functional characteristics of the input resource, and guarantee a split that will create a disjoint set of symmetrical partitions. This may lead to fewer groups created than purely dividing the total SM count by the `minCount` due to cluster requirements or alignment and granularity requirements for the minCount. These requirements can be queried with cudaDeviceGetDevResource, or cudaExecutionCtxGetDevResource for cudaDevResourceTypeSm, using the `minSmPartitionSize` and `smCoscheduledAlignment` fields to determine minimum partition size and alignment granularity, respectively.

The `remainder` set does not have the same functional or performance guarantees as the groups in `result`. Its use should be carefully planned and future partitions of the `remainder` set are discouraged.

The following flags are supported:

  * `cudaDevSmResourceSplitIgnoreSmCoscheduling` : Lower the minimum SM count and alignment, and treat each SM independent of its hierarchy. This allows more fine grained partitions but at the cost of advanced features (such as large clusters on compute capability 9.0+).

  * `cudaDevSmResourceSplitMaxPotentialClusterSize` : Compute Capability 9.0+ only. Attempt to create groups that may allow for maximally sized thread clusters. This can be queried post green context creation using cudaOccupancyMaxPotentialClusterSize.

A successful API call must either have:

  * A valid array of `result` pointers of size passed in `nbGroups`, with `input` of type `cudaDevResourceTypeSm`. Value of `minCount` must be between 0 and the SM count specified in `input`. `remaining` may be NULL.

  * NULL passed in for `result`, with a valid integer pointer in `nbGroups` and `input` of type `cudaDevResourceTypeSm`. Value of `minCount` must be between 0 and the SM count specified in `input`. `remaining` may be NULL. This queries the number of groups that would be created by the API.

Note: The API is not supported on 32-bit platforms.

See also

::cuDevSmResourceSplitByCount, cudaDeviceGetDevResource, cudaExecutionCtxGetDevResource, cudaDevResourceGenerateDesc

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **result** – - Output array of `cudaDevResource` resources. Can be NULL to query the number of groups.

  * **nbGroups** – - This is a pointer, specifying the number of groups that would be or should be created as described below.

  * **input** – - Input SM resource to be split. Must be a valid `cudaDevSmResource` resource.

  * **remaining** – - If the input resource cannot be cleanly split among `nbGroups`, the remaining is placed in here. Can be ommitted (NULL) if the user does not need the remaining set.

  * **flags** – - Flags specifying how these partitions are used or which constraints to abide by when splitting the input. Zero is valid for default behavior.

  * **minCount** – - Minimum number of SMs required

Returns

cudaSuccess, cudaErrorInvalidValue, cudaErrorNotPermitted, cudaErrorInvalidResourceType, cudaErrorInvalidResourceConfiguration, cudaErrorNotSupported, cudaErrorCudartUnloading, cudaErrorInitializationError

`` __host__ cudaError_t cudaDeviceGetDevResource(int device, cudaDevResource *resource, enum cudaDevResourceType type) ``

Get device resources.

Get the `type` resources available to the `device`. This may often be the starting point for further partitioning or configuring of resources.

Note: The API is not supported on 32-bit platforms.

See also

::cuDeviceGetDevResource, cudaExecutionCtxGetDevResource, cudaDevSmResourceSplit, cudaDevResourceGenerateDesc

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **device** – - Device to get resource for

  * **resource** – - Output pointer to a cudaDevResource structure

  * **type** – - Type of resource to retrieve

Returns

cudaSuccess, cudaErrorInvalidValue, cudaErrorNotPermitted, cudaErrorInvalidDevice, cudaErrorInvalidResourceType, cudaErrorNotSupported, cudaErrorCudartUnloading, cudaErrorInitializationError

`` __host__ cudaError_t cudaDeviceGetExecutionCtx(cudaExecutionContext_t *ctx, int device) ``

Returns the execution context for a device.

Returns in `ctx` the execution context for the specified device. This is the device’s primary context. The returned context can then be passed to APIs that take in a cudaExecutionContext_t enabling explicit context-based programming without relying on thread-local state.

Passing the returned execution context to cudaExecutionCtxDestroy() is not allowed and will result in undefined behavior.

See also

cudaExecutionCtxGetDevice, cudaExecutionCtxGetId

Parameters

  * **ctx** – - Returns the device execution context

  * **device** – - Device to get the execution context for

Returns

cudaSuccess, cudaErrorInvalidValue, cudaErrorInvalidDevice

`` __host__ cudaError_t cudaExecutionCtxDestroy(cudaExecutionContext_t ctx) ``

Destroy a execution context.

Destroys the specified execution context `ctx`. It is the responsibility of the caller to ensure that no API call issues using `ctx` while cudaExecutionCtxDestroy() is executing or subsequently.

If `ctx` is a green context, any resources provisioned for it (that were initially available via the resource descriptor) are released as well.

The API does not destroy streams created via cudaExecutionCtxStreamCreate. Users are expected to destroy these streams explicitly using cudaStreamDestroy to avoid resource leaks. Once the execution context is destroyed, any subsequent API calls involving these streams will return cudaErrorStreamDetached with the exception of the following APIs:

  * cudaStreamDestroy. Note this is only supported on CUDA drivers 13.1 and above.

Additionally, the API will invalidate all active captures on these streams.

Passing in a `ctx` that was not explicitly created via CUDA Runtime APIs is not allowed and will result in undefined behavior.

See also

cudaGreenCtxCreate

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Note

The context parameter is required and the API ignores the context that is current to the calling thread. This enables explicit context-based programming without relying on thread-local state. If no context is specified, the API will return cudaErrorInvalidValue.

Parameters

**ctx** – - Execution context to destroy (required parameter, see note below)

Returns

cudaSuccess, cudaErrorInvalidValue, cudaErrorNotPermitted, cudaErrorCudartUnloading, cudaErrorInitializationError

`` __host__ cudaError_t cudaExecutionCtxGetDevResource(cudaExecutionContext_t ctx, cudaDevResource *resource, enum cudaDevResourceType type) ``

Get context resources.

Get the `type` resources available to context represented by `ctx`.

Note: The API is not supported on 32-bit platforms.

See also

cudaDeviceGetDevResource, cudaDevSmResourceSplit, cudaDevResourceGenerateDesc, cudaGreenCtxCreate

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Note

The context parameter is required and the API ignores the context that is current to the calling thread. This enables explicit context-based programming without relying on thread-local state. If no context is specified, the API will return cudaErrorInvalidValue.

Parameters

  * **ctx** – - Execution context to get resource for (required parameter, see note below)

  * **resource** – - Output pointer to a cudaDevResource structure

  * **type** – - Type of resource to retrieve

Returns

cudaSuccess, cudaErrorInvalidValue, cudaErrorNotSupported, cudaErrorNotPermitted, cudaErrorCudartUnloading, cudaErrorInitializationError

`` __host__ cudaError_t cudaExecutionCtxGetDevice(int *device, cudaExecutionContext_t ctx) ``

Returns the device handle for the execution context.

Returns in `*device` the handle of the specified execution context’s device. The execution context should not be NULL.

See also

cudaGreenCtxCreate, cudaExecutionCtxDestroy, ::cuCtxGetDevice

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Note

The context parameter is required and the API ignores the context that is current to the calling thread. This enables explicit context-based programming without relying on thread-local state. If no context is specified, the API will return cudaErrorInvalidValue.

Parameters

  * **device** – - Returned device handle for the specified execution context

  * **ctx** – - Execution context for which to obtain the device (required parameter, see note below)

Returns

cudaSuccess, cudaErrorCudartUnloading, cudaErrorInitializationError, cudaErrorInvalidValue, cudaErrorNotPermitted

`` __host__ cudaError_t cudaExecutionCtxGetId(cudaExecutionContext_t ctx, unsigned long long *ctxId) ``

Returns the unique Id associated with the execution context supplied.

Returns in `ctxId` the unique Id which is associated with a given context. The Id is unique for the life of the program for this instance of CUDA. The execution context should not be NULL.

See also

cudaGreenCtxCreate, cudaExecutionCtxDestroy, cudaExecutionCtxGetDevice, ::cuCtxGetId

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Note

The context parameter is required and the API ignores the context that is current to the calling thread. This enables explicit context-based programming without relying on thread-local state. If no context is specified, the API will return cudaErrorInvalidValue.

Parameters

  * **ctx** – - Context for which to obtain the Id (required parameter, see note below)

  * **ctxId** – - Pointer to store the Id of the context

Returns

cudaSuccess, cudaErrorCudartUnloading, cudaErrorInitializationError, cudaErrorInvalidValue, cudaErrorNotPermitted

`` __host__ cudaError_t cudaExecutionCtxRecordEvent(cudaExecutionContext_t ctx, cudaEvent_t event) ``

Records an event for the specified execution context.

Captures in `event` all the activities of the execution context `ctx` at the time of this call. `event` and `ctx` must be from the same CUDA device, otherwise ::cudaErrorInvalidHandle will be returned. Calls such as cudaEventQuery() or cudaExecutionCtxWaitEvent() will then examine or wait for completion of the work that was captured. Uses of `ctx` after this call do not modify `event`. If the execution context passed to `ctx` is the device (primary) context obtained via cudaDeviceGetExecutionCtx(), `event` will capture all the activities of the green contexts created on the device as well.

See also

cudaEventRecord, cudaExecutionCtxWaitEvent, ::cuCtxRecordEvent, ::cuGreenCtxRecordEvent

Note

The API will return cudaErrorStreamCaptureUnsupported if the specified execution context `ctx` has a stream in the capture mode. In such a case, the call will invalidate all the conflicting captures.

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Note

The context parameter is required and the API ignores the context that is current to the calling thread. This enables explicit context-based programming without relying on thread-local state. If no context is specified, the API will return cudaErrorInvalidValue.

Parameters

  * **ctx** – - Execution context to record event for (required parameter, see note below)

  * **event** – - Event to record

Returns

cudaSuccess, cudaErrorCudartUnloading, cudaErrorInitializationError, ::cudaErrorInvalidHandle, cudaErrorStreamCaptureUnsupported

`` __host__ cudaError_t cudaExecutionCtxStreamCreate(cudaStream_t *phStream, cudaExecutionContext_t ctx, unsigned int flags, int priority) ``

Creates a stream and initializes it for the given execution context.

The API creates a CUDA stream with the specified `flags` and `priority`, initializing it with resources as defined at the time of creating the specified `ctx`. Additionally, the API also enables work submitted to to the stream to be tracked under `ctx`.

The supported values for `flags` are:

  * cudaStreamDefault: Default stream creation flag. This would be cudaStreamNonBlocking for streams created on a green context.

  * cudaStreamNonBlocking: Specifies that work running in the created stream may run concurrently with work in stream 0 (the NULL stream), and that the created stream should perform no implicit synchronization with stream 0

Specifying `priority` affects the scheduling priority of work in the stream. Priorities provide a hint to preferentially run work with higher priority when possible, but do not preempt already-running work or provide any other functional guarantee on execution order. `priority` follows a convention where lower numbers represent higher priorities. ‘0’ represents default priority. The range of meaningful numerical priorities can be queried using cudaDeviceGetStreamPriorityRange. If the specified priority is outside the numerical range returned by cudaDeviceGetStreamPriorityRange, it will automatically be clamped to the lowest or the highest number in the range.

See also

cudaStreamDestroy, cudaGreenCtxCreate, cudaDeviceGetStreamPriorityRange, cudaStreamGetFlags, cudaStreamGetPriority, cudaStreamGetDevice, cudaStreamGetDevResource, cudaLaunchKernel, cudaEventRecord, cudaStreamWaitEvent, cudaStreamQuery, cudaStreamSynchronize, cudaStreamAddCallback

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Note

The context parameter is required and the API ignores the context that is current to the calling thread. This enables explicit context-based programming without relying on thread-local state. If no context is specified, the API will return cudaErrorInvalidValue.

Note

In the current implementation, only compute kernels launched in priority streams are affected by the stream’s priority. Stream priorities have no effect on host-to-device and device-to-host memory operations.

Parameters

  * **phStream** – - Returned stream handle

  * **ctx** – - Execution context to initialize the stream with (required parameter, see note below)

  * **flags** – - Flags for stream creation

  * **priority** – - Stream priority

Returns

cudaSuccess, cudaErrorInvalidValue, cudaErrorNotPermitted, ::cudaErrorOutOfMemory, cudaErrorCudartUnloading, cudaErrorInitializationError

`` __host__ cudaError_t cudaExecutionCtxSynchronize(cudaExecutionContext_t ctx) ``

Block for the specified execution context’s tasks to complete.

Blocks until the specified execution context has completed all preceding requested tasks. If the specified execution context is the device (primary) context obtained via cudaDeviceGetExecutionCtx, green contexts that have been created on the device will also be synchronized.

The API returns an error if one of the preceding tasks failed.

See also

cudaGreenCtxCreate, cudaExecutionCtxDestroy, cudaDeviceSynchronize, ::cuCtxSynchronize_v2

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Note

The context parameter is required and the API ignores the context that is current to the calling thread. This enables explicit context-based programming without relying on thread-local state. If no context is specified, the API will return cudaErrorInvalidValue.

Parameters

**ctx** – - Execution context to synchronize (required parameter, see note below)

Returns

cudaSuccess, cudaErrorCudartUnloading, cudaErrorDeviceUninitialized, cudaErrorInvalidValue

`` __host__ cudaError_t cudaExecutionCtxWaitEvent(cudaExecutionContext_t ctx, cudaEvent_t event) ``

Make an execution context wait on an event.

Makes all future work submitted to execution context `ctx` wait for all work captured in `event`. The synchronization will be performed on the device and will not block the calling CPU thread. See cudaExecutionCtxRecordEvent() for details on what is captured by an event. If the execution context passed to `ctx` is the device (primary) context obtained via cudaDeviceGetExecutionCtx(), all green contexts created on the device will wait for `event` as well.

See also

cudaExecutionCtxRecordEvent, cudaStreamWaitEvent, ::cuCtxWaitEvent, ::cuGreenCtxWaitEvent

Note

`event` may be from a different execution context or device than `ctx`.

Note

The API will return cudaErrorStreamCaptureUnsupported and invalidate the capture if the specified event `event` is part of an ongoing capture sequence or if the specified execution context `ctx` has a stream in the capture mode.

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Note

The context parameter is required and the API ignores the context that is current to the calling thread. This enables explicit context-based programming without relying on thread-local state. If no context is specified, the API will return cudaErrorInvalidValue.

Parameters

  * **ctx** – - Execution context to wait for (required parameter, see note below)

  * **event** – - Event to wait on

Returns

cudaSuccess, cudaErrorCudartUnloading, cudaErrorInitializationError, ::cudaErrorInvalidHandle, cudaErrorStreamCaptureUnsupported

`` __host__ cudaError_t cudaGreenCtxCreate(cudaExecutionContext_t *phCtx, cudaDevResourceDesc_t desc, int device, unsigned int flags) ``

Creates a green context with a specified set of resources.

This API creates a green context with the resources specified in the descriptor `desc` and returns it in the handle represented by `phCtx`.

This API retains the device’s primary context for the lifetime of the green context. The primary context will be released when the green context is destroyed. To avoid the overhead of repeated initialization and teardown, it is recommended to explicitly initialize the device’s primary context ahead of time using cudaInitDevice. This ensures that the primary context remains initialized throughout the program’s lifetime, minimizing overhead during green context creation and destruction.

The API does not create a default stream for the green context. Developers are expected to create streams explicitly using cudaExecutionCtxStreamCreate to submit work to the green context.

Note: The API is not supported on 32-bit platforms.

See also

cudaDeviceGetDevResource, cudaDevSmResourceSplit, cudaDevResourceGenerateDesc, cudaExecutionCtxGetDevResource, cudaExecutionCtxDestroy, cudaInitDevice, cudaExecutionCtxStreamCreate

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **phCtx** – - Pointer for the output handle to the green context

  * **desc** – - Descriptor generated via cudaDevResourceGenerateDesc which contains the set of resources to be used

  * **device** – - Device on which to create the green context.

  * **flags** – - Green context creation flags. Must be 0, currently reserved for future use.

Returns

cudaSuccess, cudaErrorInvalidValue, cudaErrorInvalidDevice, cudaErrorNotPermitted, cudaErrorNotSupported, ::cudaErrorOutOfMemory, cudaErrorCudartUnloading, cudaErrorInitializationError

`` __host__ cudaError_t cudaStreamGetDevResource(cudaStream_t hStream, cudaDevResource *resource, enum cudaDevResourceType type) ``

Get stream resources.

Get the `type` resources available to the `hStream` and store them in `resource`.

Note: The API will return cudaErrorInvalidResourceType is `type` is `cudaDevResourceTypeWorkqueueConfig` or `cudaDevResourceTypeWorkqueue`.

See also

cudaGreenCtxCreate, cudaExecutionCtxStreamCreate, cudaStreamCreate, cudaDevSmResourceSplit, cudaDevResourceGenerateDesc, ::cuStreamGetDevResource

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **hStream** – - Stream to get resource for

  * **resource** – - Output pointer to a cudaDevResource structure

  * **type** – - Type of resource to retrieve

Returns

cudaSuccess, cudaErrorCudartUnloading, cudaErrorInitializationError, cudaErrorDeviceUninitialized, cudaErrorInvalidResourceType, cudaErrorInvalidValue, ::cudaErrorInvalidHandle, cudaErrorNotPermitted, cudaErrorCallRequiresNewerDriver,
