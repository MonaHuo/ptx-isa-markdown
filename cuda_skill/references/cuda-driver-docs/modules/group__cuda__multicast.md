<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/group__CUDA__MULTICAST.html

#  6.29. Multicast Object Management

This section describes the CUDA multicast object operations exposed by the low-level CUDA driver application programming interface.

##  6.29.1. overview

A multicast object created via cuMulticastCreate enables certain memory operations to be broadcast to a team of devices. Devices can be added to a multicast object via cuMulticastAddDevice. Memory can be bound on each participating device via cuMulticastBindMem, cuMulticastBindMem_v2, cuMulticastBindAddr, or cuMulticastBindAddr_v2. Multicast objects can be mapped into a device’s virtual address space using the virtual memmory management APIs (see cuMemMap and cuMemSetAccess).

##  6.29.2. Supported Platforms

Support for multicast on a specific device can be queried using the device attribute CU_DEVICE_ATTRIBUTE_MULTICAST_SUPPORTED

##  6.29.3. Functions

`` CUresult cuMulticastAddDevice(CUmemGenericAllocationHandle mcHandle, CUdevice dev) ``

Associate a device to a multicast object.

Associates a device to a multicast object. The added device will be a part of the multicast team of size specified by CUmulticastObjectProp::numDevices during cuMulticastCreate. The association of the device to the multicast object is permanent during the life time of the multicast object. All devices must be added to the multicast team before any memory can be bound to any device in the team. Any calls to cuMulticastBindMem, cuMulticastBindMem_v2, cuMulticastBindAddr, or cuMulticastBindAddr_v2 will block until all devices have been added. Similarly all devices must be added to the multicast team before a virtual address range can be mapped to the multicast object. A call to cuMemMap will block until all devices have been added.

This call may fail with CUDA_ERROR_INVALID_DEVICE if the device specified by `dev` does not belong to the same clique as the other devices previously added to this multicast object.

See also

cuMulticastCreate, cuMulticastBindMem, cuMulticastBindAddr

Parameters

  * **mcHandle** – **[in]** Handle representing a multicast object.

  * **dev** – **[in]** Device that will be associated to the multicast object.

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_OUT_OF_MEMORY, CUDA_ERROR_INVALID_DEVICE, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_PERMITTED, CUDA_ERROR_NOT_SUPPORTED

`` CUresult cuMulticastBindAddr(CUmemGenericAllocationHandle mcHandle, size_t mcOffset, CUdeviceptr memptr, size_t size, unsigned long long flags) ``

Bind a memory allocation represented by a virtual address to a multicast object.

Binds a memory allocation specified by its mapped address `memptr` to a multicast object represented by `mcHandle`. The memory must have been allocated via cuMemCreate or ::cudaMallocAsync. The intended `size` of the bind, the offset in the multicast range `mcOffset` and `memptr` must be a multiple of the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_MINIMUM. For best performance however, `size`, `mcOffset` and `memptr` should be aligned to the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_RECOMMENDED.

The `size` cannot be larger than the size of the allocated memory. Similarly the `size` \+ `mcOffset` cannot be larger than the total size of the multicast object.

On systems with Rubin+ (SM_107+) GPUs, `memptr` may be aligned to 256 instead of the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_MINIMUM or CU_MULTICAST_GRANULARITY_RECOMMENDED. In such a case the `size` \+ `memptr` cannot be larger than the size of the allocated memory. Similarly the `size` \+ `mcOffset` \+ the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_MINIMUM cannot be larger than the size of the than the size of the multicast object. The next available mcOffset for the next bind will be mcOffset + size + the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_MINIMUM

Also note that the ability to accept a `memptr` that is not aligned to the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_MINIMUM or CU_MULTICAST_GRANULARITY_RECOMMENDED is limited by HW resources and may result in error CUDA_ERROR_MULTICAST_RESOURCE_FULL

The memory allocation must have beeen created on one of the devices that was added to the multicast team via cuMulticastAddDevice. Externally shareable as well as imported multicast objects can be bound only to externally shareable memory. Note that this call will return CUDA_ERROR_OUT_OF_MEMORY if there are insufficient resources required to perform the bind. This call may also return CUDA_ERROR_SYSTEM_NOT_READY if the necessary system software is not initialized or running.

