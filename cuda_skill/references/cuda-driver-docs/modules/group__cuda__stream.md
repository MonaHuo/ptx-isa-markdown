<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/group__CUDA__STREAM.html

#  6.36. Stream Management

This section describes the stream management functions of the low-level CUDA driver application programming interface.

##  6.36.1. Enumerations

`` enum CUgraphRecaptureStatus ``

_Values:_

`` enumerator CU_GRAPH_RECAPTURE_ELIGIBLE_FOR_UPDATE ``

Node is eligible for update in an instantiated graph.

`` enumerator CU_GRAPH_RECAPTURE_INELIGIBLE_FOR_UPDATE ``

Parameter changes in the node cannot be applied to an instantiated graph.

`` enumerator CU_GRAPH_RECAPTURE_ERROR ``

Error while attempting to recapture the node.

The recapture will be ended regardless of the return value from the callback.

##  6.36.2. Functions

`` CUresult cuStreamAddCallback(CUstream hStream, CUstreamCallback callback, void *userData, unsigned int flags) ``

Add a callback to a compute stream.

Adds a callback to be called on the host after all currently enqueued items in the stream have completed. For each cuStreamAddCallback call, the callback will be executed exactly once. The callback will block later work in the stream until it is finished.

The callback may be passed CUDA_SUCCESS or an error code. In the event of a device error, all subsequently executed callbacks will receive an appropriate CUresult.

Callbacks must not make any CUDA API calls. Attempting to use a CUDA API will result in CUDA_ERROR_NOT_PERMITTED. Callbacks must not perform any synchronization that may depend on outstanding device work or other callbacks that are not mandated to run earlier. Callbacks without a mandated order (in independent streams) execute in undefined order and may be serialized.

For the purposes of Unified Memory, callback execution makes a number of guarantees:

  * The callback stream is considered idle for the duration of the callback. Thus, for example, a callback may always use memory attached to the callback stream.

  * The start of execution of a callback has the same effect as synchronizing an event recorded in the same stream immediately prior to the callback. It thus synchronizes streams which have been “joined” prior to the callback.

  * Adding device work to any stream does not have the effect of making the stream active until all preceding host functions and stream callbacks have executed. Thus, for example, a callback might use global attached memory even if work has been added to another stream, if the work has been ordered behind the callback with an event.

  * Completion of a callback does not cause a stream to become active except as described above. The callback stream will remain idle if no device work follows the callback, and will remain idle across consecutive callbacks without device work in between. Thus, for example, stream synchronization can be done by signaling from a callback at the end of the stream.

See also

cuStreamCreate, cuStreamQuery, cuStreamSynchronize, cuStreamWaitEvent, cuStreamDestroy, cuMemAllocManaged, cuStreamAttachMemAsync, cuLaunchHostFunc, ::cudaStreamAddCallback

Note

This function is slated for eventual deprecation and removal. If you do not require the callback to execute in case of a device error, consider using cuLaunchHostFunc. Additionally, this function is not supported with cuStreamBeginCapture and cuStreamEndCapture, unlike cuLaunchHostFunc.

Note

This function uses standard default stream semantics.

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **hStream** – - Stream to add callback to

  * **callback** – - The function to call once preceding stream operations are complete

  * **userData** – - User specified data to be passed to the callback function

  * **flags** – - Reserved for future use, must be 0

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_HANDLE, CUDA_ERROR_NOT_SUPPORTED

`` CUresult cuStreamAttachMemAsync(CUstream hStream, CUdeviceptr dptr, size_t length, unsigned int flags) ``

Attach memory to a stream asynchronously.

Enqueues an operation in `hStream` to specify stream association of `length` bytes of memory starting from `dptr`. This function is a stream-ordered operation, meaning that it is dependent on, and will only take effect when, previous work in stream has completed. Any previous association is automatically replaced.

`dptr` must point to one of the following types of memories:

  * managed memory declared using the **managed** keyword or allocated with cuMemAllocManaged.

  * a valid host-accessible region of system-allocated pageable memory. This type of memory may only be specified if the device associated with the stream reports a non-zero value for the device attribute CU_DEVICE_ATTRIBUTE_PAGEABLE_MEMORY_ACCESS.

For managed allocations, `length` must be either zero or the entire allocation’s size. Both indicate that the entire allocation’s stream association is being changed. Currently, it is not possible to change stream association for a portion of a managed allocation.

For pageable host allocations, `length` must be non-zero.

The stream association is specified using `flags` which must be one of CUmemAttach_flags. If the CU_MEM_ATTACH_GLOBAL flag is specified, the memory can be accessed by any stream on any device. If the CU_MEM_ATTACH_HOST flag is specified, the program makes a guarantee that it won’t access the memory on the device from any stream on a device that has a zero value for the device attribute CU_DEVICE_ATTRIBUTE_CONCURRENT_MANAGED_ACCESS. If the CU_MEM_ATTACH_SINGLE flag is specified and `hStream` is associated with a device that has a zero value for the device attribute CU_DEVICE_ATTRIBUTE_CONCURRENT_MANAGED_ACCESS, the program makes a guarantee that it will only access the memory on the device from `hStream`. It is illegal to attach singly to the NULL stream, because the NULL stream is a virtual global stream and not a specific stream. An error will be returned in this case.

