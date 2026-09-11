<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/group__CUDART__TYPES.html

#  6.2. Data types used by CUDA Runtime

Structs

CUuuid_st

cudaAccessPolicyWindow

Specifies an access policy for a window, a contiguous extent of memory beginning at base_ptr and ending at base_ptr + num_bytes.

cudaArrayMemoryRequirements

CUDA array and CUDA mipmapped array memory requirements.

cudaArraySparseProperties

Sparse CUDA array and CUDA mipmapped array properties.

cudaAsyncNotificationInfo_t

Information describing an async notification event.

cudaChannelFormatDesc

CUDA Channel format descriptor.

cudaChildGraphNodeParams

Child graph node parameters.

cudaConditionalNodeParams

CUDA conditional node parameters.

cudaDevResource

A tagged union describing different resources identified by the type field.

cudaDevSmResource

Data for SM-related resources All parameters in this structure are OUTPUT only.

cudaDevSmResourceGroupParams

Input data for splitting SMs.

cudaDevWorkqueueConfigResource

Data for workqueue configuration related resources.

cudaDevWorkqueueResource

Handle to a pre-existing workqueue related resource.

cudaDeviceProp

CUDA device properties.

cudaEglFrame

CUDA EGLFrame Descriptor - structure defining one frame of EGL.

cudaEglPlaneDesc

CUDA EGL Plane Descriptor - structure defining each plane of a CUDA EGLFrame.

cudaEventRecordNodeParams

Event record node parameters.

cudaEventWaitNodeParams

Event wait node parameters.

cudaExtent

CUDA extent.

cudaExternalMemoryBufferDesc

External memory buffer descriptor.

cudaExternalMemoryHandleDesc

External memory handle descriptor.

cudaExternalMemoryMipmappedArrayDesc

External memory mipmap descriptor.

cudaExternalSemaphoreHandleDesc

External semaphore handle descriptor.

cudaExternalSemaphoreSignalNodeParams

External semaphore signal node parameters.

cudaExternalSemaphoreSignalNodeParamsV2

External semaphore signal node parameters.

cudaExternalSemaphoreSignalParams

External semaphore signal parameters, compatible with driver type.

cudaExternalSemaphoreWaitNodeParams

External semaphore wait node parameters.

cudaExternalSemaphoreWaitNodeParamsV2

External semaphore wait node parameters.

cudaExternalSemaphoreWaitParams

External semaphore wait parameters, compatible with driver type.

cudaFuncAttributes

CUDA function attributes.

cudaGraphEdgeData

Optional annotation for edges in a CUDA graph.

cudaGraphExecUpdateResultInfo

Result information returned by cudaGraphExecUpdate.

cudaGraphInstantiateParams

Graph instantiation parameters.

cudaGraphKernelNodeUpdate

Struct to specify a single node update to pass as part of a larger array to cudaGraphKernelNodeUpdatesApply .

cudaGraphNodeParams

Graph node parameters.

cudaHostNodeParams

CUDA host node parameters.

cudaHostNodeParamsV2

CUDA host node parameters.

cudaIpcEventHandle_t

CUDA IPC event handle.

cudaIpcMemHandle_t

CUDA IPC memory handle.

cudaKernelNodeParams

CUDA GPU kernel node parameters.

cudaKernelNodeParamsV2

CUDA GPU kernel node parameters.

cudaLaunchAttribute

Launch attribute.

cudaLaunchConfig_t

CUDA extensible launch configuration.

cudaLaunchMemSyncDomainMap

Memory Synchronization Domain map.

cudaMemAccessDesc

Memory access descriptor.

cudaMemAllocNodeParams

Memory allocation node parameters.

cudaMemAllocNodeParamsV2

Memory allocation node parameters.

cudaMemFabricHandle_t

cudaMemFreeNodeParams

Memory free node parameters.

cudaMemLocation

Specifies a memory location.

cudaMemPoolProps

Specifies the properties of allocations made from the pool.

cudaMemPoolPtrExportData

Opaque data for exporting a pool allocation.

cudaMemcpy3DBatchOp

cudaMemcpy3DOperand

Struct representing an operand for copy with cudaMemcpy3DBatchAsync .

cudaMemcpy3DParms

CUDA 3D memory copying parameters.

cudaMemcpy3DPeerParms

CUDA 3D cross-device memory copying parameters.

cudaMemcpyAttributes

Attributes specific to copies within a batch.

cudaMemcpyNodeParams

Memcpy node parameters.

cudaMemsetParams

CUDA Memset node parameters.

cudaMemsetParamsV2

CUDA Memset node parameters.

cudaOffset3D

Struct representing offset into a cudaArray_t in elements.

cudaPitchedPtr

CUDA Pitched memory pointer.

cudaPointerAttributes

CUDA pointer attributes.

cudaPos

CUDA 3D position.

cudaResourceDesc

CUDA resource descriptor.

cudaResourceViewDesc

CUDA resource view descriptor.

cudaTextureDesc

CUDA texture descriptor.

cudalibraryHostUniversalFunctionAndDataTable

Unions

cudaLaunchAttributeValue

Launch attributes union; used as value field of cudaLaunchAttribute .

##  6.2.1. Macros

`` CUDART_CB __stdcall ``

`` CUDA_EGL_MAX_PLANES 3 ``

Maximum number of planes per frame.

`` CUDA_IPC_HANDLE_SIZE 64 ``

CUDA IPC Handle Size.

`` CU_UUID_HAS_BEEN_DEFINED ``

CUDA UUID types.

`` RESOURCE_ABI_BYTES 40 ``

`` cudaArrayColorAttachment 0x20 ``

Must be set in cudaExternalMemoryGetMappedMipmappedArray if the mipmapped array is used as a color target in a graphics API.

`` cudaArrayCubemap 0x04 ``

Must be set in cudaMalloc3DArray to create a cubemap CUDA array.

`` cudaArrayDefault 0x00 ``

Default CUDA array allocation flag.

`` cudaArrayDeferredMapping 0x80 ``

Must be set in cudaMallocArray, cudaMalloc3DArray or cudaMallocMipmappedArray in order to create a deferred mapping CUDA array or CUDA mipmapped array.

`` cudaArrayLayered 0x01 ``

Must be set in cudaMalloc3DArray to create a layered CUDA array.

`` cudaArraySparse 0x40 ``

Must be set in cudaMallocArray, cudaMalloc3DArray or cudaMallocMipmappedArray in order to create a sparse CUDA array or CUDA mipmapped array.

`` cudaArraySparsePropertiesSingleMipTail 0x1 ``

Indicates that the layered sparse CUDA array or CUDA mipmapped array has a single mip tail region for all layers.

`` cudaArraySurfaceLoadStore 0x02 ``

Must be set in cudaMallocArray or cudaMalloc3DArray in order to bind surfaces to the CUDA array.

`` cudaArrayTextureGather 0x08 ``

Must be set in cudaMallocArray or cudaMalloc3DArray in order to perform texture gather operations on the CUDA array.

`` cudaCpuDeviceId ((int)-1) ``

Device id that represents the CPU.

`` cudaDeviceBlockingSync 0x04 ``

Device flag - Use blocking synchronization.

`` Deprecated: ``

This flag was deprecated as of CUDA 4.0 and replaced with cudaDeviceScheduleBlockingSync.

`` cudaDeviceLmemResizeToMax 0x10 ``

Device flag - Keep local memory allocation after launch.

`` cudaDeviceMapHost 0x08 ``

Device flag - Support mapped pinned allocations.

`` cudaDeviceMask 0xff ``

Device flags mask.

`` cudaDeviceScheduleAuto 0x00 ``

Device flag - Automatic scheduling.

`` cudaDeviceScheduleBlockingSync 0x04 ``

Device flag - Use blocking synchronization.

`` cudaDeviceScheduleMask 0x07 ``

Device schedule flags mask.

`` cudaDeviceScheduleSpin 0x01 ``

Device flag - Spin default scheduling.

`` cudaDeviceScheduleYield 0x02 ``

Device flag - Yield default scheduling.

`` cudaDeviceSyncMemops 0x80 ``

Device flag - Ensure synchronous memory operations on this context will synchronize.

`` cudaEventBlockingSync 0x01 ``

Event uses blocking synchronization.

`` cudaEventDefault 0x00 ``

Default event flag.

`` cudaEventDisableTiming 0x02 ``

Event will not record timing data.

`` cudaEventInterprocess 0x04 ``

Event is suitable for interprocess use.

cudaEventDisableTiming must be set

`` cudaEventRecordDefault 0x00 ``

Default event record flag.

`` cudaEventRecordExternal 0x01 ``

Event is captured in the graph as an external event node when performing stream capture.

`` cudaEventWaitDefault 0x00 ``

Default event wait flag.

`` cudaEventWaitExternal 0x01 ``

Event is captured in the graph as an external event node when performing stream capture.

`` cudaExternalMemoryDedicated 0x1 ``

Indicates that the external memory object is a dedicated resource.

`` cudaExternalSemaphoreSignalSkipNvSciBufMemSync 0x01 ``

When the /p flags parameter of cudaExternalSemaphoreSignalParams contains this flag, it indicates that signaling an external semaphore object should skip performing appropriate memory synchronization operations over all the external memory objects that are imported as cudaExternalMemoryHandleTypeNvSciBuf, which otherwise are performed by default to ensure data coherency with other importers of the same NvSciBuf memory objects.

`` cudaExternalSemaphoreWaitSkipNvSciBufMemSync 0x02 ``

When the /p flags parameter of cudaExternalSemaphoreWaitParams contains this flag, it indicates that waiting an external semaphore object should skip performing appropriate memory synchronization operations over all the external memory objects that are imported as cudaExternalMemoryHandleTypeNvSciBuf, which otherwise are performed by default to ensure data coherency with other importers of the same NvSciBuf memory objects.

`` cudaGraphKernelNodePortDefault 0 ``

This port activates when the kernel has finished executing.

`` cudaGraphKernelNodePortLaunchCompletion 2 ``

This port activates when all blocks of the kernel have begun execution.

See also cudaLaunchAttributeLaunchCompletionEvent.

`` cudaGraphKernelNodePortProgrammatic 1 ``

This port activates when all blocks of the kernel have performed cudaTriggerProgrammaticLaunchCompletion() or have terminated.

It must be used with edge type cudaGraphDependencyTypeProgrammatic. See also cudaLaunchAttributeProgrammaticEvent.

`` cudaHostAllocDefault 0x00 ``

Default page-locked allocation flag.

`` cudaHostAllocMapped 0x02 ``

Map allocation into device space.

`` cudaHostAllocPortable 0x01 ``

Pinned memory accessible by all CUDA contexts.

`` cudaHostAllocWriteCombined 0x04 ``

Write-combined memory.

`` cudaHostRegisterDefault 0x00 ``

Default host memory registration flag.

`` cudaHostRegisterIoMemory 0x04 ``

Memory-mapped I/O space.

`` cudaHostRegisterMapped 0x02 ``

Map registered memory into device space.

`` cudaHostRegisterPortable 0x01 ``

Pinned memory accessible by all CUDA contexts.

`` cudaHostRegisterReadOnly 0x08 ``

Memory-mapped read-only.

`` cudaInitDeviceFlagsAreValid 0x01 ``

Tell the CUDA runtime that DeviceFlags is being set in cudaInitDevice call.

`` cudaInvalidDeviceId ((int)-2) ``

Device id that represents an invalid device.

`` cudaIpcMemLazyEnablePeerAccess 0x01 ``

Automatically enable peer access between remote devices as needed.

`` cudaKernelNodeAttrID cudaLaunchAttributeID ``

`` cudaKernelNodeAttrValue cudaLaunchAttributeValue ``

`` cudaKernelNodeAttributeAccessPolicyWindow cudaLaunchAttributeAccessPolicyWindow ``

`` cudaKernelNodeAttributeClusterDimension cudaLaunchAttributeClusterDimension ``

`` cudaKernelNodeAttributeClusterSchedulingPolicyPreference cudaLaunchAttributeClusterSchedulingPolicyPreference ``

`` cudaKernelNodeAttributeCooperative cudaLaunchAttributeCooperative ``

`` cudaKernelNodeAttributeDeviceUpdatableKernelNode cudaLaunchAttributeDeviceUpdatableKernelNode ``

`` cudaKernelNodeAttributeMemSyncDomain cudaLaunchAttributeMemSyncDomain ``

`` cudaKernelNodeAttributeMemSyncDomainMap cudaLaunchAttributeMemSyncDomainMap ``

`` cudaKernelNodeAttributeNvlinkUtilCentricScheduling cudaLaunchAttributeNvlinkUtilCentricScheduling ``

`` cudaKernelNodeAttributePreferredSharedMemoryCarveout cudaLaunchAttributePreferredSharedMemoryCarveout ``

`` cudaKernelNodeAttributePriority cudaLaunchAttributePriority ``

`` cudaMemAttachGlobal 0x01 ``

Memory can be accessed by any stream on any device.

`` cudaMemAttachHost 0x02 ``

Memory cannot be accessed by any stream on any device.

`` cudaMemAttachSingle 0x04 ``

Memory can only be accessed by a single stream on the associated device.

`` cudaMemPoolCreateUsageHwDecompress 0x2 ``

This flag, if set, indicates that the memory will be used as a buffer for hardware accelerated decompression.

`` cudaNvSciSyncAttrSignal 0x1 ``

When /p flags of cudaDeviceGetNvSciSyncAttributes is set to this, it indicates that application need signaler specific NvSciSyncAttr to be filled by cudaDeviceGetNvSciSyncAttributes.

`` cudaNvSciSyncAttrWait 0x2 ``

When /p flags of cudaDeviceGetNvSciSyncAttributes is set to this, it indicates that application need waiter specific NvSciSyncAttr to be filled by cudaDeviceGetNvSciSyncAttributes.

`` cudaOccupancyDefault 0x00 ``

Default behavior.

`` cudaOccupancyDisableCachingOverride 0x01 ``

Assume global caching is enabled and cannot be automatically turned off.

`` cudaPeerAccessDefault 0x00 ``

Default peer addressing enable flag.

`` cudaStreamAttrID cudaLaunchAttributeID ``

`` cudaStreamAttrValue cudaLaunchAttributeValue ``

`` cudaStreamAttributeAccessPolicyWindow cudaLaunchAttributeAccessPolicyWindow ``

`` cudaStreamAttributeMemSyncDomain cudaLaunchAttributeMemSyncDomain ``

`` cudaStreamAttributeMemSyncDomainMap cudaLaunchAttributeMemSyncDomainMap ``

`` cudaStreamAttributePriority cudaLaunchAttributePriority ``

`` cudaStreamAttributeSynchronizationPolicy cudaLaunchAttributeSynchronizationPolicy ``

`` cudaStreamDefault 0x00 ``

Default stream flag.

`` cudaStreamLegacy ((cudaStream_t)0x1) ``

Legacy stream handle.

Stream handle that can be passed as a cudaStream_t to use an implicit stream with legacy synchronization behavior.

See details of the synchronization behavior.

`` cudaStreamNonBlocking 0x01 ``

Stream does not synchronize with stream 0 (the NULL stream)

`` cudaStreamPerThread ((cudaStream_t)0x2) ``

Per-thread stream handle.

Stream handle that can be passed as a cudaStream_t to use an implicit stream with per-thread synchronization behavior.

See details of the synchronization behavior.

`` cudaSurfaceType1D 0x01 ``

`` cudaSurfaceType1DLayered 0xF1 ``

`` cudaSurfaceType2D 0x02 ``

`` cudaSurfaceType2DLayered 0xF2 ``

`` cudaSurfaceType3D 0x03 ``

`` cudaSurfaceTypeCubemap 0x0C ``

`` cudaSurfaceTypeCubemapLayered 0xFC ``

`` cudaTextureType1D 0x01 ``

`` cudaTextureType1DLayered 0xF1 ``

`` cudaTextureType2D 0x02 ``

`` cudaTextureType2DLayered 0xF2 ``

`` cudaTextureType3D 0x03 ``

`` cudaTextureTypeCubemap 0x0C ``

`` cudaTextureTypeCubemapLayered 0xFC ``

##  6.2.2. Enumerations

`` enum cudaAccessProperty ``

Specifies performance hint with cudaAccessPolicyWindow for hitProp and missProp members.

_Values:_

`` enumerator cudaAccessPropertyNormal ``

Normal cache persistence.

`` enumerator cudaAccessPropertyStreaming ``

Streaming access is less likely to persit from cache.

`` enumerator cudaAccessPropertyPersisting ``

Persisting access is more likely to persist in cache.

`` enum cudaAsyncNotificationType ``

Types of async notification that can occur.

_Values:_

`` enumerator cudaAsyncNotificationTypeOverBudget ``

Sent when the process has exceeded its device memory budget.

`` enum cudaAtomicOperation ``

CUDA-valid Atomic Operations.

_Values:_

`` enumerator cudaAtomicOperationIntegerAdd ``

`` enumerator cudaAtomicOperationIntegerMin ``

`` enumerator cudaAtomicOperationIntegerMax ``

`` enumerator cudaAtomicOperationIntegerIncrement ``

`` enumerator cudaAtomicOperationIntegerDecrement ``

`` enumerator cudaAtomicOperationAnd ``

`` enumerator cudaAtomicOperationOr ``

`` enumerator cudaAtomicOperationXOR ``

`` enumerator cudaAtomicOperationExchange ``

`` enumerator cudaAtomicOperationCAS ``

`` enumerator cudaAtomicOperationFloatAdd ``

`` enumerator cudaAtomicOperationFloatMin ``

`` enumerator cudaAtomicOperationFloatMax ``

`` enum cudaAtomicOperationCapability ``

CUDA-valid Atomic Operation capabilities.

_Values:_

`` enumerator cudaAtomicCapabilitySigned ``

`` enumerator cudaAtomicCapabilityUnsigned ``

`` enumerator cudaAtomicCapabilityReduction ``

`` enumerator cudaAtomicCapabilityScalar32 ``

`` enumerator cudaAtomicCapabilityScalar64 ``

`` enumerator cudaAtomicCapabilityScalar128 ``

`` enumerator cudaAtomicCapabilityVector32x4 ``

`` enum cudaCGScope ``

CUDA cooperative group scope.

_Values:_

`` enumerator cudaCGScopeInvalid ``

Invalid cooperative group scope.

`` enumerator cudaCGScopeGrid ``

Scope represented by a grid_group.

`` enumerator cudaCGScopeReserved ``

Reserved.

`` enum cudaChannelFormatKind ``

Channel format kind.

_Values:_

`` enumerator cudaChannelFormatKindSigned ``

Signed channel format.

`` enumerator cudaChannelFormatKindUnsigned ``

Unsigned channel format.

`` enumerator cudaChannelFormatKindFloat ``

Float channel format.

`` enumerator cudaChannelFormatKindNone ``

No channel format.

`` enumerator cudaChannelFormatKindNV12 ``

Unsigned 8-bit integers, planar 4:2:0 YUV format.

`` enumerator cudaChannelFormatKindUnsignedNormalized8X1 ``