This call may fail if the devices added via cuMulticastAddDevice do not belong to the same clique.

This call may return CUDA_ERROR_ILLEGAL_STATE if the system configuration is in an illegal state. In such cases, to continue using multicast, verify that the system configuration is in a valid state and all required driver daemons are running properly.

See also

cuMulticastCreate, cuMulticastAddDevice, cuMemCreate

See also

cuMulticastBindAddr_v2

Parameters

  * **mcHandle** – **[in]** Handle representing a multicast object.

  * **mcOffset** – **[in]** Offset into multicast va range for attachment.

  * **memptr** – **[in]** Virtual address of the memory allocation.

  * **size** – **[in]** Size of memory that will be bound to the multicast object.

  * **flags** – **[in]** Flags for future use, must be zero now.

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_INVALID_DEVICE, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_PERMITTED, CUDA_ERROR_NOT_SUPPORTED, CUDA_ERROR_OUT_OF_MEMORY, CUDA_ERROR_SYSTEM_NOT_READY, CUDA_ERROR_ILLEGAL_STATE, CUDA_ERROR_MULTICAST_RESOURCE_FULL

`` CUresult cuMulticastBindAddr_v2(CUmemGenericAllocationHandle mcHandle, CUdevice dev, size_t mcOffset, CUdeviceptr memptr, size_t size, unsigned long long flags) ``

Bind a memory allocation represented by a virtual address to a multicast object.

Binds a memory allocation specified by its mapped address `memptr` to a multicast object represented by `mcHandle`. The binding will be applicable for the device `dev`. The memory must have been allocated via cuMemCreate or ::cudaMallocAsync. The intended `size` of the bind, the offset in the multicast range `mcOffset` and `memptr` must be a multiple of the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_MINIMUM. For best performance however, `size`, `mcOffset` and `memptr` should be aligned to the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_RECOMMENDED.

The `size` cannot be larger than the size of the allocated memory. Similarly the `size` \+ `mcOffset` cannot be larger than the total size of the multicast object.

On systems with Rubin+ (SM_107+) GPUs, `memptr` may be aligned to 256 instead of the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_MINIMUM or CU_MULTICAST_GRANULARITY_RECOMMENDED. In such a case the `size` \+ `memptr` cannot be larger than the size of the allocated memory. Similarly the `size` \+ `mcOffset` \+ the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_MINIMUM cannot be larger than the size of the than the size of the multicast object. The next available mcOffset for the next bind will be mcOffset + size + the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_MINIMUM

Also note that the ability to accept a `memptr` that is not aligned to the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_MINIMUM or CU_MULTICAST_GRANULARITY_RECOMMENDED is limited by HW resources and may result in error CUDA_ERROR_MULTICAST_RESOURCE_FULL

For device memory, i.e., type CU_MEM_LOCATION_TYPE_DEVICE, the memory allocation must have been created on the device specified by `dev`. For host NUMA memory, i.e., type CU_MEM_LOCATION_TYPE_HOST_NUMA, the memory allocation must have been created on the CPU NUMA node closest to `dev`. That is, the value returned when querying CU_DEVICE_ATTRIBUTE_HOST_NUMA_ID for `dev`, must be the CPU NUMA node where the memory was allocated. In both cases, the device named by `dev` must have been added to the multicast team via cuMulticastAddDevice. Externally shareable as well as imported multicast objects can be bound only to externally shareable memory. Note that this call will return CUDA_ERROR_OUT_OF_MEMORY if there are insufficient resources required to perform the bind. This call may also return CUDA_ERROR_SYSTEM_NOT_READY if the necessary system software is not initialized or running.

This call may fail if the devices added via cuMulticastAddDevice do not belong to the same clique.

This call may return CUDA_ERROR_ILLEGAL_STATE if the system configuration is in an illegal state. In such cases, to continue using multicast, verify that the system configuration is in a valid state and all required driver daemons are running properly.

See also