When memory is associated with a single stream, the Unified Memory system will allow CPU access to this memory region so long as all operations in `hStream` have completed, regardless of whether other streams are active. In effect, this constrains exclusive ownership of the managed memory region by an active GPU to per-stream activity instead of whole-GPU activity.

Accessing memory on the device from streams that are not associated with it will produce undefined results. No error checking is performed by the Unified Memory system to ensure that kernels launched into other streams do not access this region.

It is a program’s responsibility to order calls to cuStreamAttachMemAsync via events, synchronization or other means to ensure legal access to memory at all times. Data visibility and coherency will be changed appropriately for all kernels which follow a stream-association change.

If `hStream` is destroyed while data is associated with it, the association is removed and the association reverts to the default visibility of the allocation as specified at cuMemAllocManaged. For **managed** variables, the default association is always CU_MEM_ATTACH_GLOBAL. Note that destroying a stream is an asynchronous operation, and as a result, the change to default association won’t happen until all work in the stream has completed.

See also

cuStreamCreate, cuStreamQuery, cuStreamSynchronize, cuStreamWaitEvent, cuStreamDestroy, cuMemAllocManaged, ::cudaStreamAttachMemAsync

Note

This function uses standard default stream semantics.

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **hStream** – - Stream in which to enqueue the attach operation

  * **dptr** – - Pointer to memory (must be a pointer to managed memory or to a valid host-accessible region of system-allocated pageable memory)

  * **length** – - Length of memory

  * **flags** – - Must be one of CUmemAttach_flags

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_HANDLE, CUDA_ERROR_NOT_SUPPORTED

`` CUresult cuStreamBeginCapture(CUstream hStream, CUstreamCaptureMode mode) ``

Begins graph capture on a stream.

Begin graph capture on `hStream`. When a stream is in capture mode, all operations pushed into the stream will not be executed, but will instead be captured into a graph, which will be returned via cuStreamEndCapture. Capture may not be initiated if `stream` is CU_STREAM_LEGACY. Capture must be ended on the same stream in which it was initiated, and it may only be initiated if the stream is not already in capture mode. The capture mode may be queried via cuStreamIsCapturing. A unique id representing the capture sequence may be queried via cuStreamGetCaptureInfo.

If `mode` is not CU_STREAM_CAPTURE_MODE_RELAXED, cuStreamEndCapture must be called on this stream from the same thread.

See also

cuStreamCreate, cuStreamIsCapturing, cuStreamEndCapture, cuThreadExchangeStreamCaptureMode

Note

Kernels captured using this API must not use texture and surface references. Reading or writing through any texture or surface reference is undefined behavior. This restriction does not apply to texture and surface objects.

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **hStream** – - Stream in which to initiate capture

  * **mode** – - Controls the interaction of this capture sequence with other API calls that are potentially unsafe. For more details see cuThreadExchangeStreamCaptureMode.

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_VALUE

`` CUresult cuStreamBeginCaptureToCig(CUstream hStream, CUstreamCigCaptureParams *streamCigCaptureParams) ``

Begins capture to CIG on a stream.

Support for CIG streams with D3D12 can be determined using cuDeviceGetAttribute() with CU_DEVICE_ATTRIBUTE_D3D12_CIG_STREAMS_SUPPORTED.

Begin CIG (CUDA in Graphics) capture on `hStream` for the graphics API as provided in `streamCigCaptureParams`. When a stream is in CIG capture mode, all operations pushed into the stream will not be executed, but will instead be captured into a graphics API command list/command buffer. All kernel launches and memory copy/memory set operations on the CIG stream will be recorded. When the command list is executed by the graphics API, all the stream’s operations will execute in order along with other graphics API commands in the command list.

CIG stream capture may not be initiated if `stream` is CU_STREAM_LEGACY. Capture must be ended on the same stream in which it was initiated, and it may only be initiated if the stream is not already in CIG capture mode.

The context must be also created in CIG mode previously, otherwise this operation will fail and CUDA_ERROR_INVALID_CONTEXT will be returned.

Data from the graphics client can be shared with CUDA via the `streamSharedData` in `streamCigCaptureParams`. The format of `streamSharedData` is dependent on the type of the graphics client. For D3D12, `streamSharedData` is an ID3D12CommandList object pointer. The command list must be in ready state for recording commands whenever kernels are launched on the stream. The command list provided must belong to the graphics API device that the CIG context was created with, otherwise the behavior will be undefined.