1 channel unsigned 8-bit normalized integer

`` enumerator cudaChannelFormatKindUnsignedNormalized8X2 ``

2 channel unsigned 8-bit normalized integer

`` enumerator cudaChannelFormatKindUnsignedNormalized8X4 ``

4 channel unsigned 8-bit normalized integer

`` enumerator cudaChannelFormatKindUnsignedNormalized16X1 ``

1 channel unsigned 16-bit normalized integer

`` enumerator cudaChannelFormatKindUnsignedNormalized16X2 ``

2 channel unsigned 16-bit normalized integer

`` enumerator cudaChannelFormatKindUnsignedNormalized16X4 ``

4 channel unsigned 16-bit normalized integer

`` enumerator cudaChannelFormatKindSignedNormalized8X1 ``

1 channel signed 8-bit normalized integer

`` enumerator cudaChannelFormatKindSignedNormalized8X2 ``

2 channel signed 8-bit normalized integer

`` enumerator cudaChannelFormatKindSignedNormalized8X4 ``

4 channel signed 8-bit normalized integer

`` enumerator cudaChannelFormatKindSignedNormalized16X1 ``

1 channel signed 16-bit normalized integer

`` enumerator cudaChannelFormatKindSignedNormalized16X2 ``

2 channel signed 16-bit normalized integer

`` enumerator cudaChannelFormatKindSignedNormalized16X4 ``

4 channel signed 16-bit normalized integer

`` enumerator cudaChannelFormatKindUnsignedBlockCompressed1 ``

4 channel unsigned normalized block-compressed (BC1 compression) format

`` enumerator cudaChannelFormatKindUnsignedBlockCompressed1SRGB ``

4 channel unsigned normalized block-compressed (BC1 compression) format with sRGB encoding

`` enumerator cudaChannelFormatKindUnsignedBlockCompressed2 ``

4 channel unsigned normalized block-compressed (BC2 compression) format

`` enumerator cudaChannelFormatKindUnsignedBlockCompressed2SRGB ``

4 channel unsigned normalized block-compressed (BC2 compression) format with sRGB encoding

`` enumerator cudaChannelFormatKindUnsignedBlockCompressed3 ``

4 channel unsigned normalized block-compressed (BC3 compression) format

`` enumerator cudaChannelFormatKindUnsignedBlockCompressed3SRGB ``

4 channel unsigned normalized block-compressed (BC3 compression) format with sRGB encoding

`` enumerator cudaChannelFormatKindUnsignedBlockCompressed4 ``

1 channel unsigned normalized block-compressed (BC4 compression) format

`` enumerator cudaChannelFormatKindSignedBlockCompressed4 ``

1 channel signed normalized block-compressed (BC4 compression) format

`` enumerator cudaChannelFormatKindUnsignedBlockCompressed5 ``

2 channel unsigned normalized block-compressed (BC5 compression) format

`` enumerator cudaChannelFormatKindSignedBlockCompressed5 ``

2 channel signed normalized block-compressed (BC5 compression) format

`` enumerator cudaChannelFormatKindUnsignedBlockCompressed6H ``

3 channel unsigned half-float block-compressed (BC6H compression) format

`` enumerator cudaChannelFormatKindSignedBlockCompressed6H ``

3 channel signed half-float block-compressed (BC6H compression) format

`` enumerator cudaChannelFormatKindUnsignedBlockCompressed7 ``

4 channel unsigned normalized block-compressed (BC7 compression) format

`` enumerator cudaChannelFormatKindUnsignedBlockCompressed7SRGB ``

4 channel unsigned normalized block-compressed (BC7 compression) format with sRGB encoding

`` enumerator cudaChannelFormatKindUnsignedNormalized1010102 ``

4 channel unsigned normalized (10-bit, 10-bit, 10-bit, 2-bit) format

`` enumerator cudaChannelFormatKindUnsigned8Packed422 ``

4 channel unsigned 8-bit packed format, with 4:2:2 sampling

`` enumerator cudaChannelFormatKindUnsigned8Packed444 ``

4 channel unsigned 8-bit packed format, with 4:4:4 sampling

`` enumerator cudaChannelFormatKindUnsigned8SemiPlanar420 ``

3 channel unsigned 8-bit semi-planar format, with 4:2:0 sampling

`` enumerator cudaChannelFormatKindUnsigned16SemiPlanar420 ``

3 channel unsigned 16-bit semi-planar format, with 4:2:0 sampling

`` enumerator cudaChannelFormatKindUnsigned8SemiPlanar422 ``

3 channel unsigned 8-bit semi-planar format, with 4:2:2 sampling

`` enumerator cudaChannelFormatKindUnsigned16SemiPlanar422 ``

3 channel unsigned 16-bit semi-planar format, with 4:2:2 sampling

`` enumerator cudaChannelFormatKindUnsigned8SemiPlanar444 ``

3 channel unsigned 8-bit semi-planar format, with 4:4:4 sampling

`` enumerator cudaChannelFormatKindUnsigned16SemiPlanar444 ``

3 channel unsigned 16-bit semi-planar format, with 4:4:4 sampling

`` enumerator cudaChannelFormatKindUnsigned8Planar420 ``

3 channel unsigned 8-bit planar format, with 4:2:0 sampling

`` enumerator cudaChannelFormatKindUnsigned16Planar420 ``

3 channel unsigned 16-bit planar format, with 4:2:0 sampling

`` enumerator cudaChannelFormatKindUnsigned8Planar422 ``

3 channel unsigned 8-bit planar format, with 4:2:2 sampling

`` enumerator cudaChannelFormatKindUnsigned16Planar422 ``

3 channel unsigned 16-bit planar format, with 4:2:2 sampling

`` enumerator cudaChannelFormatKindUnsigned8Planar444 ``

3 channel unsigned 8-bit planar format, with 4:4:4 sampling

`` enumerator cudaChannelFormatKindUnsigned16Planar444 ``

3 channel unsigned 16-bit planar format, with 4:4:4 sampling

`` enum cudaClusterSchedulingPolicy ``

Cluster scheduling policies.

These may be passed to cudaFuncSetAttribute

_Values:_

`` enumerator cudaClusterSchedulingPolicyDefault ``

the default policy

`` enumerator cudaClusterSchedulingPolicySpread ``

spread the blocks within a cluster to the SMs

`` enumerator cudaClusterSchedulingPolicyLoadBalancing ``

allow the hardware to load-balance the blocks in a cluster to the SMs

`` enumerator cudaClusterSchedulingPolicyRubinDsmemLocality ``

`` enum cudaComputeMode ``

CUDA device compute modes.

_Values:_

`` enumerator cudaComputeModeDefault ``

Default compute mode (Multiple threads can use cudaSetDevice() with this device)

`` enumerator cudaComputeModeExclusive ``

Compute-exclusive-thread mode (Only one thread in one process will be able to use cudaSetDevice() with this device)

`` enumerator cudaComputeModeProhibited ``

Compute-prohibited mode (No threads can use cudaSetDevice() with this device)

`` enumerator cudaComputeModeExclusiveProcess ``

Compute-exclusive-process mode (Many threads in one process will be able to use cudaSetDevice() with this device)

`` enum cudaDevResourceType ``

Type of resource.

_Values:_

`` enumerator cudaDevResourceTypeInvalid ``

`` enumerator cudaDevResourceTypeSm ``

Streaming multiprocessors related information.

`` enumerator cudaDevResourceTypeWorkqueueConfig ``

Workqueue configuration related information.

`` enumerator cudaDevResourceTypeWorkqueue ``

Pre-existing workqueue related information.

`` enum cudaDevSmResourceGroup_flags ``

Flags for a CUdevSmResource group.

_Values:_

`` enumerator cudaDevSmResourceGroupDefault ``

`` enumerator cudaDevSmResourceGroupBackfill ``

Treats constraints as a hint, ignoring them if necessary to reach the requested smCount.

Lets smCount be a non-multiple of coscheduledSmCount, filling the difference between SM count and already assigned co-scheduled groupings with other SMs. When used with cudaDevSmResourceGroupLocalityDomainId, backfill fills up to the requested smCount using the target locality domain first, then SMs not attributed to any locality domain, then SMs from other locality domains. If no SMs can be found in the requested locality domain, cudaErrorInvalidResourceConfiguration is returned.

`` enumerator cudaDevSmResourceGroupLocalityDomainId ``

The SMs must be located on a specific locality domain, specified by localityDomainId.

`` enum cudaDevSmResourceSplitByCount_flags ``

_Values:_

`` enumerator cudaDevSmResourceSplitIgnoreSmCoscheduling ``

`` enumerator cudaDevSmResourceSplitMaxPotentialClusterSize ``

`` enum cudaDevWorkqueueConfigScope ``

Sharing scope for workqueues.

_Values:_

`` enumerator cudaDevWorkqueueConfigScopeDeviceCtx ``

Use all shared workqueue resources on the device.

Default driver behaviour.

`` enumerator cudaDevWorkqueueConfigScopeGreenCtxBalanced ``

When possible, use non-overlapping workqueue resources with other balanced green contexts.

`` enum cudaDeviceAttr ``

CUDA device attributes.

_Values:_

`` enumerator cudaDevAttrMaxThreadsPerBlock ``

Maximum number of threads per block.

`` enumerator cudaDevAttrMaxBlockDimX ``

Maximum block dimension X.

`` enumerator cudaDevAttrMaxBlockDimY ``

Maximum block dimension Y.

`` enumerator cudaDevAttrMaxBlockDimZ ``

Maximum block dimension Z.

`` enumerator cudaDevAttrMaxGridDimX ``

Maximum grid dimension X.

`` enumerator cudaDevAttrMaxGridDimY ``

Maximum grid dimension Y.

`` enumerator cudaDevAttrMaxGridDimZ ``

Maximum grid dimension Z.

`` enumerator cudaDevAttrMaxSharedMemoryPerBlock ``

Maximum shared memory available per block in bytes.

`` enumerator cudaDevAttrTotalConstantMemory ``

Memory available on device for **constant** variables in a CUDA C kernel in bytes.

`` enumerator cudaDevAttrWarpSize ``

Warp size in threads.

`` enumerator cudaDevAttrMaxPitch ``

Maximum pitch in bytes allowed by memory copies.

`` enumerator cudaDevAttrMaxRegistersPerBlock ``

Maximum number of 32-bit registers available per block.

`` enumerator cudaDevAttrClockRate ``

Peak clock frequency in kilohertz.

`` enumerator cudaDevAttrTextureAlignment ``

Alignment requirement for textures.

`` enumerator cudaDevAttrGpuOverlap ``

Device can possibly copy memory and execute a kernel concurrently.

`` enumerator cudaDevAttrMultiProcessorCount ``

Number of multiprocessors on device.

`` enumerator cudaDevAttrKernelExecTimeout ``

Specifies whether there is a run time limit on kernels.

`` enumerator cudaDevAttrIntegrated ``

Device is integrated with host memory.

`` enumerator cudaDevAttrCanMapHostMemory ``

Device can map host memory into CUDA address space.

`` enumerator cudaDevAttrComputeMode ``

Compute mode (See cudaComputeMode for details)

`` enumerator cudaDevAttrMaxTexture1DWidth ``

Maximum 1D texture width.

`` enumerator cudaDevAttrMaxTexture2DWidth ``

Maximum 2D texture width.

`` enumerator cudaDevAttrMaxTexture2DHeight ``

Maximum 2D texture height.

`` enumerator cudaDevAttrMaxTexture3DWidth ``

Maximum 3D texture width.

`` enumerator cudaDevAttrMaxTexture3DHeight ``

Maximum 3D texture height.

`` enumerator cudaDevAttrMaxTexture3DDepth ``

Maximum 3D texture depth.

`` enumerator cudaDevAttrMaxTexture2DLayeredWidth ``

Maximum 2D layered texture width.

`` enumerator cudaDevAttrMaxTexture2DLayeredHeight ``

Maximum 2D layered texture height.

`` enumerator cudaDevAttrMaxTexture2DLayeredLayers ``

Maximum layers in a 2D layered texture.

`` enumerator cudaDevAttrSurfaceAlignment ``

Alignment requirement for surfaces.

`` enumerator cudaDevAttrConcurrentKernels ``

Device can possibly execute multiple kernels concurrently.

`` enumerator cudaDevAttrEccEnabled ``

Device has ECC support enabled.

`` enumerator cudaDevAttrPciBusId ``

PCI bus ID of the device.

`` enumerator cudaDevAttrPciDeviceId ``

PCI device ID of the device.

`` enumerator cudaDevAttrTccDriver ``

Device is using TCC driver model.

`` enumerator cudaDevAttrMemoryClockRate ``

Peak memory clock frequency in kilohertz.

`` enumerator cudaDevAttrGlobalMemoryBusWidth ``

Global memory bus width in bits.

`` enumerator cudaDevAttrL2CacheSize ``

Size of L2 cache in bytes.

`` enumerator cudaDevAttrMaxThreadsPerMultiProcessor ``

Maximum resident threads per multiprocessor.

`` enumerator cudaDevAttrAsyncEngineCount ``

Number of asynchronous engines.

`` enumerator cudaDevAttrUnifiedAddressing ``

Device shares a unified address space with the host.

`` enumerator cudaDevAttrMaxTexture1DLayeredWidth ``

Maximum 1D layered texture width.

`` enumerator cudaDevAttrMaxTexture1DLayeredLayers ``

Maximum layers in a 1D layered texture.

`` enumerator cudaDevAttrMaxTexture2DGatherWidth ``

Maximum 2D texture width if cudaArrayTextureGather is set.

`` enumerator cudaDevAttrMaxTexture2DGatherHeight ``

Maximum 2D texture height if cudaArrayTextureGather is set.

`` enumerator cudaDevAttrMaxTexture3DWidthAlt ``

Alternate maximum 3D texture width.

`` enumerator cudaDevAttrMaxTexture3DHeightAlt ``

Alternate maximum 3D texture height.

`` enumerator cudaDevAttrMaxTexture3DDepthAlt ``

Alternate maximum 3D texture depth.

`` enumerator cudaDevAttrPciDomainId ``

PCI domain ID of the device.

`` enumerator cudaDevAttrTexturePitchAlignment ``

Pitch alignment requirement for textures.

`` enumerator cudaDevAttrMaxTextureCubemapWidth ``

Maximum cubemap texture width/height.

`` enumerator cudaDevAttrMaxTextureCubemapLayeredWidth ``

Maximum cubemap layered texture width/height.

`` enumerator cudaDevAttrMaxTextureCubemapLayeredLayers ``

Maximum layers in a cubemap layered texture.

`` enumerator cudaDevAttrMaxSurface1DWidth ``

Maximum 1D surface width.

`` enumerator cudaDevAttrMaxSurface2DWidth ``

Maximum 2D surface width.

`` enumerator cudaDevAttrMaxSurface2DHeight ``

Maximum 2D surface height.

`` enumerator cudaDevAttrMaxSurface3DWidth ``

Maximum 3D surface width.

`` enumerator cudaDevAttrMaxSurface3DHeight ``

Maximum 3D surface height.

`` enumerator cudaDevAttrMaxSurface3DDepth ``

Maximum 3D surface depth.

`` enumerator cudaDevAttrMaxSurface1DLayeredWidth ``

Maximum 1D layered surface width.

`` enumerator cudaDevAttrMaxSurface1DLayeredLayers ``

Maximum layers in a 1D layered surface.

`` enumerator cudaDevAttrMaxSurface2DLayeredWidth ``

Maximum 2D layered surface width.

`` enumerator cudaDevAttrMaxSurface2DLayeredHeight ``

Maximum 2D layered surface height.

`` enumerator cudaDevAttrMaxSurface2DLayeredLayers ``

Maximum layers in a 2D layered surface.

`` enumerator cudaDevAttrMaxSurfaceCubemapWidth ``

Maximum cubemap surface width.

`` enumerator cudaDevAttrMaxSurfaceCubemapLayeredWidth ``

Maximum cubemap layered surface width.

`` enumerator cudaDevAttrMaxSurfaceCubemapLayeredLayers ``

Maximum layers in a cubemap layered surface.

`` enumerator cudaDevAttrMaxTexture1DLinearWidth ``

Maximum 1D linear texture width.

`` enumerator cudaDevAttrMaxTexture2DLinearWidth ``

Maximum 2D linear texture width.

`` enumerator cudaDevAttrMaxTexture2DLinearHeight ``

Maximum 2D linear texture height.

`` enumerator cudaDevAttrMaxTexture2DLinearPitch ``

Maximum 2D linear texture pitch in bytes.

`` enumerator cudaDevAttrMaxTexture2DMipmappedWidth ``

Maximum mipmapped 2D texture width.

`` enumerator cudaDevAttrMaxTexture2DMipmappedHeight ``

Maximum mipmapped 2D texture height.

`` enumerator cudaDevAttrComputeCapabilityMajor ``

Major compute capability version number.

`` enumerator cudaDevAttrComputeCapabilityMinor ``

Minor compute capability version number.

`` enumerator cudaDevAttrMaxTexture1DMipmappedWidth ``

Maximum mipmapped 1D texture width.

`` enumerator cudaDevAttrStreamPrioritiesSupported ``

Device supports stream priorities.

`` enumerator cudaDevAttrGlobalL1CacheSupported ``

Device supports caching globals in L1.

`` enumerator cudaDevAttrLocalL1CacheSupported ``

Device supports caching locals in L1.

`` enumerator cudaDevAttrMaxSharedMemoryPerMultiprocessor ``

Maximum shared memory available per multiprocessor in bytes.

`` enumerator cudaDevAttrMaxRegistersPerMultiprocessor ``

Maximum number of 32-bit registers available per multiprocessor.

`` enumerator cudaDevAttrManagedMemory ``

Device can allocate managed memory on this system.

`` enumerator cudaDevAttrIsMultiGpuBoard ``

Device is on a multi-GPU board.

`` enumerator cudaDevAttrMultiGpuBoardGroupID ``

Unique identifier for a group of devices on the same multi-GPU board.

`` enumerator cudaDevAttrHostNativeAtomicSupported ``

Link between the device and the host supports native atomic operations.

`` enumerator cudaDevAttrSingleToDoublePrecisionPerfRatio ``

Ratio of single precision performance (in floating-point operations per second) to double precision performance.

`` enumerator cudaDevAttrPageableMemoryAccess ``

Device supports coherently accessing pageable memory without calling cudaHostRegister on it.

`` enumerator cudaDevAttrConcurrentManagedAccess ``

Device can coherently access managed memory concurrently with the CPU.

`` enumerator cudaDevAttrComputePreemptionSupported ``

Device supports Compute Preemption.

`` enumerator cudaDevAttrCanUseHostPointerForRegisteredMem ``

Device can access host registered memory at the same virtual address as the CPU.

`` enumerator cudaDevAttrReserved92 ``

`` enumerator cudaDevAttrReserved93 ``

`` enumerator cudaDevAttrReserved94 ``

`` enumerator cudaDevAttrCooperativeLaunch ``