cuMulticastCreate, cuMulticastAddDevice, cuMemCreate

Parameters

  * **mcHandle** – **[in]** Handle representing a multicast object.

  * **dev** – **[in]** The device that for which the multicast memory binding will be applicable.

  * **mcOffset** – **[in]** Offset into multicast va range for attachment.

  * **memptr** – **[in]** Virtual address of the memory allocation.

  * **size** – **[in]** Size of memory that will be bound to the multicast object.

  * **flags** – **[in]** Flags for future use, must be zero now.

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_INVALID_DEVICE, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_PERMITTED, CUDA_ERROR_NOT_SUPPORTED, CUDA_ERROR_OUT_OF_MEMORY, CUDA_ERROR_SYSTEM_NOT_READY, CUDA_ERROR_ILLEGAL_STATE, CUDA_ERROR_MULTICAST_RESOURCE_FULL

`` CUresult cuMulticastBindMem(CUmemGenericAllocationHandle mcHandle, size_t mcOffset, CUmemGenericAllocationHandle memHandle, size_t memOffset, size_t size, unsigned long long flags) ``

Bind a memory allocation represented by a handle to a multicast object.

Binds a memory allocation specified by `memHandle` and created via cuMemCreate to a multicast object represented by `mcHandle` and created via cuMulticastCreate. The intended `size` of the bind, the offset in the multicast range `mcOffset` as well as the offset in the memory `memOffset` must be a multiple of the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_MINIMUM. For best performance however, `size`, `mcOffset` and `memOffset` should be aligned to the granularity of the memory allocation(see ::cuMemGetAllocationGranularity) or to the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_RECOMMENDED.

The `size` \+ `memOffset` cannot be larger than the size of the allocated memory. Similarly the `size` \+ `mcOffset` cannot be larger than the size of the multicast object.

On systems with Rubin+ (SM_107+) GPUs, `memOffset` may be aligned to 256 instead of the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_MINIMUM or CU_MULTICAST_GRANULARITY_RECOMMENDED. In such a case the `size` \+ `memOffset` cannot be larger than the size of the allocated memory. Similarly the `size` \+ `mcOffset` \+ the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_MINIMUM cannot be larger than the size of the than the size of the multicast object. The next available mcOffset for the next bind will be mcOffset + size + the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_MINIMUM.

Also note that the ability to accept a `memOffset` that is not aligned to the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_MINIMUM or CU_MULTICAST_GRANULARITY_RECOMMENDED is limited by HW resources and may result in error CUDA_ERROR_MULTICAST_RESOURCE_FULL

The memory allocation must have beeen created on one of the devices that was added to the multicast team via cuMulticastAddDevice. Externally shareable as well as imported multicast objects can be bound only to externally shareable memory. Note that this call will return CUDA_ERROR_OUT_OF_MEMORY if there are insufficient resources required to perform the bind. This call may also return CUDA_ERROR_SYSTEM_NOT_READY if the necessary system software is not initialized or running.

This call may fail if the devices added via cuMulticastAddDevice do not belong to the same clique.

This call may return CUDA_ERROR_ILLEGAL_STATE if the system configuration is in an illegal state. In such cases, to continue using multicast, verify that the system configuration is in a valid state and all required driver daemons are running properly.

See also

cuMulticastCreate, cuMulticastAddDevice, cuMemCreate

See also

cuMulticastBindMem_v2

Parameters

  * **mcHandle** – **[in]** Handle representing a multicast object.

  * **mcOffset** – **[in]** Offset into the multicast object for attachment.

  * **memHandle** – **[in]** Handle representing a memory allocation.

  * **memOffset** – **[in]** Offset into the memory for attachment.

  * **size** – **[in]** Size of the memory that will be bound to the multicast object.

  * **flags** – **[in]** Flags for future use, must be zero for now.

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_INVALID_DEVICE, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_PERMITTED, CUDA_ERROR_NOT_SUPPORTED, CUDA_ERROR_OUT_OF_MEMORY, CUDA_ERROR_SYSTEM_NOT_READY, CUDA_ERROR_ILLEGAL_STATE, CUDA_ERROR_MULTICAST_RESOURCE_FULL