The stream object may not be destroyed until its associated command list has finished executing on the GPU. The command list/command buffer used for capture may not be submitted for execution before a call to cuStreamEndCaptureToCig is made on the associated stream.

Graphics resources to be accessed by work recorded on the CIG stream must use UAV barriers on the command list prior to recording work that accesses them on the stream.

Resubmission of the same recorded command list is not allowed. Further more, care must be taken for the order of execution of the recorded CUDA work with regards to other CUDA work submitted under the same CIG context. Out-of-order execution can lead to device hangs or exceptions.

CIG capture mode operates similarly to `cuStreamBeginCapture` with the `CU_STREAM_CAPTURE_MODE_RELAXED` option. There are additional limitations to streams in CIG capture mode. The following functions are not allowed for CIG streams whether directly or indirectly via a recorded graph launch: cuLaunchHostFunc cuStreamAddCallback cuStreamSynchronize cuStreamWaitValue32 cuStreamWaitValue64 cuStreamBatchMemOp cuStreamBeginCapture cuStreamBeginCaptureToGraph cuMemAllocAsync cuMemFreeAsync

See also

cuStreamEndCaptureToCig, cuStreamBeginCapture, cuStreamWaitEvent, cuStreamQuery, cuStreamSynchronize, cuStreamAddCallback

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **hStream** – - Stream in which to initiate capture to CIG

  * **streamCigCaptureParams** – - CIG capture parameters

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_NOT_SUPPORTED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE,

`` CUresult cuStreamBeginCaptureToGraph(CUstream hStream, CUgraph hGraph, const CUgraphNode *dependencies, const CUgraphEdgeData *dependencyData, size_t numDependencies, CUstreamCaptureMode mode) ``

Begins graph capture on a stream to an existing graph.

Begin graph capture on `hStream`, placing new nodes into an existing graph. When a stream is in capture mode, all operations pushed into the stream will not be executed, but will instead be captured into `hGraph`. The graph will not be instantiable until the user calls cuStreamEndCapture.

Capture may not be initiated if `stream` is CU_STREAM_LEGACY. Capture must be ended on the same stream in which it was initiated, and it may only be initiated if the stream is not already in capture mode. The capture mode may be queried via cuStreamIsCapturing. A unique id representing the capture sequence may be queried via cuStreamGetCaptureInfo.

If `mode` is not CU_STREAM_CAPTURE_MODE_RELAXED, cuStreamEndCapture must be called on this stream from the same thread.

See also

cuStreamBeginCapture, cuStreamCreate, cuStreamIsCapturing, cuStreamEndCapture, cuThreadExchangeStreamCaptureMode, cuGraphAddNode

Note

Kernels captured using this API must not use texture and surface references. Reading or writing through any texture or surface reference is undefined behavior. This restriction does not apply to texture and surface objects.

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **hStream** – - Stream in which to initiate capture.

  * **hGraph** – - Graph to capture into.

  * **dependencies** – - Dependencies of the first node captured in the stream. Can be NULL if numDependencies is 0.

  * **dependencyData** – - Optional array of data associated with each dependency.

  * **numDependencies** – - Number of dependencies.

  * **mode** – - Controls the interaction of this capture sequence with other API calls that are potentially unsafe. For more details see cuThreadExchangeStreamCaptureMode.

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_VALUE

`` CUresult cuStreamBeginRecaptureToGraph(CUstream hStream, CUstreamCaptureMode mode, CUgraph hGraph, CUgraphRecaptureCallback callbackFunc, void *userData) ``

Begin graph capture on a stream to an existing graph.

Begin graph capture on `hStream` to the existing `hGraph`. The node creation order while recapturing the graph must be identical to the original graph. The recapture will fail immediately for:

  * Topology mismatches between the existing graph and the recaptured graph

  * Parameter mismatches for memory allocation or free nodes

Any other node parameter mismatches during recapture can be configured to call the function provided in `callbackFunc`. The recapture will fail immediately if the callback returns anything other than CUDA_SUCCESS.

If the recapture fails for any reason, the `graph` will be in an undefined state and should be destroyed.

See cuStreamBeginCapture for additional detail on beginning the capture.

See also

cuStreamCreate, cuStreamBeginCapture, cuStreamIsCapturing, cuStreamEndCapture, cuThreadExchangeStreamCaptureMode

Note

Any user objects associated with `graph` will be released prior to the recapture.

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **hStream** – - Stream in which to initiate capture

  * **mode** – - Controls the interaction of this capture sequence with other API calls that are potentially unsafe. For more details see cuThreadExchangeStreamCaptureMode.

  * **hGraph** – - Existing CUDA graph to be captured into

  * **callbackFunc** – - Function that will be called for all parameter mismatches from the original graph

  * **userData** – - A generic pointer to user data that is passed into the callback function

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_VALUE,

`` CUresult cuStreamCopyAttributes(CUstream dst, CUstream src) ``

Copies attributes from source stream to destination stream.