Device supports launching cooperative kernels via cudaLaunchCooperativeKernel.

`` enumerator cudaDevAttrReserved96 ``

`` enumerator cudaDevAttrMaxSharedMemoryPerBlockOptin ``

The maximum optin shared memory per block.

This value may vary by chip. See cudaFuncSetAttribute

`` enumerator cudaDevAttrCanFlushRemoteWrites ``

Device supports flushing of outstanding remote writes.

`` enumerator cudaDevAttrHostRegisterSupported ``

Device supports host memory registration via cudaHostRegister.

`` enumerator cudaDevAttrPageableMemoryAccessUsesHostPageTables ``

Device accesses pageable memory via the host’s page tables.

`` enumerator cudaDevAttrDirectManagedMemAccessFromHost ``

Host can directly access managed memory on the device without migration.

`` enumerator cudaDevAttrMaxBlocksPerMultiprocessor ``

Maximum number of blocks per multiprocessor.

`` enumerator cudaDevAttrMaxPersistingL2CacheSize ``

Maximum L2 persisting lines capacity setting in bytes.

`` enumerator cudaDevAttrMaxAccessPolicyWindowSize ``

Maximum value of cudaAccessPolicyWindow::num_bytes.

`` enumerator cudaDevAttrReservedSharedMemoryPerBlock ``

Shared memory reserved by CUDA driver per block in bytes.

`` enumerator cudaDevAttrSparseCudaArraySupported ``

Device supports sparse CUDA arrays and sparse CUDA mipmapped arrays.

`` enumerator cudaDevAttrHostRegisterReadOnlySupported ``

Device supports using the cudaHostRegister flag cudaHostRegisterReadOnly to register memory that must be mapped as read-only to the GPU.

`` enumerator cudaDevAttrTimelineSemaphoreInteropSupported ``

External timeline semaphore interop is supported on the device.

`` enumerator cudaDevAttrMemoryPoolsSupported ``

Device supports using the cudaMallocAsync and ::cudaMemPool family of APIs.

`` enumerator cudaDevAttrGPUDirectRDMASupported ``