`` CUresult cuMulticastBindMem_v2(CUmemGenericAllocationHandle mcHandle, CUdevice dev, size_t mcOffset, CUmemGenericAllocationHandle memHandle, size_t memOffset, size_t size, unsigned long long flags) ``

Bind a memory allocation represented by a handle to a multicast object.

Binds a memory allocation specified by `memHandle` and created via cuMemCreate to a multicast object represented by `mcHandle` and created via cuMulticastCreate. The binding will be applicable for the device `dev`. The intended `size` of the bind, the offset in the multicast range `mcOffset` as well as the offset in the memory `memOffset` must be a multiple of the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_MINIMUM. For best performance however, `size`, `mcOffset` and `memOffset` should be aligned to the granularity of the memory allocation(see ::cuMemGetAllocationGranularity) or to the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_RECOMMENDED.

The `size` \+ `memOffset` cannot be larger than the size of the allocated memory. Similarly the `size` \+ `mcOffset` cannot be larger than the size of the multicast object.

On systems with Rubin+ (SM_107+) GPUs, `memOffset` may be aligned to 256 instead of the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_MINIMUM or CU_MULTICAST_GRANULARITY_RECOMMENDED. In such a case the `size` \+ `memOffset` cannot be larger than the size of the allocated memory. Similarly the `size` \+ `mcOffset` \+ the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_MINIMUM cannot be larger than the size of the than the size of the multicast object. The next available mcOffset for the next bind will be mcOffset + size + the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_MINIMUM.

Also note that the ability to accept a `memOffset` that is not aligned to the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_MINIMUM or CU_MULTICAST_GRANULARITY_RECOMMENDED is limited by HW resources and may result in error CUDA_ERROR_MULTICAST_RESOURCE_FULL

The memory allocation must have beeen created on one of the devices that was added to the multicast team via cuMulticastAddDevice. For device memory, i.e., type CU_MEM_LOCATION_TYPE_DEVICE, the memory allocation must have been created on the device specified by `dev`. For host NUMA memory, i.e., type CU_MEM_LOCATION_TYPE_HOST_NUMA, the memory allocation must have been created on the CPU NUMA node closest to `dev`. That is, the value returned when querying CU_DEVICE_ATTRIBUTE_HOST_NUMA_ID for `dev`, must be the CPU NUMA node where the memory was allocated. In both cases, the device named by `dev` must have been added to the multicast team via cuMulticastAddDevice. Externally shareable as well as imported multicast objects can be bound only to externally shareable memory. Note that this call will return CUDA_ERROR_OUT_OF_MEMORY if there are insufficient resources required to perform the bind. This call may also return CUDA_ERROR_SYSTEM_NOT_READY if the necessary system software is not initialized or running.

This call may fail if the devices added via cuMulticastAddDevice do not belong to the same clique.

This call may return CUDA_ERROR_ILLEGAL_STATE if the system configuration is in an illegal state. In such cases, to continue using multicast, verify that the system configuration is in a valid state and all required driver daemons are running properly.

See also

cuMulticastCreate, cuMulticastAddDevice, cuMemCreate

Parameters

  * **mcHandle** – **[in]** Handle representing a multicast object.

  * **dev** – **[in]** The device that for which the multicast memory binding will be applicable.

  * **mcOffset** – **[in]** Offset into the multicast object for attachment.

  * **memHandle** – **[in]** Handle representing a memory allocation.

  * **memOffset** – **[in]** Offset into the memory for attachment.

  * **size** – **[in]** Size of the memory that will be bound to the multicast object.

  * **flags** – **[in]** Flags for future use, must be zero for now.

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_INVALID_DEVICE, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_PERMITTED, CUDA_ERROR_NOT_SUPPORTED, CUDA_ERROR_OUT_OF_MEMORY, CUDA_ERROR_SYSTEM_NOT_READY, CUDA_ERROR_ILLEGAL_STATE, CUDA_ERROR_MULTICAST_RESOURCE_FULL