Copies attributes from source stream `src` to destination stream `dst`. Both streams must have the same context.

See also

CUaccessPolicyWindow

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **dst** – **[out]** Destination stream

  * **src** – **[in]** Source stream For list of attributes see CUstreamAttrID

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_VALUE

`` CUresult cuStreamCreate(CUstream *phStream, unsigned int Flags) ``

Create a stream.

Creates a stream and returns a handle in `phStream`. The `Flags` argument determines behaviors of the stream.

Valid values for `Flags` are:

  * CU_STREAM_DEFAULT: Default stream creation flag.

  * CU_STREAM_NON_BLOCKING: Specifies that work running in the created stream may run concurrently with work in stream 0 (the NULL stream), and that the created stream should perform no implicit synchronization with stream 0.

See also

cuStreamDestroy, cuStreamCreateWithPriority, cuGreenCtxStreamCreate, cuStreamGetPriority, cuStreamGetFlags, cuStreamGetDevice cuStreamWaitEvent, cuStreamQuery, cuStreamSynchronize, cuStreamAddCallback, ::cudaStreamCreate, ::cudaStreamCreateWithFlags

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **phStream** – - Returned newly created stream

  * **Flags** – - Parameters for stream creation

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_OUT_OF_MEMORY CUDA_ERROR_EXTERNAL_DEVICE

`` CUresult cuStreamCreateWithPriority(CUstream *phStream, unsigned int flags, int priority) ``

Create a stream with the given priority.

Creates a stream with the specified priority and returns a handle in `phStream`. This affects the scheduling priority of work in the stream. Priorities provide a hint to preferentially run work with higher priority when possible, but do not preempt already-running work or provide any other functional guarantee on execution order.

`priority` follows a convention where lower numbers represent higher priorities. ‘0’ represents default priority. The range of meaningful numerical priorities can be queried using cuCtxGetStreamPriorityRange. If the specified priority is outside the numerical range returned by cuCtxGetStreamPriorityRange, it will automatically be clamped to the lowest or the highest number in the range.

See also

cuStreamDestroy, cuStreamCreate, cuGreenCtxStreamCreate, cuStreamGetPriority, cuCtxGetStreamPriorityRange, cuStreamGetFlags, cuStreamGetDevice, cuStreamWaitEvent, cuStreamQuery, cuStreamSynchronize, cuStreamAddCallback, ::cudaStreamCreateWithPriority

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Stream priorities are supported only on GPUs with compute capability 3.5 or higher.

Note

In the current implementation, only compute kernels launched in priority streams are affected by the stream’s priority. Stream priorities have no effect on host-to-device and device-to-host memory operations.

Parameters

  * **phStream** – - Returned newly created stream

  * **flags** – - Flags for stream creation. See cuStreamCreate for a list of valid flags

  * **priority** – - Stream priority. Lower numbers represent higher priorities. See cuCtxGetStreamPriorityRange for more information about meaningful stream priorities that can be passed.

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_OUT_OF_MEMORY CUDA_ERROR_EXTERNAL_DEVICE

`` CUresult cuStreamDestroy(CUstream hStream) ``

Destroys a stream.

Destroys the stream specified by `hStream`.

In case the device is still doing work in the stream `hStream` when cuStreamDestroy() is called, the function will return immediately and the resources associated with `hStream` will be released automatically once the device has completed all work in `hStream`.

See also

cuStreamCreate, cuStreamWaitEvent, cuStreamQuery, cuStreamSynchronize, cuStreamAddCallback, ::cudaStreamDestroy

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

**hStream** – - Stream to destroy

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_INVALID_HANDLE CUDA_ERROR_EXTERNAL_DEVICE

`` CUresult cuStreamEndCapture(CUstream hStream, CUgraph *phGraph) ``

Ends capture on a stream, returning the captured graph.

End capture on `hStream`, returning the captured graph via `phGraph`. Capture must have been initiated on `hStream` via a call to cuStreamBeginCapture. If capture was invalidated, due to a violation of the rules of stream capture, then a NULL graph will be returned.

If the `mode` argument to cuStreamBeginCapture was not CU_STREAM_CAPTURE_MODE_RELAXED, this call must be from the same thread as cuStreamBeginCapture.

See also

cuStreamCreate, cuStreamBeginCapture, cuStreamIsCapturing, cuGraphDestroy

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **hStream** – - Stream to query

  * **phGraph** – - The captured graph

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_STREAM_CAPTURE_WRONG_THREAD

`` CUresult cuStreamEndCaptureToCig(CUstream hStream) ``

Ends CIG capture on a stream.

End CIG capture on `hStream`. Capture must have been initiated on `hStream` via a call to cuStreamBeginCaptureToCig. Once this function is called, `hStream` will exit CIG capture mode and return to its original state, thus removing all CIG stream restrictions. Also, the command list/command buffer that was associated with `hStream` in the previous call to cuStreamBeginCaptureToCig is now allowed to be submitted for execution on the graphics API. However, the stream may not be destroyed until execution of the command list is fully done on the GPU. This requirements extends also to all streams dependant on the CIG stream (e.g. via event waits).