Device supports GPUDirect RDMA APIs, like nvidia_p2p_get_pages (see <https://docs.nvidia.com/cuda/gpudirect-rdma> for more information)

`` enumerator cudaDevAttrGPUDirectRDMAFlushWritesOptions ``

The returned attribute shall be interpreted as a bitmask, where the individual bits are listed in the cudaFlushGPUDirectRDMAWritesOptions enum.

`` enumerator cudaDevAttrGPUDirectRDMAWritesOrdering ``

GPUDirect RDMA writes to the device do not need to be flushed for consumers within the scope indicated by the returned attribute.

See cudaGPUDirectRDMAWritesOrdering for the numerical values returned here.

`` enumerator cudaDevAttrMemoryPoolSupportedHandleTypes ``

Handle types supported with mempool based IPC.

`` enumerator cudaDevAttrClusterLaunch ``

Indicates device supports cluster launch.

`` enumerator cudaDevAttrDeferredMappingCudaArraySupported ``

Device supports deferred mapping CUDA arrays and CUDA mipmapped arrays.

`` enumerator cudaDevAttrReserved122 ``

`` enumerator cudaDevAttrReserved123 ``

`` enumerator cudaDevAttrReserved124 ``

`` enumerator cudaDevAttrIpcEventSupport ``

Device supports IPC Events.

`` enumerator cudaDevAttrMemSyncDomainCount ``

Number of memory synchronization domains the device supports.

`` enumerator cudaDevAttrReserved127 ``

`` enumerator cudaDevAttrReserved128 ``

`` enumerator cudaDevAttrReserved129 ``

`` enumerator cudaDevAttrNumaConfig ``

NUMA configuration of a device: value is of type cudaDeviceNumaConfig enum.

`` enumerator cudaDevAttrNumaId ``

NUMA node ID of the GPU memory.

`` enumerator cudaDevAttrReserved132 ``

`` enumerator cudaDevAttrMpsEnabled ``

Contexts created on this device will be shared via MPS.

`` enumerator cudaDevAttrHostNumaId ``

NUMA ID of the host node closest to the device or -1 when system does not support NUMA.

`` enumerator cudaDevAttrD3D12CigSupported ``

Device supports CIG with D3D12.

`` enumerator cudaDevAttrVulkanCigSupported ``

Device supports CIG with Vulkan.

`` enumerator cudaDevAttrGpuPciDeviceId ``

The combined 16-bit PCI device ID and 16-bit PCI vendor ID.

`` enumerator cudaDevAttrGpuPciSubsystemId ``

The combined 16-bit PCI subsystem ID and 16-bit PCI subsystem vendor ID.

`` enumerator cudaDevAttrReserved141 ``

`` enumerator cudaDevAttrHostNumaMemoryPoolsSupported ``

Device supports HOST_NUMA location with the cudaMallocAsync and ::cudaMemPool family of APIs.

`` enumerator cudaDevAttrHostNumaMultinodeIpcSupported ``

Device supports HostNuma location IPC between nodes in a multi-node system.

`` enumerator cudaDevAttrHostMemoryPoolsSupported ``

Device suports HOST location with the ::cuMemAllocAsync and ::cuMemPool family of APIs.

`` enumerator cudaDevAttrReserved145 ``

`` enumerator cudaDevAttrOnlyPartialHostNativeAtomicSupported ``

Link between the device and the host supports only some native atomic operations.

`` enumerator cudaDevAttrAtomicReductionSupported ``

Device supports atomic reduction operations in stream batch memory operations.

`` enumerator cudaDevAttrLocalityDomainCount ``

Number of locality domains.

`` enumerator cudaDevAttrOversizedSharedMemoryPerBlock ``

The maximum oversized shared memory per block.

This value may vary by chip. See cudaFuncSetAttribute

`` enumerator cudaDevAttrCigStreamsSupported ``

Device supports CIG streams.

`` enumerator cudaDevAttrLocalityDomainMultiprocessorCount ``

Number of multiprocessors on each locality domain.

`` enumerator cudaDevAttrMax ``

`` enum cudaDeviceNumaConfig ``

CUDA device NUMA config.

_Values:_

`` enumerator cudaDeviceNumaConfigNone ``

The GPU is not a NUMA node.

`` enumerator cudaDeviceNumaConfigNumaNode ``

The GPU is a NUMA node, cudaDevAttrNumaId contains its NUMA ID.

`` enum cudaDeviceP2PAttr ``

CUDA device P2P attributes.

_Values:_

`` enumerator cudaDevP2PAttrPerformanceRank ``

A relative value indicating the performance of the link between two devices.

`` enumerator cudaDevP2PAttrAccessSupported ``

Peer access is enabled.

`` enumerator cudaDevP2PAttrNativeAtomicSupported ``

Native atomic operation over the link supported.

`` enumerator cudaDevP2PAttrCudaArrayAccessSupported ``

Accessing CUDA arrays over the link supported.

`` enumerator cudaDevP2PAttrOnlyPartialNativeAtomicSupported ``

Only some CUDA-valid atomic operations over the link are supported.

`` enum cudaDriverEntryPointQueryResult ``

Enum for status from obtaining driver entry points, used with ::cudaApiGetDriverEntryPoint.

_Values:_

`` enumerator cudaDriverEntryPointSuccess ``

Search for symbol found a match.

`` enumerator cudaDriverEntryPointSymbolNotFound ``

Search for symbol was not found.

`` enumerator cudaDriverEntryPointVersionNotSufficent ``

Search for symbol was found but version wasn’t great enough.

`` enum cudaEglColorFormat ``

CUDA EGL Color Format - The different planar and multiplanar formats currently supported for CUDA_EGL interops.

_Values:_

`` enumerator cudaEglColorFormatYUV420Planar ``

Y, U, V in three surfaces, each in a separate surface, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator cudaEglColorFormatYUV420SemiPlanar ``

Y, UV in two surfaces (UV as one surface) with VU byte ordering, width, height ratio same as YUV420Planar.

`` enumerator cudaEglColorFormatYUV422Planar ``

Y, U, V each in a separate surface, U/V width = 1/2 Y width, U/V height = Y height.

`` enumerator cudaEglColorFormatYUV422SemiPlanar ``

Y, UV in two surfaces with VU byte ordering, width, height ratio same as YUV422Planar.

`` enumerator cudaEglColorFormatARGB ``

R/G/B/A four channels in one surface with BGRA byte ordering.

`` enumerator cudaEglColorFormatRGBA ``

R/G/B/A four channels in one surface with ABGR byte ordering.

`` enumerator cudaEglColorFormatL ``

single luminance channel in one surface.

`` enumerator cudaEglColorFormatR ``

single color channel in one surface.

`` enumerator cudaEglColorFormatYUV444Planar ``

Y, U, V in three surfaces, each in a separate surface, U/V width = Y width, U/V height = Y height.

`` enumerator cudaEglColorFormatYUV444SemiPlanar ``

Y, UV in two surfaces (UV as one surface) with VU byte ordering, width, height ratio same as YUV444Planar.

`` enumerator cudaEglColorFormatYUYV422 ``

Y, U, V in one surface, interleaved as UYVY in one channel.

`` enumerator cudaEglColorFormatUYVY422 ``

Y, U, V in one surface, interleaved as YUYV in one channel.

`` enumerator cudaEglColorFormatABGR ``

R/G/B/A four channels in one surface with RGBA byte ordering.

`` enumerator cudaEglColorFormatBGRA ``

R/G/B/A four channels in one surface with ARGB byte ordering.

`` enumerator cudaEglColorFormatA ``

Alpha color format - one channel in one surface.

`` enumerator cudaEglColorFormatRG ``

R/G color format - two channels in one surface with GR byte ordering.

`` enumerator cudaEglColorFormatAYUV ``

Y, U, V, A four channels in one surface, interleaved as VUYA.

`` enumerator cudaEglColorFormatYVU444SemiPlanar ``

Y, VU in two surfaces (VU as one surface) with UV byte ordering, U/V width = Y width, U/V height = Y height.

`` enumerator cudaEglColorFormatYVU422SemiPlanar ``

Y, VU in two surfaces (VU as one surface) with UV byte ordering, U/V width = 1/2 Y width, U/V height = Y height.

`` enumerator cudaEglColorFormatYVU420SemiPlanar ``

Y, VU in two surfaces (VU as one surface) with UV byte ordering, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator cudaEglColorFormatY10V10U10_444SemiPlanar ``

Y10, V10U10 in two surfaces (VU as one surface) with UV byte ordering, U/V width = Y width, U/V height = Y height.

`` enumerator cudaEglColorFormatY10V10U10_420SemiPlanar ``

Y10, V10U10 in two surfaces (VU as one surface) with UV byte ordering, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator cudaEglColorFormatY12V12U12_444SemiPlanar ``

Y12, V12U12 in two surfaces (VU as one surface) with UV byte ordering, U/V width = Y width, U/V height = Y height.

`` enumerator cudaEglColorFormatY12V12U12_420SemiPlanar ``

Y12, V12U12 in two surfaces (VU as one surface) with UV byte ordering, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator cudaEglColorFormatVYUY_ER ``

Extended Range Y, U, V in one surface, interleaved as YVYU in one channel.

`` enumerator cudaEglColorFormatUYVY_ER ``

Extended Range Y, U, V in one surface, interleaved as YUYV in one channel.

`` enumerator cudaEglColorFormatYUYV_ER ``

Extended Range Y, U, V in one surface, interleaved as UYVY in one channel.

`` enumerator cudaEglColorFormatYVYU_ER ``

Extended Range Y, U, V in one surface, interleaved as VYUY in one channel.

`` enumerator cudaEglColorFormatYUVA_ER ``

Extended Range Y, U, V, A four channels in one surface, interleaved as AVUY.

`` enumerator cudaEglColorFormatAYUV_ER ``

Extended Range Y, U, V, A four channels in one surface, interleaved as VUYA.

`` enumerator cudaEglColorFormatYUV444Planar_ER ``

Extended Range Y, U, V in three surfaces, U/V width = Y width, U/V height = Y height.

`` enumerator cudaEglColorFormatYUV422Planar_ER ``

Extended Range Y, U, V in three surfaces, U/V width = 1/2 Y width, U/V height = Y height.

`` enumerator cudaEglColorFormatYUV420Planar_ER ``

Extended Range Y, U, V in three surfaces, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator cudaEglColorFormatYUV444SemiPlanar_ER ``

Extended Range Y, UV in two surfaces (UV as one surface) with VU byte ordering, U/V width = Y width, U/V height = Y height.

`` enumerator cudaEglColorFormatYUV422SemiPlanar_ER ``

Extended Range Y, UV in two surfaces (UV as one surface) with VU byte ordering, U/V width = 1/2 Y width, U/V height = Y height.

`` enumerator cudaEglColorFormatYUV420SemiPlanar_ER ``

Extended Range Y, UV in two surfaces (UV as one surface) with VU byte ordering, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator cudaEglColorFormatYVU444Planar_ER ``

Extended Range Y, V, U in three surfaces, U/V width = Y width, U/V height = Y height.

`` enumerator cudaEglColorFormatYVU422Planar_ER ``

Extended Range Y, V, U in three surfaces, U/V width = 1/2 Y width, U/V height = Y height.

`` enumerator cudaEglColorFormatYVU420Planar_ER ``

Extended Range Y, V, U in three surfaces, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator cudaEglColorFormatYVU444SemiPlanar_ER ``

Extended Range Y, VU in two surfaces (VU as one surface) with UV byte ordering, U/V width = Y width, U/V height = Y height.

`` enumerator cudaEglColorFormatYVU422SemiPlanar_ER ``

Extended Range Y, VU in two surfaces (VU as one surface) with UV byte ordering, U/V width = 1/2 Y width, U/V height = Y height.

`` enumerator cudaEglColorFormatYVU420SemiPlanar_ER ``

Extended Range Y, VU in two surfaces (VU as one surface) with UV byte ordering, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator cudaEglColorFormatBayerRGGB ``

Bayer format - one channel in one surface with interleaved RGGB ordering.

`` enumerator cudaEglColorFormatBayerBGGR ``

Bayer format - one channel in one surface with interleaved BGGR ordering.

`` enumerator cudaEglColorFormatBayerGRBG ``

Bayer format - one channel in one surface with interleaved GRBG ordering.

`` enumerator cudaEglColorFormatBayerGBRG ``

Bayer format - one channel in one surface with interleaved GBRG ordering.

`` enumerator cudaEglColorFormatBayer10RGGB ``

Bayer10 format - one channel in one surface with interleaved RGGB ordering.

Out of 16 bits, 10 bits used 6 bits No-op.

`` enumerator cudaEglColorFormatBayer10BGGR ``

Bayer10 format - one channel in one surface with interleaved BGGR ordering.

Out of 16 bits, 10 bits used 6 bits No-op.

`` enumerator cudaEglColorFormatBayer10GRBG ``

Bayer10 format - one channel in one surface with interleaved GRBG ordering.

Out of 16 bits, 10 bits used 6 bits No-op.

`` enumerator cudaEglColorFormatBayer10GBRG ``

Bayer10 format - one channel in one surface with interleaved GBRG ordering.

Out of 16 bits, 10 bits used 6 bits No-op.

`` enumerator cudaEglColorFormatBayer12RGGB ``

Bayer12 format - one channel in one surface with interleaved RGGB ordering.

Out of 16 bits, 12 bits used 4 bits No-op.

`` enumerator cudaEglColorFormatBayer12BGGR ``

Bayer12 format - one channel in one surface with interleaved BGGR ordering.

Out of 16 bits, 12 bits used 4 bits No-op.

`` enumerator cudaEglColorFormatBayer12GRBG ``

Bayer12 format - one channel in one surface with interleaved GRBG ordering.

Out of 16 bits, 12 bits used 4 bits No-op.

`` enumerator cudaEglColorFormatBayer12GBRG ``

Bayer12 format - one channel in one surface with interleaved GBRG ordering.

Out of 16 bits, 12 bits used 4 bits No-op.

`` enumerator cudaEglColorFormatBayer14RGGB ``

Bayer14 format - one channel in one surface with interleaved RGGB ordering.

Out of 16 bits, 14 bits used 2 bits No-op.

`` enumerator cudaEglColorFormatBayer14BGGR ``

Bayer14 format - one channel in one surface with interleaved BGGR ordering.

Out of 16 bits, 14 bits used 2 bits No-op.

`` enumerator cudaEglColorFormatBayer14GRBG ``

Bayer14 format - one channel in one surface with interleaved GRBG ordering.

Out of 16 bits, 14 bits used 2 bits No-op.

`` enumerator cudaEglColorFormatBayer14GBRG ``

Bayer14 format - one channel in one surface with interleaved GBRG ordering.

Out of 16 bits, 14 bits used 2 bits No-op.

`` enumerator cudaEglColorFormatBayer20RGGB ``

Bayer20 format - one channel in one surface with interleaved RGGB ordering.

Out of 32 bits, 20 bits used 12 bits No-op.

`` enumerator cudaEglColorFormatBayer20BGGR ``

Bayer20 format - one channel in one surface with interleaved BGGR ordering.

Out of 32 bits, 20 bits used 12 bits No-op.

`` enumerator cudaEglColorFormatBayer20GRBG ``

Bayer20 format - one channel in one surface with interleaved GRBG ordering.

Out of 32 bits, 20 bits used 12 bits No-op.

`` enumerator cudaEglColorFormatBayer20GBRG ``

Bayer20 format - one channel in one surface with interleaved GBRG ordering.

Out of 32 bits, 20 bits used 12 bits No-op.

`` enumerator cudaEglColorFormatYVU444Planar ``

Y, V, U in three surfaces, each in a separate surface, U/V width = Y width, U/V height = Y height.

`` enumerator cudaEglColorFormatYVU422Planar ``

Y, V, U in three surfaces, each in a separate surface, U/V width = 1/2 Y width, U/V height = Y height.

`` enumerator cudaEglColorFormatYVU420Planar ``

Y, V, U in three surfaces, each in a separate surface, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator cudaEglColorFormatBayerIspRGGB ``

Nvidia proprietary Bayer ISP format - one channel in one surface with interleaved RGGB ordering and mapped to opaque integer datatype.

`` enumerator cudaEglColorFormatBayerIspBGGR ``

Nvidia proprietary Bayer ISP format - one channel in one surface with interleaved BGGR ordering and mapped to opaque integer datatype.

`` enumerator cudaEglColorFormatBayerIspGRBG ``

Nvidia proprietary Bayer ISP format - one channel in one surface with interleaved GRBG ordering and mapped to opaque integer datatype.

`` enumerator cudaEglColorFormatBayerIspGBRG ``

Nvidia proprietary Bayer ISP format - one channel in one surface with interleaved GBRG ordering and mapped to opaque integer datatype.

`` enumerator cudaEglColorFormatBayerBCCR ``

Bayer format - one channel in one surface with interleaved BCCR ordering.

`` enumerator cudaEglColorFormatBayerRCCB ``

Bayer format - one channel in one surface with interleaved RCCB ordering.

`` enumerator cudaEglColorFormatBayerCRBC ``

Bayer format - one channel in one surface with interleaved CRBC ordering.

`` enumerator cudaEglColorFormatBayerCBRC ``

Bayer format - one channel in one surface with interleaved CBRC ordering.

`` enumerator cudaEglColorFormatBayer10CCCC ``

Bayer10 format - one channel in one surface with interleaved CCCC ordering.

Out of 16 bits, 10 bits used 6 bits No-op.

`` enumerator cudaEglColorFormatBayer12BCCR ``

Bayer12 format - one channel in one surface with interleaved BCCR ordering.

Out of 16 bits, 12 bits used 4 bits No-op.

`` enumerator cudaEglColorFormatBayer12RCCB ``

Bayer12 format - one channel in one surface with interleaved RCCB ordering.

Out of 16 bits, 12 bits used 4 bits No-op.

`` enumerator cudaEglColorFormatBayer12CRBC ``

Bayer12 format - one channel in one surface with interleaved CRBC ordering.

Out of 16 bits, 12 bits used 4 bits No-op.

`` enumerator cudaEglColorFormatBayer12CBRC ``

Bayer12 format - one channel in one surface with interleaved CBRC ordering.

Out of 16 bits, 12 bits used 4 bits No-op.

`` enumerator cudaEglColorFormatBayer12CCCC ``

Bayer12 format - one channel in one surface with interleaved CCCC ordering.

Out of 16 bits, 12 bits used 4 bits No-op.

`` enumerator cudaEglColorFormatY ``

Color format for single Y plane.

`` enumerator cudaEglColorFormatYUV420SemiPlanar_2020 ``

Y, UV in two surfaces (UV as one surface) U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator cudaEglColorFormatYVU420SemiPlanar_2020 ``

Y, VU in two surfaces (VU as one surface) U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator cudaEglColorFormatYUV420Planar_2020 ``

Y, U, V in three surfaces, each in a separate surface, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator cudaEglColorFormatYVU420Planar_2020 ``

Y, V, U in three surfaces, each in a separate surface, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator cudaEglColorFormatYUV420SemiPlanar_709 ``

Y, UV in two surfaces (UV as one surface) U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator cudaEglColorFormatYVU420SemiPlanar_709 ``

Y, VU in two surfaces (VU as one surface) U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator cudaEglColorFormatYUV420Planar_709 ``

Y, U, V in three surfaces, each in a separate surface, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator cudaEglColorFormatYVU420Planar_709 ``

Y, V, U in three surfaces, each in a separate surface, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator cudaEglColorFormatY10V10U10_420SemiPlanar_709 ``

Y10, V10U10 in two surfaces (VU as one surface) U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator cudaEglColorFormatY10V10U10_420SemiPlanar_2020 ``

Y10, V10U10 in two surfaces (VU as one surface) U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator cudaEglColorFormatY10V10U10_422SemiPlanar_2020 ``

Y10, V10U10 in two surfaces (VU as one surface) U/V width = 1/2 Y width, U/V height = Y height.

`` enumerator cudaEglColorFormatY10V10U10_422SemiPlanar ``

Y10, V10U10 in two surfaces (VU as one surface) U/V width = 1/2 Y width, U/V height = Y height.

`` enumerator cudaEglColorFormatY10V10U10_422SemiPlanar_709 ``

Y10, V10U10 in two surfaces (VU as one surface) U/V width = 1/2 Y width, U/V height = Y height.

`` enumerator cudaEglColorFormatY_ER ``

Extended Range Color format for single Y plane.

`` enumerator cudaEglColorFormatY_709_ER ``

Extended Range Color format for single Y plane.

`` enumerator cudaEglColorFormatY10_ER ``

Extended Range Color format for single Y10 plane.

`` enumerator cudaEglColorFormatY10_709_ER ``

Extended Range Color format for single Y10 plane.

`` enumerator cudaEglColorFormatY12_ER ``

Extended Range Color format for single Y12 plane.

`` enumerator cudaEglColorFormatY12_709_ER ``

Extended Range Color format for single Y12 plane.

`` enumerator cudaEglColorFormatYUVA ``

Y, U, V, A four channels in one surface, interleaved as AVUY.

`` enumerator cudaEglColorFormatYVYU ``

Y, U, V in one surface, interleaved as YVYU in one channel.

`` enumerator cudaEglColorFormatVYUY ``

Y, U, V in one surface, interleaved as VYUY in one channel.

`` enumerator cudaEglColorFormatY10V10U10_420SemiPlanar_ER ``

Extended Range Y10, V10U10 in two surfaces (VU as one surface) U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator cudaEglColorFormatY10V10U10_420SemiPlanar_709_ER ``

Extended Range Y10, V10U10 in two surfaces (VU as one surface) U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator cudaEglColorFormatY10V10U10_444SemiPlanar_ER ``

Extended Range Y10, V10U10 in two surfaces (VU as one surface) U/V width = Y width, U/V height = Y height.

`` enumerator cudaEglColorFormatY10V10U10_444SemiPlanar_709_ER ``

Extended Range Y10, V10U10 in two surfaces (VU as one surface) U/V width = Y width, U/V height = Y height.

`` enumerator cudaEglColorFormatY12V12U12_420SemiPlanar_ER ``

Extended Range Y12, V12U12 in two surfaces (VU as one surface) U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator cudaEglColorFormatY12V12U12_420SemiPlanar_709_ER ``

Extended Range Y12, V12U12 in two surfaces (VU as one surface) U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator cudaEglColorFormatY12V12U12_444SemiPlanar_ER ``

Extended Range Y12, V12U12 in two surfaces (VU as one surface) U/V width = Y width, U/V height = Y height.

`` enumerator cudaEglColorFormatY12V12U12_444SemiPlanar_709_ER ``

Extended Range Y12, V12U12 in two surfaces (VU as one surface) U/V width = Y width, U/V height = Y height.

`` enumerator cudaEglColorFormatUYVY709 ``

Y, U, V in one surface, interleaved as UYVY in one channel.

`` enumerator cudaEglColorFormatUYVY709_ER ``

Extended Range Y, U, V in one surface, interleaved as UYVY in one channel.

`` enumerator cudaEglColorFormatUYVY2020 ``

Y, U, V in one surface, interleaved as UYVY in one channel.

`` enum cudaEglFrameType ``

CUDA EglFrame type - array or pointer.

_Values:_

`` enumerator cudaEglFrameTypeArray ``

Frame type CUDA array.

`` enumerator cudaEglFrameTypePitch ``

Frame type CUDA pointer.

`` enum cudaEglResourceLocationFlags ``

Resource location flags- sysmem or vidmem.

For CUDA context on iGPU, since video and system memory are equivalent - these flags will not have an effect on the execution.

For CUDA context on dGPU, applications can use the flag cudaEglResourceLocationFlags to give a hint about the desired location.

cudaEglResourceLocationSysmem \- the frame data is made resident on the system memory to be accessed by CUDA.

cudaEglResourceLocationVidmem \- the frame data is made resident on the dedicated video memory to be accessed by CUDA.

There may be an additional latency due to new allocation and data migration, if the frame is produced on a different memory.

_Values:_

`` enumerator cudaEglResourceLocationSysmem ``

Resource location sysmem.

`` enumerator cudaEglResourceLocationVidmem ``

Resource location vidmem.

`` enum cudaError ``

CUDA error types

_Values:_

`` enumerator cudaSuccess ``

The API call returned with no errors.

In the case of query calls, this also means that the operation being queried is complete (see cudaEventQuery() and cudaStreamQuery()).

`` enumerator cudaErrorInvalidValue ``

This indicates that one or more of the parameters passed to the API call is not within an acceptable range of values.

`` enumerator cudaErrorMemoryAllocation ``

The API call failed because it was unable to allocate enough memory or other resources to perform the requested operation.

`` enumerator cudaErrorInitializationError ``

The API call failed because the CUDA driver and runtime could not be initialized.

`` enumerator cudaErrorCudartUnloading ``

This indicates that a CUDA Runtime API call cannot be executed because it is being called during process shut down, at a point in time after CUDA driver has been unloaded.

`` enumerator cudaErrorProfilerDisabled ``

This indicates profiler is not initialized for this run.

This can happen when the application is running with external profiling tools like visual profiler.

`` enumerator cudaErrorProfilerNotInitialized ``

`` Deprecated: ``

This error return is deprecated as of CUDA 5.0. It is no longer an error to attempt to enable/disable the profiling via cudaProfilerStart or cudaProfilerStop without initialization.

`` enumerator cudaErrorProfilerAlreadyStarted ``

`` Deprecated: ``

This error return is deprecated as of CUDA 5.0. It is no longer an error to call cudaProfilerStart() when profiling is already enabled.

`` enumerator cudaErrorProfilerAlreadyStopped ``

`` Deprecated: ``

This error return is deprecated as of CUDA 5.0. It is no longer an error to call cudaProfilerStop() when profiling is already disabled.

`` enumerator cudaErrorInvalidConfiguration ``

This indicates that a kernel launch is requesting resources that can never be satisfied by the current device.

Requesting more shared memory per block than the device supports will trigger this error, as will requesting too many threads or blocks. See cudaDeviceProp for more device limitations.

`` enumerator cudaErrorVersionTranslation ``

This indicates that the driver is newer than the runtime version and returned graph node parameter information that the runtime does not understand and is unable to translate.

`` enumerator cudaErrorInvalidPitchValue ``

This indicates that one or more of the pitch-related parameters passed to the API call is not within the acceptable range for pitch.

`` enumerator cudaErrorInvalidSymbol ``

This indicates that the symbol name/identifier passed to the API call is not a valid name or identifier.

`` enumerator cudaErrorInvalidHostPointer ``

This indicates that at least one host pointer passed to the API call is not a valid host pointer.

`` Deprecated: ``

This error return is deprecated as of CUDA 10.1.

`` enumerator cudaErrorInvalidDevicePointer ``

This indicates that at least one device pointer passed to the API call is not a valid device pointer.

`` Deprecated: ``

This error return is deprecated as of CUDA 10.1.

`` enumerator cudaErrorInvalidTexture ``

This indicates that the texture passed to the API call is not a valid texture.

`` enumerator cudaErrorInvalidTextureBinding ``

This indicates that the texture binding is not valid.

This occurs if you call ::cudaGetTextureAlignmentOffset() with an unbound texture.

`` enumerator cudaErrorInvalidChannelDescriptor ``

This indicates that the channel descriptor passed to the API call is not valid.

This occurs if the format is not one of the formats specified by cudaChannelFormatKind, or if one of the dimensions is invalid.

`` enumerator cudaErrorInvalidMemcpyDirection ``

This indicates that the direction of the memcpy passed to the API call is not one of the types specified by cudaMemcpyKind.

`` enumerator cudaErrorAddressOfConstant ``

This indicated that the user has taken the address of a constant variable, which was forbidden up until the CUDA 3.1 release.

`` Deprecated: ``

This error return is deprecated as of CUDA 3.1. Variables in constant memory may now have their address taken by the runtime via cudaGetSymbolAddress().

`` enumerator cudaErrorTextureFetchFailed ``

This indicated that a texture fetch was not able to be performed.

This was previously used for device emulation of texture operations.

`` Deprecated: ``

This error return is deprecated as of CUDA 3.1. Device emulation mode was removed with the CUDA 3.1 release.

`` enumerator cudaErrorTextureNotBound ``

This indicated that a texture was not bound for access.

This was previously used for device emulation of texture operations.

`` Deprecated: ``

This error return is deprecated as of CUDA 3.1. Device emulation mode was removed with the CUDA 3.1 release.

`` enumerator cudaErrorSynchronizationError ``

This indicated that a synchronization operation had failed.

This was previously used for some device emulation functions.

`` Deprecated: ``

This error return is deprecated as of CUDA 3.1. Device emulation mode was removed with the CUDA 3.1 release.

`` enumerator cudaErrorInvalidFilterSetting ``

This indicates that a non-float texture was being accessed with linear filtering.

This is not supported by CUDA.

`` enumerator cudaErrorInvalidNormSetting ``

This indicates that an attempt was made to read an unsupported data type as a normalized float.

This is not supported by CUDA.

`` enumerator cudaErrorMixedDeviceExecution ``

Mixing of device and device emulation code was not allowed.

`` Deprecated: ``

This error return is deprecated as of CUDA 3.1. Device emulation mode was removed with the CUDA 3.1 release.

`` enumerator cudaErrorNotYetImplemented ``

This indicates that the API call is not yet implemented.

Production releases of CUDA will never return this error.

`` Deprecated: ``

This error return is deprecated as of CUDA 4.1.

`` enumerator cudaErrorMemoryValueTooLarge ``

This indicated that an emulated device pointer exceeded the 32-bit address range.

`` Deprecated: ``

This error return is deprecated as of CUDA 3.1. Device emulation mode was removed with the CUDA 3.1 release.

`` enumerator cudaErrorStubLibrary ``

This indicates that the CUDA driver that the application has loaded is a stub library.

Applications that run with the stub rather than a real driver loaded will result in CUDA API returning this error.

`` enumerator cudaErrorInsufficientDriver ``

This indicates that the installed NVIDIA CUDA driver is older than the CUDA runtime library.

This is not a supported configuration. Users should install an updated NVIDIA display driver to allow the application to run.

`` enumerator cudaErrorCallRequiresNewerDriver ``

This indicates that the API call requires a newer CUDA driver than the one currently installed.

Users should install an updated NVIDIA CUDA driver to allow the API call to succeed.

`` enumerator cudaErrorInvalidSurface ``

This indicates that the surface passed to the API call is not a valid surface.

`` enumerator cudaErrorDuplicateVariableName ``

This indicates that multiple global or constant variables (across separate CUDA source files in the application) share the same string name.

`` enumerator cudaErrorDuplicateTextureName ``

This indicates that multiple textures (across separate CUDA source files in the application) share the same string name.

`` enumerator cudaErrorDuplicateSurfaceName ``

This indicates that multiple surfaces (across separate CUDA source files in the application) share the same string name.

`` enumerator cudaErrorDevicesUnavailable ``

This indicates that all CUDA devices are busy or unavailable at the current time.

Devices are often busy/unavailable due to use of cudaComputeModeProhibited, cudaComputeModeExclusiveProcess, or when long running CUDA kernels have filled up the GPU and are blocking new work from starting. They can also be unavailable due to memory constraints on a device that already has active CUDA work being performed.

`` enumerator cudaErrorIncompatibleDriverContext ``

This indicates that the current context is not compatible with this the CUDA Runtime.

This can only occur if you are using CUDA Runtime/Driver interoperability and have created an existing Driver context using the driver API. The Driver context may be incompatible either because the Driver context was created using an older version of the API, because the Runtime API call expects a primary driver context and the Driver context is not primary, or because the Driver context has been destroyed. Please see Interactions with the CUDA Driver API” for more information.

`` enumerator cudaErrorMissingConfiguration ``

The device function being invoked (usually via cudaLaunchKernel()) was not previously configured via the ::cudaConfigureCall() function.

`` enumerator cudaErrorPriorLaunchFailure ``

This indicated that a previous kernel launch failed.

This was previously used for device emulation of kernel launches.

`` Deprecated: ``

This error return is deprecated as of CUDA 3.1. Device emulation mode was removed with the CUDA 3.1 release.

`` enumerator cudaErrorLaunchMaxDepthExceeded ``

This error indicates that a device runtime grid launch did not occur because the depth of the child grid would exceed the maximum supported number of nested grid launches.

`` enumerator cudaErrorLaunchFileScopedTex ``

This error indicates that a grid launch did not occur because the kernel uses file-scoped textures which are unsupported by the device runtime.

Kernels launched via the device runtime only support textures created with the Texture Object API’s.

`` enumerator cudaErrorLaunchFileScopedSurf ``

This error indicates that a grid launch did not occur because the kernel uses file-scoped surfaces which are unsupported by the device runtime.

Kernels launched via the device runtime only support surfaces created with the Surface Object API’s.

`` enumerator cudaErrorSyncDepthExceeded ``

This error indicates that a call to cudaDeviceSynchronize made from the device runtime failed because the call was made at grid depth greater than than either the default (2 levels of grids) or user specified device limit cudaLimitDevRuntimeSyncDepth.

To be able to synchronize on launched grids at a greater depth successfully, the maximum nested depth at which cudaDeviceSynchronize will be called must be specified with the cudaLimitDevRuntimeSyncDepth limit to the cudaDeviceSetLimit api before the host-side launch of a kernel using the device runtime. Keep in mind that additional levels of sync depth require the runtime to reserve large amounts of device memory that cannot be used for user allocations. Note that cudaDeviceSynchronize made from device runtime is only supported on devices of compute capability < 9.0.

`` enumerator cudaErrorLaunchPendingCountExceeded ``

This error indicates that a device runtime grid launch failed because the launch would exceed the limit cudaLimitDevRuntimePendingLaunchCount.

For this launch to proceed successfully, cudaDeviceSetLimit must be called to set the cudaLimitDevRuntimePendingLaunchCount to be higher than the upper bound of outstanding launches that can be issued to the device runtime. Keep in mind that raising the limit of pending device runtime launches will require the runtime to reserve device memory that cannot be used for user allocations.

`` enumerator cudaErrorInvalidDeviceFunction ``

The requested device function does not exist or is not compiled for the proper device architecture.

`` enumerator cudaErrorNoDevice ``

This indicates that no CUDA-capable devices were detected by the installed CUDA driver.

`` enumerator cudaErrorInvalidDevice ``

This indicates that the device ordinal supplied by the user does not correspond to a valid CUDA device or that the action requested is invalid for the specified device.

`` enumerator cudaErrorDeviceNotLicensed ``

This indicates that the device doesn’t have a valid Grid License.

`` enumerator cudaErrorSoftwareValidityNotEstablished ``

By default, the CUDA runtime may perform a minimal set of self-tests, as well as CUDA driver tests, to establish the validity of both.

Introduced in CUDA 11.2, this error return indicates that at least one of these tests has failed and the validity of either the runtime or the driver could not be established.

`` enumerator cudaErrorStartupFailure ``

This indicates an internal startup failure in the CUDA runtime.

`` enumerator cudaErrorInvalidKernelImage ``

This indicates that the device kernel image is invalid.

`` enumerator cudaErrorDeviceUninitialized ``

This most frequently indicates that there is no context bound to the current thread.

This can also be returned if the context passed to an API call is not a valid handle (such as a context that has had ::cuCtxDestroy() invoked on it). This can also be returned if a user mixes different API versions (i.e. 3010 context with 3020 API calls). See ::cuCtxGetApiVersion() for more details.

`` enumerator cudaErrorMapBufferObjectFailed ``

This indicates that the buffer object could not be mapped.

`` enumerator cudaErrorUnmapBufferObjectFailed ``

This indicates that the buffer object could not be unmapped.

`` enumerator cudaErrorArrayIsMapped ``

This indicates that the specified array is currently mapped and thus cannot be destroyed.

`` enumerator cudaErrorAlreadyMapped ``

This indicates that the resource is already mapped.

`` enumerator cudaErrorNoKernelImageForDevice ``

This indicates that there is no kernel image available that is suitable for the device.

This can occur when a user specifies code generation options for a particular CUDA source file that do not include the corresponding device configuration.

`` enumerator cudaErrorAlreadyAcquired ``

This indicates that a resource has already been acquired.

`` enumerator cudaErrorNotMapped ``

This indicates that a resource is not mapped.

`` enumerator cudaErrorNotMappedAsArray ``

This indicates that a mapped resource is not available for access as an array.

`` enumerator cudaErrorNotMappedAsPointer ``

This indicates that a mapped resource is not available for access as a pointer.

`` enumerator cudaErrorECCUncorrectable ``

This indicates that an uncorrectable ECC error was detected during execution.

`` enumerator cudaErrorUnsupportedLimit ``

This indicates that the cudaLimit passed to the API call is not supported by the active device.

`` enumerator cudaErrorDeviceAlreadyInUse ``

This indicates that a call tried to access an exclusive-thread device that is already in use by a different thread.

`` enumerator cudaErrorPeerAccessUnsupported ``

This error indicates that P2P access is not supported across the given devices.

`` enumerator cudaErrorInvalidPtx ``

A PTX compilation failed.

The runtime may fall back to compiling PTX if an application does not contain a suitable binary for the current device.

`` enumerator cudaErrorInvalidGraphicsContext ``

This indicates an error with the OpenGL or DirectX context.

`` enumerator cudaErrorNvlinkUncorrectable ``

This indicates that an uncorrectable NVLink error was detected during the execution.

`` enumerator cudaErrorJitCompilerNotFound ``

This indicates that the PTX JIT compiler library was not found.

The JIT Compiler library is used for PTX compilation. The runtime may fall back to compiling PTX if an application does not contain a suitable binary for the current device.

`` enumerator cudaErrorUnsupportedPtxVersion ``

This indicates that the provided PTX was compiled with an unsupported toolchain.

The most common reason for this, is the PTX was generated by a compiler newer than what is supported by the CUDA driver and PTX JIT compiler.

`` enumerator cudaErrorJitCompilationDisabled ``

This indicates that the JIT compilation was disabled.

The JIT compilation compiles PTX. The runtime may fall back to compiling PTX if an application does not contain a suitable binary for the current device.

`` enumerator cudaErrorUnsupportedExecAffinity ``

This indicates that the provided execution affinity is not supported by the device.

`` enumerator cudaErrorUnsupportedDevSideSync ``

This indicates that the code to be compiled by the PTX JIT contains unsupported call to cudaDeviceSynchronize.

`` enumerator cudaErrorContained ``

This indicates that an exception occurred on the device that is now contained by the GPU’s error containment capability.

Common causes are - a. Certain types of invalid accesses of peer GPU memory over nvlink b. Certain classes of hardware errors This leaves the process in an inconsistent state and any further CUDA work will return the same error. To continue using CUDA, the process must be terminated and relaunched.

`` enumerator cudaErrorInsufficientLoaderVersion ``

This indicates that loader version is insufficient for Fatbin.

`` enumerator cudaErrorInvalidSource ``

This indicates that the device kernel source is invalid.

`` enumerator cudaErrorFileNotFound ``

This indicates that the file specified was not found.

`` enumerator cudaErrorSharedObjectSymbolNotFound ``

This indicates that a link to a shared object failed to resolve.

`` enumerator cudaErrorSharedObjectInitFailed ``

This indicates that initialization of a shared object failed.

`` enumerator cudaErrorOperatingSystem ``

This error indicates that an OS call failed.

`` enumerator cudaErrorInvalidResourceHandle ``

This indicates that a resource handle passed to the API call was not valid.

Resource handles are opaque types like cudaStream_t and cudaEvent_t.

`` enumerator cudaErrorIllegalState ``

This indicates that a resource required by the API call is not in a valid state to perform the requested operation.

`` enumerator cudaErrorLossyQuery ``

This indicates an attempt was made to introspect an object in a way that would discard semantically important information.

This is either due to the object using funtionality newer than the API version used to introspect it or omission of optional return arguments.

`` enumerator cudaErrorSymbolNotFound ``

This indicates that a named symbol was not found.

Examples of symbols are global/constant variable names, driver function names, texture names, and surface names.

`` enumerator cudaErrorNotReady ``

This indicates that asynchronous operations issued previously have not completed yet.

This result is not actually an error, but must be indicated differently than cudaSuccess (which indicates completion). Calls that may return this value include cudaEventQuery() and cudaStreamQuery().

`` enumerator cudaErrorIllegalAddress ``

The device encountered a load or store instruction on an invalid memory address.

This leaves the process in an inconsistent state and any further CUDA work will return the same error. To continue using CUDA, the process must be terminated and relaunched.

`` enumerator cudaErrorLaunchOutOfResources ``

This indicates that a launch did not occur because it did not have appropriate resources.

Although this error is similar to cudaErrorInvalidConfiguration, this error usually indicates that the user has attempted to pass too many arguments to the device kernel, or the kernel launch specifies too many threads for the kernel’s register count.

`` enumerator cudaErrorLaunchTimeout ``

This indicates that the device kernel took too long to execute.

This can only occur if timeouts are enabled - see the device attribute cudaDevAttrKernelExecTimeout for more information. This leaves the process in an inconsistent state and any further CUDA work will return the same error. To continue using CUDA, the process must be terminated and relaunched.

`` enumerator cudaErrorLaunchIncompatibleTexturing ``

This error indicates a kernel launch that uses an incompatible texturing mode.

`` enumerator cudaErrorPeerAccessAlreadyEnabled ``

This error indicates that a call to cudaDeviceEnablePeerAccess() is trying to re-enable peer addressing on from a context which has already had peer addressing enabled.

`` enumerator cudaErrorPeerAccessNotEnabled ``

This error indicates that cudaDeviceDisablePeerAccess() is trying to disable peer addressing which has not been enabled yet via cudaDeviceEnablePeerAccess().

`` enumerator cudaErrorSetOnActiveProcess ``

This indicates that the user has called cudaSetValidDevices(), cudaSetDeviceFlags(), cudaD3D9SetDirect3DDevice(), cudaD3D10SetDirect3DDevice, cudaD3D11SetDirect3DDevice(), or cudaVDPAUSetVDPAUDevice() after initializing the CUDA runtime by calling non-device management operations (allocating memory and launching kernels are examples of non-device management operations).

This error can also be returned if using runtime/driver interoperability and there is an existing ::CUcontext active on the host thread.

`` enumerator cudaErrorContextIsDestroyed ``

This error indicates that the context current to the calling thread has been destroyed using ::cuCtxDestroy, or is a primary context which has not yet been initialized.

`` enumerator cudaErrorAssert ``

An assert triggered in device code during kernel execution.

The device cannot be used again. All existing allocations are invalid. To continue using CUDA, the process must be terminated and relaunched.

`` enumerator cudaErrorTooManyPeers ``

This error indicates that the hardware resources required to enable peer access have been exhausted for one or more of the devices passed to ::cudaEnablePeerAccess().

`` enumerator cudaErrorHostMemoryAlreadyRegistered ``

This error indicates that the memory range passed to cudaHostRegister() has already been registered.

`` enumerator cudaErrorHostMemoryNotRegistered ``

This error indicates that the pointer passed to cudaHostUnregister() does not correspond to any currently registered memory region.

`` enumerator cudaErrorHardwareStackError ``

Device encountered an error in the call stack during kernel execution, possibly due to stack corruption or exceeding the stack size limit.

This leaves the process in an inconsistent state and any further CUDA work will return the same error. To continue using CUDA, the process must be terminated and relaunched.

`` enumerator cudaErrorIllegalInstruction ``

The device encountered an illegal instruction during kernel execution This leaves the process in an inconsistent state and any further CUDA work will return the same error.

To continue using CUDA, the process must be terminated and relaunched.

`` enumerator cudaErrorMisalignedAddress ``

The device encountered a load or store instruction on a memory address which is not aligned.

This leaves the process in an inconsistent state and any further CUDA work will return the same error. To continue using CUDA, the process must be terminated and relaunched.

`` enumerator cudaErrorInvalidAddressSpace ``

While executing a kernel, the device encountered an instruction which can only operate on memory locations in certain address spaces (global, shared, or local), but was supplied a memory address not belonging to an allowed address space.

This leaves the process in an inconsistent state and any further CUDA work will return the same error. To continue using CUDA, the process must be terminated and relaunched.

`` enumerator cudaErrorInvalidPc ``

The device encountered an invalid program counter.

This leaves the process in an inconsistent state and any further CUDA work will return the same error. To continue using CUDA, the process must be terminated and relaunched.

`` enumerator cudaErrorLaunchFailure ``

An exception occurred on the device while executing a kernel.

Common causes include dereferencing an invalid device pointer and accessing out of bounds shared memory. Less common cases can be system specific - more information about these cases can be found in the system specific user guide. This leaves the process in an inconsistent state and any further CUDA work will return the same error. To continue using CUDA, the process must be terminated and relaunched.

`` enumerator cudaErrorCooperativeLaunchTooLarge ``

This error indicates that the number of blocks launched per grid for a kernel that was launched via either cudaLaunchCooperativeKernel exceeds the maximum number of blocks as allowed by cudaOccupancyMaxActiveBlocksPerMultiprocessor or cudaOccupancyMaxActiveBlocksPerMultiprocessorWithFlags times the number of multiprocessors as specified by the device attribute cudaDevAttrMultiProcessorCount.

`` enumerator cudaErrorTensorMemoryLeak ``

An exception occurred on the device while exiting a kernel using tensor memory: the tensor memory was not completely deallocated.

This leaves the process in an inconsistent state and any further CUDA work will return the same error. To continue using CUDA, the process must be terminated and relaunched.

`` enumerator cudaErrorNotPermitted ``

This error indicates the attempted operation is not permitted.

`` enumerator cudaErrorNotSupported ``

This error indicates the attempted operation is not supported on the current system or device.

`` enumerator cudaErrorSystemNotReady ``

This error indicates that the system is not yet ready to start any CUDA work.

To continue using CUDA, verify the system configuration is in a valid state and all required driver daemons are actively running. More information about this error can be found in the system specific user guide.

`` enumerator cudaErrorSystemDriverMismatch ``

This error indicates that there is a mismatch between the versions of the display driver and the CUDA driver.

Refer to the compatibility documentation for supported versions.

`` enumerator cudaErrorCompatNotSupportedOnDevice ``

This error indicates that the system was upgraded to run with forward compatibility but the visible hardware detected by CUDA does not support this configuration.

Refer to the compatibility documentation for the supported hardware matrix or ensure that only supported hardware is visible during initialization via the CUDA_VISIBLE_DEVICES environment variable.

`` enumerator cudaErrorMpsConnectionFailed ``

This error indicates that the MPS client failed to connect to the MPS control daemon or the MPS server.

`` enumerator cudaErrorMpsRpcFailure ``

This error indicates that the remote procedural call between the MPS server and the MPS client failed.

`` enumerator cudaErrorMpsServerNotReady ``

This error indicates that the MPS server is not ready to accept new MPS client requests.

This error can be returned when the MPS server is in the process of recovering from a fatal failure.

`` enumerator cudaErrorMpsMaxClientsReached ``

This error indicates that the hardware resources required to create MPS client have been exhausted.

`` enumerator cudaErrorMpsMaxConnectionsReached ``

This error indicates the the hardware resources required to device connections have been exhausted.

`` enumerator cudaErrorMpsClientTerminated ``

This error indicates that the MPS client has been terminated by the server.

To continue using CUDA, the process must be terminated and relaunched.

`` enumerator cudaErrorCdpNotSupported ``

This error indicates, that the program is using CUDA Dynamic Parallelism, but the current configuration, like MPS, does not support it.

`` enumerator cudaErrorCdpVersionMismatch ``

This error indicates, that the program contains an unsupported interaction between different versions of CUDA Dynamic Parallelism.

`` enumerator cudaErrorStreamCaptureUnsupported ``

The operation is not permitted when the stream is capturing.

`` enumerator cudaErrorStreamCaptureInvalidated ``

The current capture sequence on the stream has been invalidated due to a previous error.

`` enumerator cudaErrorStreamCaptureMerge ``

The operation would have resulted in a merge of two independent capture sequences.

`` enumerator cudaErrorStreamCaptureUnmatched ``

The capture was not initiated in this stream.

`` enumerator cudaErrorStreamCaptureUnjoined ``

The capture sequence contains a fork that was not joined to the primary stream.

`` enumerator cudaErrorStreamCaptureIsolation ``

A dependency would have been created which crosses the capture sequence boundary.

Only implicit in-stream ordering dependencies are allowed to cross the boundary.

`` enumerator cudaErrorStreamCaptureImplicit ``

The operation would have resulted in a disallowed implicit dependency on a current capture sequence from cudaStreamLegacy.

`` enumerator cudaErrorCapturedEvent ``

The operation is not permitted on an event which was last recorded in a capturing stream.

`` enumerator cudaErrorStreamCaptureWrongThread ``

A stream capture sequence not initiated with the cudaStreamCaptureModeRelaxed argument to cudaStreamBeginCapture was passed to cudaStreamEndCapture in a different thread.

`` enumerator cudaErrorTimeout ``

This indicates that the wait operation has timed out.

`` enumerator cudaErrorGraphExecUpdateFailure ``

This error indicates that the graph update was not performed because it included changes which violated constraints specific to instantiated graph update.

`` enumerator cudaErrorExternalDevice ``

This indicates that an error has occurred in a device outside of GPU.

It can be a synchronous error w.r.t. CUDA API or an asynchronous error from the external device. In case of asynchronous error, it means that if cuda was waiting for an external device’s signal before consuming shared data, the external device signaled an error indicating that the data is not valid for consumption. This leaves the process in an inconsistent state and any further CUDA work will return the same error. To continue using CUDA, the process must be terminated and relaunched. In case of synchronous error, it means that one or more external devices have encountered an error and cannot complete the operation.

`` enumerator cudaErrorInvalidClusterSize ``

This indicates that a kernel launch error has occurred due to cluster misconfiguration.

`` enumerator cudaErrorFunctionNotLoaded ``

Indiciates a function handle is not loaded when calling an API that requires a loaded function.

`` enumerator cudaErrorInvalidResourceType ``

This error indicates one or more resources passed in are not valid resource types for the operation.

`` enumerator cudaErrorInvalidResourceConfiguration ``

This error indicates one or more resources are insufficient or non-applicable for the operation.

`` enumerator cudaErrorStreamDetached ``

This error indicates that the requested operation is not permitted because the stream is in a detached state.

This can occur if the green context associated with the stream has been destroyed, limiting the stream’s operational capabilities.

`` enumerator cudaErrorGraphRecaptureFailure ``

This error indicates that a graph recapture failed and had to be terminated.

`` enumerator cudaErrorFabricNotReady ``

This error indicates GPU fabric is not ready within the bounded wait while the fabric manager probe is still in progress.

Applications may retry after a delay; for the initialization wait budget, see environment variables such as CUDA_FABRIC_INIT_TIMEOUT_MS.

`` enumerator cudaErrorUnknown ``

This indicates that an unknown internal error has occurred.

`` enumerator cudaErrorApiFailureBase ``

`` enum cudaExternalMemoryHandleType ``

External memory handle types.

_Values:_

`` enumerator cudaExternalMemoryHandleTypeOpaqueFd ``

Handle is an opaque file descriptor.

`` enumerator cudaExternalMemoryHandleTypeOpaqueWin32 ``

Handle is an opaque shared NT handle.

`` enumerator cudaExternalMemoryHandleTypeOpaqueWin32Kmt ``

Handle is an opaque, globally shared handle.

`` enumerator cudaExternalMemoryHandleTypeD3D12Heap ``

Handle is a D3D12 heap object.

`` enumerator cudaExternalMemoryHandleTypeD3D12Resource ``

Handle is a D3D12 committed resource.

`` enumerator cudaExternalMemoryHandleTypeD3D11Resource ``

Handle is a shared NT handle to a D3D11 resource.

`` enumerator cudaExternalMemoryHandleTypeD3D11ResourceKmt ``

Handle is a globally shared handle to a D3D11 resource.

`` enumerator cudaExternalMemoryHandleTypeNvSciBuf ``

Handle is an NvSciBuf object.

`` enum cudaExternalSemaphoreHandleType ``

External semaphore handle types.

_Values:_

`` enumerator cudaExternalSemaphoreHandleTypeOpaqueFd ``

Handle is an opaque file descriptor.

`` enumerator cudaExternalSemaphoreHandleTypeOpaqueWin32 ``

Handle is an opaque shared NT handle.

`` enumerator cudaExternalSemaphoreHandleTypeOpaqueWin32Kmt ``

Handle is an opaque, globally shared handle.

`` enumerator cudaExternalSemaphoreHandleTypeD3D12Fence ``

Handle is a shared NT handle referencing a D3D12 fence object.

`` enumerator cudaExternalSemaphoreHandleTypeD3D11Fence ``

Handle is a shared NT handle referencing a D3D11 fence object.

`` enumerator cudaExternalSemaphoreHandleTypeNvSciSync ``

Opaque handle to NvSciSync Object.

`` enumerator cudaExternalSemaphoreHandleTypeKeyedMutex ``

Handle is a shared NT handle referencing a D3D11 keyed mutex object.

`` enumerator cudaExternalSemaphoreHandleTypeKeyedMutexKmt ``

Handle is a shared KMT handle referencing a D3D11 keyed mutex object.

`` enumerator cudaExternalSemaphoreHandleTypeTimelineSemaphoreFd ``

Handle is an opaque handle file descriptor referencing a timeline semaphore.

`` enumerator cudaExternalSemaphoreHandleTypeTimelineSemaphoreWin32 ``

Handle is an opaque handle file descriptor referencing a timeline semaphore.

`` enum cudaFabricOpStatusInfo ``

Fabric operation status info.

_Values:_

`` enumerator cudaFabricOpStatusInfoSuccess ``

`` enumerator cudaFabricOpStatusInfoLast ``

`` enumerator cudaFabricOpStatusInfoMax ``

`` enum cudaFabricOpStatusSource ``

Fabric operation status source.

_Values:_

`` enumerator cudaFabricOpStatusSourceMbarrierV1 ``

1B-aligned 1B-wide status from an mbarrier.layout::v1

`` enumerator cudaFabricOpStatusSourceMax ``

`` enum cudaFlushGPUDirectRDMAWritesOptions ``

CUDA GPUDirect RDMA flush writes APIs supported on the device.

_Values:_

`` enumerator cudaFlushGPUDirectRDMAWritesOptionHost ``

cudaDeviceFlushGPUDirectRDMAWrites() and its CUDA Driver API counterpart are supported on the device.

`` enumerator cudaFlushGPUDirectRDMAWritesOptionMemOps ``

The ::CU_STREAM_WAIT_VALUE_FLUSH flag and the ::CU_STREAM_MEM_OP_FLUSH_REMOTE_WRITES MemOp are supported on the CUDA device.

`` enum cudaFlushGPUDirectRDMAWritesScope ``

CUDA GPUDirect RDMA flush writes scopes.

_Values:_

`` enumerator cudaFlushGPUDirectRDMAWritesToOwner ``

Blocks until remote writes are visible to the CUDA device context owning the data.

`` enumerator cudaFlushGPUDirectRDMAWritesToAllDevices ``

Blocks until remote writes are visible to all CUDA device contexts.

`` enum cudaFlushGPUDirectRDMAWritesTarget ``

CUDA GPUDirect RDMA flush writes targets.

_Values:_

`` enumerator cudaFlushGPUDirectRDMAWritesTargetCurrentDevice ``

Sets the target for cudaDeviceFlushGPUDirectRDMAWrites() to the currently active CUDA device context.

`` enum cudaFuncAttribute ``

CUDA function attributes that can be set using cudaFuncSetAttribute.

_Values:_

`` enumerator cudaFuncAttributeMaxDynamicSharedMemorySize ``

Maximum dynamic shared memory size.

`` enumerator cudaFuncAttributePreferredSharedMemoryCarveout ``

Preferred shared memory-L1 cache split.

`` enumerator cudaFuncAttributeClusterDimMustBeSet ``

Indicator to enforce valid cluster dimension specification on kernel launch.

`` enumerator cudaFuncAttributeRequiredClusterWidth ``

Required cluster width.

`` enumerator cudaFuncAttributeRequiredClusterHeight ``

Required cluster height.

`` enumerator cudaFuncAttributeRequiredClusterDepth ``

Required cluster depth.

`` enumerator cudaFuncAttributeNonPortableClusterSizeAllowed ``

Whether non-portable cluster scheduling policy is supported.

`` enumerator cudaFuncAttributeClusterSchedulingPolicyPreference ``

Required cluster scheduling policy preference.

`` enumerator cudaFuncAttributeSharedMemoryMode ``

Setting that controls a kernel’s use of non-portable or oversized shared memory configurations.

`` enumerator cudaFuncAttributeMax ``

`` enum cudaFuncCache ``

CUDA function cache configurations.

_Values:_

`` enumerator cudaFuncCachePreferNone ``

Default function cache configuration, no preference.

`` enumerator cudaFuncCachePreferShared ``

Prefer larger shared memory and smaller L1 cache

`` enumerator cudaFuncCachePreferL1 ``

Prefer larger L1 cache and smaller shared memory.

`` enumerator cudaFuncCachePreferEqual ``

Prefer equal size L1 cache and shared memory.

`` enum cudaGPUDirectRDMAWritesOrdering ``

CUDA GPUDirect RDMA flush writes ordering features of the device.

_Values:_

`` enumerator cudaGPUDirectRDMAWritesOrderingNone ``

The device does not natively support ordering of GPUDirect RDMA writes.

::cudaFlushGPUDirectRDMAWrites() can be leveraged if supported.

`` enumerator cudaGPUDirectRDMAWritesOrderingOwner ``

Natively, the device can consistently consume GPUDirect RDMA writes, although other CUDA devices may not.

`` enumerator cudaGPUDirectRDMAWritesOrderingAllDevices ``

Any CUDA device in the system can consistently consume GPUDirect RDMA writes to this device.

`` enum cudaGetDriverEntryPointFlags ``

Flags to specify search options to be used with cudaGetDriverEntryPoint For more details see ::cuGetProcAddress.

_Values:_

`` enumerator cudaEnableDefault ``

Default search mode for driver symbols.

`` enumerator cudaEnableLegacyStream ``

Search for legacy versions of driver symbols.

`` enumerator cudaEnablePerThreadDefaultStream ``

Search for per-thread versions of driver symbols.

`` enum cudaGraphChildGraphNodeOwnership ``

Child graph node ownership.

_Values:_

`` enumerator cudaGraphChildGraphOwnershipClone ``

Default behavior for a child graph node.

Child graph is cloned into the parent and memory allocation/free nodes can’t be present in the child graph.

`` enumerator cudaGraphChildGraphOwnershipMove ``

The child graph is moved to the parent.

The handle to the child graph is owned by the parent and will be destroyed when the parent is destroyed.

The following restrictions apply to child graphs after they have been moved: Cannot be independently instantiated or destroyed; Cannot be added as a child graph of a separate parent graph; Cannot be used as an argument to cudaGraphExecUpdate; Cannot have additional memory allocation or free nodes added.

`` enumerator cudaGraphChildGraphOwnershipInvalid ``

Invalid ownership flag.

Set when params are queried to prevent accidentally reusing the driver-owned graph object

`` enum cudaGraphConditionalHandleFlags ``

_Values:_

`` enumerator cudaGraphCondAssignDefault ``

Apply default handle value when graph is launched.

`` enum cudaGraphConditionalNodeType ``

CUDA conditional node types.

_Values:_

`` enumerator cudaGraphCondTypeIf ``

Conditional ‘if/else’ Node.

Body[0] executed if condition is non-zero. If `size` == 2, an optional ELSE graph is created and this is executed if the condition is zero.

`` enumerator cudaGraphCondTypeWhile ``

Conditional ‘while’ Node.

Body executed repeatedly while condition value is non-zero.

`` enumerator cudaGraphCondTypeSwitch ``

Conditional ‘switch’ Node.

Body[n] is executed once, where ‘n’ is the value of the condition. If the condition does not match a body index, no body is launched.

`` enum cudaGraphDebugDotFlags ``

CUDA Graph debug write options.

_Values:_

`` enumerator cudaGraphDebugDotFlagsVerbose ``

Output all debug data as if every debug flag is enabled.

`` enumerator cudaGraphDebugDotFlagsKernelNodeParams ``

Adds cudaKernelNodeParams to output.

`` enumerator cudaGraphDebugDotFlagsMemcpyNodeParams ``

Adds cudaMemcpy3DParms to output.

`` enumerator cudaGraphDebugDotFlagsMemsetNodeParams ``

Adds cudaMemsetParams to output.

`` enumerator cudaGraphDebugDotFlagsHostNodeParams ``

Adds cudaHostNodeParams to output.

`` enumerator cudaGraphDebugDotFlagsEventNodeParams ``

Adds cudaEvent_t handle from record and wait nodes to output.

`` enumerator cudaGraphDebugDotFlagsExtSemasSignalNodeParams ``

Adds cudaExternalSemaphoreSignalNodeParams values to output.

`` enumerator cudaGraphDebugDotFlagsExtSemasWaitNodeParams ``

Adds cudaExternalSemaphoreWaitNodeParams to output.

`` enumerator cudaGraphDebugDotFlagsKernelNodeAttributes ``

Adds cudaKernelNodeAttrID values to output.

`` enumerator cudaGraphDebugDotFlagsHandles ``

Adds node handles and every kernel function handle to output.

`` enumerator cudaGraphDebugDotFlagsConditionalNodeParams ``

Adds cudaConditionalNodeParams to output.

`` enum cudaGraphDependencyType ``

Type annotations that can be applied to graph edges as part of cudaGraphEdgeData.

_Values:_

`` enumerator cudaGraphDependencyTypeDefault ``

This is an ordinary dependency.

`` enumerator cudaGraphDependencyTypeProgrammatic ``

This dependency type allows the downstream node to use `cudaGridDependencySynchronize()`.

It may only be used between kernel nodes, and must be used with either the cudaGraphKernelNodePortProgrammatic or cudaGraphKernelNodePortLaunchCompletion outgoing port.

`` enum cudaGraphExecUpdateResult ``

CUDA Graph Update error types.

_Values:_

`` enumerator cudaGraphExecUpdateSuccess ``

The update succeeded.

`` enumerator cudaGraphExecUpdateError ``

The update failed for an unexpected reason which is described in the return value of the function.

`` enumerator cudaGraphExecUpdateErrorTopologyChanged ``

The update failed because the topology changed.

`` enumerator cudaGraphExecUpdateErrorNodeTypeChanged ``

The update failed because a node type changed.

`` enumerator cudaGraphExecUpdateErrorFunctionChanged ``

The update failed because the function of a kernel node changed (CUDA driver < 11.2)

`` enumerator cudaGraphExecUpdateErrorParametersChanged ``

The update failed because the parameters changed in a way that is not supported.

`` enumerator cudaGraphExecUpdateErrorNotSupported ``

The update failed because something about the node is not supported.

`` enumerator cudaGraphExecUpdateErrorUnsupportedFunctionChange ``

The update failed because the function of a kernel node changed in an unsupported way.

`` enumerator cudaGraphExecUpdateErrorAttributesChanged ``

The update failed because the node attributes changed in a way that is not supported.

`` enum cudaGraphInstantiateFlags ``

Flags for instantiating a graph.

_Values:_

`` enumerator cudaGraphInstantiateFlagAutoFreeOnLaunch ``

Automatically free memory allocated in a graph before relaunching.

`` enumerator cudaGraphInstantiateFlagUpload ``

Automatically upload the graph after instantiation.

Only supported by cudaGraphInstantiateWithParams

. The upload will be performed using the

stream provided in

`instantiateParams`.

`` enumerator cudaGraphInstantiateFlagDeviceLaunch ``

Instantiate the graph to be launchable from the device.

This flag can only

be used on platforms which support unified addressing. This flag cannot be

used in conjunction with cudaGraphInstantiateFlagAutoFreeOnLaunch.

`` enumerator cudaGraphInstantiateFlagUseNodePriority ``

Run the graph using the per-node priority attributes rather than the priority of the stream it is launched into.

`` enum cudaGraphInstantiateResult ``

Graph instantiation results.

_Values:_

`` enumerator cudaGraphInstantiateSuccess ``

Instantiation succeeded.

`` enumerator cudaGraphInstantiateError ``

Instantiation failed for an unexpected reason which is described in the return value of the function.

`` enumerator cudaGraphInstantiateInvalidStructure ``

Instantiation failed due to invalid structure, such as cycles.

`` enumerator cudaGraphInstantiateNodeOperationNotSupported ``

Instantiation for device launch failed because the graph contained an unsupported operation.

`` enumerator cudaGraphInstantiateMultipleDevicesNotSupported ``

Instantiation for device launch failed due to the nodes belonging to different contexts.

`` enumerator cudaGraphInstantiateConditionalHandleUnused ``

One or more conditional handles are not associated with conditional nodes.

`` enum cudaGraphKernelNodeField ``

Specifies the field to update when performing multiple node updates from the device.

_Values:_

`` enumerator cudaGraphKernelNodeFieldInvalid ``

Invalid field.

`` enumerator cudaGraphKernelNodeFieldGridDim ``

Grid dimension update.

`` enumerator cudaGraphKernelNodeFieldParam ``

Kernel parameter update.

`` enumerator cudaGraphKernelNodeFieldEnabled ``

Node enable/disable.

`` enum cudaGraphMemAttributeType ``

Graph memory attributes.

_Values:_

`` enumerator cudaGraphMemAttrUsedMemCurrent ``

(value type = cuuint64_t) Amount of memory, in bytes, currently associated with graphs.

`` enumerator cudaGraphMemAttrUsedMemHigh ``

(value type = cuuint64_t) High watermark of memory, in bytes, associated with graphs since the last time it was reset.

High watermark can only be reset to zero.

`` enumerator cudaGraphMemAttrReservedMemCurrent ``

(value type = cuuint64_t) Amount of memory, in bytes, currently allocated for use by the CUDA graphs asynchronous allocator.

`` enumerator cudaGraphMemAttrReservedMemHigh ``

(value type = cuuint64_t) High watermark of memory, in bytes, currently allocated for use by the CUDA graphs asynchronous allocator.

`` enum cudaGraphNodeType ``

CUDA Graph node types.

_Values:_

`` enumerator cudaGraphNodeTypeKernel ``

GPU kernel node.

`` enumerator cudaGraphNodeTypeMemcpy ``

Memcpy node.

`` enumerator cudaGraphNodeTypeMemset ``

Memset node.

`` enumerator cudaGraphNodeTypeHost ``

Host (executable) node.

`` enumerator cudaGraphNodeTypeGraph ``

Node which executes an embedded graph.

`` enumerator cudaGraphNodeTypeEmpty ``

Empty (no-op) node.

`` enumerator cudaGraphNodeTypeWaitEvent ``

External event wait node.

`` enumerator cudaGraphNodeTypeEventRecord ``

External event record node.

`` enumerator cudaGraphNodeTypeExtSemaphoreSignal ``

External semaphore signal node.

`` enumerator cudaGraphNodeTypeExtSemaphoreWait ``

External semaphore wait node.

`` enumerator cudaGraphNodeTypeMemAlloc ``

Memory allocation node.

`` enumerator cudaGraphNodeTypeMemFree ``

Memory free node.

`` enumerator cudaGraphNodeTypeConditional ``

Conditional node.

```cpp
May be used to implement a conditional execution path or loop
                                   inside of a graph. The graph(s) contained within the body of the conditional node
                                   can be selectively executed or iterated upon based on the value of a conditional
                                   variable.

                                   Handles must be created in advance of creating the node
                                   using ::cudaGraphConditionalHandleCreate.

                                   The following restrictions apply to graphs which contain conditional nodes:
                                     The graph cannot be used in a child node.
                                     Only one instantiation of the graph may exist at any point in time.
                                     The graph cannot be cloned.

                                   To set the control value, supply a default value when creating the handle and/or
                                   call ::cudaGraphSetConditional from device code.
```

`` enumerator cudaGraphNodeTypeReserved16 ``

Reserved.

`` enumerator cudaGraphNodeTypeCount ``

`` enum cudaGraphRecaptureStatus ``

Possible recapture statuses that can be returned to the user callback.

_Values:_

`` enumerator cudaGraphRecaptureEligibleForUpdate ``

Node is eligible for update in an instantiated graph.

`` enumerator cudaGraphRecaptureIneligibleForUpdate ``

Parameter changes in the node cannot be applied to an instantiated graph.

`` enumerator cudaGraphRecaptureError ``

Error while attempting to recapture the node.

The recapture will be ended regardless of the return value from the callback.

`` enum cudaGraphicsCubeFace ``

CUDA graphics interop array indices for cube maps.

_Values:_

`` enumerator cudaGraphicsCubeFacePositiveX ``

Positive X face of cubemap.

`` enumerator cudaGraphicsCubeFaceNegativeX ``

Negative X face of cubemap.

`` enumerator cudaGraphicsCubeFacePositiveY ``

Positive Y face of cubemap.

`` enumerator cudaGraphicsCubeFaceNegativeY ``

Negative Y face of cubemap.

`` enumerator cudaGraphicsCubeFacePositiveZ ``

Positive Z face of cubemap.

`` enumerator cudaGraphicsCubeFaceNegativeZ ``

Negative Z face of cubemap.

`` enum cudaGraphicsMapFlags ``

CUDA graphics interop map flags.

_Values:_

`` enumerator cudaGraphicsMapFlagsNone ``

Default; Assume resource can be read/written.

`` enumerator cudaGraphicsMapFlagsReadOnly ``

CUDA will not write to this resource.

`` enumerator cudaGraphicsMapFlagsWriteDiscard ``

CUDA will only write to and will not read from this resource.

`` enum cudaGraphicsRegisterFlags ``

CUDA graphics interop register flags.

_Values:_

`` enumerator cudaGraphicsRegisterFlagsNone ``

Default.

`` enumerator cudaGraphicsRegisterFlagsReadOnly ``

CUDA will not write to this resource.

`` enumerator cudaGraphicsRegisterFlagsWriteDiscard ``

CUDA will only write to and will not read from this resource.

`` enumerator cudaGraphicsRegisterFlagsSurfaceLoadStore ``

CUDA will bind this resource to a surface reference.

`` enumerator cudaGraphicsRegisterFlagsTextureGather ``

CUDA will perform texture gather operations on this resource.

`` enum cudaHostTaskSyncMode ``

Flags for host task sync mode.

_Values:_

`` enumerator cudaHostTaskBlocking ``

`` enumerator cudaHostTaskSpinWait ``

`` enum cudaJitOption ``

Online compiler and linker options.

_Values:_

`` enumerator cudaJitMaxRegisters ``

Max number of registers that a thread may use.

Option type: unsigned int

Applies to: compiler only

`` enumerator cudaJitThreadsPerBlock ``

IN: Specifies minimum number of threads per block to target compilation for

OUT: Returns the number of threads the compiler actually targeted.

This restricts the resource utilization of the compiler (e.g. max registers) such that a block with the given number of threads should be able to launch based on register limitations. Note, this option does not currently take into account any other resource limitations, such as shared memory utilization.

Option type: unsigned int

Applies to: compiler only

`` enumerator cudaJitWallTime ``

Overwrites the option value with the total wall clock time, in milliseconds, spent in the compiler and linker

Option type: float

Applies to: compiler and linker.

`` enumerator cudaJitInfoLogBuffer ``

Pointer to a buffer in which to print any log messages that are informational in nature (the buffer size is specified via option cudaJitInfoLogBufferSizeBytes

)

Option type: char *

Applies to: compiler and linker.

`` enumerator cudaJitInfoLogBufferSizeBytes ``

IN: Log buffer size in bytes.

Log messages will be capped at this size (including null terminator)

OUT: Amount of log buffer filled with messages

Option type: unsigned int

Applies to: compiler and linker

`` enumerator cudaJitErrorLogBuffer ``

Pointer to a buffer in which to print any log messages that reflect errors (the buffer size is specified via option cudaJitErrorLogBufferSizeBytes

)

Option type: char *

Applies to: compiler and linker.

`` enumerator cudaJitErrorLogBufferSizeBytes ``

IN: Log buffer size in bytes.

Log messages will be capped at this size (including null terminator)

OUT: Amount of log buffer filled with messages

Option type: unsigned int

Applies to: compiler and linker

`` enumerator cudaJitOptimizationLevel ``

Level of optimizations to apply to generated code (0 - 4), with 4 being the default and highest level of optimizations.

Option type: unsigned int

Applies to: compiler only

`` enumerator cudaJitFallbackStrategy ``

Specifies choice of fallback strategy if matching cubin is not found.

Choice is based on supplied cudaJit_Fallback. Option type: unsigned int for enumerated type cudaJit_Fallback Applies to: compiler only

`` enumerator cudaJitGenerateDebugInfo ``

Specifies whether to create debug information in output (-g) (0: false, default)

Option type: int

Applies to: compiler and linker.

`` enumerator cudaJitLogVerbose ``

Generate verbose log messages (0: false, default)

Option type: int

Applies to: compiler and linker.

`` enumerator cudaJitGenerateLineInfo ``

Generate line number information (-lineinfo) (0: false, default)

Option type: int

Applies to: compiler only.

`` enumerator cudaJitCacheMode ``

Specifies whether to enable caching explicitly (-dlcm)

Choice is based on supplied

cudaJit_CacheMode.

Option type: unsigned int for enumerated type cudaJit_CacheMode Applies to: compiler only

`` enumerator cudaJitPositionIndependentCode ``

Generate position independent code (0: false)

Option type: int

Applies to: compiler only.

`` enumerator cudaJitMinCtaPerSm ``

This option hints to the JIT compiler the minimum number of CTAs from the kernel’s grid to be mapped to a SM.

This option is ignored when used together with cudaJitMaxRegisters or cudaJitThreadsPerBlock. Optimizations based on this option need cudaJitMaxThreadsPerBlock to be specified as well. For kernels already using PTX directive .minnctapersm, this option will be ignored by default. Use cudaJitOverrideDirectiveValues

to let this option take precedence over the PTX directive. Option type: unsigned int

Applies to: compiler only

`` enumerator cudaJitMaxThreadsPerBlock ``

Maximum number threads in a thread block, computed as the product of the maximum extent specifed for each dimension of the block.

This limit is guaranteed not to be exeeded in any invocation of the kernel. Exceeding the the maximum number of threads results in runtime error or kernel launch failure. For kernels already using PTX directive .maxntid, this option will be ignored by default. Use cudaJitOverrideDirectiveValues

to let this option take precedence over the PTX directive. Option type: int

Applies to: compiler only

`` enumerator cudaJitOverrideDirectiveValues ``

This option lets the values specified using cudaJitMaxRegisters, cudaJitThreadsPerBlock, cudaJitMaxThreadsPerBlock and cudaJitMinCtaPerSm take precedence over any PTX directives.

(0: Disable, default; 1: Enable) Option type: int

Applies to: compiler only

`` enum cudaJit_CacheMode ``

Caching modes for dlcm.

_Values:_

`` enumerator cudaJitCacheOptionNone ``

Compile with no -dlcm flag specified.

`` enumerator cudaJitCacheOptionCG ``

Compile with L1 cache disabled.

`` enumerator cudaJitCacheOptionCA ``

Compile with L1 cache enabled.

`` enum cudaJit_Fallback ``

Cubin matching fallback strategies.

_Values:_

`` enumerator cudaPreferPtx ``

Prefer to compile ptx if exact binary match not found.

`` enumerator cudaPreferBinary ``

Prefer to fall back to compatible binary code if exact match not found.

`` enum cudaKernelFunctionType ``

CUDA Kernel Function Handle Type.

_Values:_

`` enumerator cudaKernelFunctionTypeUnspecified ``

CUDA will attempt to deduce the type of the function handle.

`` enumerator cudaKernelFunctionTypeDeviceEntry ``

Function handle is a device-entry function pointer(i.e.

**global** function pointer)

`` enumerator cudaKernelFunctionTypeKernel ``

Function handle is a cudaKernel_t.

`` enumerator cudaKernelFunctionTypeFunction ``

Function handle is a cudaFunction_t.

`` enum cudaLaunchAttributeID ``

Launch attributes enum; used as id field of cudaLaunchAttribute.

_Values:_

`` enumerator cudaLaunchAttributeIgnore ``

Ignored entry, for convenient composition.

`` enumerator cudaLaunchAttributeAccessPolicyWindow ``

Valid for streams, graph nodes, launches.

See cudaLaunchAttributeValue::accessPolicyWindow.

`` enumerator cudaLaunchAttributeCooperative ``

Valid for graph nodes, launches.

See cudaLaunchAttributeValue::cooperative.

`` enumerator cudaLaunchAttributeSynchronizationPolicy ``

Valid for streams.

See cudaLaunchAttributeValue::syncPolicy.

`` enumerator cudaLaunchAttributeClusterDimension ``

Valid for graph nodes, launches.

See cudaLaunchAttributeValue::clusterDim.

`` enumerator cudaLaunchAttributeClusterSchedulingPolicyPreference ``

Valid for graph nodes, launches.

See cudaLaunchAttributeValue::clusterSchedulingPolicyPreference.

`` enumerator cudaLaunchAttributeProgrammaticStreamSerialization ``

Valid for launches.

Setting cudaLaunchAttributeValue::programmaticStreamSerializationAllowed to non-0 signals that the kernel will use programmatic means to resolve its stream dependency, so that the CUDA runtime should opportunistically allow the grid’s execution to overlap with the previous kernel in the stream, if that kernel requests the overlap. The dependent launches can choose to wait on the dependency using the programmatic sync (cudaGridDependencySynchronize() or equivalent PTX instructions).

`` enumerator cudaLaunchAttributeProgrammaticEvent ``

Valid for launches.

Set cudaLaunchAttributeValue::programmaticEvent to record the event. Event recorded through this launch attribute is guaranteed to only trigger after all block in the associated kernel trigger the event. A block can trigger the event programmatically in a future CUDA release. A trigger can also be inserted at the beginning of each block’s execution if triggerAtBlockStart is set to non-0. The dependent launches can choose to wait on the dependency using the programmatic sync (cudaGridDependencySynchronize() or equivalent PTX instructions). Note that dependents (including the CPU thread calling cudaEventSynchronize()) are not guaranteed to observe the release precisely when it is released. For example, cudaEventSynchronize()

may only observe the event trigger long after the associated kernel has completed. This recording type is primarily meant for establishing programmatic dependency between device tasks. Note also this type of dependency allows, but does not guarantee, concurrent execution of tasks.

The event supplied must not be an interprocess or interop event. The event must disable timing (i.e. must be created with the

cudaEventDisableTiming flag set).

`` enumerator cudaLaunchAttributePriority ``

Valid for streams, graph nodes, launches.

See cudaLaunchAttributeValue::priority.

`` enumerator cudaLaunchAttributeMemSyncDomainMap ``

Valid for streams, graph nodes, launches.

See cudaLaunchAttributeValue::memSyncDomainMap.

`` enumerator cudaLaunchAttributeMemSyncDomain ``

Valid for streams, graph nodes, launches.

See cudaLaunchAttributeValue::memSyncDomain.

`` enumerator cudaLaunchAttributePreferredClusterDimension ``

Valid for graph nodes and launches.

Set cudaLaunchAttributeValue::preferredClusterDim to allow the kernel launch to specify a preferred substitute cluster dimension. Blocks may be grouped according to either the dimensions specified with this attribute (grouped into a “preferred substitute cluster”), or the one specified with cudaLaunchAttributeClusterDimension

attribute (grouped into a “regular cluster”). The cluster dimensions of a “preferred substitute cluster” shall be an integer multiple greater than zero of the regular cluster dimensions. The device will attempt - on a best-effort basis - to group thread blocks into preferred clusters over grouping them into regular clusters. When it deems necessary (primarily when the device temporarily runs out of physical resources to launch the larger preferred clusters), the device may switch to launch the regular clusters instead to attempt to utilize as much of the physical device resources as possible.

Each type of cluster will have its enumeration / coordinate setup as if the grid consists solely of its type of cluster. For example, if the preferred substitute cluster dimensions double the regular cluster dimensions, there might be simultaneously a regular cluster indexed at (1,0,0), and a preferred cluster indexed at (1,0,0). In this example, the preferred substitute cluster (1,0,0) replaces regular clusters (2,0,0) and (3,0,0) and groups their blocks.

This attribute will only take effect when a regular cluster dimension has been specified. The preferred substitute cluster dimension must be an integer multiple greater than zero of the regular cluster dimension and must divide the grid. It must also be no more than `maxBlocksPerCluster`, if it is set in the kernel’s `__launch_bounds__`. Otherwise it must be less than the maximum value the driver can support. Otherwise, setting this attribute to a value physically unable to fit on any particular device is permitted.

`` enumerator cudaLaunchAttributeLaunchCompletionEvent ``

Valid for launches.

Set cudaLaunchAttributeValue::launchCompletionEvent

to record the event.

Nominally, the event is triggered once all blocks of the kernel have begun execution. Currently this is a best effort. If a kernel B has a launch completion dependency on a kernel A, B may wait until A is complete. Alternatively, blocks of B may begin before all blocks of A have begun, for example if B can claim execution resources unavailable to A (e.g. they run on different GPUs) or if B is a higher priority than A. Exercise caution if such an ordering inversion could lead to deadlock.

A launch completion event is nominally similar to a programmatic event with `triggerAtBlockStart` set except that it is not visible to `cudaGridDependencySynchronize()`

and can be used with compute capability less than 9.0.

The event supplied must not be an interprocess or interop event. The event must disable timing (i.e. must be created with the

cudaEventDisableTiming flag set).

`` enumerator cudaLaunchAttributeDeviceUpdatableKernelNode ``

Valid for graph nodes, launches.

This attribute is graphs-only, and passing it to a launch in a non-capturing stream will result in an error.

:cudaLaunchAttributeValue::deviceUpdatableKernelNode::deviceUpdatable can only be set to 0 or 1. Setting the field to 1 indicates that the corresponding kernel node should be device-updatable. On success, a handle will be returned via ::cudaLaunchAttributeValue::deviceUpdatableKernelNode::devNode which can be passed to the various device-side update functions to update the node’s kernel parameters from within another kernel. For more information on the types of device updates that can be made, as well as the relevant limitations thereof, see

cudaGraphKernelNodeUpdatesApply

.

Nodes which are device-updatable have additional restrictions compared to regular kernel nodes. Firstly, device-updatable nodes cannot be removed from their graph via

cudaGraphDestroyNode. Additionally, once opted-in to this functionality, a node cannot opt out, and any attempt to set the deviceUpdatable attribute to 0 will result in an error. Device-updatable kernel nodes also cannot have their attributes copied to/from another kernel node via cudaGraphKernelNodeCopyAttributes. Graphs containing one or more device-updatable nodes also do not allow multiple instantiation, and neither the graph nor its instantiated version can be passed to cudaGraphExecUpdate

.

If a graph contains device-updatable nodes and updates those nodes from the device from within the graph, the graph must be uploaded with ::cuGraphUpload before it is launched. For such a graph, if host-side executable graph updates are made to the device-updatable nodes, the graph must be uploaded before it is launched again.

`` enumerator cudaLaunchAttributePreferredSharedMemoryCarveout ``

Valid for launches.

On devices where the L1 cache and shared memory use the same hardware resources, setting cudaLaunchAttributeValue::sharedMemCarveout to a percentage between 0-100 signals sets the shared memory carveout preference in percent of the total shared memory for that kernel launch. This attribute takes precedence over cudaFuncAttributePreferredSharedMemoryCarveout. This is only a hint, and the driver can choose a different configuration if required for the launch.

`` enumerator cudaLaunchAttributeNvlinkUtilCentricScheduling ``

Valid for streams, graph nodes, launches.

This attribute is a hint to the CUDA runtime that the launch should attempt to make the kernel maximize its NVLINK utilization.

When possible to honor this hint, CUDA will assume each block in the grid launch will carry out an even amount of NVLINK traffic, and make a best-effort attempt to adjust the kernel launch based on that assumption.

This attribute is a hint only. CUDA makes no functional or performance guarantee. Its applicability can be affected by many different factors, including driver version (i.e. CUDA doesn’t guarantee the performance characteristics will be maintained between driver versions or a driver update could alter or regress previously observed perf characteristics.) It also doesn’t guarantee a successful result, i.e. applying the attribute may not improve the performance of either the targeted kernel or the encapsulating application.

Valid values for

cudaLaunchAttributeValue::nvlinkUtilCentricScheduling are 0 (disabled) and 1 (enabled).

`` enumerator cudaLaunchAttributePortableClusterSizeMode ``

Valid for graph nodes, launches.

This indicates whether the kernel launch is allowed to use a non-portable cluster size. Valid values for cudaLaunchAttributeValue::portableClusterSizeMode are values for cudaLaunchAttributePortableClusterMode Any other value will return cudaErrorInvalidValue

`` enumerator cudaLaunchAttributeSharedMemoryMode ``

Valid for graph nodes, launches.

This indicates that the kernel launch is allowed to use a non-portable shared memory mode.

`` enum cudaLaunchAttributePortableClusterMode ``

Enum for defining applicability of portable cluster size, used with cudaLaunchKernelEx.

_Values:_

`` enumerator cudaLaunchPortableClusterModeDefault ``

The default to use for allowing non-portable cluster size on launch - uses current function attribute for cudaFuncAttributeNonPortableClusterSizeAllowed.

`` enumerator cudaLaunchPortableClusterModeRequirePortable ``

Specifies that the cluster size requested must be a portable size.

`` enumerator cudaLaunchPortableClusterModeAllowNonPortable ``

Specifies that the cluster size requested may be a non-portable size.

`` enum cudaLaunchMemSyncDomain ``

Memory Synchronization Domain.

A kernel can be launched in a specified memory synchronization domain that affects all memory operations issued by that kernel. A memory barrier issued in one domain will only order memory operations in that domain, thus eliminating latency increase from memory barriers ordering unrelated traffic.

By default, kernels are launched in domain 0. Kernel launched with cudaLaunchMemSyncDomainRemote will have a different domain ID. User may also alter the domain ID with cudaLaunchMemSyncDomainMap for a specific stream / graph node / kernel launch. See cudaLaunchAttributeMemSyncDomain, cudaStreamSetAttribute, cudaLaunchKernelEx, cudaGraphKernelNodeSetAttribute.

Memory operations done in kernels launched in different domains are considered system-scope distanced. In other words, a GPU scoped memory synchronization is not sufficient for memory order to be observed by kernels in another memory synchronization domain even if they are on the same GPU.

_Values:_

`` enumerator cudaLaunchMemSyncDomainDefault ``

Launch kernels in the default domain.

`` enumerator cudaLaunchMemSyncDomainRemote ``

Launch kernels in the remote domain.

`` enum cudaLibraryOption ``

Library options to be specified with cudaLibraryLoadData() or cudaLibraryLoadFromFile()

_Values:_

`` enumerator cudaLibraryHostUniversalFunctionAndDataTable ``

`` enumerator cudaLibraryBinaryIsPreserved ``

Specifes that the argument `code` passed to cudaLibraryLoadData() will be preserved.

Specifying this option will let the driver know that `code` can be accessed at any point until cudaLibraryUnload(). The default behavior is for the driver to allocate and maintain its own copy of `code`. Note that this is only a memory usage optimization hint and the driver can choose to ignore it if required. Specifying this option with cudaLibraryLoadFromFile() is invalid and will return cudaErrorInvalidValue.

`` enum cudaLimit ``

CUDA Limits.

_Values:_

`` enumerator cudaLimitStackSize ``

GPU thread stack size.

`` enumerator cudaLimitPrintfFifoSize ``

GPU printf FIFO size.

`` enumerator cudaLimitMallocHeapSize ``

GPU malloc heap size.

`` enumerator cudaLimitDevRuntimeSyncDepth ``

GPU device runtime synchronize depth.

`` enumerator cudaLimitDevRuntimePendingLaunchCount ``

GPU device runtime pending launch count.

`` enumerator cudaLimitMaxL2FetchGranularity ``

A value between 0 and 128 that indicates the maximum fetch granularity of L2 (in Bytes).

This is a hint

`` enumerator cudaLimitPersistingL2CacheSize ``

A size in bytes for L2 persisting lines cache size.

`` enumerator cudaLimitPerBlockMemorySize ``

Per-block memory size.

`` enum cudaLogLevel ``

_Values:_

`` enumerator cudaLogLevelError ``

`` enumerator cudaLogLevelWarning ``

`` enum cudaMemAccessFlags ``

Specifies the memory protection flags for mapping.

_Values:_

`` enumerator cudaMemAccessFlagsProtNone ``

Default, make the address range not accessible.

`` enumerator cudaMemAccessFlagsProtRead ``

Make the address range read accessible.

`` enumerator cudaMemAccessFlagsProtReadWrite ``

Make the address range read-write accessible.

`` enum cudaMemAllocationHandleType ``

Flags for specifying particular handle types.

_Values:_

`` enumerator cudaMemHandleTypeNone ``

Does not allow any export mechanism.

>

`` enumerator cudaMemHandleTypePosixFileDescriptor ``

Allows a file descriptor to be used for exporting.

Permitted only on POSIX systems. (int)

`` enumerator cudaMemHandleTypeWin32 ``

Allows a Win32 NT handle to be used for exporting.

(HANDLE)

`` enumerator cudaMemHandleTypeWin32Kmt ``

Allows a Win32 KMT handle to be used for exporting.

(D3DKMT_HANDLE)

`` enumerator cudaMemHandleTypeFabric ``

Allows a fabric handle to be used for exporting.

(cudaMemFabricHandle_t)

`` enum cudaMemAllocationType ``

Defines the allocation types available.

_Values:_

`` enumerator cudaMemAllocationTypeInvalid ``

`` enumerator cudaMemAllocationTypePinned ``

This allocation type is ‘pinned’, i.e.

cannot migrate from its current location while the application is actively using it

`` enumerator cudaMemAllocationTypeManaged ``

This allocation type is managed memory.

`` enumerator cudaMemAllocationTypeMax ``

`` enum cudaMemLocationType ``

Specifies the type of location.

_Values:_

`` enumerator cudaMemLocationTypeInvalid ``

`` enumerator cudaMemLocationTypeNone ``

Location is unspecified.

This is used when creating a managed memory pool to indicate no preferred location for the pool

`` enumerator cudaMemLocationTypeDevice ``

Location is a device location, thus id is a device ordinal.

`` enumerator cudaMemLocationTypeHost ``

Location is host, id is ignored.

`` enumerator cudaMemLocationTypeHostNuma ``

Location is a host NUMA node, thus id is a host NUMA node id.

`` enumerator cudaMemLocationTypeHostNumaCurrent ``

Location is the host NUMA node closest to the current thread’s CPU, id is ignored.

`` enumerator cudaMemLocationTypeInvisible ``

Location is not visible but device is accessible, id is always cudaInvalidDeviceId.

`` enumerator cudaMemLocationTypeDeviceLocalityDomain ``

Location is a portion of device memory, specified by the locality domain ID.

`` enum cudaMemPoolAttr ``

CUDA memory pool attributes.

_Values:_

`` enumerator cudaMemPoolReuseFollowEventDependencies ``

(value type = int) Allow cuMemAllocAsync to use memory asynchronously freed in another streams as long as a stream ordering dependency of the allocating stream on the free action exists.

Cuda events and null stream interactions can create the required stream ordered dependencies. (default enabled)

`` enumerator cudaMemPoolReuseAllowOpportunistic ``

(value type = int) Allow reuse of already completed frees when there is no dependency between the free and allocation.

(default enabled)

`` enumerator cudaMemPoolReuseAllowInternalDependencies ``

(value type = int) Allow cuMemAllocAsync to insert new stream dependencies in order to establish the stream ordering required to reuse a piece of memory released by cuFreeAsync (default enabled).

`` enumerator cudaMemPoolAttrReleaseThreshold ``

(value type = cuuint64_t) Amount of reserved memory in bytes to hold onto before trying to release memory back to the OS.

When more than the release threshold bytes of memory are held by the memory pool, the allocator will try to release memory back to the OS on the next call to stream, event or context synchronize. (default 0)

`` enumerator cudaMemPoolAttrReservedMemCurrent ``

(value type = cuuint64_t) Amount of backing memory currently allocated for the mempool.

`` enumerator cudaMemPoolAttrReservedMemHigh ``

(value type = cuuint64_t) High watermark of backing memory allocated for the mempool since the last time it was reset.

High watermark can only be reset to zero.

`` enumerator cudaMemPoolAttrUsedMemCurrent ``

(value type = cuuint64_t) Amount of memory from the pool that is currently in use by the application.

`` enumerator cudaMemPoolAttrUsedMemHigh ``

(value type = cuuint64_t) High watermark of the amount of memory from the pool that was in use by the application since the last time it was reset.

High watermark can only be reset to zero.

`` enumerator cudaMemPoolAttrAllocationType ``

(value type = cudaMemAllocationType) The allocation type of the mempool

`` enumerator cudaMemPoolAttrExportHandleTypes ``

(value type = cudaMemAllocationHandleType) Available export handle types for the mempool.

For imported pools this value is always cudaMemHandleTypeNone as an imported pool cannot be re-exported

`` enumerator cudaMemPoolAttrLocationId ``

(value type = int) The location id for the mempool.

If the location type for this pool is cudaMemLocationTypeInvisible then ID will be cudaInvalidDeviceId

`` enumerator cudaMemPoolAttrLocationType ``

(value type = cudaMemLocationType) The location type for the mempool.

For imported memory pools where the device is not directly visible to the importing process or pools imported via fabric handles across nodes this will be cudaMemLocationTypeInvisible

`` enumerator cudaMemPoolAttrMaxPoolSize ``

(value type = cuuint64_t) Maximum size of the pool in bytes, this value may be higher than what was initially passed to cudaMemPoolCreate due to alignment requirements.

A value of 0 indicates no maximum size. For cudaMemAllocationTypeManaged and IPC imported pools this value will be system dependent.

`` enumerator cudaMemPoolAttrHwDecompressEnabled ``

(value type = int) Indicates whether the pool has hardware compresssion enabled

`` enumerator cudaMemPoolAttrLocalityDomainId ``

(value type = int) The locality domain id for the mempool, if the mempool is localized to a locality domain.

A value of -1 indicates that the mempool is not localized to a locality domain.

`` enum cudaMemRangeAttribute ``

CUDA range attributes.

_Values:_

`` enumerator cudaMemRangeAttributeReadMostly ``

Whether the range will mostly be read and only occassionally be written to.

`` enumerator cudaMemRangeAttributePreferredLocation ``

The preferred location of the range.

`` enumerator cudaMemRangeAttributeAccessedBy ``

Memory range has cudaMemAdviseSetAccessedBy set for specified device.

`` enumerator cudaMemRangeAttributeLastPrefetchLocation ``

The last location to which the range was prefetched.

`` enumerator cudaMemRangeAttributePreferredLocationType ``

The preferred location type of the range.

`` enumerator cudaMemRangeAttributePreferredLocationId ``

The preferred location id of the range.

`` enumerator cudaMemRangeAttributeLastPrefetchLocationType ``

The last location type to which the range was prefetched.

`` enumerator cudaMemRangeAttributeLastPrefetchLocationId ``

The last location id to which the range was prefetched.

`` enum cudaMemcpy3DOperandType ``

These flags allow applications to convey the operand type for individual copies specified in cudaMemcpy3DBatchAsync.

_Values:_

`` enumerator cudaMemcpyOperandTypePointer ``

Memcpy operand is a valid pointer.

`` enumerator cudaMemcpyOperandTypeArray ``

Memcpy operand is a CUarray.

`` enumerator cudaMemcpyOperandTypeMax ``

`` enum cudaMemcpyFlags ``

Flags to specify for copies within a batch.

For more details see cudaMemcpyBatchAsync.

_Values:_

`` enumerator cudaMemcpyFlagDefault ``

`` enumerator cudaMemcpyFlagPreferOverlapWithCompute ``

Hint to the driver to try and overlap the copy with compute work on the SMs.

`` enum cudaMemcpyKind ``

CUDA memory copy types.

_Values:_

`` enumerator cudaMemcpyHostToHost ``

Host -> Host.

`` enumerator cudaMemcpyHostToDevice ``

Host -> Device.

`` enumerator cudaMemcpyDeviceToHost ``

Device -> Host.

`` enumerator cudaMemcpyDeviceToDevice ``

Device -> Device.

`` enumerator cudaMemcpyDefault ``

Direction of the transfer is inferred from the pointer values.

Requires unified virtual addressing

`` enum cudaMemcpySrcAccessOrder ``

_Values:_

`` enumerator cudaMemcpySrcAccessOrderInvalid ``

Default invalid.

`` enumerator cudaMemcpySrcAccessOrderStream ``

Indicates that access to the source pointer must be in stream order.

`` enumerator cudaMemcpySrcAccessOrderDuringApiCall ``

Indicates that access to the source pointer can be out of stream order and all accesses must be complete before the API call returns.

This flag is suited for ephemeral sources (ex., stack variables) when it’s known that no prior operations in the stream can be accessing the memory and also that the lifetime of the memory is limited to the scope that the source variable was declared in. Specifying this flag allows the driver to optimize the copy and removes the need for the user to synchronize the stream after the API call.

`` enumerator cudaMemcpySrcAccessOrderAny ``

Indicates that access to the source pointer can be out of stream order and the accesses can happen even after the API call returns.

This flag is suited for host pointers allocated outside CUDA (ex., via malloc) when it’s known that no prior operations in the stream can be accessing the memory. Specifying this flag allows the driver to optimize the copy on certain platforms.

`` enumerator cudaMemcpySrcAccessOrderMax ``

`` enum cudaMemoryAdvise ``

CUDA Memory Advise values.

_Values:_

`` enumerator cudaMemAdviseSetReadMostly ``

Data will mostly be read and only occassionally be written to.

`` enumerator cudaMemAdviseUnsetReadMostly ``

Undo the effect of cudaMemAdviseSetReadMostly.

`` enumerator cudaMemAdviseSetPreferredLocation ``

Set the preferred location for the data as the specified device.

`` enumerator cudaMemAdviseUnsetPreferredLocation ``

Clear the preferred location for the data.

`` enumerator cudaMemAdviseSetAccessedBy ``

Data will be accessed by the specified device, so prevent page faults as much as possible.

`` enumerator cudaMemAdviseUnsetAccessedBy ``

Let the Unified Memory subsystem decide on the page faulting policy for the specified device.

`` enum cudaMemoryType ``

CUDA memory types.

_Values:_

`` enumerator cudaMemoryTypeUnregistered ``

Unregistered memory.

`` enumerator cudaMemoryTypeHost ``

Host memory.

`` enumerator cudaMemoryTypeDevice ``

Device memory.

`` enumerator cudaMemoryTypeManaged ``

Managed memory.

`` enum cudaResourceType ``

CUDA resource types.

_Values:_

`` enumerator cudaResourceTypeArray ``

Array resource.

`` enumerator cudaResourceTypeMipmappedArray ``

Mipmapped array resource.

`` enumerator cudaResourceTypeLinear ``

Linear resource.

`` enumerator cudaResourceTypePitch2D ``

Pitch 2D resource.

`` enum cudaResourceViewFormat ``

CUDA texture resource view formats.

_Values:_

`` enumerator cudaResViewFormatNone ``

No resource view format (use underlying resource format)

`` enumerator cudaResViewFormatUnsignedChar1 ``

1 channel unsigned 8-bit integers

`` enumerator cudaResViewFormatUnsignedChar2 ``

2 channel unsigned 8-bit integers

`` enumerator cudaResViewFormatUnsignedChar4 ``

4 channel unsigned 8-bit integers

`` enumerator cudaResViewFormatSignedChar1 ``

1 channel signed 8-bit integers

`` enumerator cudaResViewFormatSignedChar2 ``

2 channel signed 8-bit integers

`` enumerator cudaResViewFormatSignedChar4 ``

4 channel signed 8-bit integers

`` enumerator cudaResViewFormatUnsignedShort1 ``

1 channel unsigned 16-bit integers

`` enumerator cudaResViewFormatUnsignedShort2 ``

2 channel unsigned 16-bit integers

`` enumerator cudaResViewFormatUnsignedShort4 ``

4 channel unsigned 16-bit integers

`` enumerator cudaResViewFormatSignedShort1 ``

1 channel signed 16-bit integers

`` enumerator cudaResViewFormatSignedShort2 ``

2 channel signed 16-bit integers

`` enumerator cudaResViewFormatSignedShort4 ``

4 channel signed 16-bit integers

`` enumerator cudaResViewFormatUnsignedInt1 ``

1 channel unsigned 32-bit integers

`` enumerator cudaResViewFormatUnsignedInt2 ``

2 channel unsigned 32-bit integers

`` enumerator cudaResViewFormatUnsignedInt4 ``

4 channel unsigned 32-bit integers

`` enumerator cudaResViewFormatSignedInt1 ``

1 channel signed 32-bit integers

`` enumerator cudaResViewFormatSignedInt2 ``

2 channel signed 32-bit integers

`` enumerator cudaResViewFormatSignedInt4 ``

4 channel signed 32-bit integers

`` enumerator cudaResViewFormatHalf1 ``

1 channel 16-bit floating point

`` enumerator cudaResViewFormatHalf2 ``

2 channel 16-bit floating point

`` enumerator cudaResViewFormatHalf4 ``

4 channel 16-bit floating point

`` enumerator cudaResViewFormatFloat1 ``

1 channel 32-bit floating point

`` enumerator cudaResViewFormatFloat2 ``

2 channel 32-bit floating point

`` enumerator cudaResViewFormatFloat4 ``

4 channel 32-bit floating point

`` enumerator cudaResViewFormatUnsignedBlockCompressed1 ``

Block compressed 1.

`` enumerator cudaResViewFormatUnsignedBlockCompressed2 ``

Block compressed 2.

`` enumerator cudaResViewFormatUnsignedBlockCompressed3 ``

Block compressed 3.

`` enumerator cudaResViewFormatUnsignedBlockCompressed4 ``

Block compressed 4 unsigned.

`` enumerator cudaResViewFormatSignedBlockCompressed4 ``

Block compressed 4 signed.

`` enumerator cudaResViewFormatUnsignedBlockCompressed5 ``

Block compressed 5 unsigned.

`` enumerator cudaResViewFormatSignedBlockCompressed5 ``

Block compressed 5 signed.

`` enumerator cudaResViewFormatUnsignedBlockCompressed6H ``

Block compressed 6 unsigned half-float.

`` enumerator cudaResViewFormatSignedBlockCompressed6H ``

Block compressed 6 signed half-float.

`` enumerator cudaResViewFormatUnsignedBlockCompressed7 ``

Block compressed 7.

`` enum cudaSharedCarveout ``

Shared memory carveout configurations.

These may be passed to cudaFuncSetAttribute

_Values:_

`` enumerator cudaSharedmemCarveoutDefault ``

No preference for shared memory or L1 (default)

`` enumerator cudaSharedmemCarveoutMaxShared ``

Prefer maximum available shared memory, minimum L1 cache.

`` enumerator cudaSharedmemCarveoutMaxL1 ``

Prefer maximum available L1 cache, minimum shared memory.

`` enum cudaSharedMemConfig ``

CUDA shared memory configuration.

`` Deprecated: ``

_Values:_

`` enumerator cudaSharedMemBankSizeDefault ``

`` enumerator cudaSharedMemBankSizeFourByte ``

`` enumerator cudaSharedMemBankSizeEightByte ``

`` enum cudaSharedMemoryMode ``

Shared memory related attributes for use with ::cuLaunchKernelEx.

_Values:_

`` enumerator cudaSharedMemoryModeDefault ``

The default to use for allowing non-portable shared memory size on launch - uses current function attributes for cudaFuncAttributeMaxDynamicSharedMemorySize.

`` enumerator cudaSharedMemoryModeRequirePortable ``

Specifies that the shared memory size requested must be a portable size within cudaDevAttrMaxSharedMemoryPerBlock.

`` enumerator cudaSharedMemoryModeAllowNonPortable ``

Specifies that the shared memory size requested may be a non-portable size up to cudaDevAttrMaxSharedMemoryPerBlockOptin.

`` enumerator cudaSharedMemoryModeAllowOversizedSharedMemory ``

Specifies that oversized shared memory configurations may be used (with the limitation of only 8kB L1 cache)

`` enumerator cudaSharedMemoryModePreferOversizedSharedMemory ``

Specifies that oversized shared memory configurations may be used (with the limitation of only 8kB L1 cache), and prefer an oversized shared memory configuration.

`` enum cudaStreamCaptureMode ``

Possible modes for stream capture thread interactions.

For more details see cudaStreamBeginCapture and cudaThreadExchangeStreamCaptureMode

_Values:_

`` enumerator cudaStreamCaptureModeGlobal ``

`` enumerator cudaStreamCaptureModeThreadLocal ``

`` enumerator cudaStreamCaptureModeRelaxed ``

`` enum cudaStreamCaptureStatus ``

Possible stream capture statuses returned by cudaStreamIsCapturing.

_Values:_

`` enumerator cudaStreamCaptureStatusNone ``

Stream is not capturing.

`` enumerator cudaStreamCaptureStatusActive ``

Stream is actively capturing.

`` enumerator cudaStreamCaptureStatusInvalidated ``

Stream is part of a capture sequence that has been invalidated, but not terminated.

`` enum cudaStreamUpdateCaptureDependenciesFlags ``

Flags for cudaStreamUpdateCaptureDependencies.

_Values:_

`` enumerator cudaStreamAddCaptureDependencies ``

Add new nodes to the dependency set.

`` enumerator cudaStreamSetCaptureDependencies ``

Replace the dependency set with the new nodes.

`` enum cudaSurfaceBoundaryMode ``

CUDA Surface boundary modes.

_Values:_

`` enumerator cudaBoundaryModeZero ``

Zero boundary mode.

`` enumerator cudaBoundaryModeClamp ``

Clamp boundary mode.

`` enumerator cudaBoundaryModeTrap ``

Trap boundary mode.

`` enum cudaSurfaceFormatMode ``

CUDA Surface format modes.

_Values:_

`` enumerator cudaFormatModeForced ``

Forced format mode.

`` enumerator cudaFormatModeAuto ``

Auto format mode.

`` enum cudaSynchronizationPolicy ``

_Values:_

`` enumerator cudaSyncPolicyAuto ``

`` enumerator cudaSyncPolicySpin ``

`` enumerator cudaSyncPolicyYield ``

`` enumerator cudaSyncPolicyBlockingSync ``

`` enum cudaTextureAddressMode ``

CUDA texture address modes.

_Values:_

`` enumerator cudaAddressModeWrap ``

Wrapping address mode.

`` enumerator cudaAddressModeClamp ``

Clamp to edge address mode.

`` enumerator cudaAddressModeMirror ``

Mirror address mode.

`` enumerator cudaAddressModeBorder ``

Border address mode.

`` enum cudaTextureFilterMode ``

CUDA texture filter modes.

_Values:_

`` enumerator cudaFilterModePoint ``

Point filter mode.

`` enumerator cudaFilterModeLinear ``

Linear filter mode.

`` enum cudaTextureReadMode ``

CUDA texture read modes.

_Values:_

`` enumerator cudaReadModeElementType ``

Read texture as specified element type.

`` enumerator cudaReadModeNormalizedFloat ``

Read texture as normalized float.

`` enum cudaUserObjectFlags ``

Flags for user objects for graphs.

_Values:_

`` enumerator cudaUserObjectNoDestructorSync ``

Indicates the destructor execution is not synchronized by any CUDA handle.

`` enum cudaUserObjectRetainFlags ``

Flags for retaining user object references for graphs.

_Values:_

`` enumerator cudaGraphUserObjectMove ``

Transfer references from the caller rather than creating new references.

##  6.2.3. Typedefs

`` typedef const struct cudaArray *cudaArray_const_t ``

CUDA array (as source copy argument)

`` typedef struct cudaArray *cudaArray_t ``

CUDA array.

`` typedef void (*cudaAsyncCallback)(cudaAsyncNotificationInfo_t*, void*, cudaAsyncCallbackHandle_t) ``

`` typedef struct cudaAsyncCallbackEntry *cudaAsyncCallbackHandle_t ``

CUDA async callback handle.

`` typedef struct CUdevResourceDesc_st *cudaDevResourceDesc_t ``

An opaque descriptor handle.

The descriptor encapsulates multiple created and configured resources. Created via ::cudaDeviceResourceGenerateDesc

`` typedef struct CUeglStreamConnection_st *cudaEglStreamConnection ``

CUDA EGLSream Connection.

`` typedef enum cudaError cudaError_t ``

CUDA Error types.

`` typedef struct CUevent_st *cudaEvent_t ``

CUDA event types.

`` typedef struct cudaExecutionContext_st *cudaExecutionContext_t ``

An opaque handle to a CUDA execution context.

It represents an execution context created via CUDA Runtime APIs such as cudaGreenCtxCreate.

`` typedef struct CUexternalMemory_st *cudaExternalMemory_t ``

CUDA external memory.

`` typedef struct CUexternalSemaphore_st *cudaExternalSemaphore_t ``

CUDA external semaphore.

`` typedef struct CUfunc_st *cudaFunction_t ``

CUDA function.

`` typedef unsigned long long cudaGraphConditionalHandle ``

CUDA handle for conditional graph nodes.

`` typedef struct CUgraphDeviceUpdatableNode_st *cudaGraphDeviceNode_t ``

CUDA device node handle for device-side node update.

`` typedef struct CUgraphExec_st *cudaGraphExec_t ``

CUDA executable (launchable) graph.

`` typedef struct CUgraphNode_st *cudaGraphNode_t ``

CUDA graph node.

`` typedef struct CUgraph_st *cudaGraph_t ``

CUDA graph.

`` typedef struct cudaGraphicsResource *cudaGraphicsResource_t ``

CUDA graphics resource types.

`` void(__stdcall * cudaHostFn_t )(void *userData) ``

CUDA host function.

Param userData

Argument value passed to the function

`` typedef struct CUkern_st *cudaKernel_t ``

CUDA kernel.

`` typedef struct CUlib_st *cudaLibrary_t ``

CUDA library.

`` typedef unsigned int cudaLogIterator ``

`` typedef struct CUlogsCallbackEntry_st *cudaLogsCallbackHandle ``

`` typedef struct CUmemPoolHandle_st *cudaMemPool_t ``

CUDA memory pool.

`` typedef const struct cudaMipmappedArray *cudaMipmappedArray_const_t ``

CUDA mipmapped array (as source argument)

`` typedef struct cudaMipmappedArray *cudaMipmappedArray_t ``

CUDA mipmapped array.

`` typedef struct CUstream_st *cudaStream_t ``

CUDA stream.

`` typedef unsigned long long cudaSurfaceObject_t ``

An opaque value that represents a CUDA Surface object.

`` typedef unsigned long long cudaTextureObject_t ``

An opaque value that represents a CUDA texture object.

`` typedef struct CUuserObject_st *cudaUserObject_t ``

CUDA user object for graphs.