`` CUresult cuMulticastCreate(CUmemGenericAllocationHandle *mcHandle, const CUmulticastObjectProp *prop) ``

Create a generic allocation handle representing a multicast object described by the given properties.

This creates a multicast object as described by `prop`. The number of participating devices is specified by CUmulticastObjectProp::numDevices. Devices can be added to the multicast object via cuMulticastAddDevice. All participating devices must be added to the multicast object before memory can be bound to it. Memory is bound to the multicast object via cuMulticastBindMem, cuMulticastBindMem_v2, cuMulticastBindAddr, or cuMulticastBindAddr_v2. and can be unbound via cuMulticastUnbind. The total amount of memory that can be bound per device is specified by :CUmulticastObjectProp::size. This size must be a multiple of the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_MINIMUM. For best performance however, the size should be aligned to the value returned by cuMulticastGetGranularity with the flag CU_MULTICAST_GRANULARITY_RECOMMENDED.

After all participating devices have been added, multicast objects can also be mapped to a device’s virtual address space using the virtual memory management APIs (see cuMemMap and cuMemSetAccess). Multicast objects can also be shared with other processes by requesting a shareable handle via cuMemExportToShareableHandle. Note that the desired types of shareable handles must be specified in the bitmask CUmulticastObjectProp::handleTypes. Multicast objects can be released using the virtual memory management API cuMemRelease.

See also

cuMulticastAddDevice, cuMulticastBindMem, cuMulticastBindAddr, cuMulticastUnbind

See also

cuMemCreate, cuMemRelease, cuMemExportToShareableHandle, cuMemImportFromShareableHandle

See also

cuMulticastBindAddr_v2, cuMulticastBindMem_v2

Parameters

  * **mcHandle** – **[out]** Value of handle returned.

  * **prop** – **[in]** Properties of the multicast object to create.

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_OUT_OF_MEMORY, CUDA_ERROR_INVALID_DEVICE, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_PERMITTED, CUDA_ERROR_NOT_SUPPORTED

`` CUresult cuMulticastGetGranularity(size_t *granularity, const CUmulticastObjectProp *prop, CUmulticastGranularity_flags option) ``

Calculates either the minimal or recommended granularity for multicast object.

Calculates either the minimal or recommended granularity for a given set of multicast object properties and returns it in granularity. This granularity can be used as a multiple for size, bind offsets and address mappings of the multicast object.

See also

cuMulticastCreate, cuMulticastBindMem, cuMulticastBindAddr, cuMulticastUnbind

See also

cuMulticastBindMem_v2, cuMulticastBindAddr_v2

Parameters

  * **granularity** – **[out]** Returned granularity.

  * **prop** – **[in]** Properties of the multicast object.

  * **option** – **[in]** Determines which granularity to return.

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_PERMITTED, CUDA_ERROR_NOT_SUPPORTED

`` CUresult cuMulticastUnbind(CUmemGenericAllocationHandle mcHandle, CUdevice dev, size_t mcOffset, size_t size) ``

Unbind any memory allocations bound to a multicast object at a given offset and upto a given size.

Unbinds any memory allocations hosted on `dev` and bound to a multicast object at `mcOffset` and upto a given `size`. The intended `size` of the unbind and the offset in the multicast range ( `mcOffset` ) must be a multiple of the value returned by cuMulticastGetGranularity flag CU_MULTICAST_GRANULARITY_MINIMUM. The `size` \+ `mcOffset` cannot be larger than the total size of the multicast object.

See also

cuMulticastBindMem, cuMulticastBindAddr

See also

cuMulticastBindMem_v2, cuMulticastBindAddr_v2

Note

Warning: The `mcOffset` and the `size` must match the corresponding values specified during the bind call. Any other values may result in undefined behavior.

Parameters

  * **mcHandle** – **[in]** Handle representing a multicast object.

  * **dev** – **[in]** Device that hosts the memory allocation.

  * **mcOffset** – **[in]** Offset into the multicast object.

  * **size** – **[in]** Desired size to unbind.

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_INVALID_DEVICE, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_PERMITTED, CUDA_ERROR_NOT_SUPPORTED