See also

cuStreamBeginCaptureToCig

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

**hStream** – - Stream to end CIG capture

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_STREAM_CAPTURE_WRONG_THREAD

`` CUresult cuStreamGetAttribute(CUstream hStream, CUstreamAttrID attr, CUstreamAttrValue *value_out) ``

Queries stream attribute.

Queries attribute `attr` from `hStream` and stores it in corresponding member of `value_out`.

See also

CUaccessPolicyWindow

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **hStream** – **[in]**

  * **attr** – **[in]**

  * **value_out** –

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_INVALID_HANDLE

`` CUresult cuStreamGetCaptureInfo(CUstream hStream, CUstreamCaptureStatus *captureStatus_out, cuuint64_t *id_out, CUgraph *graph_out, const CUgraphNode **dependencies_out, const CUgraphEdgeData **edgeData_out, size_t *numDependencies_out) ``

Query a stream’s capture state.

Query stream state related to stream capture.

If called on CU_STREAM_LEGACY (the “null stream”) while a stream not created with CU_STREAM_NON_BLOCKING is capturing, returns CUDA_ERROR_STREAM_CAPTURE_IMPLICIT.

Valid data (other than capture status) is returned only if both of the following are true:

  * the call returns CUDA_SUCCESS

  * the returned capture status is CU_STREAM_CAPTURE_STATUS_ACTIVE

If `edgeData_out` is non-NULL then `dependencies_out` must be as well. If `dependencies_out` is non-NULL and `edgeData_out` is NULL, but there is non-zero edge data for one or more of the current stream dependencies, the call will return CUDA_ERROR_LOSSY_QUERY.

See also

cuStreamBeginCapture, cuStreamIsCapturing, cuStreamUpdateCaptureDependencies

Note

Graph objects are not threadsafe. More here.

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **hStream** – - The stream to query

  * **captureStatus_out** – - Location to return the capture status of the stream; required

  * **id_out** – - Optional location to return an id for the capture sequence, which is unique over the lifetime of the process

  * **graph_out** – - Optional location to return the graph being captured into. All operations other than destroy and node removal are permitted on the graph while the capture sequence is in progress. This API does not transfer ownership of the graph, which is transferred or destroyed at cuStreamEndCapture. Note that the graph handle may be invalidated before end of capture for certain errors. Nodes that are or become unreachable from the original stream at cuStreamEndCapture due to direct actions on the graph do not trigger CUDA_ERROR_STREAM_CAPTURE_UNJOINED.

  * **dependencies_out** – - Optional location to store a pointer to an array of nodes. The next node to be captured in the stream will depend on this set of nodes, absent operations such as event wait which modify this set. The array pointer is valid until the next API call which operates on the stream or until the capture is terminated. The node handles may be copied out and are valid until they or the graph is destroyed. The driver-owned array may also be passed directly to APIs that operate on the graph (not the stream) without copying.

  * **edgeData_out** – - Optional location to store a pointer to an array of graph edge data. This array parallels `dependencies_out`; the next node to be added has an edge to `dependencies_out`[i] with annotation `edgeData_out`[i] for each `i`. The array pointer is valid until the next API call which operates on the stream or until the capture is terminated.

  * **numDependencies_out** – - Optional location to store the size of the array returned in dependencies_out.

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_STREAM_CAPTURE_IMPLICIT, CUDA_ERROR_LOSSY_QUERY

`` CUresult cuStreamGetCtx(CUstream hStream, CUcontext *pctx) ``

Query the context associated with a stream.

Returns the CUDA context that the stream is associated with.

If the stream was created via the API cuGreenCtxStreamCreate, the returned context is equivalent to the one returned by cuCtxFromGreenCtx() on the green context associated with the stream at creation time.

The stream handle `hStream` can refer to any of the following:

  * a stream created via any of the CUDA driver APIs such as cuStreamCreate and cuStreamCreateWithPriority, or their runtime API equivalents such as ::cudaStreamCreate, ::cudaStreamCreateWithFlags and ::cudaStreamCreateWithPriority. The returned context is the context that was active in the calling thread when the stream was created. Passing an invalid handle will result in undefined behavior.

  * any of the special streams such as the NULL stream, CU_STREAM_LEGACY and CU_STREAM_PER_THREAD. The runtime API equivalents of these are also accepted, which are NULL, ::cudaStreamLegacy and ::cudaStreamPerThread respectively. Specifying any of the special handles will return the context current to the calling thread. If no context is current to the calling thread, CUDA_ERROR_INVALID_CONTEXT is returned.

See also

cuStreamDestroy, cuStreamCreateWithPriority, cuStreamGetPriority, cuStreamGetFlags, cuStreamGetDevice cuStreamWaitEvent, cuStreamQuery, cuStreamSynchronize, cuStreamAddCallback, ::cudaStreamCreate, ::cudaStreamCreateWithFlags

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **hStream** – - Handle to the stream to be queried

  * **pctx** – - Returned context associated with the stream

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_HANDLE, CUDA_ERROR_NOT_SUPPORTED

`` CUresult cuStreamGetCtx_v2(CUstream hStream, CUcontext *pCtx, CUgreenCtx *pGreenCtx) ``

Query the contexts associated with a stream.

Returns the contexts that the stream is associated with.

If the stream is associated with a green context, the API returns the green context in `pGreenCtx` and the primary context of the associated device in `pCtx`.

If the stream is associated with a regular context, the API returns the regular context in `pCtx` and NULL in `pGreenCtx`.

The stream handle `hStream` can refer to any of the following:

  * a stream created via any of the CUDA driver APIs such as cuStreamCreate, cuStreamCreateWithPriority and cuGreenCtxStreamCreate, or their runtime API equivalents such as ::cudaStreamCreate, ::cudaStreamCreateWithFlags and ::cudaStreamCreateWithPriority. Passing an invalid handle will result in undefined behavior.

  * any of the special streams such as the NULL stream, CU_STREAM_LEGACY and CU_STREAM_PER_THREAD. The runtime API equivalents of these are also accepted, which are NULL, ::cudaStreamLegacy and ::cudaStreamPerThread respectively. If any of the special handles are specified, the API will operate on the context current to the calling thread. If a green context (that was converted via cuCtxFromGreenCtx() before setting it current) is current to the calling thread, the API will return the green context in `pGreenCtx` and the primary context of the associated device in `pCtx`. If a regular context is current, the API returns the regular context in `pCtx` and NULL in `pGreenCtx`. Note that specifying CU_STREAM_PER_THREAD or ::cudaStreamPerThread will return CUDA_ERROR_INVALID_HANDLE if a green context is current to the calling thread. If no context is current to the calling thread, CUDA_ERROR_INVALID_CONTEXT is returned.

See also

cuStreamDestroy, cuStreamCreate cuStreamCreateWithPriority, cuGreenCtxStreamCreate, cuStreamGetPriority, cuStreamGetFlags, cuStreamGetDevice, cuStreamWaitEvent, cuStreamQuery, cuStreamSynchronize, cuStreamAddCallback, ::cudaStreamCreate, ::cudaStreamCreateWithFlags,

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **hStream** – - Handle to the stream to be queried

  * **pCtx** – - Returned regular context associated with the stream

  * **pGreenCtx** – - Returned green context if the stream is associated with a green context or NULL if not

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_HANDLE

`` CUresult cuStreamGetDevice(CUstream hStream, CUdevice *device) ``

Returns the device handle of the stream.

Returns in `*device` the device handle of the stream

See also

cuStreamDestroy, cuStreamCreate, cuGreenCtxStreamCreate, cuStreamGetFlags

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **hStream** – - Handle to the stream to be queried

  * **device** – - Returns the device to which a stream belongs

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_INVALID_HANDLE, CUDA_ERROR_OUT_OF_MEMORY

`` CUresult cuStreamGetFlags(CUstream hStream, unsigned int *flags) ``

Query the flags of a given stream.

Query the flags of a stream created using cuStreamCreate, cuStreamCreateWithPriority or cuGreenCtxStreamCreate and return the flags in `flags`.

See also

cuStreamDestroy, cuStreamCreate, cuGreenCtxStreamCreate, cuStreamGetPriority, ::cudaStreamGetFlags, cuStreamGetDevice

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **hStream** – - Handle to the stream to be queried

  * **flags** – - Pointer to an unsigned integer in which the stream’s flags are returned The value returned in `flags` is a logical ‘OR’ of all flags that were used while creating this stream. See cuStreamCreate for the list of valid flags

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_INVALID_HANDLE, CUDA_ERROR_OUT_OF_MEMORY

`` CUresult cuStreamGetId(CUstream hStream, unsigned long long *streamId) ``

Returns the unique Id associated with the stream handle supplied.

Returns in `streamId` the unique Id which is associated with the given stream handle. The Id is unique for the life of the program.

The stream handle `hStream` can refer to any of the following:

  * a stream created via any of the CUDA driver APIs such as cuStreamCreate and cuStreamCreateWithPriority, or their runtime API equivalents such as ::cudaStreamCreate, ::cudaStreamCreateWithFlags and ::cudaStreamCreateWithPriority. Passing an invalid handle will result in undefined behavior.

  * any of the special streams such as the NULL stream, CU_STREAM_LEGACY and CU_STREAM_PER_THREAD. The runtime API equivalents of these are also accepted, which are NULL, ::cudaStreamLegacy and ::cudaStreamPerThread respectively.

See also

cuStreamDestroy, cuStreamCreate, cuStreamGetPriority, ::cudaStreamGetId

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **hStream** – - Handle to the stream to be queried

  * **streamId** – - Pointer to store the Id of the stream

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_INVALID_HANDLE

`` CUresult cuStreamGetPriority(CUstream hStream, int *priority) ``

Query the priority of a given stream.

Query the priority of a stream created using cuStreamCreate, cuStreamCreateWithPriority or cuGreenCtxStreamCreate and return the priority in `priority`. Note that if the stream was created with a priority outside the numerical range returned by cuCtxGetStreamPriorityRange, this function returns the clamped priority. See cuStreamCreateWithPriority for details about priority clamping.

See also

cuStreamDestroy, cuStreamCreate, cuStreamCreateWithPriority, cuGreenCtxStreamCreate, cuCtxGetStreamPriorityRange, cuStreamGetFlags, cuStreamGetDevice, ::cudaStreamGetPriority

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **hStream** – - Handle to the stream to be queried

  * **priority** – - Pointer to a signed integer in which the stream’s priority is returned

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_INVALID_HANDLE, CUDA_ERROR_OUT_OF_MEMORY

`` CUresult cuStreamIsCapturing(CUstream hStream, CUstreamCaptureStatus *captureStatus) ``

Returns a stream’s capture status.

Return the capture status of `hStream` via `captureStatus`. After a successful call, `*captureStatus` will contain one of the following:

  * CU_STREAM_CAPTURE_STATUS_NONE: The stream is not capturing.

  * CU_STREAM_CAPTURE_STATUS_ACTIVE: The stream is capturing.

  * CU_STREAM_CAPTURE_STATUS_INVALIDATED: The stream was capturing but an error has invalidated the capture sequence. The capture sequence must be terminated with cuStreamEndCapture on the stream where it was initiated in order to continue using `hStream`.

Note that, if this is called on CU_STREAM_LEGACY (the “null stream”) while a blocking stream in the same context is capturing, it will return CUDA_ERROR_STREAM_CAPTURE_IMPLICIT and `*captureStatus` is unspecified after the call. The blocking stream capture is not invalidated.

When a blocking stream is capturing, the legacy stream is in an unusable state until the blocking stream capture is terminated. The legacy stream is not supported for stream capture, but attempted use would have an implicit dependency on the capturing stream(s).

See also

cuStreamCreate, cuStreamBeginCapture, cuStreamEndCapture

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **hStream** – - Stream to query

  * **captureStatus** – - Returns the stream’s capture status

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_STREAM_CAPTURE_IMPLICIT

`` CUresult cuStreamQuery(CUstream hStream) ``

Determine status of a compute stream.

Returns CUDA_SUCCESS if all operations in the stream specified by `hStream` have completed, or CUDA_ERROR_NOT_READY if not.

For the purposes of Unified Memory, a return value of CUDA_SUCCESS is equivalent to having called cuStreamSynchronize().

See also

cuStreamCreate, cuStreamWaitEvent, cuStreamDestroy, cuStreamSynchronize, cuStreamAddCallback, ::cudaStreamQuery

Note

This function uses standard default stream semantics.

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

**hStream** – - Stream to query status of

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_HANDLE, CUDA_ERROR_NOT_READY

`` CUresult cuStreamSetAttribute(CUstream hStream, CUstreamAttrID attr, const CUstreamAttrValue *value) ``

Sets stream attribute.

Sets attribute `attr` on `hStream` from corresponding attribute of `value`. The updated attribute will be applied to subsequent work submitted to the stream. It will not affect previously submitted work.

See also

CUaccessPolicyWindow

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **hStream** – **[out]**

  * **attr** – **[in]**

  * **value** –

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_INVALID_HANDLE

`` CUresult cuStreamSynchronize(CUstream hStream) ``

Wait until a stream’s tasks are completed.

Waits until the device has completed all operations in the stream specified by `hStream`. If the context was created with the CU_CTX_SCHED_BLOCKING_SYNC flag, the CPU thread will block until the stream is finished with all of its tasks.

See also

cuStreamCreate, cuStreamDestroy, cuStreamWaitEvent, cuStreamQuery, cuStreamAddCallback, ::cudaStreamSynchronize

Note

This function uses standard default stream semantics.

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

**hStream** – - Stream to wait for

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_HANDLE

`` CUresult cuStreamUpdateCaptureDependencies(CUstream hStream, CUgraphNode *dependencies, const CUgraphEdgeData *dependencyData, size_t numDependencies, unsigned int flags) ``

Update the set of dependencies in a capturing stream.

Modifies the dependency set of a capturing stream. The dependency set is the set of nodes that the next captured node in the stream will depend on along with the edge data for those dependencies.

Valid flags are CU_STREAM_ADD_CAPTURE_DEPENDENCIES and CU_STREAM_SET_CAPTURE_DEPENDENCIES. These control whether the set passed to the API is added to the existing set or replaces it. A flags value of 0 defaults to CU_STREAM_ADD_CAPTURE_DEPENDENCIES.

Nodes that are removed from the dependency set via this API do not result in CUDA_ERROR_STREAM_CAPTURE_UNJOINED if they are unreachable from the stream at cuStreamEndCapture.

Returns CUDA_ERROR_ILLEGAL_STATE if the stream is not capturing.

See also

cuStreamBeginCapture, cuStreamGetCaptureInfo

Parameters

  * **hStream** – - The stream to update

  * **dependencies** – - The set of dependencies to add

  * **dependencyData** – - Optional array of data associated with each dependency.

  * **numDependencies** – - The size of the dependencies array

  * **flags** – - See above

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_ILLEGAL_STATE

`` CUresult cuStreamWaitEvent(CUstream hStream, CUevent hEvent, unsigned int Flags) ``

Make a compute stream wait on an event.

Makes all future work submitted to `hStream` wait for all work captured in `hEvent`. See cuEventRecord() for details on what is captured by an event. The synchronization will be performed efficiently on the device when applicable. `hEvent` may be from a different context or device than `hStream`.

flags include:

  * CU_EVENT_WAIT_DEFAULT: Default event creation flag.

  * CU_EVENT_WAIT_EXTERNAL: Event is captured in the graph as an external event node when performing stream capture. This flag is invalid outside of stream capture.

See also

cuStreamCreate, cuEventRecord, cuStreamQuery, cuStreamSynchronize, cuStreamAddCallback, cuStreamDestroy, ::cudaStreamWaitEvent

Note

This function uses standard default stream semantics.

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **hStream** – - Stream to wait

  * **hEvent** – - Event to wait on (may not be NULL)

  * **Flags** – - See ::CUevent_capture_flags

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_HANDLE,

`` CUresult cuThreadExchangeStreamCaptureMode(CUstreamCaptureMode *mode) ``

Swaps the stream capture interaction mode for a thread.

Sets the calling thread’s stream capture interaction mode to the value contained in `*mode`, and overwrites `*mode` with the previous mode for the thread. To facilitate deterministic behavior across function or module boundaries, callers are encouraged to use this API in a push-pop fashion:

```cpp
CUstreamCaptureMode mode = desiredMode;
cuThreadExchangeStreamCaptureMode(&mode);
...
cuThreadExchangeStreamCaptureMode(&mode); // restore previous mode
```

During stream capture (see cuStreamBeginCapture), some actions, such as a call to ::cudaMalloc, may be unsafe. In the case of ::cudaMalloc, the operation is not enqueued asynchronously to a stream, and is not observed by stream capture. Therefore, if the sequence of operations captured via cuStreamBeginCapture depended on the allocation being replayed whenever the graph is launched, the captured graph would be invalid.

Therefore, stream capture places restrictions on API calls that can be made within or concurrently to a cuStreamBeginCapture-cuStreamEndCapture sequence. This behavior can be controlled via this API and flags to cuStreamBeginCapture.

A thread’s mode is one of the following:

  * `CU_STREAM_CAPTURE_MODE_GLOBAL:` This is the default mode. If the local thread has an ongoing capture sequence that was not initiated with `CU_STREAM_CAPTURE_MODE_RELAXED` at `cuStreamBeginCapture`, or if any other thread has a concurrent capture sequence initiated with `CU_STREAM_CAPTURE_MODE_GLOBAL`, this thread is prohibited from potentially unsafe API calls.

  * `CU_STREAM_CAPTURE_MODE_THREAD_LOCAL:` If the local thread has an ongoing capture sequence not initiated with `CU_STREAM_CAPTURE_MODE_RELAXED`, it is prohibited from potentially unsafe API calls. Concurrent capture sequences in other threads are ignored.

  * `CU_STREAM_CAPTURE_MODE_RELAXED:` The local thread is not prohibited from potentially unsafe API calls. Note that the thread is still prohibited from API calls which necessarily conflict with stream capture, for example, attempting cuEventQuery on an event that was last recorded inside a capture sequence.

See also

cuStreamBeginCapture

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

**mode** – - Pointer to mode value to swap with the current mode

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_VALUE

##  6.36.3. Typedefs

`` typedef CUresult (*CUgraphRecaptureCallback)(void *data, CUgraphNode node, const CUgraphNodeParams *originalParams, const CUgraphNodeParams *recaptureParams, CUgraphRecaptureStatus status) ``

Callback function invoked when node parameter mismatches are detected while recapturing to an existing graph.

Parameter struct pointers are only valid within the callback.

Param data

User parameter provided at beginning of recapture

Param node

Graph node with the parameter mismatch

Param originalParams

The original node parameters from the graph

Param recaptureParams

The node parameters received during the recapture

Param status

Status code for the recapture of the node

Return

Error code for the callback. Anything other than CUDA_SUCCESS will cause the recapture to fail immediately.
