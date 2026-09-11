<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/group__CUDA__TYPES.html

#  6.5. Data types used by CUDA driver

Structs

CUDA_ARRAY3D_DESCRIPTOR_v2

3D array descriptor

CUDA_ARRAY_DESCRIPTOR_v2

Array descriptor.

CUDA_ARRAY_MEMORY_REQUIREMENTS_v1

CUDA array memory requirements.

CUDA_ARRAY_SPARSE_PROPERTIES_v1

CUDA array sparse properties.

CUDA_BATCH_MEM_OP_NODE_PARAMS_v1

Batch memory operation node parameters.

CUDA_BATCH_MEM_OP_NODE_PARAMS_v2

Batch memory operation node parameters.

CUDA_CHILD_GRAPH_NODE_PARAMS

Child graph node parameters.

CUDA_CONDITIONAL_NODE_PARAMS

Conditional node parameters.

CUDA_EVENT_RECORD_NODE_PARAMS

Event record node parameters.

CUDA_EVENT_WAIT_NODE_PARAMS

Event wait node parameters.

CUDA_EXTERNAL_MEMORY_BUFFER_DESC_v1

External memory buffer descriptor.

CUDA_EXTERNAL_MEMORY_HANDLE_DESC_v1

External memory handle descriptor.

CUDA_EXTERNAL_MEMORY_MIPMAPPED_ARRAY_DESC_v1

External memory mipmap descriptor.

CUDA_EXTERNAL_SEMAPHORE_HANDLE_DESC_v1

External semaphore handle descriptor.

CUDA_EXTERNAL_SEMAPHORE_SIGNAL_PARAMS_v1

External semaphore signal parameters.

CUDA_EXTERNAL_SEMAPHORE_WAIT_PARAMS_v1

External semaphore wait parameters.

CUDA_EXT_SEM_SIGNAL_NODE_PARAMS_v1

Semaphore signal node parameters.

CUDA_EXT_SEM_SIGNAL_NODE_PARAMS_v2

Semaphore signal node parameters.

CUDA_EXT_SEM_WAIT_NODE_PARAMS_v1

Semaphore wait node parameters.

CUDA_EXT_SEM_WAIT_NODE_PARAMS_v2

Semaphore wait node parameters.

CUDA_GRAPH_INSTANTIATE_PARAMS

Graph instantiation parameters.

CUDA_HOST_NODE_PARAMS_v1

Host node parameters.

CUDA_HOST_NODE_PARAMS_v2

Host node parameters.

CUDA_KERNEL_NODE_PARAMS_v1

GPU kernel node parameters.

CUDA_KERNEL_NODE_PARAMS_v2

GPU kernel node parameters.

CUDA_KERNEL_NODE_PARAMS_v3

GPU kernel node parameters.

CUDA_LAUNCH_PARAMS_v1

Kernel launch parameters.

CUDA_MEMCPY2D_v2

2D memory copy parameters

CUDA_MEMCPY3D_BATCH_OP_v1

CUDA_MEMCPY3D_PEER_v1

3D memory cross-context copy parameters

CUDA_MEMCPY3D_v2

3D memory copy parameters

CUDA_MEMCPY_NODE_PARAMS

Memcpy node parameters.

CUDA_MEMSET_NODE_PARAMS_v1

Memset node parameters.

CUDA_MEMSET_NODE_PARAMS_v2

Memset node parameters.

CUDA_MEM_ALLOC_NODE_PARAMS_v1

Memory allocation node parameters.

CUDA_MEM_ALLOC_NODE_PARAMS_v2

Memory allocation node parameters.

CUDA_MEM_FREE_NODE_PARAMS

Memory free node parameters.

CUDA_POINTER_ATTRIBUTE_P2P_TOKENS_v1

GPU Direct v3 tokens.

CUDA_RESOURCE_DESC_v1

CUDA Resource descriptor.

CUDA_RESOURCE_VIEW_DESC_v1

Resource view descriptor.

CUDA_TEXTURE_DESC_v1

Texture descriptor.

CUaccessPolicyWindow_v1

Specifies an access policy for a window, a contiguous extent of memory beginning at base_ptr and ending at base_ptr + num_bytes.

CUarrayMapInfo_v1

Specifies the CUDA array or CUDA mipmapped array memory mapping information.

CUasyncNotificationInfo

Information passed to the user via the async notification callback.

CUcheckpointCheckpointArgs

CUDA checkpoint optional checkpoint arguments.

CUcheckpointCustomStorageInfo

Output from CUDA custom storage checkpoint/restore: per-GPU device pointers and a handle to complete the operation.

CUcheckpointCustomStoragePerDeviceData

Per-GPU data for zero-copy mapped device memory used with CUDA checkpoint/restore on custom storage.

CUcheckpointGpuPair

CUDA checkpoint GPU UUID pairs for device remapping during restore.

CUcheckpointLockArgs

CUDA checkpoint optional lock arguments.

CUcheckpointRestoreArgs

CUDA checkpoint optional restore arguments.

CUcheckpointUnlockArgs

CUDA checkpoint optional unlock arguments.

CUctxCigParam

CIG Context Create Params.

CUctxCreateParams

Params for creating CUDA context.

CUdevprop_v1

Legacy device properties.

CUeglFrame_v1

CUDA EGLFrame structure Descriptor - structure defining one frame of EGL.

CUexecAffinityParam_v1

Execution Affinity Parameters.

CUexecAffinitySmCount_v1

Value for CU_EXEC_AFFINITY_TYPE_SM_COUNT .

CUextent3D_v1

Struct representing width/height/depth of a CUarray in elements.

CUgraphEdgeData

Optional annotation for edges in a CUDA graph.

CUgraphExecUpdateResultInfo_v1

Result information returned by cuGraphExecUpdate.

CUgraphNodeParams

Graph node parameters.

CUipcEventHandle_v1

CUDA IPC event handle.

CUipcMemHandle_v1

CUDA IPC mem handle.

CUlaunchAttribute

Launch attribute.

CUlaunchConfig

CUDA extensible launch configuration.

CUlaunchMemSyncDomainMap

Memory Synchronization Domain map.

CUlibraryHostUniversalFunctionAndDataTable

CUmemAccessDesc_v1

Memory access descriptor.

CUmemAllocationProp_v1

Specifies the allocation properties for a allocation.

CUmemFabricHandle_v1

Fabric handle - An opaque handle representing a memory allocation that can be exported to processes in same or different nodes.

CUmemLocation_v1

Specifies a memory location.

CUmemPoolProps_v1

Specifies the properties of allocations made from the pool.

CUmemPoolPtrExportData_v1

Opaque data for exporting a pool allocation.

CUmemcpy3DOperand_v1

Struct representing an operand for copy with cuMemcpy3DBatchAsync.

CUmemcpyAttributes_v1

Attributes specific to copies within a batch.

CUmulticastObjectProp_v1

Specifies the properties for a multicast object.

CUoffset3D_v1

Struct representing a 3D offset.

CUstreamCigCaptureParams

Params for capturing CUDA stream to CIG streamCigParams must be non-NULL.

CUstreamCigParam

CIG Stream Capture Params.

CUtensorMap

Tensor map descriptor.

CUuuid

Unions

CUlaunchAttributeValue

Launch attributes union; used as value field of CUlaunchAttribute .

CUstreamBatchMemOpParams_v1

Per-operation parameters for cuStreamBatchMemOp.

##  6.5.1. Macros

`` CUDA_ARRAY3D_2DARRAY 0x01 ``

Deprecated, use CUDA_ARRAY3D_LAYERED.

`` CUDA_ARRAY3D_COLOR_ATTACHMENT 0x20 ``

This flag indicates that the CUDA array may be bound as a color target in an external graphics API.

`` CUDA_ARRAY3D_CUBEMAP 0x04 ``

If set, the CUDA array is a collection of six 2D arrays, representing faces of a cube.

The width of such a CUDA array must be equal to its height, and Depth must be six. If CUDA_ARRAY3D_LAYERED flag is also set, then the CUDA array is a collection of cubemaps and Depth must be a multiple of six.

`` CUDA_ARRAY3D_DEFERRED_MAPPING 0x80 ``

This flag if set indicates that the CUDA array or CUDA mipmapped array will allow deferred memory mapping.

`` CUDA_ARRAY3D_DEPTH_TEXTURE 0x10 ``

This flag if set indicates that the CUDA array is a DEPTH_TEXTURE.

`` CUDA_ARRAY3D_LAYERED 0x01 ``

If set, the CUDA array is a collection of layers, where each layer is either a 1D or a 2D array and the Depth member of CUDA_ARRAY3D_DESCRIPTOR specifies the number of layers, not the depth of a 3D array.

`` CUDA_ARRAY3D_SPARSE 0x40 ``

This flag if set indicates that the CUDA array or CUDA mipmapped array is a sparse CUDA array or CUDA mipmapped array respectively.

`` CUDA_ARRAY3D_SURFACE_LDST 0x02 ``

This flag must be set in order to bind a surface reference to the CUDA array.

`` CUDA_ARRAY3D_TEXTURE_GATHER 0x08 ``

This flag must be set in order to perform texture gather operations on a CUDA array.

`` CUDA_ARRAY3D_VIDEO_ENCODE_DECODE 0x100 ``

This flag indicates that the CUDA array will be used for hardware accelerated video encode/decode operations.

`` CUDA_CB __stdcall ``

`` CUDA_COOPERATIVE_LAUNCH_MULTI_DEVICE_NO_POST_LAUNCH_SYNC 0x02 ``

If set, any subsequent work pushed in a stream that participated in a call to cuLaunchCooperativeKernelMultiDevice will only wait for the kernel launched on the GPU corresponding to that stream to complete before it begins execution.

`` CUDA_COOPERATIVE_LAUNCH_MULTI_DEVICE_NO_PRE_LAUNCH_SYNC 0x01 ``

If set, each kernel launched as part of cuLaunchCooperativeKernelMultiDevice only waits for prior work in the stream corresponding to that GPU to complete before the kernel begins execution.

`` CUDA_EGL_INFINITE_TIMEOUT 0xFFFFFFFF ``

Indicates that timeout for cuEGLStreamConsumerAcquireFrame is infinite.

`` CUDA_EXTERNAL_MEMORY_DEDICATED 0x1 ``

Indicates that the external memory object is a dedicated resource.

`` CUDA_EXTERNAL_SEMAPHORE_SIGNAL_SKIP_NVSCIBUF_MEMSYNC 0x01 ``

When the `flags` parameter of CUDA_EXTERNAL_SEMAPHORE_SIGNAL_PARAMS contains this flag, it indicates that signaling an external semaphore object should skip performing appropriate memory synchronization operations over all the external memory objects that are imported as CU_EXTERNAL_MEMORY_HANDLE_TYPE_NVSCIBUF, which otherwise are performed by default to ensure data coherency with other importers of the same NvSciBuf memory objects.

`` CUDA_EXTERNAL_SEMAPHORE_WAIT_SKIP_NVSCIBUF_MEMSYNC 0x02 ``

When the `flags` parameter of CUDA_EXTERNAL_SEMAPHORE_WAIT_PARAMS contains this flag, it indicates that waiting on an external semaphore object should skip performing appropriate memory synchronization operations over all the external memory objects that are imported as CU_EXTERNAL_MEMORY_HANDLE_TYPE_NVSCIBUF, which otherwise are performed by default to ensure data coherency with other importers of the same NvSciBuf memory objects.

`` CUDA_NVSCISYNC_ATTR_SIGNAL 0x1 ``

When `flags` of cuDeviceGetNvSciSyncAttributes is set to this, it indicates that application needs signaler specific NvSciSyncAttr to be filled by cuDeviceGetNvSciSyncAttributes.

`` CUDA_NVSCISYNC_ATTR_WAIT 0x2 ``

When `flags` of cuDeviceGetNvSciSyncAttributes is set to this, it indicates that application needs waiter specific NvSciSyncAttr to be filled by cuDeviceGetNvSciSyncAttributes.

`` CUDA_VERSION 13040 ``

CUDA API version number.

`` CU_ARRAY_SPARSE_PROPERTIES_SINGLE_MIPTAIL 0x1 ``

Indicates that the layered sparse CUDA array or CUDA mipmapped array has a single mip tail region for all layers.

`` CU_COMPUTE_ACCELERATED_TARGET_BASE 0x10000 ``

`` CU_COMPUTE_FAMILY_TARGET_BASE 0x20000 ``

`` CU_DEVICE_CPU ((CUdevice)-1) ``

Device that represents the CPU.

`` CU_DEVICE_INVALID ((CUdevice)-2) ``

Device that represents an invalid device.

`` CU_GRAPH_COND_ASSIGN_DEFAULT 0x1 ``

Conditional node handle flags.

Default value is applied when graph is launched.

`` CU_GRAPH_KERNEL_NODE_PORT_DEFAULT 0 ``

This port activates when the kernel has finished executing.

`` CU_GRAPH_KERNEL_NODE_PORT_LAUNCH_ORDER 2 ``

This port activates when all blocks of the kernel have begun execution.

See also CU_LAUNCH_ATTRIBUTE_LAUNCH_COMPLETION_EVENT.

`` CU_GRAPH_KERNEL_NODE_PORT_PROGRAMMATIC 1 ``

This port activates when all blocks of the kernel have performed cudaTriggerProgrammaticLaunchCompletion() or have terminated.

It must be used with edge type CU_GRAPH_DEPENDENCY_TYPE_PROGRAMMATIC. See also CU_LAUNCH_ATTRIBUTE_PROGRAMMATIC_EVENT.

`` CU_IPC_HANDLE_SIZE 64 ``

CUDA IPC handle size.

`` CU_KERNEL_NODE_ATTRIBUTE_ACCESS_POLICY_WINDOW CU_LAUNCH_ATTRIBUTE_ACCESS_POLICY_WINDOW ``

`` CU_KERNEL_NODE_ATTRIBUTE_CLUSTER_DIMENSION CU_LAUNCH_ATTRIBUTE_CLUSTER_DIMENSION ``

`` CU_KERNEL_NODE_ATTRIBUTE_CLUSTER_SCHEDULING_POLICY_PREFERENCE CU_LAUNCH_ATTRIBUTE_CLUSTER_SCHEDULING_POLICY_PREFERENCE ``

`` CU_KERNEL_NODE_ATTRIBUTE_COOPERATIVE CU_LAUNCH_ATTRIBUTE_COOPERATIVE ``

`` CU_KERNEL_NODE_ATTRIBUTE_DEVICE_UPDATABLE_KERNEL_NODE CU_LAUNCH_ATTRIBUTE_DEVICE_UPDATABLE_KERNEL_NODE ``

`` CU_KERNEL_NODE_ATTRIBUTE_MEM_SYNC_DOMAIN CU_LAUNCH_ATTRIBUTE_MEM_SYNC_DOMAIN ``

`` CU_KERNEL_NODE_ATTRIBUTE_MEM_SYNC_DOMAIN_MAP CU_LAUNCH_ATTRIBUTE_MEM_SYNC_DOMAIN_MAP ``

`` CU_KERNEL_NODE_ATTRIBUTE_PREFERRED_CLUSTER_DIMENSION CU_LAUNCH_ATTRIBUTE_PREFERRED_CLUSTER_DIMENSION ``

`` CU_KERNEL_NODE_ATTRIBUTE_PREFERRED_SHARED_MEMORY_CARVEOUT CU_LAUNCH_ATTRIBUTE_PREFERRED_SHARED_MEMORY_CARVEOUT ``

`` CU_KERNEL_NODE_ATTRIBUTE_PRIORITY CU_LAUNCH_ATTRIBUTE_PRIORITY ``

`` CU_LAUNCH_KERNEL_REQUIRED_BLOCK_DIM 1 ``

Launch with the required block dimension.

`` CU_LAUNCH_PARAM_BUFFER_POINTER ((void*)CU_LAUNCH_PARAM_BUFFER_POINTER_AS_INT) ``

Indicator that the next value in the `extra` parameter to cuLaunchKernel will be a pointer to a buffer containing all kernel parameters used for launching kernel `f`.

This buffer needs to honor all alignment/padding requirements of the individual parameters. If CU_LAUNCH_PARAM_BUFFER_SIZE is not also specified in the `extra` array, then CU_LAUNCH_PARAM_BUFFER_POINTER will have no effect.

`` CU_LAUNCH_PARAM_BUFFER_POINTER_AS_INT 0x01 ``

C++ compile time constant for CU_LAUNCH_PARAM_BUFFER_POINTER.

`` CU_LAUNCH_PARAM_BUFFER_SIZE ((void*)CU_LAUNCH_PARAM_BUFFER_SIZE_AS_INT) ``

Indicator that the next value in the `extra` parameter to cuLaunchKernel will be a pointer to a size_t which contains the size of the buffer specified with CU_LAUNCH_PARAM_BUFFER_POINTER.

It is required that CU_LAUNCH_PARAM_BUFFER_POINTER also be specified in the `extra` array if the value associated with CU_LAUNCH_PARAM_BUFFER_SIZE is not zero.

`` CU_LAUNCH_PARAM_BUFFER_SIZE_AS_INT 0x02 ``

C++ compile time constant for CU_LAUNCH_PARAM_BUFFER_SIZE.

`` CU_LAUNCH_PARAM_END ((void*)CU_LAUNCH_PARAM_END_AS_INT) ``

End of array terminator for the `extra` parameter to cuLaunchKernel.

`` CU_LAUNCH_PARAM_END_AS_INT 0x00 ``

C++ compile time constant for CU_LAUNCH_PARAM_END.

`` CU_MEMHOSTALLOC_DEVICEMAP 0x02 ``

If set, host memory is mapped into CUDA address space and cuMemHostGetDevicePointer() may be called on the host pointer.

Flag for cuMemHostAlloc()

`` CU_MEMHOSTALLOC_PORTABLE 0x01 ``

If set, host memory is portable between CUDA contexts.

Flag for cuMemHostAlloc()

`` CU_MEMHOSTALLOC_WRITECOMBINED 0x04 ``

If set, host memory is allocated as write-combined - fast to write, faster to DMA, slow to read except via SSE4 streaming load instruction (MOVNTDQA).

Flag for cuMemHostAlloc()

`` CU_MEMHOSTREGISTER_DEVICEMAP 0x02 ``

If set, host memory is mapped into CUDA address space and cuMemHostGetDevicePointer() may be called on the host pointer.

Flag for cuMemHostRegister()

`` CU_MEMHOSTREGISTER_IOMEMORY 0x04 ``

If set, the passed memory pointer is treated as pointing to some memory-mapped I/O space, e.g.

belonging to a third-party PCIe device. On Windows the flag is a no-op. On Linux that memory is marked as non cache-coherent for the GPU and is expected to be physically contiguous. It may return CUDA_ERROR_NOT_PERMITTED if run as an unprivileged user, CUDA_ERROR_NOT_SUPPORTED on older Linux kernel versions. On all other platforms, it is not supported and CUDA_ERROR_NOT_SUPPORTED is returned. Flag for cuMemHostRegister()

`` CU_MEMHOSTREGISTER_PORTABLE 0x01 ``

If set, host memory is portable between CUDA contexts.

Flag for cuMemHostRegister()

`` CU_MEMHOSTREGISTER_READ_ONLY 0x08 ``

If set, the passed memory pointer is treated as pointing to memory that is considered read-only by the device.

On platforms without CU_DEVICE_ATTRIBUTE_PAGEABLE_MEMORY_ACCESS_USES_HOST_PAGE_TABLES, this flag is required in order to register memory mapped to the CPU as read-only. Support for the use of this flag can be queried from the device attribute CU_DEVICE_ATTRIBUTE_READ_ONLY_HOST_REGISTER_SUPPORTED. Using this flag with a current context associated with a device that does not have this attribute set will cause cuMemHostRegister to error with CUDA_ERROR_NOT_SUPPORTED.

`` CU_MEM_CREATE_USAGE_GPU_DIRECT_RDMA_OVER_PCIE 0x4 ``

Setting this flag forces GPUDirect RDMA on a locality-domain-localized allocation to use the PCIe (BAR1) path, allowing the allocation to remain locality-domain localized on platforms where the platform-coherent RDMA path does not support localized allocations.

Because on some platforms the PCIe bandwidth is limited, using this flag may result in lower RDMA bandwidth than the default RDMA mapping link. Note that this flag does not itself force PCIe to be used, and that this must be done when creating the RDMA export. CU_DEVICE_ATTRIBUTE_GPU_DIRECT_RDMA_WITH_LOCALIZED_MEMORY_SUPPORTED indicates whether this flag is needed to create GPUDirect RDMA capable localized memory allocations. This flag is only valid if gpuDirectRDMACapable is set.

`` CU_MEM_CREATE_USAGE_HW_DECOMPRESS 0x2 ``

This flag, if set, indicates that the memory will be used as a buffer for hardware accelerated decompression.

`` CU_MEM_CREATE_USAGE_TILE_POOL 0x1 ``

This flag if set indicates that the memory will be used as a tile pool.

`` CU_MEM_POOL_CREATE_USAGE_HW_DECOMPRESS 0x2 ``

This flag, if set, indicates that the memory will be used as a buffer for hardware accelerated decompression.

`` CU_PARAM_TR_DEFAULT -1 ``

For texture references loaded into the module, use default texunit from texture reference.

`` CU_STREAM_ATTRIBUTE_ACCESS_POLICY_WINDOW CU_LAUNCH_ATTRIBUTE_ACCESS_POLICY_WINDOW ``

`` CU_STREAM_ATTRIBUTE_MEM_SYNC_DOMAIN CU_LAUNCH_ATTRIBUTE_MEM_SYNC_DOMAIN ``

`` CU_STREAM_ATTRIBUTE_MEM_SYNC_DOMAIN_MAP CU_LAUNCH_ATTRIBUTE_MEM_SYNC_DOMAIN_MAP ``

`` CU_STREAM_ATTRIBUTE_PRIORITY CU_LAUNCH_ATTRIBUTE_PRIORITY ``

`` CU_STREAM_ATTRIBUTE_SYNCHRONIZATION_POLICY CU_LAUNCH_ATTRIBUTE_SYNCHRONIZATION_POLICY ``

`` CU_STREAM_LEGACY ((CUstream)0x1) ``

Legacy stream handle.

Stream handle that can be passed as a CUstream to use an implicit stream with legacy synchronization behavior.

See details of the

Note

See ‘Stream sync behavior’

`` CU_STREAM_PER_THREAD ((CUstream)0x2) ``

Per-thread stream handle.

Stream handle that can be passed as a CUstream to use an implicit stream with per-thread synchronization behavior.

See details of the

Note

See ‘Stream sync behavior’

`` CU_TENSOR_MAP_NUM_QWORDS 16 ``

Size of tensor map descriptor.

`` CU_TRSA_OVERRIDE_FORMAT 0x01 ``

Override the texref format with a format inferred from the array.

Flag for cuTexRefSetArray()

`` CU_TRSF_DISABLE_TRILINEAR_OPTIMIZATION 0x20 ``

Disable any trilinear filtering optimizations.

Flag for cuTexRefSetFlags() and cuTexObjectCreate()

`` CU_TRSF_NORMALIZED_COORDINATES 0x02 ``

Use normalized texture coordinates in the range [0,1) instead of [0,dim).

Flag for cuTexRefSetFlags() and cuTexObjectCreate()

`` CU_TRSF_READ_AS_INTEGER 0x01 ``

Read the texture as integers rather than promoting the values to floats in the range [0,1].

Flag for cuTexRefSetFlags() and cuTexObjectCreate()

`` CU_TRSF_SEAMLESS_CUBEMAP 0x40 ``

Enable seamless cube map filtering.

Flag for cuTexObjectCreate()

`` CU_TRSF_SRGB 0x10 ``

Perform sRGB->linear conversion during texture read.

Flag for cuTexRefSetFlags() and cuTexObjectCreate()

`` CU_UUID_HAS_BEEN_DEFINED ``

`` MAX_PLANES 3 ``

Maximum number of planes per frame.

##  6.5.2. Enumerations

`` enum CUDA_POINTER_ATTRIBUTE_ACCESS_FLAGS ``

Access flags that specify the level of access the current context’s device has on the memory referenced.

_Values:_

`` enumerator CU_POINTER_ATTRIBUTE_ACCESS_FLAG_NONE ``

No access, meaning the device cannot access this memory at all, thus must be staged through accessible memory in order to complete certain operations.

`` enumerator CU_POINTER_ATTRIBUTE_ACCESS_FLAG_READ ``

Read-only access, meaning writes to this memory are considered invalid accesses and thus return error in that case.

`` enumerator CU_POINTER_ATTRIBUTE_ACCESS_FLAG_READWRITE ``

Read-write access, the device has full read-write access to the memory.

`` enum CUGPUDirectRDMAWritesOrdering ``

Platform native ordering for GPUDirect RDMA writes.

_Values:_

`` enumerator CU_GPU_DIRECT_RDMA_WRITES_ORDERING_NONE ``

The device does not natively support ordering of remote writes.

cuFlushGPUDirectRDMAWrites() can be leveraged if supported.

`` enumerator CU_GPU_DIRECT_RDMA_WRITES_ORDERING_OWNER ``

Natively, the device can consistently consume remote writes, although other CUDA devices may not.

`` enumerator CU_GPU_DIRECT_RDMA_WRITES_ORDERING_ALL_DEVICES ``

Any CUDA device in the system can consistently consume remote writes to this device.

`` enum CUaccessProperty ``

Specifies performance hint with CUaccessPolicyWindow for hitProp and missProp members.

_Values:_

`` enumerator CU_ACCESS_PROPERTY_NORMAL ``

Normal cache persistence.

`` enumerator CU_ACCESS_PROPERTY_STREAMING ``

Streaming access is less likely to persit from cache.

`` enumerator CU_ACCESS_PROPERTY_PERSISTING ``

Persisting access is more likely to persist in cache.

`` enum CUaddress_mode ``

Texture reference addressing modes.

_Values:_

`` enumerator CU_TR_ADDRESS_MODE_WRAP ``

Wrapping address mode.

`` enumerator CU_TR_ADDRESS_MODE_CLAMP ``

Clamp to edge address mode.

`` enumerator CU_TR_ADDRESS_MODE_MIRROR ``

Mirror address mode.

`` enumerator CU_TR_ADDRESS_MODE_BORDER ``

Border address mode.

`` enum CUarraySparseSubresourceType ``

Sparse subresource types.

_Values:_

`` enumerator CU_ARRAY_SPARSE_SUBRESOURCE_TYPE_SPARSE_LEVEL ``

`` enumerator CU_ARRAY_SPARSE_SUBRESOURCE_TYPE_MIPTAIL ``

`` enum CUarray_cubemap_face ``

Array indices for cube faces.

_Values:_

`` enumerator CU_CUBEMAP_FACE_POSITIVE_X ``

Positive X face of cubemap.

`` enumerator CU_CUBEMAP_FACE_NEGATIVE_X ``

Negative X face of cubemap.

`` enumerator CU_CUBEMAP_FACE_POSITIVE_Y ``

Positive Y face of cubemap.

`` enumerator CU_CUBEMAP_FACE_NEGATIVE_Y ``

Negative Y face of cubemap.

`` enumerator CU_CUBEMAP_FACE_POSITIVE_Z ``

Positive Z face of cubemap.

`` enumerator CU_CUBEMAP_FACE_NEGATIVE_Z ``

Negative Z face of cubemap.

`` enum CUarray_format ``

Array formats.

_Values:_

`` enumerator CU_AD_FORMAT_UNSIGNED_INT8 ``

Unsigned 8-bit integers.

`` enumerator CU_AD_FORMAT_UNSIGNED_INT16 ``

Unsigned 16-bit integers.

`` enumerator CU_AD_FORMAT_UNSIGNED_INT32 ``

Unsigned 32-bit integers.

`` enumerator CU_AD_FORMAT_SIGNED_INT8 ``

Signed 8-bit integers.

`` enumerator CU_AD_FORMAT_SIGNED_INT16 ``

Signed 16-bit integers.

`` enumerator CU_AD_FORMAT_SIGNED_INT32 ``

Signed 32-bit integers.

`` enumerator CU_AD_FORMAT_HALF ``

16-bit floating point

`` enumerator CU_AD_FORMAT_FLOAT ``

32-bit floating point

`` enumerator CU_AD_FORMAT_NV12 ``

8-bit YUV planar format, with 4:2:0 sampling

`` enumerator CU_AD_FORMAT_UNORM_INT8X1 ``

1 channel unsigned 8-bit normalized integer

`` enumerator CU_AD_FORMAT_UNORM_INT8X2 ``

2 channel unsigned 8-bit normalized integer

`` enumerator CU_AD_FORMAT_UNORM_INT8X4 ``

4 channel unsigned 8-bit normalized integer

`` enumerator CU_AD_FORMAT_UNORM_INT16X1 ``

1 channel unsigned 16-bit normalized integer

`` enumerator CU_AD_FORMAT_UNORM_INT16X2 ``

2 channel unsigned 16-bit normalized integer

`` enumerator CU_AD_FORMAT_UNORM_INT16X4 ``

4 channel unsigned 16-bit normalized integer

`` enumerator CU_AD_FORMAT_SNORM_INT8X1 ``

1 channel signed 8-bit normalized integer

`` enumerator CU_AD_FORMAT_SNORM_INT8X2 ``

2 channel signed 8-bit normalized integer

`` enumerator CU_AD_FORMAT_SNORM_INT8X4 ``

4 channel signed 8-bit normalized integer

`` enumerator CU_AD_FORMAT_SNORM_INT16X1 ``

1 channel signed 16-bit normalized integer

`` enumerator CU_AD_FORMAT_SNORM_INT16X2 ``

2 channel signed 16-bit normalized integer

`` enumerator CU_AD_FORMAT_SNORM_INT16X4 ``

4 channel signed 16-bit normalized integer

`` enumerator CU_AD_FORMAT_BC1_UNORM ``

4 channel unsigned normalized block-compressed (BC1 compression) format

`` enumerator CU_AD_FORMAT_BC1_UNORM_SRGB ``

4 channel unsigned normalized block-compressed (BC1 compression) format with sRGB encoding

`` enumerator CU_AD_FORMAT_BC2_UNORM ``

4 channel unsigned normalized block-compressed (BC2 compression) format

`` enumerator CU_AD_FORMAT_BC2_UNORM_SRGB ``

4 channel unsigned normalized block-compressed (BC2 compression) format with sRGB encoding

`` enumerator CU_AD_FORMAT_BC3_UNORM ``

4 channel unsigned normalized block-compressed (BC3 compression) format

`` enumerator CU_AD_FORMAT_BC3_UNORM_SRGB ``

4 channel unsigned normalized block-compressed (BC3 compression) format with sRGB encoding

`` enumerator CU_AD_FORMAT_BC4_UNORM ``

1 channel unsigned normalized block-compressed (BC4 compression) format

`` enumerator CU_AD_FORMAT_BC4_SNORM ``

1 channel signed normalized block-compressed (BC4 compression) format

`` enumerator CU_AD_FORMAT_BC5_UNORM ``

2 channel unsigned normalized block-compressed (BC5 compression) format

`` enumerator CU_AD_FORMAT_BC5_SNORM ``

2 channel signed normalized block-compressed (BC5 compression) format

`` enumerator CU_AD_FORMAT_BC6H_UF16 ``

3 channel unsigned half-float block-compressed (BC6H compression) format

`` enumerator CU_AD_FORMAT_BC6H_SF16 ``

3 channel signed half-float block-compressed (BC6H compression) format

`` enumerator CU_AD_FORMAT_BC7_UNORM ``

4 channel unsigned normalized block-compressed (BC7 compression) format

`` enumerator CU_AD_FORMAT_BC7_UNORM_SRGB ``

4 channel unsigned normalized block-compressed (BC7 compression) format with sRGB encoding

`` enumerator CU_AD_FORMAT_P010 ``

10-bit YUV planar format, with 4:2:0 sampling

`` enumerator CU_AD_FORMAT_P016 ``

16-bit YUV planar format, with 4:2:0 sampling

`` enumerator CU_AD_FORMAT_NV16 ``

8-bit YUV planar format, with 4:2:2 sampling

`` enumerator CU_AD_FORMAT_P210 ``

10-bit YUV planar format, with 4:2:2 sampling

`` enumerator CU_AD_FORMAT_P216 ``

16-bit YUV planar format, with 4:2:2 sampling

`` enumerator CU_AD_FORMAT_YUY2 ``

2 channel, 8-bit YUV packed planar format, with 4:2:2 sampling

`` enumerator CU_AD_FORMAT_Y210 ``

2 channel, 10-bit YUV packed planar format, with 4:2:2 sampling

`` enumerator CU_AD_FORMAT_Y216 ``

2 channel, 16-bit YUV packed planar format, with 4:2:2 sampling

`` enumerator CU_AD_FORMAT_AYUV ``

4 channel, 8-bit YUV packed planar format, with 4:4:4 sampling

`` enumerator CU_AD_FORMAT_Y410 ``

10-bit YUV packed planar format, with 4:4:4 sampling

`` enumerator CU_AD_FORMAT_Y416 ``

4 channel, 12-bit YUV packed planar format, with 4:4:4 sampling

`` enumerator CU_AD_FORMAT_Y444_PLANAR8 ``

3 channel 8-bit YUV planar format, with 4:4:4 sampling

`` enumerator CU_AD_FORMAT_Y444_PLANAR10 ``

3 channel 10-bit YUV planar format, with 4:4:4 sampling

`` enumerator CU_AD_FORMAT_YUV444_8bit_SemiPlanar ``

3 channel 8-bit YUV semi-planar format, with 4:4:4 sampling

`` enumerator CU_AD_FORMAT_YUV444_16bit_SemiPlanar ``

3 channel 16-bit YUV semi-planar format, with 4:4:4 sampling

`` enumerator CU_AD_FORMAT_UNORM_INT_101010_2 ``

4 channel unorm R10G10B10A2 RGB format

`` enumerator CU_AD_FORMAT_UINT8_PACKED_422 ``

4 channel unsigned 8-bit YUV packed format, with 4:2:2 sampling

`` enumerator CU_AD_FORMAT_UINT8_PACKED_444 ``

4 channel unsigned 8-bit YUV packed format, with 4:4:4 sampling

`` enumerator CU_AD_FORMAT_UINT8_SEMIPLANAR_420 ``

3 channel unsigned 8-bit YUV semi-planar format, with 4:2:0 sampling

`` enumerator CU_AD_FORMAT_UINT16_SEMIPLANAR_420 ``

3 channel unsigned 16-bit YUV semi-planar format, with 4:2:0 sampling

`` enumerator CU_AD_FORMAT_UINT8_SEMIPLANAR_422 ``

3 channel unsigned 8-bit YUV semi-planar format, with 4:2:2 sampling

`` enumerator CU_AD_FORMAT_UINT16_SEMIPLANAR_422 ``

3 channel unsigned 16-bit YUV semi-planar format, with 4:2:2 sampling

`` enumerator CU_AD_FORMAT_UINT8_SEMIPLANAR_444 ``

3 channel unsigned 8-bit YUV semi-planar format, with 4:4:4 sampling

`` enumerator CU_AD_FORMAT_UINT16_SEMIPLANAR_444 ``

3 channel unsigned 16-bit YUV semi-planar format, with 4:4:4 sampling

`` enumerator CU_AD_FORMAT_UINT8_PLANAR_420 ``

3 channel unsigned 8-bit YUV planar format, with 4:2:0 sampling

`` enumerator CU_AD_FORMAT_UINT16_PLANAR_420 ``

3 channel unsigned 16-bit YUV planar format, with 4:2:0 sampling

`` enumerator CU_AD_FORMAT_UINT8_PLANAR_422 ``

3 channel unsigned 8-bit YUV planar format, with 4:2:2 sampling

`` enumerator CU_AD_FORMAT_UINT16_PLANAR_422 ``

3 channel unsigned 16-bit YUV planar format, with 4:2:2 sampling

`` enumerator CU_AD_FORMAT_UINT8_PLANAR_444 ``

3 channel unsigned 8-bit YUV planar format, with 4:4:4 sampling

`` enumerator CU_AD_FORMAT_UINT16_PLANAR_444 ``

3 channel unsigned 16-bit YUV planar format, with 4:4:4 sampling

`` enumerator CU_AD_FORMAT_MAX ``

`` enum CUasyncNotificationType ``

Types of async notification that can be sent.

_Values:_

`` enumerator CU_ASYNC_NOTIFICATION_TYPE_OVER_BUDGET ``

Sent when the process has exceeded its device memory budget.

`` enum CUatomicOperation ``

CUDA-valid Atomic Operations.

_Values:_

`` enumerator CU_ATOMIC_OPERATION_INTEGER_ADD ``

`` enumerator CU_ATOMIC_OPERATION_INTEGER_MIN ``

`` enumerator CU_ATOMIC_OPERATION_INTEGER_MAX ``

`` enumerator CU_ATOMIC_OPERATION_INTEGER_INCREMENT ``

`` enumerator CU_ATOMIC_OPERATION_INTEGER_DECREMENT ``

`` enumerator CU_ATOMIC_OPERATION_AND ``

`` enumerator CU_ATOMIC_OPERATION_OR ``

`` enumerator CU_ATOMIC_OPERATION_XOR ``

`` enumerator CU_ATOMIC_OPERATION_EXCHANGE ``

`` enumerator CU_ATOMIC_OPERATION_CAS ``

`` enumerator CU_ATOMIC_OPERATION_FLOAT_ADD ``

`` enumerator CU_ATOMIC_OPERATION_FLOAT_MIN ``

`` enumerator CU_ATOMIC_OPERATION_FLOAT_MAX ``

`` enumerator CU_ATOMIC_OPERATION_MAX ``

`` enum CUatomicOperationCapability ``

CUDA-valid Atomic Operation capabilities.

_Values:_

`` enumerator CU_ATOMIC_CAPABILITY_SIGNED ``

`` enumerator CU_ATOMIC_CAPABILITY_UNSIGNED ``

`` enumerator CU_ATOMIC_CAPABILITY_REDUCTION ``

`` enumerator CU_ATOMIC_CAPABILITY_SCALAR_32 ``

`` enumerator CU_ATOMIC_CAPABILITY_SCALAR_64 ``

`` enumerator CU_ATOMIC_CAPABILITY_SCALAR_128 ``

`` enumerator CU_ATOMIC_CAPABILITY_VECTOR_32x4 ``

`` enum CUcigDataType ``

_Values:_

`` enumerator CIG_DATA_TYPE_D3D12_COMMAND_QUEUE ``

D3D12 Command Queue Handle.

`` enumerator CIG_DATA_TYPE_NV_BLOB ``

Nvidia specific data blob used for Vulkan and other NV clients.

`` enum CUclusterSchedulingPolicy ``

Cluster scheduling policies.

These may be passed to cuFuncSetAttribute or cuKernelSetAttribute

_Values:_

`` enumerator CU_CLUSTER_SCHEDULING_POLICY_DEFAULT ``

the default policy

`` enumerator CU_CLUSTER_SCHEDULING_POLICY_SPREAD ``

spread the blocks within a cluster to the SMs

`` enumerator CU_CLUSTER_SCHEDULING_POLICY_LOAD_BALANCING ``

allow the hardware to load-balance the blocks in a cluster to the SMs

`` enumerator CU_CLUSTER_SCHEDULING_POLICY_RUBIN_DSMEM_LOCALITY ``

`` enum CUcomputemode ``

Compute Modes.

_Values:_

`` enumerator CU_COMPUTEMODE_DEFAULT ``

Default compute mode (Multiple contexts allowed per device)

`` enumerator CU_COMPUTEMODE_PROHIBITED ``

Compute-prohibited mode (No contexts can be created on this device at this time)

`` enumerator CU_COMPUTEMODE_EXCLUSIVE_PROCESS ``

Compute-exclusive-process mode (Only one context used by a single process can be present on this device at a time)

`` enum CUctx_flags ``

Context creation flags.

_Values:_

`` enumerator CU_CTX_SCHED_AUTO ``

Automatic scheduling.

`` enumerator CU_CTX_SCHED_SPIN ``

Set spin as default scheduling.

`` enumerator CU_CTX_SCHED_YIELD ``

Set yield as default scheduling.

`` enumerator CU_CTX_SCHED_BLOCKING_SYNC ``

Set blocking synchronization as default scheduling.

`` enumerator CU_CTX_BLOCKING_SYNC ``

Set blocking synchronization as default scheduling.

`` Deprecated: ``

This flag was deprecated as of CUDA 4.0 and was replaced with CU_CTX_SCHED_BLOCKING_SYNC.

`` enumerator CU_CTX_SCHED_MASK ``

`` enumerator CU_CTX_MAP_HOST ``

`` Deprecated: ``

This flag was deprecated as of CUDA 11.0 and it no longer has any effect. All contexts as of CUDA 3.2 behave as though the flag is enabled.

`` enumerator CU_CTX_LMEM_RESIZE_TO_MAX ``

Keep local memory allocation after launch.

`` enumerator CU_CTX_COREDUMP_ENABLE ``

Trigger coredumps from exceptions in this context.

`` enumerator CU_CTX_USER_COREDUMP_ENABLE ``

Enable user pipe to trigger coredumps in this context.

`` enumerator CU_CTX_SYNC_MEMOPS ``

Ensure synchronous memory operations on this context will synchronize.

`` enumerator CU_CTX_FLAGS_MASK ``

`` enum CUdeviceNumaConfig ``

CUDA device NUMA configuration.

_Values:_

`` enumerator CU_DEVICE_NUMA_CONFIG_NONE ``

The GPU is not a NUMA node.

`` enumerator CU_DEVICE_NUMA_CONFIG_NUMA_NODE ``

The GPU is a NUMA node, CU_DEVICE_ATTRIBUTE_NUMA_ID contains its NUMA ID.

`` enum CUdevice_P2PAttribute ``

P2P Attributes.

_Values:_

`` enumerator CU_DEVICE_P2P_ATTRIBUTE_PERFORMANCE_RANK ``

A relative value indicating the performance of the link between two devices.

`` enumerator CU_DEVICE_P2P_ATTRIBUTE_ACCESS_SUPPORTED ``

P2P Access is enable.

`` enumerator CU_DEVICE_P2P_ATTRIBUTE_NATIVE_ATOMIC_SUPPORTED ``

All CUDA-valid atomic operation over the link are supported.

`` enumerator CU_DEVICE_P2P_ATTRIBUTE_ACCESS_ACCESS_SUPPORTED ``

`` Deprecated: ``

use CU_DEVICE_P2P_ATTRIBUTE_CUDA_ARRAY_ACCESS_SUPPORTED instead

`` enumerator CU_DEVICE_P2P_ATTRIBUTE_CUDA_ARRAY_ACCESS_SUPPORTED ``

Accessing CUDA arrays over the link supported.

`` enumerator CU_DEVICE_P2P_ATTRIBUTE_ONLY_PARTIAL_NATIVE_ATOMIC_SUPPORTED ``

Only some CUDA-valid atomic operations over the link are supported.

`` enum CUdevice_attribute ``

Device properties.

_Values:_

`` enumerator CU_DEVICE_ATTRIBUTE_MAX_THREADS_PER_BLOCK ``

Maximum number of threads per block.

`` enumerator CU_DEVICE_ATTRIBUTE_MAX_BLOCK_DIM_X ``

Maximum block dimension X.

`` enumerator CU_DEVICE_ATTRIBUTE_MAX_BLOCK_DIM_Y ``

Maximum block dimension Y.

`` enumerator CU_DEVICE_ATTRIBUTE_MAX_BLOCK_DIM_Z ``

Maximum block dimension Z.

`` enumerator CU_DEVICE_ATTRIBUTE_MAX_GRID_DIM_X ``

Maximum grid dimension X.

`` enumerator CU_DEVICE_ATTRIBUTE_MAX_GRID_DIM_Y ``

Maximum grid dimension Y.

`` enumerator CU_DEVICE_ATTRIBUTE_MAX_GRID_DIM_Z ``

Maximum grid dimension Z.

`` enumerator CU_DEVICE_ATTRIBUTE_MAX_SHARED_MEMORY_PER_BLOCK ``

Maximum shared memory available per block in bytes.

`` enumerator CU_DEVICE_ATTRIBUTE_SHARED_MEMORY_PER_BLOCK ``

Deprecated, use CU_DEVICE_ATTRIBUTE_MAX_SHARED_MEMORY_PER_BLOCK.

`` enumerator CU_DEVICE_ATTRIBUTE_TOTAL_CONSTANT_MEMORY ``

Memory available on device for **constant** variables in a CUDA C kernel in bytes.

`` enumerator CU_DEVICE_ATTRIBUTE_WARP_SIZE ``

Warp size in threads.

`` enumerator CU_DEVICE_ATTRIBUTE_MAX_PITCH ``

Maximum pitch in bytes allowed by memory copies.

`` enumerator CU_DEVICE_ATTRIBUTE_MAX_REGISTERS_PER_BLOCK ``

Maximum number of 32-bit registers available per block.

`` enumerator CU_DEVICE_ATTRIBUTE_REGISTERS_PER_BLOCK ``

Deprecated, use CU_DEVICE_ATTRIBUTE_MAX_REGISTERS_PER_BLOCK.

`` enumerator CU_DEVICE_ATTRIBUTE_CLOCK_RATE ``

Typical clock frequency in kilohertz.

`` enumerator CU_DEVICE_ATTRIBUTE_TEXTURE_ALIGNMENT ``

Alignment requirement for textures.

`` enumerator CU_DEVICE_ATTRIBUTE_GPU_OVERLAP ``

Device can possibly copy memory and execute a kernel concurrently.

Deprecated. Use instead CU_DEVICE_ATTRIBUTE_ASYNC_ENGINE_COUNT.

`` enumerator CU_DEVICE_ATTRIBUTE_MULTIPROCESSOR_COUNT ``

Number of multiprocessors on device.

`` enumerator CU_DEVICE_ATTRIBUTE_KERNEL_EXEC_TIMEOUT ``

Specifies whether there is a run time limit on kernels.

`` enumerator CU_DEVICE_ATTRIBUTE_INTEGRATED ``

Device is integrated with host memory.

`` enumerator CU_DEVICE_ATTRIBUTE_CAN_MAP_HOST_MEMORY ``

Device can map host memory into CUDA address space.

`` enumerator CU_DEVICE_ATTRIBUTE_COMPUTE_MODE ``

Compute mode (See CUcomputemode for details)

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE1D_WIDTH ``

Maximum 1D texture width.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_WIDTH ``

Maximum 2D texture width.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_HEIGHT ``

Maximum 2D texture height.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE3D_WIDTH ``

Maximum 3D texture width.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE3D_HEIGHT ``

Maximum 3D texture height.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE3D_DEPTH ``

Maximum 3D texture depth.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_LAYERED_WIDTH ``

Maximum 2D layered texture width.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_LAYERED_HEIGHT ``

Maximum 2D layered texture height.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_LAYERED_LAYERS ``

Maximum layers in a 2D layered texture.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_ARRAY_WIDTH ``

Deprecated, use CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_LAYERED_WIDTH.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_ARRAY_HEIGHT ``

Deprecated, use CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_LAYERED_HEIGHT.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_ARRAY_NUMSLICES ``

Deprecated, use CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_LAYERED_LAYERS.

`` enumerator CU_DEVICE_ATTRIBUTE_SURFACE_ALIGNMENT ``

Alignment requirement for surfaces.

`` enumerator CU_DEVICE_ATTRIBUTE_CONCURRENT_KERNELS ``

Device can possibly execute multiple kernels concurrently.

`` enumerator CU_DEVICE_ATTRIBUTE_ECC_ENABLED ``

Device has ECC support enabled.

`` enumerator CU_DEVICE_ATTRIBUTE_PCI_BUS_ID ``

PCI bus ID of the device.

`` enumerator CU_DEVICE_ATTRIBUTE_PCI_DEVICE_ID ``

PCI device ID of the device.

`` enumerator CU_DEVICE_ATTRIBUTE_TCC_DRIVER ``

Device is using TCC driver model.

`` enumerator CU_DEVICE_ATTRIBUTE_MEMORY_CLOCK_RATE ``

Peak memory clock frequency in kilohertz.

`` enumerator CU_DEVICE_ATTRIBUTE_GLOBAL_MEMORY_BUS_WIDTH ``

Global memory bus width in bits.

`` enumerator CU_DEVICE_ATTRIBUTE_L2_CACHE_SIZE ``

Size of L2 cache in bytes.

`` enumerator CU_DEVICE_ATTRIBUTE_MAX_THREADS_PER_MULTIPROCESSOR ``

Maximum resident threads per multiprocessor.

`` enumerator CU_DEVICE_ATTRIBUTE_ASYNC_ENGINE_COUNT ``

Number of asynchronous engines.

`` enumerator CU_DEVICE_ATTRIBUTE_UNIFIED_ADDRESSING ``

Device shares a unified address space with the host.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE1D_LAYERED_WIDTH ``

Maximum 1D layered texture width.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE1D_LAYERED_LAYERS ``

Maximum layers in a 1D layered texture.

`` enumerator CU_DEVICE_ATTRIBUTE_CAN_TEX2D_GATHER ``

Deprecated, do not use.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_GATHER_WIDTH ``

Maximum 2D texture width if CUDA_ARRAY3D_TEXTURE_GATHER is set.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_GATHER_HEIGHT ``

Maximum 2D texture height if CUDA_ARRAY3D_TEXTURE_GATHER is set.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE3D_WIDTH_ALTERNATE ``

Alternate maximum 3D texture width.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE3D_HEIGHT_ALTERNATE ``

Alternate maximum 3D texture height.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE3D_DEPTH_ALTERNATE ``

Alternate maximum 3D texture depth.

`` enumerator CU_DEVICE_ATTRIBUTE_PCI_DOMAIN_ID ``

PCI domain ID of the device.

`` enumerator CU_DEVICE_ATTRIBUTE_TEXTURE_PITCH_ALIGNMENT ``

Pitch alignment requirement for textures.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURECUBEMAP_WIDTH ``

Maximum cubemap texture width/height.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURECUBEMAP_LAYERED_WIDTH ``

Maximum cubemap layered texture width/height.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURECUBEMAP_LAYERED_LAYERS ``

Maximum layers in a cubemap layered texture.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACE1D_WIDTH ``

Maximum 1D surface width.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACE2D_WIDTH ``

Maximum 2D surface width.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACE2D_HEIGHT ``

Maximum 2D surface height.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACE3D_WIDTH ``

Maximum 3D surface width.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACE3D_HEIGHT ``

Maximum 3D surface height.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACE3D_DEPTH ``

Maximum 3D surface depth.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACE1D_LAYERED_WIDTH ``

Maximum 1D layered surface width.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACE1D_LAYERED_LAYERS ``

Maximum layers in a 1D layered surface.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACE2D_LAYERED_WIDTH ``

Maximum 2D layered surface width.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACE2D_LAYERED_HEIGHT ``

Maximum 2D layered surface height.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACE2D_LAYERED_LAYERS ``

Maximum layers in a 2D layered surface.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACECUBEMAP_WIDTH ``

Maximum cubemap surface width.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACECUBEMAP_LAYERED_WIDTH ``

Maximum cubemap layered surface width.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACECUBEMAP_LAYERED_LAYERS ``

Maximum layers in a cubemap layered surface.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE1D_LINEAR_WIDTH ``

Deprecated, do not use.

Use cudaDeviceGetTexture1DLinearMaxWidth() or cuDeviceGetTexture1DLinearMaxWidth() instead.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_LINEAR_WIDTH ``

Maximum 2D linear texture width.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_LINEAR_HEIGHT ``

Maximum 2D linear texture height.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_LINEAR_PITCH ``

Maximum 2D linear texture pitch in bytes.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_MIPMAPPED_WIDTH ``

Maximum mipmapped 2D texture width.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_MIPMAPPED_HEIGHT ``

Maximum mipmapped 2D texture height.

`` enumerator CU_DEVICE_ATTRIBUTE_COMPUTE_CAPABILITY_MAJOR ``

Major compute capability version number.

`` enumerator CU_DEVICE_ATTRIBUTE_COMPUTE_CAPABILITY_MINOR ``

Minor compute capability version number.

`` enumerator CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE1D_MIPMAPPED_WIDTH ``

Maximum mipmapped 1D texture width.

`` enumerator CU_DEVICE_ATTRIBUTE_STREAM_PRIORITIES_SUPPORTED ``

Device supports stream priorities.

`` enumerator CU_DEVICE_ATTRIBUTE_GLOBAL_L1_CACHE_SUPPORTED ``

Device supports caching globals in L1.

`` enumerator CU_DEVICE_ATTRIBUTE_LOCAL_L1_CACHE_SUPPORTED ``

Device supports caching locals in L1.

`` enumerator CU_DEVICE_ATTRIBUTE_MAX_SHARED_MEMORY_PER_MULTIPROCESSOR ``

Maximum shared memory available per multiprocessor in bytes.

`` enumerator CU_DEVICE_ATTRIBUTE_MAX_REGISTERS_PER_MULTIPROCESSOR ``

Maximum number of 32-bit registers available per multiprocessor.

`` enumerator CU_DEVICE_ATTRIBUTE_MANAGED_MEMORY ``

Device can allocate managed memory on this system.

`` enumerator CU_DEVICE_ATTRIBUTE_MULTI_GPU_BOARD ``

Device is on a multi-GPU board.

`` enumerator CU_DEVICE_ATTRIBUTE_MULTI_GPU_BOARD_GROUP_ID ``

Unique id for a group of devices on the same multi-GPU board.

`` enumerator CU_DEVICE_ATTRIBUTE_HOST_NATIVE_ATOMIC_SUPPORTED ``

Link between the device and the host supports all native atomic operations.

`` enumerator CU_DEVICE_ATTRIBUTE_SINGLE_TO_DOUBLE_PRECISION_PERF_RATIO ``

Ratio of single precision performance (in floating-point operations per second) to double precision performance.

`` enumerator CU_DEVICE_ATTRIBUTE_PAGEABLE_MEMORY_ACCESS ``

Device supports coherently accessing pageable memory without calling cudaHostRegister on it.

`` enumerator CU_DEVICE_ATTRIBUTE_CONCURRENT_MANAGED_ACCESS ``

Device can coherently access managed memory concurrently with the CPU.

`` enumerator CU_DEVICE_ATTRIBUTE_COMPUTE_PREEMPTION_SUPPORTED ``

Device supports compute preemption.

`` enumerator CU_DEVICE_ATTRIBUTE_CAN_USE_HOST_POINTER_FOR_REGISTERED_MEM ``

Device can access host registered memory at the same virtual address as the CPU.

`` enumerator CU_DEVICE_ATTRIBUTE_CAN_USE_STREAM_MEM_OPS_V1 ``

Deprecated, along with v1 MemOps API, cuStreamBatchMemOp and related APIs are supported.

`` enumerator CU_DEVICE_ATTRIBUTE_CAN_USE_64_BIT_STREAM_MEM_OPS_V1 ``

Deprecated, along with v1 MemOps API, 64-bit operations are supported in cuStreamBatchMemOp and related APIs.

`` enumerator CU_DEVICE_ATTRIBUTE_CAN_USE_STREAM_WAIT_VALUE_NOR_V1 ``

Deprecated, along with v1 MemOps API, CU_STREAM_WAIT_VALUE_NOR is supported.

`` enumerator CU_DEVICE_ATTRIBUTE_COOPERATIVE_LAUNCH ``

Device supports launching cooperative kernels via cuLaunchCooperativeKernel.

`` enumerator CU_DEVICE_ATTRIBUTE_COOPERATIVE_MULTI_DEVICE_LAUNCH ``

Deprecated, cuLaunchCooperativeKernelMultiDevice is deprecated.

`` enumerator CU_DEVICE_ATTRIBUTE_MAX_SHARED_MEMORY_PER_BLOCK_OPTIN ``

Maximum optin shared memory per block.

That is shared memory that is available for dynamic allocation or static allocation (including architecture specific static shared memory) on this device but is not guaranteed to be portable.

`` enumerator CU_DEVICE_ATTRIBUTE_CAN_FLUSH_REMOTE_WRITES ``

The CU_STREAM_WAIT_VALUE_FLUSH flag and the CU_STREAM_MEM_OP_FLUSH_REMOTE_WRITES MemOp are supported on the device.

See Stream Memory Operations for additional details.

`` enumerator CU_DEVICE_ATTRIBUTE_HOST_REGISTER_SUPPORTED ``

Device supports host memory registration via ::cudaHostRegister.

`` enumerator CU_DEVICE_ATTRIBUTE_PAGEABLE_MEMORY_ACCESS_USES_HOST_PAGE_TABLES ``

Device accesses pageable memory via the host’s page tables.

`` enumerator CU_DEVICE_ATTRIBUTE_DIRECT_MANAGED_MEM_ACCESS_FROM_HOST ``

The host can directly access managed memory on the device without migration.

`` enumerator CU_DEVICE_ATTRIBUTE_VIRTUAL_ADDRESS_MANAGEMENT_SUPPORTED ``

Deprecated, Use CU_DEVICE_ATTRIBUTE_VIRTUAL_MEMORY_MANAGEMENT_SUPPORTED.

`` enumerator CU_DEVICE_ATTRIBUTE_VIRTUAL_MEMORY_MANAGEMENT_SUPPORTED ``

Device supports virtual memory management APIs like cuMemAddressReserve, cuMemCreate, cuMemMap and related APIs.

`` enumerator CU_DEVICE_ATTRIBUTE_HANDLE_TYPE_POSIX_FILE_DESCRIPTOR_SUPPORTED ``

Device supports exporting memory to a posix file descriptor with cuMemExportToShareableHandle, if requested via cuMemCreate.

`` enumerator CU_DEVICE_ATTRIBUTE_HANDLE_TYPE_WIN32_HANDLE_SUPPORTED ``

Device supports exporting memory to a Win32 NT handle with cuMemExportToShareableHandle, if requested via cuMemCreate.

`` enumerator CU_DEVICE_ATTRIBUTE_HANDLE_TYPE_WIN32_KMT_HANDLE_SUPPORTED ``

Device supports exporting memory to a Win32 KMT handle with cuMemExportToShareableHandle, if requested via cuMemCreate.

`` enumerator CU_DEVICE_ATTRIBUTE_MAX_BLOCKS_PER_MULTIPROCESSOR ``

Maximum number of blocks per multiprocessor.

`` enumerator CU_DEVICE_ATTRIBUTE_GENERIC_COMPRESSION_SUPPORTED ``

Device supports compression of memory.

`` enumerator CU_DEVICE_ATTRIBUTE_MAX_PERSISTING_L2_CACHE_SIZE ``

Maximum L2 persisting lines capacity setting in bytes.

`` enumerator CU_DEVICE_ATTRIBUTE_MAX_ACCESS_POLICY_WINDOW_SIZE ``

Maximum value of CUaccessPolicyWindow::num_bytes.

`` enumerator CU_DEVICE_ATTRIBUTE_GPU_DIRECT_RDMA_WITH_CUDA_VMM_SUPPORTED ``

Device supports specifying the GPUDirect RDMA flag with cuMemCreate.

`` enumerator CU_DEVICE_ATTRIBUTE_RESERVED_SHARED_MEMORY_PER_BLOCK ``

Shared memory reserved by CUDA driver per block in bytes.

`` enumerator CU_DEVICE_ATTRIBUTE_SPARSE_CUDA_ARRAY_SUPPORTED ``

Device supports sparse CUDA arrays and sparse CUDA mipmapped arrays.

`` enumerator CU_DEVICE_ATTRIBUTE_READ_ONLY_HOST_REGISTER_SUPPORTED ``

Device supports using the cuMemHostRegister flag ::CU_MEMHOSTERGISTER_READ_ONLY to register memory that must be mapped as read-only to the GPU.

`` enumerator CU_DEVICE_ATTRIBUTE_TIMELINE_SEMAPHORE_INTEROP_SUPPORTED ``

External timeline semaphore interop is supported on the device.

`` enumerator CU_DEVICE_ATTRIBUTE_MEMORY_POOLS_SUPPORTED ``

Device supports using the cuMemAllocAsync and ::cuMemPool family of APIs.

`` enumerator CU_DEVICE_ATTRIBUTE_GPU_DIRECT_RDMA_SUPPORTED ``

Device supports GPUDirect RDMA APIs, like nvidia_p2p_get_pages (see <https://docs.nvidia.com/cuda/gpudirect-rdma> for more information)

`` enumerator CU_DEVICE_ATTRIBUTE_GPU_DIRECT_RDMA_FLUSH_WRITES_OPTIONS ``

The returned attribute shall be interpreted as a bitmask, where the individual bits are described by the CUflushGPUDirectRDMAWritesOptions enum.

`` enumerator CU_DEVICE_ATTRIBUTE_GPU_DIRECT_RDMA_WRITES_ORDERING ``

GPUDirect RDMA writes to the device do not need to be flushed for consumers within the scope indicated by the returned attribute.

See CUGPUDirectRDMAWritesOrdering for the numerical values returned here.

`` enumerator CU_DEVICE_ATTRIBUTE_MEMPOOL_SUPPORTED_HANDLE_TYPES ``

Handle types supported with mempool based IPC.

`` enumerator CU_DEVICE_ATTRIBUTE_CLUSTER_LAUNCH ``

Indicates device supports cluster launch.

`` enumerator CU_DEVICE_ATTRIBUTE_DEFERRED_MAPPING_CUDA_ARRAY_SUPPORTED ``

Device supports deferred mapping CUDA arrays and CUDA mipmapped arrays.

`` enumerator CU_DEVICE_ATTRIBUTE_CAN_USE_64_BIT_STREAM_MEM_OPS ``

64-bit operations are supported in cuStreamBatchMemOp and related MemOp APIs.

`` enumerator CU_DEVICE_ATTRIBUTE_CAN_USE_STREAM_WAIT_VALUE_NOR ``

CU_STREAM_WAIT_VALUE_NOR is supported by MemOp APIs.

`` enumerator CU_DEVICE_ATTRIBUTE_DMA_BUF_SUPPORTED ``

Device supports buffer sharing with dma_buf mechanism.

`` enumerator CU_DEVICE_ATTRIBUTE_IPC_EVENT_SUPPORTED ``

Device supports IPC Events.

`` enumerator CU_DEVICE_ATTRIBUTE_MEM_SYNC_DOMAIN_COUNT ``

Number of memory domains the device supports.

`` enumerator CU_DEVICE_ATTRIBUTE_TENSOR_MAP_ACCESS_SUPPORTED ``

Device supports accessing memory using Tensor Map.

`` enumerator CU_DEVICE_ATTRIBUTE_HANDLE_TYPE_FABRIC_SUPPORTED ``

Device supports exporting memory to a fabric handle with cuMemExportToShareableHandle() or requested with cuMemCreate()

`` enumerator CU_DEVICE_ATTRIBUTE_UNIFIED_FUNCTION_POINTERS ``

Device supports unified function pointers.

`` enumerator CU_DEVICE_ATTRIBUTE_NUMA_CONFIG ``

NUMA configuration of a device: value is of type CUdeviceNumaConfig enum.

`` enumerator CU_DEVICE_ATTRIBUTE_NUMA_ID ``

NUMA node ID of the GPU memory.

`` enumerator CU_DEVICE_ATTRIBUTE_MULTICAST_SUPPORTED ``

Device supports switch multicast and reduction operations.

`` enumerator CU_DEVICE_ATTRIBUTE_MPS_ENABLED ``

Indicates if contexts created on this device will be shared via MPS.

`` enumerator CU_DEVICE_ATTRIBUTE_HOST_NUMA_ID ``

NUMA ID of the host node closest to the device.

Returns -1 when system does not support NUMA.

`` enumerator CU_DEVICE_ATTRIBUTE_D3D12_CIG_SUPPORTED ``

Device supports CIG with D3D12.

`` enumerator CU_DEVICE_ATTRIBUTE_MEM_DECOMPRESS_ALGORITHM_MASK ``

The returned valued shall be interpreted as a bitmask, where the individual bits are described by the CUmemDecompressAlgorithm enum.

`` enumerator CU_DEVICE_ATTRIBUTE_MEM_DECOMPRESS_MAXIMUM_LENGTH ``

The returned valued is the maximum length in bytes of a single decompress operation that is allowed.

`` enumerator CU_DEVICE_ATTRIBUTE_VULKAN_CIG_SUPPORTED ``

Device supports CIG with Vulkan.

`` enumerator CU_DEVICE_ATTRIBUTE_GPU_PCI_DEVICE_ID ``

The combined 16-bit PCI device ID and 16-bit PCI vendor ID.

`` enumerator CU_DEVICE_ATTRIBUTE_GPU_PCI_SUBSYSTEM_ID ``

The combined 16-bit PCI subsystem ID and 16-bit PCI subsystem vendor ID.

`` enumerator CU_DEVICE_ATTRIBUTE_HOST_NUMA_VIRTUAL_MEMORY_MANAGEMENT_SUPPORTED ``

Device supports HOST_NUMA location with the virtual memory management APIs like cuMemCreate, cuMemMap and related APIs.

`` enumerator CU_DEVICE_ATTRIBUTE_HOST_NUMA_MEMORY_POOLS_SUPPORTED ``

Device supports HOST_NUMA location with the cuMemAllocAsync and ::cuMemPool family of APIs.

`` enumerator CU_DEVICE_ATTRIBUTE_HOST_NUMA_MULTINODE_IPC_SUPPORTED ``

Device supports HOST_NUMA location IPC between nodes in a multi-node system.

`` enumerator CU_DEVICE_ATTRIBUTE_HOST_MEMORY_POOLS_SUPPORTED ``

Device suports HOST location with the cuMemAllocAsync and ::cuMemPool family of APIs.

`` enumerator CU_DEVICE_ATTRIBUTE_HOST_VIRTUAL_MEMORY_MANAGEMENT_SUPPORTED ``

Device supports HOST location with the virtual memory management APIs like cuMemCreate, cuMemMap and related APIs.

`` enumerator CU_DEVICE_ATTRIBUTE_HOST_ALLOC_DMA_BUF_SUPPORTED ``

Device supports page-locked host memory buffer sharing with dma_buf mechanism.

`` enumerator CU_DEVICE_ATTRIBUTE_ONLY_PARTIAL_HOST_NATIVE_ATOMIC_SUPPORTED ``

Link between the device and the host supports only some native atomic operations.

`` enumerator CU_DEVICE_ATTRIBUTE_ATOMIC_REDUCTION_SUPPORTED ``

Device supports atomic reduction operations in stream batch memory operations.

`` enumerator CU_DEVICE_ATTRIBUTE_LOCALITY_DOMAIN_COUNT ``

Number of locality domains.

`` enumerator CU_DEVICE_ATTRIBUTE_MAX_OVERSIZED_SHARED_MEMORY_PER_BLOCK ``

Maximum oversized shared memory per block.

`` enumerator CU_DEVICE_ATTRIBUTE_D3D12_CIG_STREAMS_SUPPORTED ``

Device supports CIG streams with D3D12.

`` enumerator CU_DEVICE_ATTRIBUTE_DMA_BUF_MMAP_SUPPORTED ``

Device supports mmap() of dmabuf file descriptors for CUDA device memory allocations.

`` enumerator CU_DEVICE_ATTRIBUTE_LOGICAL_ENDPOINT_UNICAST_SUPPORTED ``

Device supports unicast logical endpoints.

`` enumerator CU_DEVICE_ATTRIBUTE_LOGICAL_ENDPOINT_MULTICAST_SUPPORTED ``

Device supports multicast logical endpoints.

`` enumerator CU_DEVICE_ATTRIBUTE_LOGICAL_ENDPOINT_COUNTED_OPS_SUPPORTED ``

Device supports counted operations via logical endpoints.

`` enumerator CU_DEVICE_ATTRIBUTE_LOGICAL_ENDPOINT_UNICAST_ACCESS_ON_OWNER_DEVICE_SUPPORTED ``

Device supports unicast logical endpoint access on the owner device.

`` enumerator CU_DEVICE_ATTRIBUTE_LOCALITY_DOMAIN_MULTIPROCESSOR_COUNT ``

Number of multiprocessors on each locality domain.

`` enumerator CU_DEVICE_ATTRIBUTE_LOGICAL_ENDPOINT_SUPPORTED_HANDLE_TYPES ``

Handle types supported with logical endpoint IPC.

`` enumerator CU_DEVICE_ATTRIBUTE_GPU_DIRECT_RDMA_WITH_LOCALIZED_MEMORY_SUPPORTED ``

Device supports GPUDirect RDMA with localized memory using the default RDMA mapping link.

`` enumerator CU_DEVICE_ATTRIBUTE_MAX ``

`` enum CUdriverProcAddressQueryResult ``

Flags to indicate search status.

For more details see cuGetProcAddress

_Values:_

`` enumerator CU_GET_PROC_ADDRESS_SUCCESS ``

Symbol was succesfully found.

`` enumerator CU_GET_PROC_ADDRESS_SYMBOL_NOT_FOUND ``

Symbol was not found in search.

`` enumerator CU_GET_PROC_ADDRESS_VERSION_NOT_SUFFICIENT ``

Symbol was found but version supplied was not sufficient.

`` enum CUdriverProcAddress_flags ``

Flags to specify search options.

For more details see cuGetProcAddress

_Values:_

`` enumerator CU_GET_PROC_ADDRESS_DEFAULT ``

Default search mode for driver symbols.

`` enumerator CU_GET_PROC_ADDRESS_LEGACY_STREAM ``

Search for legacy versions of driver symbols.

`` enumerator CU_GET_PROC_ADDRESS_PER_THREAD_DEFAULT_STREAM ``

Search for per-thread versions of driver symbols.

`` enum CUeglColorFormat ``

CUDA EGL Color Format - The different planar and multiplanar formats currently supported for CUDA_EGL interops.

Three channel formats are currently not supported for CU_EGL_FRAME_TYPE_ARRAY

_Values:_

`` enumerator CU_EGL_COLOR_FORMAT_YUV420_PLANAR ``

Y, U, V in three surfaces, each in a separate surface, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YUV420_SEMIPLANAR ``

Y, UV in two surfaces (UV as one surface) with VU byte ordering, width, height ratio same as YUV420Planar.

`` enumerator CU_EGL_COLOR_FORMAT_YUV422_PLANAR ``

Y, U, V each in a separate surface, U/V width = 1/2 Y width, U/V height = Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YUV422_SEMIPLANAR ``

Y, UV in two surfaces with VU byte ordering, width, height ratio same as YUV422Planar.

`` enumerator CU_EGL_COLOR_FORMAT_RGB ``

R/G/B three channels in one surface with BGR byte ordering.

Only pitch linear format supported.

`` enumerator CU_EGL_COLOR_FORMAT_BGR ``

R/G/B three channels in one surface with RGB byte ordering.

Only pitch linear format supported.

`` enumerator CU_EGL_COLOR_FORMAT_ARGB ``

R/G/B/A four channels in one surface with BGRA byte ordering.

`` enumerator CU_EGL_COLOR_FORMAT_RGBA ``

R/G/B/A four channels in one surface with ABGR byte ordering.

`` enumerator CU_EGL_COLOR_FORMAT_L ``

single luminance channel in one surface.

`` enumerator CU_EGL_COLOR_FORMAT_R ``

single color channel in one surface.

`` enumerator CU_EGL_COLOR_FORMAT_YUV444_PLANAR ``

Y, U, V in three surfaces, each in a separate surface, U/V width = Y width, U/V height = Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YUV444_SEMIPLANAR ``

Y, UV in two surfaces (UV as one surface) with VU byte ordering, width, height ratio same as YUV444Planar.

`` enumerator CU_EGL_COLOR_FORMAT_YUYV_422 ``

Y, U, V in one surface, interleaved as UYVY in one channel.

`` enumerator CU_EGL_COLOR_FORMAT_UYVY_422 ``

Y, U, V in one surface, interleaved as YUYV in one channel.

`` enumerator CU_EGL_COLOR_FORMAT_ABGR ``

R/G/B/A four channels in one surface with RGBA byte ordering.

`` enumerator CU_EGL_COLOR_FORMAT_BGRA ``

R/G/B/A four channels in one surface with ARGB byte ordering.

`` enumerator CU_EGL_COLOR_FORMAT_A ``

Alpha color format - one channel in one surface.

`` enumerator CU_EGL_COLOR_FORMAT_RG ``

R/G color format - two channels in one surface with GR byte ordering.

`` enumerator CU_EGL_COLOR_FORMAT_AYUV ``

Y, U, V, A four channels in one surface, interleaved as VUYA.

`` enumerator CU_EGL_COLOR_FORMAT_YVU444_SEMIPLANAR ``

Y, VU in two surfaces (VU as one surface) with UV byte ordering, U/V width = Y width, U/V height = Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YVU422_SEMIPLANAR ``

Y, VU in two surfaces (VU as one surface) with UV byte ordering, U/V width = 1/2 Y width, U/V height = Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YVU420_SEMIPLANAR ``

Y, VU in two surfaces (VU as one surface) with UV byte ordering, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator CU_EGL_COLOR_FORMAT_Y10V10U10_444_SEMIPLANAR ``

Y10, V10U10 in two surfaces (VU as one surface) with UV byte ordering, U/V width = Y width, U/V height = Y height.

`` enumerator CU_EGL_COLOR_FORMAT_Y10V10U10_420_SEMIPLANAR ``

Y10, V10U10 in two surfaces (VU as one surface) with UV byte ordering, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator CU_EGL_COLOR_FORMAT_Y12V12U12_444_SEMIPLANAR ``

Y12, V12U12 in two surfaces (VU as one surface) with UV byte ordering, U/V width = Y width, U/V height = Y height.

`` enumerator CU_EGL_COLOR_FORMAT_Y12V12U12_420_SEMIPLANAR ``

Y12, V12U12 in two surfaces (VU as one surface) with UV byte ordering, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator CU_EGL_COLOR_FORMAT_VYUY_ER ``

Extended Range Y, U, V in one surface, interleaved as YVYU in one channel.

`` enumerator CU_EGL_COLOR_FORMAT_UYVY_ER ``

Extended Range Y, U, V in one surface, interleaved as YUYV in one channel.

`` enumerator CU_EGL_COLOR_FORMAT_YUYV_ER ``

Extended Range Y, U, V in one surface, interleaved as UYVY in one channel.

`` enumerator CU_EGL_COLOR_FORMAT_YVYU_ER ``

Extended Range Y, U, V in one surface, interleaved as VYUY in one channel.

`` enumerator CU_EGL_COLOR_FORMAT_YUV_ER ``

Extended Range Y, U, V three channels in one surface, interleaved as VUY.

Only pitch linear format supported.

`` enumerator CU_EGL_COLOR_FORMAT_YUVA_ER ``

Extended Range Y, U, V, A four channels in one surface, interleaved as AVUY.

`` enumerator CU_EGL_COLOR_FORMAT_AYUV_ER ``

Extended Range Y, U, V, A four channels in one surface, interleaved as VUYA.

`` enumerator CU_EGL_COLOR_FORMAT_YUV444_PLANAR_ER ``

Extended Range Y, U, V in three surfaces, U/V width = Y width, U/V height = Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YUV422_PLANAR_ER ``

Extended Range Y, U, V in three surfaces, U/V width = 1/2 Y width, U/V height = Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YUV420_PLANAR_ER ``

Extended Range Y, U, V in three surfaces, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YUV444_SEMIPLANAR_ER ``

Extended Range Y, UV in two surfaces (UV as one surface) with VU byte ordering, U/V width = Y width, U/V height = Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YUV422_SEMIPLANAR_ER ``

Extended Range Y, UV in two surfaces (UV as one surface) with VU byte ordering, U/V width = 1/2 Y width, U/V height = Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YUV420_SEMIPLANAR_ER ``

Extended Range Y, UV in two surfaces (UV as one surface) with VU byte ordering, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YVU444_PLANAR_ER ``

Extended Range Y, V, U in three surfaces, U/V width = Y width, U/V height = Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YVU422_PLANAR_ER ``

Extended Range Y, V, U in three surfaces, U/V width = 1/2 Y width, U/V height = Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YVU420_PLANAR_ER ``

Extended Range Y, V, U in three surfaces, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YVU444_SEMIPLANAR_ER ``

Extended Range Y, VU in two surfaces (VU as one surface) with UV byte ordering, U/V width = Y width, U/V height = Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YVU422_SEMIPLANAR_ER ``

Extended Range Y, VU in two surfaces (VU as one surface) with UV byte ordering, U/V width = 1/2 Y width, U/V height = Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YVU420_SEMIPLANAR_ER ``

Extended Range Y, VU in two surfaces (VU as one surface) with UV byte ordering, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER_RGGB ``

Bayer format - one channel in one surface with interleaved RGGB ordering.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER_BGGR ``

Bayer format - one channel in one surface with interleaved BGGR ordering.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER_GRBG ``

Bayer format - one channel in one surface with interleaved GRBG ordering.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER_GBRG ``

Bayer format - one channel in one surface with interleaved GBRG ordering.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER10_RGGB ``

Bayer10 format - one channel in one surface with interleaved RGGB ordering.

Out of 16 bits, 10 bits used 6 bits No-op.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER10_BGGR ``

Bayer10 format - one channel in one surface with interleaved BGGR ordering.

Out of 16 bits, 10 bits used 6 bits No-op.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER10_GRBG ``

Bayer10 format - one channel in one surface with interleaved GRBG ordering.

Out of 16 bits, 10 bits used 6 bits No-op.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER10_GBRG ``

Bayer10 format - one channel in one surface with interleaved GBRG ordering.

Out of 16 bits, 10 bits used 6 bits No-op.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER12_RGGB ``

Bayer12 format - one channel in one surface with interleaved RGGB ordering.

Out of 16 bits, 12 bits used 4 bits No-op.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER12_BGGR ``

Bayer12 format - one channel in one surface with interleaved BGGR ordering.

Out of 16 bits, 12 bits used 4 bits No-op.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER12_GRBG ``

Bayer12 format - one channel in one surface with interleaved GRBG ordering.

Out of 16 bits, 12 bits used 4 bits No-op.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER12_GBRG ``

Bayer12 format - one channel in one surface with interleaved GBRG ordering.

Out of 16 bits, 12 bits used 4 bits No-op.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER14_RGGB ``

Bayer14 format - one channel in one surface with interleaved RGGB ordering.

Out of 16 bits, 14 bits used 2 bits No-op.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER14_BGGR ``

Bayer14 format - one channel in one surface with interleaved BGGR ordering.

Out of 16 bits, 14 bits used 2 bits No-op.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER14_GRBG ``

Bayer14 format - one channel in one surface with interleaved GRBG ordering.

Out of 16 bits, 14 bits used 2 bits No-op.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER14_GBRG ``

Bayer14 format - one channel in one surface with interleaved GBRG ordering.

Out of 16 bits, 14 bits used 2 bits No-op.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER20_RGGB ``

Bayer20 format - one channel in one surface with interleaved RGGB ordering.

Out of 32 bits, 20 bits used 12 bits No-op.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER20_BGGR ``

Bayer20 format - one channel in one surface with interleaved BGGR ordering.

Out of 32 bits, 20 bits used 12 bits No-op.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER20_GRBG ``

Bayer20 format - one channel in one surface with interleaved GRBG ordering.

Out of 32 bits, 20 bits used 12 bits No-op.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER20_GBRG ``

Bayer20 format - one channel in one surface with interleaved GBRG ordering.

Out of 32 bits, 20 bits used 12 bits No-op.

`` enumerator CU_EGL_COLOR_FORMAT_YVU444_PLANAR ``

Y, V, U in three surfaces, each in a separate surface, U/V width = Y width, U/V height = Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YVU422_PLANAR ``

Y, V, U in three surfaces, each in a separate surface, U/V width = 1/2 Y width, U/V height = Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YVU420_PLANAR ``

Y, V, U in three surfaces, each in a separate surface, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER_ISP_RGGB ``

Nvidia proprietary Bayer ISP format - one channel in one surface with interleaved RGGB ordering and mapped to opaque integer datatype.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER_ISP_BGGR ``

Nvidia proprietary Bayer ISP format - one channel in one surface with interleaved BGGR ordering and mapped to opaque integer datatype.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER_ISP_GRBG ``

Nvidia proprietary Bayer ISP format - one channel in one surface with interleaved GRBG ordering and mapped to opaque integer datatype.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER_ISP_GBRG ``

Nvidia proprietary Bayer ISP format - one channel in one surface with interleaved GBRG ordering and mapped to opaque integer datatype.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER_BCCR ``

Bayer format - one channel in one surface with interleaved BCCR ordering.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER_RCCB ``

Bayer format - one channel in one surface with interleaved RCCB ordering.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER_CRBC ``

Bayer format - one channel in one surface with interleaved CRBC ordering.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER_CBRC ``

Bayer format - one channel in one surface with interleaved CBRC ordering.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER10_CCCC ``

Bayer10 format - one channel in one surface with interleaved CCCC ordering.

Out of 16 bits, 10 bits used 6 bits No-op.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER12_BCCR ``

Bayer12 format - one channel in one surface with interleaved BCCR ordering.

Out of 16 bits, 12 bits used 4 bits No-op.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER12_RCCB ``

Bayer12 format - one channel in one surface with interleaved RCCB ordering.

Out of 16 bits, 12 bits used 4 bits No-op.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER12_CRBC ``

Bayer12 format - one channel in one surface with interleaved CRBC ordering.

Out of 16 bits, 12 bits used 4 bits No-op.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER12_CBRC ``

Bayer12 format - one channel in one surface with interleaved CBRC ordering.

Out of 16 bits, 12 bits used 4 bits No-op.

`` enumerator CU_EGL_COLOR_FORMAT_BAYER12_CCCC ``

Bayer12 format - one channel in one surface with interleaved CCCC ordering.

Out of 16 bits, 12 bits used 4 bits No-op.

`` enumerator CU_EGL_COLOR_FORMAT_Y ``

Color format for single Y plane.

`` enumerator CU_EGL_COLOR_FORMAT_YUV420_SEMIPLANAR_2020 ``

Y, UV in two surfaces (UV as one surface) U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YVU420_SEMIPLANAR_2020 ``

Y, VU in two surfaces (VU as one surface) U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YUV420_PLANAR_2020 ``

Y, U, V each in a separate surface, U/V width = 1/2 Y width, U/V height= 1/2 Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YVU420_PLANAR_2020 ``

Y, V, U each in a separate surface, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YUV420_SEMIPLANAR_709 ``

Y, UV in two surfaces (UV as one surface) U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YVU420_SEMIPLANAR_709 ``

Y, VU in two surfaces (VU as one surface) U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YUV420_PLANAR_709 ``

Y, U, V each in a separate surface, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator CU_EGL_COLOR_FORMAT_YVU420_PLANAR_709 ``

Y, V, U each in a separate surface, U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator CU_EGL_COLOR_FORMAT_Y10V10U10_420_SEMIPLANAR_709 ``

Y10, V10U10 in two surfaces (VU as one surface), U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator CU_EGL_COLOR_FORMAT_Y10V10U10_420_SEMIPLANAR_2020 ``

Y10, V10U10 in two surfaces (VU as one surface), U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator CU_EGL_COLOR_FORMAT_Y10V10U10_422_SEMIPLANAR_2020 ``

Y10, V10U10 in two surfaces(VU as one surface) U/V width = 1/2 Y width, U/V height = Y height.

`` enumerator CU_EGL_COLOR_FORMAT_Y10V10U10_422_SEMIPLANAR ``

Y10, V10U10 in two surfaces(VU as one surface) U/V width = 1/2 Y width, U/V height = Y height.

`` enumerator CU_EGL_COLOR_FORMAT_Y10V10U10_422_SEMIPLANAR_709 ``

Y10, V10U10 in two surfaces(VU as one surface) U/V width = 1/2 Y width, U/V height = Y height.

`` enumerator CU_EGL_COLOR_FORMAT_Y_ER ``

Extended Range Color format for single Y plane.

`` enumerator CU_EGL_COLOR_FORMAT_Y_709_ER ``

Extended Range Color format for single Y plane.

`` enumerator CU_EGL_COLOR_FORMAT_Y10_ER ``

Extended Range Color format for single Y10 plane.

`` enumerator CU_EGL_COLOR_FORMAT_Y10_709_ER ``

Extended Range Color format for single Y10 plane.

`` enumerator CU_EGL_COLOR_FORMAT_Y12_ER ``

Extended Range Color format for single Y12 plane.

`` enumerator CU_EGL_COLOR_FORMAT_Y12_709_ER ``

Extended Range Color format for single Y12 plane.

`` enumerator CU_EGL_COLOR_FORMAT_YUVA ``

Y, U, V, A four channels in one surface, interleaved as AVUY.

`` enumerator CU_EGL_COLOR_FORMAT_YUV ``

Y, U, V three channels in one surface, interleaved as VUY.

Only pitch linear format supported.

`` enumerator CU_EGL_COLOR_FORMAT_YVYU ``

Y, U, V in one surface, interleaved as YVYU in one channel.

`` enumerator CU_EGL_COLOR_FORMAT_VYUY ``

Y, U, V in one surface, interleaved as VYUY in one channel.

`` enumerator CU_EGL_COLOR_FORMAT_Y10V10U10_420_SEMIPLANAR_ER ``

Extended Range Y10, V10U10 in two surfaces(VU as one surface) U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator CU_EGL_COLOR_FORMAT_Y10V10U10_420_SEMIPLANAR_709_ER ``

Extended Range Y10, V10U10 in two surfaces(VU as one surface) U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator CU_EGL_COLOR_FORMAT_Y10V10U10_444_SEMIPLANAR_ER ``

Extended Range Y10, V10U10 in two surfaces (VU as one surface) U/V width = Y width, U/V height = Y height.

`` enumerator CU_EGL_COLOR_FORMAT_Y10V10U10_444_SEMIPLANAR_709_ER ``

Extended Range Y10, V10U10 in two surfaces (VU as one surface) U/V width = Y width, U/V height = Y height.

`` enumerator CU_EGL_COLOR_FORMAT_Y12V12U12_420_SEMIPLANAR_ER ``

Extended Range Y12, V12U12 in two surfaces (VU as one surface) U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator CU_EGL_COLOR_FORMAT_Y12V12U12_420_SEMIPLANAR_709_ER ``

Extended Range Y12, V12U12 in two surfaces (VU as one surface) U/V width = 1/2 Y width, U/V height = 1/2 Y height.

`` enumerator CU_EGL_COLOR_FORMAT_Y12V12U12_444_SEMIPLANAR_ER ``

Extended Range Y12, V12U12 in two surfaces (VU as one surface) U/V width = Y width, U/V height = Y height.

`` enumerator CU_EGL_COLOR_FORMAT_Y12V12U12_444_SEMIPLANAR_709_ER ``

Extended Range Y12, V12U12 in two surfaces (VU as one surface) U/V width = Y width, U/V height = Y height.

`` enumerator CU_EGL_COLOR_FORMAT_UYVY_709 ``

Y, U, V in one surface, interleaved as UYVY in one channel.

`` enumerator CU_EGL_COLOR_FORMAT_UYVY_709_ER ``

Extended Range Y, U, V in one surface, interleaved as UYVY in one channel.

`` enumerator CU_EGL_COLOR_FORMAT_UYVY_2020 ``

Y, U, V in one surface, interleaved as UYVY in one channel.

`` enumerator CU_EGL_COLOR_FORMAT_MAX ``

`` enum CUeglFrameType ``

CUDA EglFrame type - array or pointer.

_Values:_

`` enumerator CU_EGL_FRAME_TYPE_ARRAY ``

Frame type CUDA array.

`` enumerator CU_EGL_FRAME_TYPE_PITCH ``

Frame type pointer.

`` enum CUeglResourceLocationFlags ``

Resource location flags- sysmem or vidmem.

For CUDA context on iGPU, since video and system memory are equivalent - these flags will not have an effect on the execution.

For CUDA context on dGPU, applications can use the flag CUeglResourceLocationFlags to give a hint about the desired location.

CU_EGL_RESOURCE_LOCATION_SYSMEM \- the frame data is made resident on the system memory to be accessed by CUDA.

CU_EGL_RESOURCE_LOCATION_VIDMEM \- the frame data is made resident on the dedicated video memory to be accessed by CUDA.

There may be an additional latency due to new allocation and data migration, if the frame is produced on a different memory.

_Values:_

`` enumerator CU_EGL_RESOURCE_LOCATION_SYSMEM ``

Resource location sysmem.

`` enumerator CU_EGL_RESOURCE_LOCATION_VIDMEM ``

Resource location vidmem.

`` enum CUevent_flags ``

Event creation flags.

_Values:_

`` enumerator CU_EVENT_DEFAULT ``

Default event flag.

`` enumerator CU_EVENT_BLOCKING_SYNC ``

Event uses blocking synchronization.

`` enumerator CU_EVENT_DISABLE_TIMING ``

Event will not record timing data.

`` enumerator CU_EVENT_INTERPROCESS ``

Event is suitable for interprocess use.

CU_EVENT_DISABLE_TIMING must be set

`` enum CUevent_record_flags ``

Event record flags.

_Values:_

`` enumerator CU_EVENT_RECORD_DEFAULT ``

Default event record flag.

`` enumerator CU_EVENT_RECORD_EXTERNAL ``

When using stream capture, create an event record node instead of the default behavior.

This flag is invalid when used outside of capture.

`` enum CUevent_sched_flags ``

Event sched flags.

_Values:_

`` enumerator CU_EVENT_SCHED_AUTO ``

Automatic scheduling.

`` enumerator CU_EVENT_SCHED_SPIN ``

Set spin as default scheduling.

`` enumerator CU_EVENT_SCHED_YIELD ``

Set yield as default scheduling.

`` enumerator CU_EVENT_SCHED_BLOCKING_SYNC ``

Set blocking synchronization as default scheduling.

`` enum CUevent_wait_flags ``

Event wait flags.

_Values:_

`` enumerator CU_EVENT_WAIT_DEFAULT ``

Default event wait flag.

`` enumerator CU_EVENT_WAIT_EXTERNAL ``

When using stream capture, create an event wait node instead of the default behavior.

This flag is invalid when used outside of capture.

`` enum CUexecAffinityType ``

Execution Affinity Types.

_Values:_

`` enumerator CU_EXEC_AFFINITY_TYPE_SM_COUNT ``

Create a context with limited SMs.

`` enumerator CU_EXEC_AFFINITY_TYPE_MAX ``

`` enum CUexternalMemoryHandleType ``

External memory handle types.

_Values:_

`` enumerator CU_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_FD ``

Handle is an opaque file descriptor.

`` enumerator CU_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32 ``

Handle is an opaque shared NT handle.

`` enumerator CU_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_KMT ``

Handle is an opaque, globally shared handle.

`` enumerator CU_EXTERNAL_MEMORY_HANDLE_TYPE_D3D12_HEAP ``

Handle is a D3D12 heap object.

`` enumerator CU_EXTERNAL_MEMORY_HANDLE_TYPE_D3D12_RESOURCE ``

Handle is a D3D12 committed resource.

`` enumerator CU_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_RESOURCE ``

Handle is a shared NT handle to a D3D11 resource.

`` enumerator CU_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_RESOURCE_KMT ``

Handle is a globally shared handle to a D3D11 resource.

`` enumerator CU_EXTERNAL_MEMORY_HANDLE_TYPE_NVSCIBUF ``

Handle is an NvSciBuf object.

`` enumerator CU_EXTERNAL_MEMORY_HANDLE_TYPE_DMABUF_FD ``

Handle is a dma_buf file descriptor.

`` enum CUexternalSemaphoreHandleType ``

External semaphore handle types.

_Values:_

`` enumerator CU_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_FD ``

Handle is an opaque file descriptor.

`` enumerator CU_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_WIN32 ``

Handle is an opaque shared NT handle.

`` enumerator CU_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_WIN32_KMT ``

Handle is an opaque, globally shared handle.

`` enumerator CU_EXTERNAL_SEMAPHORE_HANDLE_TYPE_D3D12_FENCE ``

Handle is a shared NT handle referencing a D3D12 fence object.

`` enumerator CU_EXTERNAL_SEMAPHORE_HANDLE_TYPE_D3D11_FENCE ``

Handle is a shared NT handle referencing a D3D11 fence object.

`` enumerator CU_EXTERNAL_SEMAPHORE_HANDLE_TYPE_NVSCISYNC ``

Opaque handle to NvSciSync Object.

`` enumerator CU_EXTERNAL_SEMAPHORE_HANDLE_TYPE_D3D11_KEYED_MUTEX ``

Handle is a shared NT handle referencing a D3D11 keyed mutex object.

`` enumerator CU_EXTERNAL_SEMAPHORE_HANDLE_TYPE_D3D11_KEYED_MUTEX_KMT ``

Handle is a globally shared handle referencing a D3D11 keyed mutex object.

`` enumerator CU_EXTERNAL_SEMAPHORE_HANDLE_TYPE_TIMELINE_SEMAPHORE_FD ``

Handle is an opaque file descriptor referencing a timeline semaphore.

`` enumerator CU_EXTERNAL_SEMAPHORE_HANDLE_TYPE_TIMELINE_SEMAPHORE_WIN32 ``

Handle is an opaque shared NT handle referencing a timeline semaphore.

`` enum CUfilter_mode ``

Texture reference filtering modes.

_Values:_

`` enumerator CU_TR_FILTER_MODE_POINT ``

Point filter mode.

`` enumerator CU_TR_FILTER_MODE_LINEAR ``

Linear filter mode.

`` enum CUflushGPUDirectRDMAWritesOptions ``

Bitmasks for CU_DEVICE_ATTRIBUTE_GPU_DIRECT_RDMA_FLUSH_WRITES_OPTIONS.

_Values:_

`` enumerator CU_FLUSH_GPU_DIRECT_RDMA_WRITES_OPTION_HOST ``

cuFlushGPUDirectRDMAWrites() and its CUDA Runtime API counterpart are supported on the device.

`` enumerator CU_FLUSH_GPU_DIRECT_RDMA_WRITES_OPTION_MEMOPS ``

The CU_STREAM_WAIT_VALUE_FLUSH flag and the CU_STREAM_MEM_OP_FLUSH_REMOTE_WRITES MemOp are supported on the device.

`` enum CUflushGPUDirectRDMAWritesScope ``

The scopes for cuFlushGPUDirectRDMAWrites.

_Values:_

`` enumerator CU_FLUSH_GPU_DIRECT_RDMA_WRITES_TO_OWNER ``

Blocks until remote writes are visible to the CUDA device context owning the data.

`` enumerator CU_FLUSH_GPU_DIRECT_RDMA_WRITES_TO_ALL_DEVICES ``

Blocks until remote writes are visible to all CUDA device contexts.

`` enum CUflushGPUDirectRDMAWritesTarget ``

The targets for cuFlushGPUDirectRDMAWrites.

_Values:_

`` enumerator CU_FLUSH_GPU_DIRECT_RDMA_WRITES_TARGET_CURRENT_CTX ``

Sets the target for cuFlushGPUDirectRDMAWrites() to the currently active CUDA device context.

`` enum CUfunc_cache ``

Function cache configurations.

_Values:_

`` enumerator CU_FUNC_CACHE_PREFER_NONE ``

no preference for shared memory or L1 (default)

`` enumerator CU_FUNC_CACHE_PREFER_SHARED ``

prefer larger shared memory and smaller L1 cache

`` enumerator CU_FUNC_CACHE_PREFER_L1 ``

prefer larger L1 cache and smaller shared memory

`` enumerator CU_FUNC_CACHE_PREFER_EQUAL ``

prefer equal sized L1 cache and shared memory

`` enum CUfunction_attribute ``

Function properties.

_Values:_

`` enumerator CU_FUNC_ATTRIBUTE_MAX_THREADS_PER_BLOCK ``

The maximum number of threads per block, beyond which a launch of the function would fail.

This number depends on both the function and the device on which the function is currently loaded.

`` enumerator CU_FUNC_ATTRIBUTE_SHARED_SIZE_BYTES ``

The size in bytes of statically-allocated shared memory required by this function.

This does not include dynamically-allocated shared memory requested by the user at runtime.

`` enumerator CU_FUNC_ATTRIBUTE_CONST_SIZE_BYTES ``

The size in bytes of user-allocated constant memory required by this function.

`` enumerator CU_FUNC_ATTRIBUTE_LOCAL_SIZE_BYTES ``

The size in bytes of local memory used by each thread of this function.

`` enumerator CU_FUNC_ATTRIBUTE_NUM_REGS ``

The number of registers used by each thread of this function.

`` enumerator CU_FUNC_ATTRIBUTE_PTX_VERSION ``

The PTX virtual architecture version for which the function was compiled.

This value is the major PTX version * 10 + the minor PTX version, so a PTX version 1.3 function would return the value 13. Note that this may return the undefined value of 0 for cubins compiled prior to CUDA 3.0.

`` enumerator CU_FUNC_ATTRIBUTE_BINARY_VERSION ``

The binary architecture version for which the function was compiled.

This value is the major binary version * 10 + the minor binary version, so a binary version 1.3 function would return the value 13. Note that this will return a value of 10 for legacy cubins that do not have a properly-encoded binary architecture version.

`` enumerator CU_FUNC_ATTRIBUTE_CACHE_MODE_CA ``

The attribute to indicate whether the function has been compiled with user specified option “-Xptxas –dlcm=ca” set .

`` enumerator CU_FUNC_ATTRIBUTE_MAX_DYNAMIC_SHARED_SIZE_BYTES ``

The maximum size in bytes of dynamically-allocated shared memory that can be used by this function.

If the user-specified dynamic shared memory size is larger than this value, the launch will fail.

The default value of this attribute is CU_DEVICE_ATTRIBUTE_MAX_SHARED_MEMORY_PER_BLOCK \- CU_FUNC_ATTRIBUTE_SHARED_SIZE_BYTES, except when CU_FUNC_ATTRIBUTE_SHARED_SIZE_BYTES is greater than CU_DEVICE_ATTRIBUTE_MAX_SHARED_MEMORY_PER_BLOCK, then the default value of this attribute is 0. The value can be increased to CU_DEVICE_ATTRIBUTE_MAX_SHARED_MEMORY_PER_BLOCK_OPTIN \- CU_FUNC_ATTRIBUTE_SHARED_SIZE_BYTES.

This attribute is ignored if CU_FUNC_ATTRIBUTE_SHARED_MEMORY_MODE or CU_LAUNCH_ATTRIBUTE_SHARED_MEMORY_MODE is set.

This attribute cannot be used to access oversized shared memory. Oversized shared memory can only be accessed by setting CU_FUNC_ATTRIBUTE_SHARED_MEMORY_MODE or CU_LAUNCH_ATTRIBUTE_SHARED_MEMORY_MODE.

See cuFuncSetAttribute, cuKernelSetAttribute

`` enumerator CU_FUNC_ATTRIBUTE_PREFERRED_SHARED_MEMORY_CARVEOUT ``

On devices where the L1 cache and shared memory use the same hardware resources, this sets the shared memory carveout preference, in percent of the total shared memory.

Refer to CU_DEVICE_ATTRIBUTE_MAX_SHARED_MEMORY_PER_MULTIPROCESSOR. This is only a hint, and the driver can choose a different ratio if required to execute the function.

See cuFuncSetAttribute, cuKernelSetAttribute

`` enumerator CU_FUNC_ATTRIBUTE_CLUSTER_SIZE_MUST_BE_SET ``

If this attribute is set, the kernel must launch with a valid cluster size specified.

See cuFuncSetAttribute, cuKernelSetAttribute

`` enumerator CU_FUNC_ATTRIBUTE_REQUIRED_CLUSTER_WIDTH ``

The required cluster width in blocks.

The values must either all be 0 or all be positive. The validity of the cluster dimensions is otherwise checked at launch time.

If the value is set during compile time, it cannot be set at runtime. Setting it at runtime will return CUDA_ERROR_NOT_PERMITTED.

See cuFuncSetAttribute, cuKernelSetAttribute

`` enumerator CU_FUNC_ATTRIBUTE_REQUIRED_CLUSTER_HEIGHT ``

The required cluster height in blocks.

The values must either all be 0 or all be positive. The validity of the cluster dimensions is otherwise checked at launch time.

If the value is set during compile time, it cannot be set at runtime. Setting it at runtime should return CUDA_ERROR_NOT_PERMITTED.

See cuFuncSetAttribute, cuKernelSetAttribute

`` enumerator CU_FUNC_ATTRIBUTE_REQUIRED_CLUSTER_DEPTH ``

The required cluster depth in blocks.

The values must either all be 0 or all be positive. The validity of the cluster dimensions is otherwise checked at launch time.

If the value is set during compile time, it cannot be set at runtime. Setting it at runtime should return CUDA_ERROR_NOT_PERMITTED.

See cuFuncSetAttribute, cuKernelSetAttribute

`` enumerator CU_FUNC_ATTRIBUTE_NON_PORTABLE_CLUSTER_SIZE_ALLOWED ``

Whether the function can be launched with non-portable cluster size.

1 is allowed, 0 is disallowed. A non-portable cluster size may only function on the specific SKUs the program is tested on. The launch might fail if the program is run on a different hardware platform.

CUDA API provides cudaOccupancyMaxActiveClusters to assist with checking whether the desired size can be launched on the current device.

Portable Cluster Size

A portable cluster size is guaranteed to be functional on all compute capabilities higher than the target compute capability. The portable cluster size for sm_90 is 8 blocks per cluster. This value may increase for future compute capabilities.

The specific hardware unit may support higher cluster sizes that’s not guaranteed to be portable.

See cuFuncSetAttribute, cuKernelSetAttribute

`` enumerator CU_FUNC_ATTRIBUTE_CLUSTER_SCHEDULING_POLICY_PREFERENCE ``

The block scheduling policy of a function.

The value type is CUclusterSchedulingPolicy / cudaClusterSchedulingPolicy.

See cuFuncSetAttribute, cuKernelSetAttribute

`` enumerator CU_FUNC_ATTRIBUTE_DEVICE_NODE_UPDATE_SUPPORTED ``

Whether the function can be updated on device.

1 means device node update is supported, 0 is unsupported.

See cuFuncGetAttribute.

`` enumerator CU_FUNC_ATTRIBUTE_SHARED_MEMORY_MODE ``

The shared memory mode of a function.

The value type is CUsharedMemoryMode / cudaSharedMemoryMode.

See cuFuncSetAttribute, cuKernelSetAttribute

`` enumerator CU_FUNC_ATTRIBUTE_MAX ``

`` enum CUgraphChildGraphNodeOwnership ``

Child graph node ownership.

_Values:_

`` enumerator CU_GRAPH_CHILD_GRAPH_OWNERSHIP_CLONE ``

Default behavior for a child graph node.

Child graph is cloned into the parent and memory allocation/free nodes can’t be present in the child graph.

`` enumerator CU_GRAPH_CHILD_GRAPH_OWNERSHIP_MOVE ``

The child graph is moved to the parent.

The handle to the child graph is owned by the parent and will be destroyed when the parent is destroyed.

The following restrictions apply to child graphs after they have been moved: Cannot be independently instantiated or destroyed; Cannot be added as a child graph of a separate parent graph; Cannot be used as an argument to cuGraphExecUpdate; Cannot have additional memory allocation or free nodes added.

`` enumerator CU_GRAPH_CHILD_GRAPH_OWNERSHIP_INVALID ``

Invalid ownership flag.

Set when params are queried to prevent accidentally reusing the driver-owned graph object

`` enum CUgraphConditionalNodeType ``

Conditional node types.

_Values:_

`` enumerator CU_GRAPH_COND_TYPE_IF ``

Conditional ‘if/else’ Node.

Body[0] executed if condition is non-zero. If `size` == 2, an optional ELSE graph is created and this is executed if the condition is zero.

`` enumerator CU_GRAPH_COND_TYPE_WHILE ``

Conditional ‘while’ Node.

Body executed repeatedly while condition value is non-zero.

`` enumerator CU_GRAPH_COND_TYPE_SWITCH ``

Conditional ‘switch’ Node.

Body[n] is executed once, where ‘n’ is the value of the condition. If the condition does not match a body index, no body is launched.

`` enum CUgraphDebugDot_flags ``

The additional write options for cuGraphDebugDotPrint.

_Values:_

`` enumerator CU_GRAPH_DEBUG_DOT_FLAGS_VERBOSE ``

Output all debug data as if every debug flag is enabled.

`` enumerator CU_GRAPH_DEBUG_DOT_FLAGS_RUNTIME_TYPES ``

Use CUDA Runtime structures for output.

`` enumerator CU_GRAPH_DEBUG_DOT_FLAGS_KERNEL_NODE_PARAMS ``

Adds CUDA_KERNEL_NODE_PARAMS values to output.

`` enumerator CU_GRAPH_DEBUG_DOT_FLAGS_MEMCPY_NODE_PARAMS ``

Adds CUDA_MEMCPY3D values to output.

`` enumerator CU_GRAPH_DEBUG_DOT_FLAGS_MEMSET_NODE_PARAMS ``

Adds CUDA_MEMSET_NODE_PARAMS values to output.

`` enumerator CU_GRAPH_DEBUG_DOT_FLAGS_HOST_NODE_PARAMS ``

Adds CUDA_HOST_NODE_PARAMS values to output.

`` enumerator CU_GRAPH_DEBUG_DOT_FLAGS_EVENT_NODE_PARAMS ``

Adds CUevent handle from record and wait nodes to output.

`` enumerator CU_GRAPH_DEBUG_DOT_FLAGS_EXT_SEMAS_SIGNAL_NODE_PARAMS ``

Adds CUDA_EXT_SEM_SIGNAL_NODE_PARAMS values to output.

`` enumerator CU_GRAPH_DEBUG_DOT_FLAGS_EXT_SEMAS_WAIT_NODE_PARAMS ``

Adds CUDA_EXT_SEM_WAIT_NODE_PARAMS values to output.

`` enumerator CU_GRAPH_DEBUG_DOT_FLAGS_KERNEL_NODE_ATTRIBUTES ``

Adds CUkernelNodeAttrValue values to output.

`` enumerator CU_GRAPH_DEBUG_DOT_FLAGS_HANDLES ``

Adds node handles and every kernel function handle to output.

`` enumerator CU_GRAPH_DEBUG_DOT_FLAGS_MEM_ALLOC_NODE_PARAMS ``

Adds memory alloc node parameters to output.

`` enumerator CU_GRAPH_DEBUG_DOT_FLAGS_MEM_FREE_NODE_PARAMS ``

Adds memory free node parameters to output.

`` enumerator CU_GRAPH_DEBUG_DOT_FLAGS_BATCH_MEM_OP_NODE_PARAMS ``

Adds batch mem op node parameters to output.

`` enumerator CU_GRAPH_DEBUG_DOT_FLAGS_EXTRA_TOPO_INFO ``

Adds edge numbering information.

`` enumerator CU_GRAPH_DEBUG_DOT_FLAGS_CONDITIONAL_NODE_PARAMS ``

Adds conditional node parameters to output.

`` enum CUgraphDependencyType ``

Type annotations that can be applied to graph edges as part of CUgraphEdgeData.

_Values:_

`` enumerator CU_GRAPH_DEPENDENCY_TYPE_DEFAULT ``

This is an ordinary dependency.

`` enumerator CU_GRAPH_DEPENDENCY_TYPE_PROGRAMMATIC ``

This dependency type allows the downstream node to use cudaGridDependencySynchronize().

It may only be used between kernel nodes, and must be used with either the CU_GRAPH_KERNEL_NODE_PORT_PROGRAMMATIC or CU_GRAPH_KERNEL_NODE_PORT_LAUNCH_ORDER outgoing port.

`` enum CUgraphExecUpdateResult ``

CUDA Graph Update error types.

_Values:_

`` enumerator CU_GRAPH_EXEC_UPDATE_SUCCESS ``

The update succeeded.

`` enumerator CU_GRAPH_EXEC_UPDATE_ERROR ``

The update failed for an unexpected reason which is described in the return value of the function.

`` enumerator CU_GRAPH_EXEC_UPDATE_ERROR_TOPOLOGY_CHANGED ``

The update failed because the topology changed.

`` enumerator CU_GRAPH_EXEC_UPDATE_ERROR_NODE_TYPE_CHANGED ``

The update failed because a node type changed.

`` enumerator CU_GRAPH_EXEC_UPDATE_ERROR_FUNCTION_CHANGED ``

The update failed because the function of a kernel node changed (CUDA driver < 11.2)

`` enumerator CU_GRAPH_EXEC_UPDATE_ERROR_PARAMETERS_CHANGED ``

The update failed because the parameters changed in a way that is not supported.

`` enumerator CU_GRAPH_EXEC_UPDATE_ERROR_NOT_SUPPORTED ``

The update failed because something about the node is not supported.

`` enumerator CU_GRAPH_EXEC_UPDATE_ERROR_UNSUPPORTED_FUNCTION_CHANGE ``

The update failed because the function of a kernel node changed in an unsupported way.

`` enumerator CU_GRAPH_EXEC_UPDATE_ERROR_ATTRIBUTES_CHANGED ``

The update failed because the node attributes changed in a way that is not supported.

`` enum CUgraphInstantiateResult ``

Graph instantiation results.

_Values:_

`` enumerator CUDA_GRAPH_INSTANTIATE_SUCCESS ``

Instantiation succeeded.

`` enumerator CUDA_GRAPH_INSTANTIATE_ERROR ``

Instantiation failed for an unexpected reason which is described in the return value of the function.

`` enumerator CUDA_GRAPH_INSTANTIATE_INVALID_STRUCTURE ``

Instantiation failed due to invalid structure, such as cycles.

`` enumerator CUDA_GRAPH_INSTANTIATE_NODE_OPERATION_NOT_SUPPORTED ``

Instantiation for device launch failed because the graph contained an unsupported operation.

`` enumerator CUDA_GRAPH_INSTANTIATE_MULTIPLE_CTXS_NOT_SUPPORTED ``

Instantiation for device launch failed due to the nodes belonging to different contexts.

`` enumerator CUDA_GRAPH_INSTANTIATE_CONDITIONAL_HANDLE_UNUSED ``

One or more conditional handles are not associated with conditional nodes.

`` enum CUgraphInstantiate_flags ``

Flags for instantiating a graph.

_Values:_

`` enumerator CUDA_GRAPH_INSTANTIATE_FLAG_AUTO_FREE_ON_LAUNCH ``

Automatically free memory allocated in a graph before relaunching.

`` enumerator CUDA_GRAPH_INSTANTIATE_FLAG_UPLOAD ``

Automatically upload the graph after instantiation.

Only supported by cuGraphInstantiateWithParams. The upload will be performed using the stream provided in `instantiateParams`.

`` enumerator CUDA_GRAPH_INSTANTIATE_FLAG_DEVICE_LAUNCH ``

Instantiate the graph to be launchable from the device.

This flag can only be used on platforms which support unified addressing. This flag cannot be used in conjunction with CUDA_GRAPH_INSTANTIATE_FLAG_AUTO_FREE_ON_LAUNCH.

`` enumerator CUDA_GRAPH_INSTANTIATE_FLAG_USE_NODE_PRIORITY ``

Run the graph using the per-node priority attributes rather than the priority of the stream it is launched into.

`` enum CUgraphMem_attribute ``

_Values:_

`` enumerator CU_GRAPH_MEM_ATTR_USED_MEM_CURRENT ``

(value type = cuuint64_t) Amount of memory, in bytes, currently associated with graphs

`` enumerator CU_GRAPH_MEM_ATTR_USED_MEM_HIGH ``

(value type = cuuint64_t) High watermark of memory, in bytes, associated with graphs since the last time it was reset.

High watermark can only be reset to zero.

`` enumerator CU_GRAPH_MEM_ATTR_RESERVED_MEM_CURRENT ``

(value type = cuuint64_t) Amount of memory, in bytes, currently allocated for use by the CUDA graphs asynchronous allocator.

`` enumerator CU_GRAPH_MEM_ATTR_RESERVED_MEM_HIGH ``

(value type = cuuint64_t) High watermark of memory, in bytes, currently allocated for use by the CUDA graphs asynchronous allocator.

`` enum CUgraphNodeType ``

Graph node types.

_Values:_

`` enumerator CU_GRAPH_NODE_TYPE_KERNEL ``

GPU kernel node.

`` enumerator CU_GRAPH_NODE_TYPE_MEMCPY ``

Memcpy node.

`` enumerator CU_GRAPH_NODE_TYPE_MEMSET ``

Memset node.

`` enumerator CU_GRAPH_NODE_TYPE_HOST ``

Host (executable) node.

`` enumerator CU_GRAPH_NODE_TYPE_GRAPH ``

Node which executes an embedded graph.

`` enumerator CU_GRAPH_NODE_TYPE_EMPTY ``

Empty (no-op) node.

`` enumerator CU_GRAPH_NODE_TYPE_WAIT_EVENT ``

External event wait node.

`` enumerator CU_GRAPH_NODE_TYPE_EVENT_RECORD ``

External event record node.

`` enumerator CU_GRAPH_NODE_TYPE_EXT_SEMAS_SIGNAL ``

External semaphore signal node.

`` enumerator CU_GRAPH_NODE_TYPE_EXT_SEMAS_WAIT ``

External semaphore wait node.

`` enumerator CU_GRAPH_NODE_TYPE_MEM_ALLOC ``

Memory Allocation Node.

`` enumerator CU_GRAPH_NODE_TYPE_MEM_FREE ``

Memory Free Node.

`` enumerator CU_GRAPH_NODE_TYPE_BATCH_MEM_OP ``

Batch MemOp Node See cuStreamBatchMemOp and CUstreamBatchMemOpType for what these nodes can do.

`` enumerator CU_GRAPH_NODE_TYPE_CONDITIONAL ``

Conditional Node.

```cpp
May be used to implement a conditional execution path or loop
                                        inside of a graph. The graph(s) contained within the body of the conditional node
                                        can be selectively executed or iterated upon based on the value of a conditional
                                        variable.

                                        Handles must be created in advance of creating the node
                                        using ::cuGraphConditionalHandleCreate.

                                        The following restrictions apply to graphs which contain conditional nodes:
                                         The graph cannot be used in a child node.
                                         Only one instantiation of the graph may exist at any point in time.
                                         The graph cannot be cloned.

                                        To set the control value, supply a default value when creating the handle and/or
                                        call ::cudaGraphSetConditional from device code.
```

`` enumerator CU_GRAPH_NODE_TYPE_RESERVED_16 ``

Reserved.

`` enum CUgraphicsMapResourceFlags ``

Flags for mapping and unmapping interop resources.

_Values:_

`` enumerator CU_GRAPHICS_MAP_RESOURCE_FLAGS_NONE ``

`` enumerator CU_GRAPHICS_MAP_RESOURCE_FLAGS_READ_ONLY ``

`` enumerator CU_GRAPHICS_MAP_RESOURCE_FLAGS_WRITE_DISCARD ``

`` enum CUgraphicsRegisterFlags ``

Flags to register a graphics resource.

_Values:_

`` enumerator CU_GRAPHICS_REGISTER_FLAGS_NONE ``

`` enumerator CU_GRAPHICS_REGISTER_FLAGS_READ_ONLY ``

`` enumerator CU_GRAPHICS_REGISTER_FLAGS_WRITE_DISCARD ``

`` enumerator CU_GRAPHICS_REGISTER_FLAGS_SURFACE_LDST ``

`` enumerator CU_GRAPHICS_REGISTER_FLAGS_TEXTURE_GATHER ``

`` enum CUhostTaskSyncMode ``

_Values:_

`` enumerator CU_HOST_TASK_BLOCKING ``

The execution thread will block until new host tasks are ready to run.

`` enumerator CU_HOST_TASK_SPINWAIT ``

The execution thread will spin wait until new host tasks are ready to run.

`` enum CUipcMem_flags ``

CUDA Ipc Mem Flags.

_Values:_

`` enumerator CU_IPC_MEM_LAZY_ENABLE_PEER_ACCESS ``

Automatically enable peer access between remote devices as needed.

`` enum CUjitInputType ``

Device code formats.

_Values:_

`` enumerator CU_JIT_INPUT_CUBIN ``

Compiled device-class-specific device code

Applicable options: none.

`` enumerator CU_JIT_INPUT_PTX ``

PTX source code

Applicable options: PTX compiler options.

`` enumerator CU_JIT_INPUT_FATBINARY ``

Bundle of multiple cubins and/or PTX of some device code

Applicable options: PTX compiler options,

CU_JIT_FALLBACK_STRATEGY.

`` enumerator CU_JIT_INPUT_OBJECT ``

Host object with embedded device code

Applicable options: PTX compiler options,

CU_JIT_FALLBACK_STRATEGY.

`` enumerator CU_JIT_INPUT_LIBRARY ``

Archive of host objects with embedded device code

Applicable options: PTX compiler options,

CU_JIT_FALLBACK_STRATEGY.

`` enumerator CU_JIT_INPUT_NVVM ``

`` Deprecated: ``

High-level intermediate code for link-time optimization

Applicable options: NVVM compiler options, PTX compiler options

Only valid with LTO-IR compiled with toolkits prior to CUDA 12.0

`` enumerator CU_JIT_NUM_INPUT_TYPES ``

`` enum CUjit_cacheMode ``

Caching modes for dlcm.

_Values:_

`` enumerator CU_JIT_CACHE_OPTION_NONE ``

Compile with no -dlcm flag specified.

`` enumerator CU_JIT_CACHE_OPTION_CG ``

Compile with L1 cache disabled.

`` enumerator CU_JIT_CACHE_OPTION_CA ``

Compile with L1 cache enabled.

`` enum CUjit_fallback ``

Cubin matching fallback strategies.

_Values:_

`` enumerator CU_PREFER_PTX ``

Prefer to compile ptx if exact binary match not found.

`` enumerator CU_PREFER_BINARY ``

Prefer to fall back to compatible binary code if exact match not found.

`` enum CUjit_option ``

Online compiler and linker options.

_Values:_

`` enumerator CU_JIT_MAX_REGISTERS ``

Max number of registers that a thread may use.

Option type: unsigned int

Applies to: compiler only

`` enumerator CU_JIT_THREADS_PER_BLOCK ``

IN: Specifies minimum number of threads per block to target compilation for

OUT: Returns the number of threads the compiler actually targeted.

This restricts the resource utilization of the compiler (e.g. max registers) such that a block with the given number of threads should be able to launch based on register limitations. Note, this option does not currently take into account any other resource limitations, such as shared memory utilization.

Cannot be combined with

CU_JIT_TARGET

.

Option type: unsigned int

Applies to: compiler only

`` enumerator CU_JIT_WALL_TIME ``

Overwrites the option value with the total wall clock time, in milliseconds, spent in the compiler and linker

Option type: float

Applies to: compiler and linker.

`` enumerator CU_JIT_INFO_LOG_BUFFER ``

Pointer to a buffer in which to print any log messages that are informational in nature (the buffer size is specified via option CU_JIT_INFO_LOG_BUFFER_SIZE_BYTES

)

Option type: char *

Applies to: compiler and linker.

`` enumerator CU_JIT_INFO_LOG_BUFFER_SIZE_BYTES ``

IN: Log buffer size in bytes.

Log messages will be capped at this size (including null terminator)

OUT: Amount of log buffer filled with messages

Option type: unsigned int

Applies to: compiler and linker

`` enumerator CU_JIT_ERROR_LOG_BUFFER ``

Pointer to a buffer in which to print any log messages that reflect errors (the buffer size is specified via option CU_JIT_ERROR_LOG_BUFFER_SIZE_BYTES

)

Option type: char *

Applies to: compiler and linker.

`` enumerator CU_JIT_ERROR_LOG_BUFFER_SIZE_BYTES ``

IN: Log buffer size in bytes.

Log messages will be capped at this size (including null terminator)

OUT: Amount of log buffer filled with messages

Option type: unsigned int

Applies to: compiler and linker

`` enumerator CU_JIT_OPTIMIZATION_LEVEL ``

Level of optimizations to apply to generated code (0 - 4), with 4 being the default and highest level of optimizations.

Option type: unsigned int

Applies to: compiler only

`` enumerator CU_JIT_TARGET_FROM_CUCONTEXT ``

No option value required.

Determines the target based on the current attached context (default)

Option type: No option value needed

Applies to: compiler and linker

`` enumerator CU_JIT_TARGET ``

Target is chosen based on supplied CUjit_target.

Cannot be combined with CU_JIT_THREADS_PER_BLOCK

.

Option type: unsigned int for enumerated type

CUjit_target Applies to: compiler and linker

`` enumerator CU_JIT_FALLBACK_STRATEGY ``

Specifies choice of fallback strategy if matching cubin is not found.

Choice is based on supplied CUjit_fallback

. This option cannot be used with cuLink* APIs as the linker requires exact matches.

Option type: unsigned int for enumerated type

CUjit_fallback Applies to: compiler only

`` enumerator CU_JIT_GENERATE_DEBUG_INFO ``

Specifies whether to create debug information in output (-g) (0: false, default)

Option type: int

Applies to: compiler and linker.

`` enumerator CU_JIT_LOG_VERBOSE ``

Generate verbose log messages (0: false, default)

Option type: int

Applies to: compiler and linker.

`` enumerator CU_JIT_GENERATE_LINE_INFO ``

Generate line number information (-lineinfo) (0: false, default)

Option type: int

Applies to: compiler only.

`` enumerator CU_JIT_CACHE_MODE ``

Specifies whether to enable caching explicitly (-dlcm)

Choice is based on supplied ::CUjit_cacheMode_enum.

Option type: unsigned int for enumerated type ::CUjit_cacheMode_enum

Applies to: compiler only

`` enumerator CU_JIT_NEW_SM3X_OPT ``

`` Deprecated: ``

This jit option is deprecated and should not be used.

`` enumerator CU_JIT_FAST_COMPILE ``

This jit option is used for internal purpose only.

`` enumerator CU_JIT_GLOBAL_SYMBOL_NAMES ``

Array of device symbol names that will be relocated to the corresponding host addresses stored in CU_JIT_GLOBAL_SYMBOL_ADDRESSES.

Must contain CU_JIT_GLOBAL_SYMBOL_COUNT

entries.

When loading a device module, driver will relocate all encountered unresolved symbols to the host addresses.

It is only allowed to register symbols that correspond to unresolved global variables.

It is illegal to register the same device symbol at multiple addresses.

Option type: const char **

Applies to: dynamic linker only

`` enumerator CU_JIT_GLOBAL_SYMBOL_ADDRESSES ``

Array of host addresses that will be used to relocate corresponding device symbols stored in CU_JIT_GLOBAL_SYMBOL_NAMES.

Must contain CU_JIT_GLOBAL_SYMBOL_COUNT

entries.

Option type: void **

Applies to: dynamic linker only

`` enumerator CU_JIT_GLOBAL_SYMBOL_COUNT ``

Number of entries in CU_JIT_GLOBAL_SYMBOL_NAMES and CU_JIT_GLOBAL_SYMBOL_ADDRESSES arrays.

Option type: unsigned int

Applies to: dynamic linker only

`` enumerator CU_JIT_LTO ``

`` Deprecated: ``

Enable link-time optimization (-dlto) for device code (Disabled by default).

This option is not supported on 32-bit platforms.

Option type: int

Applies to: compiler and linker

Only valid with LTO-IR compiled with toolkits prior to CUDA 12.0

`` enumerator CU_JIT_FTZ ``

`` Deprecated: ``

Control single-precision denormals (-ftz) support (0: false, default). 1 : flushes denormal values to zero 0 : preserves denormal values Option type: int

Applies to: link-time optimization specified with CU_JIT_LTO

Only valid with LTO-IR compiled with toolkits prior to CUDA 12.0

`` enumerator CU_JIT_PREC_DIV ``

`` Deprecated: ``

Control single-precision floating-point division and reciprocals (-prec-div) support (1: true, default). 1 : Enables the IEEE round-to-nearest mode 0 : Enables the fast approximation mode Option type: int

Applies to: link-time optimization specified with CU_JIT_LTO

Only valid with LTO-IR compiled with toolkits prior to CUDA 12.0

`` enumerator CU_JIT_PREC_SQRT ``

`` Deprecated: ``

Control single-precision floating-point square root (-prec-sqrt) support (1: true, default). 1 : Enables the IEEE round-to-nearest mode 0 : Enables the fast approximation mode Option type: int

Applies to: link-time optimization specified with CU_JIT_LTO

Only valid with LTO-IR compiled with toolkits prior to CUDA 12.0

`` enumerator CU_JIT_FMA ``

`` Deprecated: ``

Enable/Disable the contraction of floating-point multiplies and adds/subtracts into floating-point multiply-add (-fma) operations (1: Enable, default; 0: Disable). Option type: int

Applies to: link-time optimization specified with CU_JIT_LTO

Only valid with LTO-IR compiled with toolkits prior to CUDA 12.0

`` enumerator CU_JIT_REFERENCED_KERNEL_NAMES ``

`` Deprecated: ``

Array of kernel names that should be preserved at link time while others can be removed.

Must contain

CU_JIT_REFERENCED_KERNEL_COUNT

entries.

Note that kernel names can be mangled by the compiler in which case the mangled name needs to be specified.

Wildcard “*” can be used to represent zero or more characters instead of specifying the full or mangled name.

It is important to note that the wildcard “*” is also added implicitly. For example, specifying “foo” will match “foobaz”, “barfoo”, “barfoobaz” and thus preserve all kernels with those names. This can be avoided by providing a more specific name like “barfoobaz”.

Option type: const char **

Applies to: dynamic linker only

Only valid with LTO-IR compiled with toolkits prior to CUDA 12.0

`` enumerator CU_JIT_REFERENCED_KERNEL_COUNT ``

`` Deprecated: ``

Number of entries in CU_JIT_REFERENCED_KERNEL_NAMES

array.

Option type: unsigned int

Applies to: dynamic linker only

Only valid with LTO-IR compiled with toolkits prior to CUDA 12.0

`` enumerator CU_JIT_REFERENCED_VARIABLE_NAMES ``

`` Deprecated: ``

Array of variable names (**device** and/or **constant**

) that should be preserved at link time while others can be removed.

Must contain

CU_JIT_REFERENCED_VARIABLE_COUNT

entries.

Note that variable names can be mangled by the compiler in which case the mangled name needs to be specified.

Wildcard “*” can be used to represent zero or more characters instead of specifying the full or mangled name.

It is important to note that the wildcard “*” is also added implicitly. For example, specifying “foo” will match “foobaz”, “barfoo”, “barfoobaz” and thus preserve all variables with those names. This can be avoided by providing a more specific name like “barfoobaz”.

Option type: const char **

Applies to: link-time optimization specified with CU_JIT_LTO

Only valid with LTO-IR compiled with toolkits prior to CUDA 12.0

`` enumerator CU_JIT_REFERENCED_VARIABLE_COUNT ``

`` Deprecated: ``

Number of entries in CU_JIT_REFERENCED_VARIABLE_NAMES

array.

Option type: unsigned int

Applies to: link-time optimization specified with CU_JIT_LTO

Only valid with LTO-IR compiled with toolkits prior to CUDA 12.0

`` enumerator CU_JIT_OPTIMIZE_UNUSED_DEVICE_VARIABLES ``

`` Deprecated: ``

This option serves as a hint to enable the JIT compiler/linker to remove constant (**constant**) and device (**device**

) variables unreferenced in device code (Disabled by default).

Note that host references to constant and device variables using APIs like cuModuleGetGlobal() with this option specified may result in undefined behavior unless the variables are explicitly specified using

CU_JIT_REFERENCED_VARIABLE_NAMES

.

Option type: int

Applies to: link-time optimization specified with CU_JIT_LTO

Only valid with LTO-IR compiled with toolkits prior to CUDA 12.0

`` enumerator CU_JIT_POSITION_INDEPENDENT_CODE ``

Generate position independent code (0: false)

Option type: int

Applies to: compiler only.

`` enumerator CU_JIT_MIN_CTA_PER_SM ``

This option hints to the JIT compiler the minimum number of CTAs from the kernel’s grid to be mapped to a SM.

This option is ignored when used together with CU_JIT_MAX_REGISTERS or CU_JIT_THREADS_PER_BLOCK. Optimizations based on this option need CU_JIT_MAX_THREADS_PER_BLOCK to be specified as well. For kernels already using PTX directive .minnctapersm, this option will be ignored by default. Use CU_JIT_OVERRIDE_DIRECTIVE_VALUES

to let this option take precedence over the PTX directive. Option type: unsigned int

Applies to: compiler only

`` enumerator CU_JIT_MAX_THREADS_PER_BLOCK ``

Maximum number threads in a thread block, computed as the product of the maximum extent specifed for each dimension of the block.

This limit is guaranteed not to be exeeded in any invocation of the kernel. Exceeding the the maximum number of threads results in runtime error or kernel launch failure. For kernels already using PTX directive .maxntid, this option will be ignored by default. Use CU_JIT_OVERRIDE_DIRECTIVE_VALUES

to let this option take precedence over the PTX directive. Option type: int

Applies to: compiler only

`` enumerator CU_JIT_OVERRIDE_DIRECTIVE_VALUES ``

This option lets the values specified using CU_JIT_MAX_REGISTERS, CU_JIT_THREADS_PER_BLOCK, CU_JIT_MAX_THREADS_PER_BLOCK and CU_JIT_MIN_CTA_PER_SM take precedence over any PTX directives.

(0: Disable, default; 1: Enable) Option type: int

Applies to: compiler only

`` enumerator CU_JIT_SPLIT_COMPILE ``

This option specifies the maximum number of concurrent threads to use when running compiler optimizations.

If the specified value is 1, the option will be ignored. If the specified value is 0, the number of threads will match the number of CPUs on the underlying machine. Otherwise, if the option is N, then up to N threads will be used. Option type: unsigned int

Applies to: compiler only

`` enumerator CU_JIT_BINARY_LOADER_THREAD_COUNT ``

This option specifies the maximum number of concurrent threads to use when compiling device code.

If the specified value is 1, the option will be ignored. If the specified value is 0, the number of threads will match the number of CPUs on the underlying machine. Otherwise, if the option is N, then up to N threads will be used. This option is ignored if the env var CUDA_BINARY_LOADER_THREAD_COUNT is set. Option type: unsigned int

Applies to: compiler and linker

`` enumerator CU_JIT_NUM_OPTIONS ``

`` enum CUjit_target ``

Online compilation targets.

_Values:_

`` enumerator CU_TARGET_COMPUTE_30 ``

Compute device class 3.0.

`` enumerator CU_TARGET_COMPUTE_32 ``

Compute device class 3.2.

`` enumerator CU_TARGET_COMPUTE_35 ``

Compute device class 3.5.

`` enumerator CU_TARGET_COMPUTE_37 ``

Compute device class 3.7.

`` enumerator CU_TARGET_COMPUTE_50 ``

Compute device class 5.0.

`` enumerator CU_TARGET_COMPUTE_52 ``

Compute device class 5.2.

`` enumerator CU_TARGET_COMPUTE_53 ``

Compute device class 5.3.

`` enumerator CU_TARGET_COMPUTE_60 ``

Compute device class 6.0.

`` enumerator CU_TARGET_COMPUTE_61 ``

Compute device class 6.1.

`` enumerator CU_TARGET_COMPUTE_62 ``

Compute device class 6.2.

`` enumerator CU_TARGET_COMPUTE_70 ``

Compute device class 7.0.

`` enumerator CU_TARGET_COMPUTE_72 ``

Compute device class 7.2.

`` enumerator CU_TARGET_COMPUTE_75 ``

Compute device class 7.5.

`` enumerator CU_TARGET_COMPUTE_80 ``

Compute device class 8.0.

`` enumerator CU_TARGET_COMPUTE_86 ``

Compute device class 8.6.

`` enumerator CU_TARGET_COMPUTE_87 ``

Compute device class 8.7.

`` enumerator CU_TARGET_COMPUTE_89 ``

Compute device class 8.9.

`` enumerator CU_TARGET_COMPUTE_90 ``

Compute device class 9.0.

`` enumerator CU_TARGET_COMPUTE_100 ``

Compute device class 10.0.

`` enumerator CU_TARGET_COMPUTE_110 ``

Compute device class 11.0.

`` enumerator CU_TARGET_COMPUTE_103 ``

Compute device class 10.3.

`` enumerator CU_TARGET_COMPUTE_107 ``

Compute device class 10.7.

`` enumerator CU_TARGET_COMPUTE_120 ``

Compute device class 12.0.

`` enumerator CU_TARGET_COMPUTE_121 ``

Compute device class 12.1.

Compute device class 9.0. with accelerated features.

`` enumerator CU_TARGET_COMPUTE_90A ``

Compute device class 10.0.

with accelerated features.

`` enumerator CU_TARGET_COMPUTE_100A ``

Compute device class 11.0 with accelerated features.

`` enumerator CU_TARGET_COMPUTE_110A ``

Compute device class 10.3.

with accelerated features.

`` enumerator CU_TARGET_COMPUTE_103A ``

`` enumerator CU_TARGET_COMPUTE_107A ``

Compute device class 12.0.

with accelerated features.

`` enumerator CU_TARGET_COMPUTE_120A ``

Compute device class 12.1.

with accelerated features.

`` enumerator CU_TARGET_COMPUTE_121A ``

Compute device class 10.x with family features.

`` enumerator CU_TARGET_COMPUTE_100F ``

Compute device class 11.0 with family features.

`` enumerator CU_TARGET_COMPUTE_110F ``

Compute device class 10.3.

with family features.

`` enumerator CU_TARGET_COMPUTE_103F ``

`` enumerator CU_TARGET_COMPUTE_107F ``

Compute device class 12.0.

with family features.

`` enumerator CU_TARGET_COMPUTE_120F ``

Compute device class 12.1.

with family features.

`` enumerator CU_TARGET_COMPUTE_121F ``

`` enum CUlaunchAttributeID ``

Launch attributes enum; used as id field of CUlaunchAttribute.

_Values:_

`` enumerator CU_LAUNCH_ATTRIBUTE_IGNORE ``

Ignored entry, for convenient composition.

`` enumerator CU_LAUNCH_ATTRIBUTE_ACCESS_POLICY_WINDOW ``

Valid for streams, graph nodes, launches.

See CUlaunchAttributeValue::accessPolicyWindow.

`` enumerator CU_LAUNCH_ATTRIBUTE_COOPERATIVE ``

Valid for graph nodes, launches.

See CUlaunchAttributeValue::cooperative.

`` enumerator CU_LAUNCH_ATTRIBUTE_SYNCHRONIZATION_POLICY ``

Valid for streams.

See CUlaunchAttributeValue::syncPolicy.

`` enumerator CU_LAUNCH_ATTRIBUTE_CLUSTER_DIMENSION ``

Valid for graph nodes, launches.

See CUlaunchAttributeValue::clusterDim.

`` enumerator CU_LAUNCH_ATTRIBUTE_CLUSTER_SCHEDULING_POLICY_PREFERENCE ``

Valid for graph nodes, launches.

See CUlaunchAttributeValue::clusterSchedulingPolicyPreference.

`` enumerator CU_LAUNCH_ATTRIBUTE_PROGRAMMATIC_STREAM_SERIALIZATION ``

Valid for launches.

Setting CUlaunchAttributeValue::programmaticStreamSerializationAllowed to non-0 signals that the kernel will use programmatic means to resolve its stream dependency, so that the CUDA runtime should opportunistically allow the grid’s execution to overlap with the previous kernel in the stream, if that kernel requests the overlap. The dependent launches can choose to wait on the dependency using the programmatic sync (cudaGridDependencySynchronize() or equivalent PTX instructions).

`` enumerator CU_LAUNCH_ATTRIBUTE_PROGRAMMATIC_EVENT ``

Valid for launches.

Set CUlaunchAttributeValue::programmaticEvent to record the event. Event recorded through this launch attribute is guaranteed to only trigger after all block in the associated kernel trigger the event. A block can trigger the event through PTX launchdep.release or CUDA builtin function cudaTriggerProgrammaticLaunchCompletion(). A trigger can also be inserted at the beginning of each block’s execution if triggerAtBlockStart is set to non-0. The dependent launches can choose to wait on the dependency using the programmatic sync (cudaGridDependencySynchronize() or equivalent PTX instructions). Note that dependents (including the CPU thread calling cuEventSynchronize()) are not guaranteed to observe the release precisely when it is released. For example, cuEventSynchronize()

may only observe the event trigger long after the associated kernel has completed. This recording type is primarily meant for establishing programmatic dependency between device tasks. Note also this type of dependency allows, but does not guarantee, concurrent execution of tasks.

The event supplied must not be an interprocess or interop event. The event must disable timing (i.e. must be created with the

CU_EVENT_DISABLE_TIMING flag set).

`` enumerator CU_LAUNCH_ATTRIBUTE_PRIORITY ``

Valid for streams, graph nodes, launches.

See CUlaunchAttributeValue::priority.

`` enumerator CU_LAUNCH_ATTRIBUTE_MEM_SYNC_DOMAIN_MAP ``

Valid for streams, graph nodes, launches.

See CUlaunchAttributeValue::memSyncDomainMap.

`` enumerator CU_LAUNCH_ATTRIBUTE_MEM_SYNC_DOMAIN ``

Valid for streams, graph nodes, launches.

See CUlaunchAttributeValue::memSyncDomain.

`` enumerator CU_LAUNCH_ATTRIBUTE_PREFERRED_CLUSTER_DIMENSION ``

Valid for graph nodes, launches.

Set CUlaunchAttributeValue::preferredClusterDim to allow the kernel launch to specify a preferred substitute cluster dimension. Blocks may be grouped according to either the dimensions specified with this attribute (grouped into a “preferred substitute cluster”), or the one specified with CU_LAUNCH_ATTRIBUTE_CLUSTER_DIMENSION

attribute (grouped into a “regular cluster”). The cluster dimensions of a “preferred substitute cluster” shall be an integer multiple greater than zero of the regular cluster dimensions. The device will attempt - on a best-effort basis - to group thread blocks into preferred clusters over grouping them into regular clusters. When it deems necessary (primarily when the device temporarily runs out of physical resources to launch the larger preferred clusters), the device may switch to launch the regular clusters instead to attempt to utilize as much of the physical device resources as possible.

Each type of cluster will have its enumeration / coordinate setup as if the grid consists solely of its type of cluster. For example, if the preferred substitute cluster dimensions double the regular cluster dimensions, there might be simultaneously a regular cluster indexed at (1,0,0), and a preferred cluster indexed at (1,0,0). In this example, the preferred substitute cluster (1,0,0) replaces regular clusters (2,0,0) and (3,0,0) and groups their blocks.

This attribute will only take effect when a regular cluster dimension has been specified. The preferred substitute cluster dimension must be an integer multiple greater than zero of the regular cluster dimension and must divide the grid. It must also be no more than `maxBlocksPerCluster`, if it is set in the kernel’s `__launch_bounds__`. Otherwise it must be less than the maximum value the driver can support. Otherwise, setting this attribute to a value physically unable to fit on any particular device is permitted.

`` enumerator CU_LAUNCH_ATTRIBUTE_LAUNCH_COMPLETION_EVENT ``

Valid for launches.

Set CUlaunchAttributeValue::launchCompletionEvent

to record the event.

Nominally, the event is triggered once all blocks of the kernel have begun execution. Currently this is a best effort. If a kernel B has a launch completion dependency on a kernel A, B may wait until A is complete. Alternatively, blocks of B may begin before all blocks of A have begun, for example if B can claim execution resources unavailable to A (e.g. they run on different GPUs) or if B is a higher priority than A. Exercise caution if such an ordering inversion could lead to deadlock.

A launch completion event is nominally similar to a programmatic event with `triggerAtBlockStart`

set except that it is not visible to cudaGridDependencySynchronize() and can be used with compute capability less than 9.0.

The event supplied must not be an interprocess or interop event. The event must disable timing (i.e. must be created with the

CU_EVENT_DISABLE_TIMING flag set).

`` enumerator CU_LAUNCH_ATTRIBUTE_DEVICE_UPDATABLE_KERNEL_NODE ``

Valid for graph nodes, launches.

This attribute is graphs-only, and passing it to a launch in a non-capturing stream will result in an error.

::CUlaunchAttributeValue::deviceUpdatableKernelNode::deviceUpdatable can only be set to 0 or 1. Setting the field to 1 indicates that the corresponding kernel node should be device-updatable. On success, a handle will be returned via ::CUlaunchAttributeValue::deviceUpdatableKernelNode::devNode which can be passed to the various device-side update functions to update the node’s kernel parameters from within another kernel. For more information on the types of device updates that can be made, as well as the relevant limitations thereof, see ::cudaGraphKernelNodeUpdatesApply.

Nodes which are device-updatable have additional restrictions compared to regular kernel nodes. Firstly, device-updatable nodes cannot be removed from their graph via cuGraphDestroyNode. Additionally, once opted-in to this functionality, a node cannot opt out, and any attempt to set the deviceUpdatable attribute to 0 will result in an error. Device-updatable kernel nodes also cannot have their attributes copied to/from another kernel node via cuGraphKernelNodeCopyAttributes

. Graphs containing one or more device-updatable nodes also do not allow multiple instantiation, and neither the graph nor its instantiated version can be passed to cuGraphExecUpdate.

If a graph contains device-updatable nodes and updates those nodes from the device from within the graph, the graph must be uploaded with

cuGraphUpload before it is launched. For such a graph, if host-side executable graph updates are made to the device-updatable nodes, the graph must be uploaded before it is launched again.

`` enumerator CU_LAUNCH_ATTRIBUTE_PREFERRED_SHARED_MEMORY_CARVEOUT ``

Valid for launches.

On devices where the L1 cache and shared memory use the same hardware resources, setting CUlaunchAttributeValue::sharedMemCarveout to a percentage between 0-100 signals the CUDA driver to set the shared memory carveout preference, in percent of the total shared memory for that kernel launch. This attribute takes precedence over CU_FUNC_ATTRIBUTE_PREFERRED_SHARED_MEMORY_CARVEOUT. This is only a hint, and the CUDA driver can choose a different configuration if required for the launch.

`` enumerator CU_LAUNCH_ATTRIBUTE_NVLINK_UTIL_CENTRIC_SCHEDULING ``

Valid for streams, graph nodes, launches.

This attribute is a hint to the CUDA runtime that the launch should attempt to make the kernel maximize its NVLINK utilization.

When possible to honor this hint, CUDA will assume each block in the grid launch will carry out an even amount of NVLINK traffic, and make a best-effort attempt to adjust the kernel launch based on that assumption.

This attribute is a hint only. CUDA makes no functional or performance guarantee. Its applicability can be affected by many different factors, including driver version (i.e. CUDA doesn’t guarantee the performance characteristics will be maintained between driver versions or a driver update could alter or regress previously observed perf characteristics.) It also doesn’t guarantee a successful result, i.e. applying the attribute may not improve the performance of either the targeted kernel or the encapsulating application.

Valid values for CUlaunchAttributeValue::nvlinkUtilCentricScheduling are 0 (disabled) and 1 (enabled).

`` enumerator CU_LAUNCH_ATTRIBUTE_PORTABLE_CLUSTER_SIZE_MODE ``

Valid for graph nodes, launches.

This controls whether the kernel launch is allowed to use a non-portable cluster size. Valid values for CUlaunchAttributeValue::portableClusterSizeMode are described in CUlaunchAttributePortableClusterMode. Any other value will return CUDA_ERROR_INVALID_VALUE

`` enumerator CU_LAUNCH_ATTRIBUTE_SHARED_MEMORY_MODE ``

Valid for graph nodes, launches.

This controls a kernel’s use of non-portable or oversized shared memory configurations.

`` enum CUlaunchAttributePortableClusterMode ``

Enum for defining applicability of portable cluster size, used with cuLaunchKernelEx.

_Values:_

`` enumerator CU_LAUNCH_PORTABLE_CLUSTER_MODE_DEFAULT ``

The default to use for allowing non-portable cluster size on launch - uses current function attribute for CU_FUNC_ATTRIBUTE_NON_PORTABLE_CLUSTER_SIZE_ALLOWED.

`` enumerator CU_LAUNCH_PORTABLE_CLUSTER_MODE_REQUIRE_PORTABLE ``

Specifies that the cluster size requested must be a portable size.

`` enumerator CU_LAUNCH_PORTABLE_CLUSTER_MODE_ALLOW_NON_PORTABLE ``

Specifies that the cluster size requested may be a non-portable size.

`` enum CUlaunchMemSyncDomain ``

Memory Synchronization Domain.

A kernel can be launched in a specified memory synchronization domain that affects all memory operations issued by that kernel. A memory barrier issued in one domain will only order memory operations in that domain, thus eliminating latency increase from memory barriers ordering unrelated traffic.

By default, kernels are launched in domain 0. Kernel launched with CU_LAUNCH_MEM_SYNC_DOMAIN_REMOTE will have a different domain ID. User may also alter the domain ID with CUlaunchMemSyncDomainMap for a specific stream / graph node / kernel launch. See CU_LAUNCH_ATTRIBUTE_MEM_SYNC_DOMAIN, cuStreamSetAttribute, cuLaunchKernelEx, cuGraphKernelNodeSetAttribute.

Memory operations done in kernels launched in different domains are considered system-scope distanced. In other words, a GPU scoped memory synchronization is not sufficient for memory order to be observed by kernels in another memory synchronization domain even if they are on the same GPU.

_Values:_

`` enumerator CU_LAUNCH_MEM_SYNC_DOMAIN_DEFAULT ``

Launch kernels in the default domain.

`` enumerator CU_LAUNCH_MEM_SYNC_DOMAIN_REMOTE ``

Launch kernels in the remote domain.

`` enum CUlibraryOption ``

Library options to be specified with cuLibraryLoadData() or cuLibraryLoadFromFile()

_Values:_

`` enumerator CU_LIBRARY_HOST_UNIVERSAL_FUNCTION_AND_DATA_TABLE ``

`` enumerator CU_LIBRARY_BINARY_IS_PRESERVED ``

Specifes that the argument `code` passed to cuLibraryLoadData() will be preserved.

Specifying this option will let the driver know that `code` can be accessed at any point until cuLibraryUnload(). The default behavior is for the driver to allocate and maintain its own copy of `code`. Note that this is only a memory usage optimization hint and the driver can choose to ignore it if required. Specifying this option with cuLibraryLoadFromFile() is invalid and will return CUDA_ERROR_INVALID_VALUE.

`` enumerator CU_LIBRARY_NUM_OPTIONS ``

`` enum CUlimit ``

Limits.

_Values:_

`` enumerator CU_LIMIT_STACK_SIZE ``

GPU thread stack size.

`` enumerator CU_LIMIT_PRINTF_FIFO_SIZE ``

GPU printf FIFO size.

`` enumerator CU_LIMIT_MALLOC_HEAP_SIZE ``

GPU malloc heap size.

`` enumerator CU_LIMIT_DEV_RUNTIME_SYNC_DEPTH ``

GPU device runtime launch synchronize depth.

`` enumerator CU_LIMIT_DEV_RUNTIME_PENDING_LAUNCH_COUNT ``

GPU device runtime pending launch count.

`` enumerator CU_LIMIT_MAX_L2_FETCH_GRANULARITY ``

A value between 0 and 128 that indicates the maximum fetch granularity of L2 (in Bytes).

This is a hint

`` enumerator CU_LIMIT_PERSISTING_L2_CACHE_SIZE ``

A size in bytes for L2 persisting lines cache size.

`` enumerator CU_LIMIT_SHMEM_SIZE ``

A maximum size in bytes of shared memory available to CUDA kernels on a CIG context.

Can only be queried, cannot be set

`` enumerator CU_LIMIT_CIG_ENABLED ``

A non-zero value indicates this CUDA context is a CIG-enabled context.

Can only be queried, cannot be set

`` enumerator CU_LIMIT_CIG_SHMEM_FALLBACK_ENABLED ``

When set to zero, CUDA will fail to launch a kernel on a CIG context, instead of using the fallback path, if the kernel uses more shared memory than available.

`` enumerator CU_LIMIT_PER_BLOCK_MEMORY_SIZE ``

Per-block memory size.

`` enumerator CU_LIMIT_MAX ``

`` enum CUmemAccess_flags ``

Specifies the memory protection flags for mapping.

_Values:_

`` enumerator CU_MEM_ACCESS_FLAGS_PROT_NONE ``

Default, make the address range not accessible.

`` enumerator CU_MEM_ACCESS_FLAGS_PROT_READ ``

Make the address range read accessible.

`` enumerator CU_MEM_ACCESS_FLAGS_PROT_READWRITE ``

Make the address range read-write accessible.

`` enumerator CU_MEM_ACCESS_FLAGS_PROT_MAX ``

`` enum CUmemAllocationCompType ``

Specifies compression attribute for an allocation.

_Values:_

`` enumerator CU_MEM_ALLOCATION_COMP_NONE ``

Allocating non-compressible memory.

`` enumerator CU_MEM_ALLOCATION_COMP_GENERIC ``

Allocating compressible memory.

`` enum CUmemAllocationGranularity_flags ``

Flag for requesting different optimal and required granularities for an allocation.

_Values:_

`` enumerator CU_MEM_ALLOC_GRANULARITY_MINIMUM ``

Minimum required granularity for allocation.

`` enumerator CU_MEM_ALLOC_GRANULARITY_RECOMMENDED ``

Recommended granularity for allocation for best performance.

`` enum CUmemAllocationHandleType ``

Flags for specifying particular handle types.

_Values:_

`` enumerator CU_MEM_HANDLE_TYPE_NONE ``

Does not allow any export mechanism.

>

`` enumerator CU_MEM_HANDLE_TYPE_POSIX_FILE_DESCRIPTOR ``

Allows a file descriptor to be used for exporting.

Permitted only on POSIX systems. (int)

`` enumerator CU_MEM_HANDLE_TYPE_WIN32 ``

Allows a Win32 NT handle to be used for exporting.

(HANDLE)

`` enumerator CU_MEM_HANDLE_TYPE_WIN32_KMT ``

Allows a Win32 KMT handle to be used for exporting.

(D3DKMT_HANDLE)

`` enumerator CU_MEM_HANDLE_TYPE_FABRIC ``

Allows a fabric handle to be used for exporting.

(CUmemFabricHandle)

`` enumerator CU_MEM_HANDLE_TYPE_MAX ``

`` enum CUmemAllocationType ``

Defines the allocation types available.

_Values:_

`` enumerator CU_MEM_ALLOCATION_TYPE_INVALID ``

`` enumerator CU_MEM_ALLOCATION_TYPE_PINNED ``

This allocation type is ‘pinned’, i.e.

cannot migrate from its current location while the application is actively using it

`` enumerator CU_MEM_ALLOCATION_TYPE_MANAGED ``

This allocation type is managed memory.

`` enumerator CU_MEM_ALLOCATION_TYPE_MAX ``

`` enum CUmemAttach_flags ``

CUDA Mem Attach Flags.

_Values:_

`` enumerator CU_MEM_ATTACH_GLOBAL ``

Memory can be accessed by any stream on any device.

`` enumerator CU_MEM_ATTACH_HOST ``

Memory cannot be accessed by any stream on any device.

`` enumerator CU_MEM_ATTACH_SINGLE ``

Memory can only be accessed by a single stream on the associated device.

`` enum CUmemHandleType ``

Memory handle types.

_Values:_

`` enumerator CU_MEM_HANDLE_TYPE_GENERIC ``

`` enum CUmemLocationType ``

Specifies the type of location.

_Values:_

`` enumerator CU_MEM_LOCATION_TYPE_INVALID ``

`` enumerator CU_MEM_LOCATION_TYPE_NONE ``

Location is unspecified.

This is used when creating a managed memory pool to indicate no preferred location for the pool

`` enumerator CU_MEM_LOCATION_TYPE_DEVICE ``

Location is a device location, thus id is a device ordinal.

`` enumerator CU_MEM_LOCATION_TYPE_HOST ``

Location is host, id is ignored.

`` enumerator CU_MEM_LOCATION_TYPE_HOST_NUMA ``

Location is a host NUMA node, thus id is a host NUMA node id.

`` enumerator CU_MEM_LOCATION_TYPE_HOST_NUMA_CURRENT ``

Location is a host NUMA node of the current thread, id is ignored.

`` enumerator CU_MEM_LOCATION_TYPE_INVISIBLE ``

Location is not visible but device is accessible, id is always CU_DEVICE_INVALID.

`` enumerator CU_MEM_LOCATION_TYPE_DEVICE_LOCALITY_DOMAIN ``

Location is a portion of device memory, specified by the locality domain ID.

`` enumerator CU_MEM_LOCATION_TYPE_MAX ``

`` enum CUmemOperationType ``

Memory operation types.

_Values:_

`` enumerator CU_MEM_OPERATION_TYPE_MAP ``

`` enumerator CU_MEM_OPERATION_TYPE_UNMAP ``

`` enum CUmemPool_attribute ``

CUDA memory pool attributes.

_Values:_

`` enumerator CU_MEMPOOL_ATTR_REUSE_FOLLOW_EVENT_DEPENDENCIES ``

(value type = int) Allow cuMemAllocAsync to use memory asynchronously freed in another streams as long as a stream ordering dependency of the allocating stream on the free action exists.

Cuda events and null stream interactions can create the required stream ordered dependencies. (default enabled)

`` enumerator CU_MEMPOOL_ATTR_REUSE_ALLOW_OPPORTUNISTIC ``

(value type = int) Allow reuse of already completed frees when there is no dependency between the free and allocation.

(default enabled)

`` enumerator CU_MEMPOOL_ATTR_REUSE_ALLOW_INTERNAL_DEPENDENCIES ``

(value type = int) Allow cuMemAllocAsync to insert new stream dependencies in order to establish the stream ordering required to reuse a piece of memory released by cuMemFreeAsync (default enabled).

`` enumerator CU_MEMPOOL_ATTR_RELEASE_THRESHOLD ``

(value type = cuuint64_t) Amount of reserved memory in bytes to hold onto before trying to release memory back to the OS.

When more than the release threshold bytes of memory are held by the memory pool, the allocator will try to release memory back to the OS on the next call to stream, event or context synchronize. (default 0)

`` enumerator CU_MEMPOOL_ATTR_RESERVED_MEM_CURRENT ``

(value type = cuuint64_t) Amount of backing memory currently allocated for the mempool.

`` enumerator CU_MEMPOOL_ATTR_RESERVED_MEM_HIGH ``

(value type = cuuint64_t) High watermark of backing memory allocated for the mempool since the last time it was reset.

High watermark can only be reset to zero.

`` enumerator CU_MEMPOOL_ATTR_USED_MEM_CURRENT ``

(value type = cuuint64_t) Amount of memory from the pool that is currently in use by the application.

`` enumerator CU_MEMPOOL_ATTR_USED_MEM_HIGH ``

(value type = cuuint64_t) High watermark of the amount of memory from the pool that was in use by the application since the last time it was reset.

High watermark can only be reset to zero.

`` enumerator CU_MEMPOOL_ATTR_ALLOCATION_TYPE ``

(value type = CUmemAllocationType) The allocation type of the mempool

`` enumerator CU_MEMPOOL_ATTR_EXPORT_HANDLE_TYPES ``

(value type = CUmemAllocationHandleType) Available export handle types for the mempool.

For imported pools this value is always CU_MEM_HANDLE_TYPE_NONE as an imported pool cannot be re-exported

`` enumerator CU_MEMPOOL_ATTR_LOCATION_ID ``

(value type = int) The location id for the mempool.

If the location type for this pool is CU_MEM_LOCATION_TYPE_INVISIBLE then ID will be CU_DEVICE_INVALID.

`` enumerator CU_MEMPOOL_ATTR_LOCATION_TYPE ``

(value type = CUmemLocationType) The location type for the mempool.

For imported memory pools where the device is not directly visible to the importing process or pools imported via fabric handles across nodes this will be CU_MEM_LOCATION_TYPE_INVISIBLE.

`` enumerator CU_MEMPOOL_ATTR_MAX_POOL_SIZE ``

(value type = cuuint64_t) Maximum size of the pool in bytes, this value may be higher than what was initially passed to cuMemPoolCreate due to alignment requirements.

A value of 0 indicates no maximum size. For CU_MEM_ALLOCATION_TYPE_MANAGED and IPC imported pools this value will be system dependent.

`` enumerator CU_MEMPOOL_ATTR_HW_DECOMPRESS_ENABLED ``

(value type = int) Indicates whether the pool has hardware compresssion enabled

`` enumerator CU_MEMPOOL_ATTR_LOCALITY_DOMAIN_ID ``

(value type = int) The locality domain ID for the mempool, if the mempool is localized to a locality domain.

A value of -1 indicates that the mempool is not localized.

Note: On devices with a single locality domain, mempools created with CU_MEM_LOCATION_TYPE_DEVICE_LOCALITY_DOMAIN and localityDomainId 0 are equivalent to full-device mempools created with CU_MEM_LOCATION_TYPE_DEVICE. The value of this attribute will be -1 for such mempools.

`` enum CUmemRangeFlags ``

Flag for requesting handle type for address range.

_Values:_

`` enumerator CU_MEM_RANGE_FLAG_DMA_BUF_MAPPING_TYPE_PCIE ``

Indicates that DMA_BUF handle should be mapped via PCIe BAR1.

`` enum CUmemRangeHandleType ``

Specifies the handle type for address range.

_Values:_

`` enumerator CU_MEM_RANGE_HANDLE_TYPE_DMA_BUF_FD ``

`` enumerator CU_MEM_RANGE_HANDLE_TYPE_MAX ``

`` enum CUmem_advise ``

Memory advise values.

_Values:_

`` enumerator CU_MEM_ADVISE_SET_READ_MOSTLY ``

Data will mostly be read and only occasionally be written to.

`` enumerator CU_MEM_ADVISE_UNSET_READ_MOSTLY ``

Undo the effect of CU_MEM_ADVISE_SET_READ_MOSTLY.

`` enumerator CU_MEM_ADVISE_SET_PREFERRED_LOCATION ``

Set the preferred location for the data as the specified device.

`` enumerator CU_MEM_ADVISE_UNSET_PREFERRED_LOCATION ``

Clear the preferred location for the data.

`` enumerator CU_MEM_ADVISE_SET_ACCESSED_BY ``

Data will be accessed by the specified device, so prevent page faults as much as possible.

`` enumerator CU_MEM_ADVISE_UNSET_ACCESSED_BY ``

Let the Unified Memory subsystem decide on the page faulting policy for the specified device.

`` enum CUmem_range_attribute ``

_Values:_

`` enumerator CU_MEM_RANGE_ATTRIBUTE_READ_MOSTLY ``

Whether the range will mostly be read and only occasionally be written to.

`` enumerator CU_MEM_RANGE_ATTRIBUTE_PREFERRED_LOCATION ``

The preferred location of the range.

`` enumerator CU_MEM_RANGE_ATTRIBUTE_ACCESSED_BY ``

Memory range has CU_MEM_ADVISE_SET_ACCESSED_BY set for specified device.

`` enumerator CU_MEM_RANGE_ATTRIBUTE_LAST_PREFETCH_LOCATION ``

The last location to which the range was prefetched.

`` enumerator CU_MEM_RANGE_ATTRIBUTE_PREFERRED_LOCATION_TYPE ``

The preferred location type of the range.

`` enumerator CU_MEM_RANGE_ATTRIBUTE_PREFERRED_LOCATION_ID ``

The preferred location id of the range.

`` enumerator CU_MEM_RANGE_ATTRIBUTE_LAST_PREFETCH_LOCATION_TYPE ``

The last location type to which the range was prefetched.

`` enumerator CU_MEM_RANGE_ATTRIBUTE_LAST_PREFETCH_LOCATION_ID ``

The last location id to which the range was prefetched.

`` enum CUmemcpy3DOperandType ``

These flags allow applications to convey the operand type for individual copies specified in cuMemcpy3DBatchAsync.

_Values:_

`` enumerator CU_MEMCPY_OPERAND_TYPE_POINTER ``

Memcpy operand is a valid pointer.

`` enumerator CU_MEMCPY_OPERAND_TYPE_ARRAY ``

Memcpy operand is a CUarray.

`` enumerator CU_MEMCPY_OPERAND_TYPE_MAX ``

`` enum CUmemcpyFlags ``

Flags to specify for copies within a batch.

For more details see cuMemcpyBatchAsync.

_Values:_

`` enumerator CU_MEMCPY_FLAG_DEFAULT ``

`` enumerator CU_MEMCPY_FLAG_PREFER_OVERLAP_WITH_COMPUTE ``

Hint to the driver to try and overlap the copy with compute work on the SMs.

`` enum CUmemcpySrcAccessOrder ``

These flags allow applications to convey the source access ordering CUDA must maintain.

The destination will always be accessed in stream order.

_Values:_

`` enumerator CU_MEMCPY_SRC_ACCESS_ORDER_INVALID ``

Default invalid.

`` enumerator CU_MEMCPY_SRC_ACCESS_ORDER_STREAM ``

Indicates that access to the source pointer must be in stream order.

`` enumerator CU_MEMCPY_SRC_ACCESS_ORDER_DURING_API_CALL ``

Indicates that access to the source pointer can be out of stream order and all accesses must be complete before the API call returns.

This flag is suited for ephemeral sources (ex., stack variables) when it’s known that no prior operations in the stream can be accessing the memory and also that the lifetime of the memory is limited to the scope that the source variable was declared in. Specifying this flag allows the driver to optimize the copy and removes the need for the user to synchronize the stream after the API call.

`` enumerator CU_MEMCPY_SRC_ACCESS_ORDER_ANY ``

Indicates that access to the source pointer can be out of stream order and the accesses can happen even after the API call returns.

This flag is suited for host pointers allocated outside CUDA (ex., via malloc) when it’s known that no prior operations in the stream can be accessing the memory. Specifying this flag allows the driver to optimize the copy on certain platforms.

`` enumerator CU_MEMCPY_SRC_ACCESS_ORDER_MAX ``

`` enum CUmemorytype ``

Memory types.

_Values:_

`` enumerator CU_MEMORYTYPE_HOST ``

Host memory.

`` enumerator CU_MEMORYTYPE_DEVICE ``

Device memory.

`` enumerator CU_MEMORYTYPE_ARRAY ``

Array memory.

`` enumerator CU_MEMORYTYPE_UNIFIED ``

Unified device or host memory.

`` enum CUmulticastGranularity_flags ``

Flags for querying different granularities for a multicast object.

_Values:_

`` enumerator CU_MULTICAST_GRANULARITY_MINIMUM ``

Minimum required granularity.

`` enumerator CU_MULTICAST_GRANULARITY_RECOMMENDED ``

Recommended granularity for best performance.

`` enum CUoccupancy_flags ``

Occupancy calculator flag.

_Values:_

`` enumerator CU_OCCUPANCY_DEFAULT ``

Default behavior.

`` enumerator CU_OCCUPANCY_DISABLE_CACHING_OVERRIDE ``

Assume global caching is enabled and cannot be automatically turned off.

`` enum CUpointer_attribute ``

Pointer information.

_Values:_

`` enumerator CU_POINTER_ATTRIBUTE_CONTEXT ``

The CUcontext on which a pointer was allocated or registered.

`` enumerator CU_POINTER_ATTRIBUTE_MEMORY_TYPE ``

The CUmemorytype describing the physical location of a pointer.

`` enumerator CU_POINTER_ATTRIBUTE_DEVICE_POINTER ``

The address at which a pointer’s memory may be accessed on the device.

`` enumerator CU_POINTER_ATTRIBUTE_HOST_POINTER ``

The address at which a pointer’s memory may be accessed on the host.

`` enumerator CU_POINTER_ATTRIBUTE_P2P_TOKENS ``

A pair of tokens for use with the nv-p2p.h Linux kernel interface.

`` enumerator CU_POINTER_ATTRIBUTE_SYNC_MEMOPS ``

Synchronize every synchronous memory operation initiated on this region.

`` enumerator CU_POINTER_ATTRIBUTE_BUFFER_ID ``

A process-wide unique ID for an allocated memory region.

`` enumerator CU_POINTER_ATTRIBUTE_IS_MANAGED ``

Indicates if the pointer points to managed memory.

`` enumerator CU_POINTER_ATTRIBUTE_DEVICE_ORDINAL ``

A device ordinal of a device on which a pointer was allocated or registered.

`` enumerator CU_POINTER_ATTRIBUTE_IS_LEGACY_CUDA_IPC_CAPABLE ``

1 if this pointer maps to an allocation that is suitable for ::cudaIpcGetMemHandle, 0 otherwise

`` enumerator CU_POINTER_ATTRIBUTE_RANGE_START_ADDR ``

Starting address for this requested pointer.

`` enumerator CU_POINTER_ATTRIBUTE_RANGE_SIZE ``

Size of the address range for this requested pointer.

`` enumerator CU_POINTER_ATTRIBUTE_MAPPED ``

1 if this pointer is in a valid address range that is mapped to a backing allocation, 0 otherwise

`` enumerator CU_POINTER_ATTRIBUTE_ALLOWED_HANDLE_TYPES ``

Bitmask of allowed CUmemAllocationHandleType for this allocation.

`` enumerator CU_POINTER_ATTRIBUTE_IS_GPU_DIRECT_RDMA_CAPABLE ``

1 if the memory this pointer is referencing can be used with the GPUDirect RDMA API

`` enumerator CU_POINTER_ATTRIBUTE_ACCESS_FLAGS ``

Returns the access flags the device associated with the current context has on the corresponding memory referenced by the pointer given.

`` enumerator CU_POINTER_ATTRIBUTE_MEMPOOL_HANDLE ``

Returns the mempool handle for the allocation if it was allocated from a mempool.

Otherwise returns NULL.

`` enumerator CU_POINTER_ATTRIBUTE_MAPPING_SIZE ``

Size of the actual underlying mapping that the pointer belongs to.

`` enumerator CU_POINTER_ATTRIBUTE_MAPPING_BASE_ADDR ``

The start address of the mapping that the pointer belongs to.

`` enumerator CU_POINTER_ATTRIBUTE_MEMORY_BLOCK_ID ``

A process-wide unique id corresponding to the physical allocation the pointer belongs to.

`` enumerator CU_POINTER_ATTRIBUTE_IS_HW_DECOMPRESS_CAPABLE ``

Returns in `*data` a boolean that indicates whether the pointer points to memory that is capable to be used for hardware accelerated decompression.

`` enumerator CU_POINTER_ATTRIBUTE_LOCALITY_DOMAIN_ORDINAL ``

Returns in `*data` an integer representing the locality domain ordinal of the memory allocation, or -1 if the allocation is not localized to a locality domain.

`` enum CUprocessState ``

CUDA Process States.

_Values:_

`` enumerator CU_PROCESS_STATE_RUNNING ``

Default process state.

`` enumerator CU_PROCESS_STATE_LOCKED ``

CUDA API locks are taken so further CUDA API calls will block.

`` enumerator CU_PROCESS_STATE_CHECKPOINTED ``

Application memory contents have been checkpointed and underlying allocations and device handles have been released.

`` enumerator CU_PROCESS_STATE_FAILED ``

Application entered an uncorrectable error during the checkpoint/restore process.

`` enumerator CU_PROCESS_STATE_CHECKPOINTING ``

Application memory contents are being checkpointed.

`` enumerator CU_PROCESS_STATE_RESTORING ``

Application memory contents are being restored.

`` enum CUresourceViewFormat ``

Resource view format.

_Values:_

`` enumerator CU_RES_VIEW_FORMAT_NONE ``

No resource view format (use underlying resource format)

`` enumerator CU_RES_VIEW_FORMAT_UINT_1X8 ``

1 channel unsigned 8-bit integers

`` enumerator CU_RES_VIEW_FORMAT_UINT_2X8 ``

2 channel unsigned 8-bit integers

`` enumerator CU_RES_VIEW_FORMAT_UINT_4X8 ``

4 channel unsigned 8-bit integers

`` enumerator CU_RES_VIEW_FORMAT_SINT_1X8 ``

1 channel signed 8-bit integers

`` enumerator CU_RES_VIEW_FORMAT_SINT_2X8 ``

2 channel signed 8-bit integers

`` enumerator CU_RES_VIEW_FORMAT_SINT_4X8 ``

4 channel signed 8-bit integers

`` enumerator CU_RES_VIEW_FORMAT_UINT_1X16 ``

1 channel unsigned 16-bit integers

`` enumerator CU_RES_VIEW_FORMAT_UINT_2X16 ``

2 channel unsigned 16-bit integers

`` enumerator CU_RES_VIEW_FORMAT_UINT_4X16 ``

4 channel unsigned 16-bit integers

`` enumerator CU_RES_VIEW_FORMAT_SINT_1X16 ``

1 channel signed 16-bit integers

`` enumerator CU_RES_VIEW_FORMAT_SINT_2X16 ``

2 channel signed 16-bit integers

`` enumerator CU_RES_VIEW_FORMAT_SINT_4X16 ``

4 channel signed 16-bit integers

`` enumerator CU_RES_VIEW_FORMAT_UINT_1X32 ``

1 channel unsigned 32-bit integers

`` enumerator CU_RES_VIEW_FORMAT_UINT_2X32 ``

2 channel unsigned 32-bit integers

`` enumerator CU_RES_VIEW_FORMAT_UINT_4X32 ``

4 channel unsigned 32-bit integers

`` enumerator CU_RES_VIEW_FORMAT_SINT_1X32 ``

1 channel signed 32-bit integers

`` enumerator CU_RES_VIEW_FORMAT_SINT_2X32 ``

2 channel signed 32-bit integers

`` enumerator CU_RES_VIEW_FORMAT_SINT_4X32 ``

4 channel signed 32-bit integers

`` enumerator CU_RES_VIEW_FORMAT_FLOAT_1X16 ``

1 channel 16-bit floating point

`` enumerator CU_RES_VIEW_FORMAT_FLOAT_2X16 ``

2 channel 16-bit floating point

`` enumerator CU_RES_VIEW_FORMAT_FLOAT_4X16 ``

4 channel 16-bit floating point

`` enumerator CU_RES_VIEW_FORMAT_FLOAT_1X32 ``

1 channel 32-bit floating point

`` enumerator CU_RES_VIEW_FORMAT_FLOAT_2X32 ``

2 channel 32-bit floating point

`` enumerator CU_RES_VIEW_FORMAT_FLOAT_4X32 ``

4 channel 32-bit floating point

`` enumerator CU_RES_VIEW_FORMAT_UNSIGNED_BC1 ``

Block compressed 1.

`` enumerator CU_RES_VIEW_FORMAT_UNSIGNED_BC2 ``

Block compressed 2.

`` enumerator CU_RES_VIEW_FORMAT_UNSIGNED_BC3 ``

Block compressed 3.

`` enumerator CU_RES_VIEW_FORMAT_UNSIGNED_BC4 ``

Block compressed 4 unsigned.

`` enumerator CU_RES_VIEW_FORMAT_SIGNED_BC4 ``

Block compressed 4 signed.

`` enumerator CU_RES_VIEW_FORMAT_UNSIGNED_BC5 ``

Block compressed 5 unsigned.

`` enumerator CU_RES_VIEW_FORMAT_SIGNED_BC5 ``

Block compressed 5 signed.

`` enumerator CU_RES_VIEW_FORMAT_UNSIGNED_BC6H ``

Block compressed 6 unsigned half-float.

`` enumerator CU_RES_VIEW_FORMAT_SIGNED_BC6H ``

Block compressed 6 signed half-float.

`` enumerator CU_RES_VIEW_FORMAT_UNSIGNED_BC7 ``

Block compressed 7.

`` enum CUresourcetype ``

Resource types.

_Values:_

`` enumerator CU_RESOURCE_TYPE_ARRAY ``

Array resource.

`` enumerator CU_RESOURCE_TYPE_MIPMAPPED_ARRAY ``

Mipmapped array resource.

`` enumerator CU_RESOURCE_TYPE_LINEAR ``

Linear resource.

`` enumerator CU_RESOURCE_TYPE_PITCH2D ``

Pitch 2D resource.

`` enum CUresult ``

Error codes.

_Values:_

`` enumerator CUDA_SUCCESS ``

The API call returned with no errors.

In the case of query calls, this also means that the operation being queried is complete (see cuEventQuery() and cuStreamQuery()).

`` enumerator CUDA_ERROR_INVALID_VALUE ``

This indicates that one or more of the parameters passed to the API call is not within an acceptable range of values.

`` enumerator CUDA_ERROR_OUT_OF_MEMORY ``

The API call failed because it was unable to allocate enough memory or other resources to perform the requested operation.

`` enumerator CUDA_ERROR_NOT_INITIALIZED ``

This indicates that the CUDA driver has not been initialized with cuInit() or that initialization has failed.

`` enumerator CUDA_ERROR_DEINITIALIZED ``

This indicates that the CUDA driver is in the process of shutting down.

`` enumerator CUDA_ERROR_PROFILER_DISABLED ``

This indicates profiler is not initialized for this run.

This can happen when the application is running with external profiling tools like visual profiler.

`` enumerator CUDA_ERROR_PROFILER_NOT_INITIALIZED ``

`` Deprecated: ``

This error return is deprecated as of CUDA 5.0. It is no longer an error to attempt to enable/disable the profiling via cuProfilerStart or cuProfilerStop without initialization.

`` enumerator CUDA_ERROR_PROFILER_ALREADY_STARTED ``

`` Deprecated: ``

This error return is deprecated as of CUDA 5.0. It is no longer an error to call cuProfilerStart() when profiling is already enabled.

`` enumerator CUDA_ERROR_PROFILER_ALREADY_STOPPED ``

`` Deprecated: ``

This error return is deprecated as of CUDA 5.0. It is no longer an error to call cuProfilerStop() when profiling is already disabled.

`` enumerator CUDA_ERROR_STUB_LIBRARY ``

This indicates that the CUDA driver that the application has loaded is a stub library.

Applications that run with the stub rather than a real driver loaded will result in CUDA API returning this error.

`` enumerator CUDA_ERROR_CALL_REQUIRES_NEWER_DRIVER ``

This indicates that the API call requires a newer CUDA driver than the one currently installed.

Users should install an updated NVIDIA CUDA driver to allow the API call to succeed.

`` enumerator CUDA_ERROR_DEVICE_UNAVAILABLE ``

This indicates that requested CUDA device is unavailable at the current time.

Devices are often unavailable due to use of CU_COMPUTEMODE_EXCLUSIVE_PROCESS or CU_COMPUTEMODE_PROHIBITED.

`` enumerator CUDA_ERROR_MULTICAST_RESOURCE_FULL ``

The API call failed because of a hardware resource required to bind memory to a multicast object is unavailable.

`` enumerator CUDA_ERROR_NO_DEVICE ``

This indicates that no CUDA-capable devices were detected by the installed CUDA driver.

`` enumerator CUDA_ERROR_INVALID_DEVICE ``

This indicates that the device ordinal supplied by the user does not correspond to a valid CUDA device or that the action requested is invalid for the specified device.

`` enumerator CUDA_ERROR_DEVICE_NOT_LICENSED ``

This error indicates that the Grid license is not applied.

`` enumerator CUDA_ERROR_INVALID_IMAGE ``

This indicates that the device kernel image is invalid.

This can also indicate an invalid CUDA module.

`` enumerator CUDA_ERROR_INVALID_CONTEXT ``

This most frequently indicates that there is no context bound to the current thread.

This can also be returned if the context passed to an API call is not a valid handle (such as a context that has had cuCtxDestroy() invoked on it). This can also be returned if a user mixes different API versions (i.e. 3010 context with 3020 API calls). See cuCtxGetApiVersion() for more details. This can also be returned if the green context passed to an API call was not converted to a CUcontext using cuCtxFromGreenCtx API.

`` enumerator CUDA_ERROR_CONTEXT_ALREADY_CURRENT ``

This indicated that the context being supplied as a parameter to the API call was already the active context.

`` Deprecated: ``

This error return is deprecated as of CUDA 3.2. It is no longer an error to attempt to push the active context via cuCtxPushCurrent().

`` enumerator CUDA_ERROR_MAP_FAILED ``

This indicates that a map or register operation has failed.

`` enumerator CUDA_ERROR_UNMAP_FAILED ``

This indicates that an unmap or unregister operation has failed.

`` enumerator CUDA_ERROR_ARRAY_IS_MAPPED ``

This indicates that the specified array is currently mapped and thus cannot be destroyed.

`` enumerator CUDA_ERROR_ALREADY_MAPPED ``

This indicates that the resource is already mapped.

`` enumerator CUDA_ERROR_NO_BINARY_FOR_GPU ``

This indicates that there is no kernel image available that is suitable for the device.

This can occur when a user specifies code generation options for a particular CUDA source file that do not include the corresponding device configuration.

`` enumerator CUDA_ERROR_ALREADY_ACQUIRED ``

This indicates that a resource has already been acquired.

`` enumerator CUDA_ERROR_NOT_MAPPED ``

This indicates that a resource is not mapped.

`` enumerator CUDA_ERROR_NOT_MAPPED_AS_ARRAY ``

This indicates that a mapped resource is not available for access as an array.

`` enumerator CUDA_ERROR_NOT_MAPPED_AS_POINTER ``

This indicates that a mapped resource is not available for access as a pointer.

`` enumerator CUDA_ERROR_ECC_UNCORRECTABLE ``

This indicates that an uncorrectable ECC error was detected during execution.

`` enumerator CUDA_ERROR_UNSUPPORTED_LIMIT ``

This indicates that the CUlimit passed to the API call is not supported by the active device.

`` enumerator CUDA_ERROR_CONTEXT_ALREADY_IN_USE ``

This indicates that the CUcontext passed to the API call can only be bound to a single CPU thread at a time but is already bound to a CPU thread.

`` enumerator CUDA_ERROR_PEER_ACCESS_UNSUPPORTED ``

This indicates that peer access is not supported across the given devices.

`` enumerator CUDA_ERROR_INVALID_PTX ``

This indicates that a PTX JIT compilation failed.

`` enumerator CUDA_ERROR_INVALID_GRAPHICS_CONTEXT ``

This indicates an error with OpenGL or DirectX context.

`` enumerator CUDA_ERROR_NVLINK_UNCORRECTABLE ``

This indicates that an uncorrectable NVLink error was detected during the execution.

`` enumerator CUDA_ERROR_JIT_COMPILER_NOT_FOUND ``

This indicates that the PTX JIT compiler library was not found.

`` enumerator CUDA_ERROR_UNSUPPORTED_PTX_VERSION ``

This indicates that the provided PTX was compiled with an unsupported toolchain.

`` enumerator CUDA_ERROR_JIT_COMPILATION_DISABLED ``

This indicates that the PTX JIT compilation was disabled.

`` enumerator CUDA_ERROR_UNSUPPORTED_EXEC_AFFINITY ``

This indicates that the CUexecAffinityType passed to the API call is not supported by the active device.

`` enumerator CUDA_ERROR_UNSUPPORTED_DEVSIDE_SYNC ``

This indicates that the code to be compiled by the PTX JIT contains unsupported call to cudaDeviceSynchronize.

`` enumerator CUDA_ERROR_CONTAINED ``

This indicates that an exception occurred on the device that is now contained by the GPU’s error containment capability.

Common causes are - a. Certain types of invalid accesses of peer GPU memory over nvlink b. Certain classes of hardware errors This leaves the process in an inconsistent state and any further CUDA work will return the same error. To continue using CUDA, the process must be terminated and relaunched.

`` enumerator CUDA_ERROR_INSUFFICIENT_LOADER_VERSION ``

This indicates that the Loader version is insufficient for fatbin.

`` enumerator CUDA_ERROR_INVALID_SOURCE ``

This indicates that the device kernel source is invalid.

This includes compilation/linker errors encountered in device code or user error.

`` enumerator CUDA_ERROR_FILE_NOT_FOUND ``

This indicates that the file specified was not found.

`` enumerator CUDA_ERROR_SHARED_OBJECT_SYMBOL_NOT_FOUND ``

This indicates that a link to a shared object failed to resolve.

`` enumerator CUDA_ERROR_SHARED_OBJECT_INIT_FAILED ``

This indicates that initialization of a shared object failed.

`` enumerator CUDA_ERROR_OPERATING_SYSTEM ``

This indicates that an OS call failed.

`` enumerator CUDA_ERROR_INVALID_HANDLE ``

This indicates that a resource handle passed to the API call was not valid.

Resource handles are opaque types like CUstream and CUevent.

`` enumerator CUDA_ERROR_ILLEGAL_STATE ``

This indicates that a resource required by the API call is not in a valid state to perform the requested operation.

`` enumerator CUDA_ERROR_LOSSY_QUERY ``

This indicates an attempt was made to introspect an object in a way that would discard semantically important information.

This is either due to the object using funtionality newer than the API version used to introspect it or omission of optional return arguments.

`` enumerator CUDA_ERROR_NOT_FOUND ``

This indicates that a named symbol was not found.

Examples of symbols are global/constant variable names, driver function names, texture names, and surface names.

`` enumerator CUDA_ERROR_NOT_READY ``

This indicates that asynchronous operations issued previously have not completed yet.

This result is not actually an error, but must be indicated differently than CUDA_SUCCESS (which indicates completion). Calls that may return this value include cuEventQuery() and cuStreamQuery().

`` enumerator CUDA_ERROR_ILLEGAL_ADDRESS ``

While executing a kernel, the device encountered a load or store instruction on an invalid memory address.

This leaves the process in an inconsistent state and any further CUDA work will return the same error. To continue using CUDA, the process must be terminated and relaunched.

`` enumerator CUDA_ERROR_LAUNCH_OUT_OF_RESOURCES ``

This indicates that a launch did not occur because it did not have appropriate resources.

This error usually indicates that the user has attempted to pass too many arguments to the device kernel, or the kernel launch specifies too many threads for the kernel’s register count. Passing arguments of the wrong size (i.e. a 64-bit pointer when a 32-bit int is expected) is equivalent to passing too many arguments and can also result in this error.

`` enumerator CUDA_ERROR_LAUNCH_TIMEOUT ``

This indicates that the device kernel took too long to execute.

This can only occur if timeouts are enabled - see the device attribute CU_DEVICE_ATTRIBUTE_KERNEL_EXEC_TIMEOUT for more information. This leaves the process in an inconsistent state and any further CUDA work will return the same error. To continue using CUDA, the process must be terminated and relaunched.

`` enumerator CUDA_ERROR_LAUNCH_INCOMPATIBLE_TEXTURING ``

This error indicates a kernel launch that uses an incompatible texturing mode.

`` enumerator CUDA_ERROR_PEER_ACCESS_ALREADY_ENABLED ``

This error indicates that a call to cuCtxEnablePeerAccess() is trying to re-enable peer access to a context which has already had peer access to it enabled.

`` enumerator CUDA_ERROR_PEER_ACCESS_NOT_ENABLED ``

This error indicates that cuCtxDisablePeerAccess() is trying to disable peer access which has not been enabled yet via cuCtxEnablePeerAccess().

`` enumerator CUDA_ERROR_PRIMARY_CONTEXT_ACTIVE ``

This error indicates that the primary context for the specified device has already been initialized.

`` enumerator CUDA_ERROR_CONTEXT_IS_DESTROYED ``

This error indicates that the context current to the calling thread has been destroyed using cuCtxDestroy, or is a primary context which has not yet been initialized.

`` enumerator CUDA_ERROR_ASSERT ``

A device-side assert triggered during kernel execution.

The context cannot be used anymore, and must be destroyed. All existing device memory allocations from this context are invalid and must be reconstructed if the program is to continue using CUDA.

`` enumerator CUDA_ERROR_TOO_MANY_PEERS ``

This error indicates that the hardware resources required to enable peer access have been exhausted for one or more of the devices passed to cuCtxEnablePeerAccess().

`` enumerator CUDA_ERROR_HOST_MEMORY_ALREADY_REGISTERED ``

This error indicates that the memory range passed to cuMemHostRegister() has already been registered.

`` enumerator CUDA_ERROR_HOST_MEMORY_NOT_REGISTERED ``

This error indicates that the pointer passed to cuMemHostUnregister() does not correspond to any currently registered memory region.

`` enumerator CUDA_ERROR_HARDWARE_STACK_ERROR ``

While executing a kernel, the device encountered a stack error.

This can be due to stack corruption or exceeding the stack size limit. This leaves the process in an inconsistent state and any further CUDA work will return the same error. To continue using CUDA, the process must be terminated and relaunched.

`` enumerator CUDA_ERROR_ILLEGAL_INSTRUCTION ``

While executing a kernel, the device encountered an illegal instruction.

This leaves the process in an inconsistent state and any further CUDA work will return the same error. To continue using CUDA, the process must be terminated and relaunched.

`` enumerator CUDA_ERROR_MISALIGNED_ADDRESS ``

While executing a kernel, the device encountered a load or store instruction on a memory address which is not aligned.

This leaves the process in an inconsistent state and any further CUDA work will return the same error. To continue using CUDA, the process must be terminated and relaunched.

`` enumerator CUDA_ERROR_INVALID_ADDRESS_SPACE ``

While executing a kernel, the device encountered an instruction which can only operate on memory locations in certain address spaces (global, shared, or local), but was supplied a memory address not belonging to an allowed address space.

This leaves the process in an inconsistent state and any further CUDA work will return the same error. To continue using CUDA, the process must be terminated and relaunched.

`` enumerator CUDA_ERROR_INVALID_PC ``

While executing a kernel, the device program counter wrapped its address space.

This leaves the process in an inconsistent state and any further CUDA work will return the same error. To continue using CUDA, the process must be terminated and relaunched.

`` enumerator CUDA_ERROR_LAUNCH_FAILED ``

An exception occurred on the device while executing a kernel.

Common causes include dereferencing an invalid device pointer and accessing out of bounds shared memory. Less common cases can be system specific - more information about these cases can be found in the system specific user guide. This leaves the process in an inconsistent state and any further CUDA work will return the same error. To continue using CUDA, the process must be terminated and relaunched.

`` enumerator CUDA_ERROR_COOPERATIVE_LAUNCH_TOO_LARGE ``

This error indicates that the number of blocks launched per grid for a kernel that was launched via either cuLaunchCooperativeKernel or cuLaunchCooperativeKernelMultiDevice exceeds the maximum number of blocks as allowed by cuOccupancyMaxActiveBlocksPerMultiprocessor or cuOccupancyMaxActiveBlocksPerMultiprocessorWithFlags times the number of multiprocessors as specified by the device attribute CU_DEVICE_ATTRIBUTE_MULTIPROCESSOR_COUNT.

`` enumerator CUDA_ERROR_TENSOR_MEMORY_LEAK ``

An exception occurred on the device while exiting a kernel using tensor memory: the tensor memory was not completely deallocated.

This leaves the process in an inconsistent state and any further CUDA work will return the same error. To continue using CUDA, the process must be terminated and relaunched.

`` enumerator CUDA_ERROR_NOT_PERMITTED ``

This error indicates that the attempted operation is not permitted.

`` enumerator CUDA_ERROR_NOT_SUPPORTED ``

This error indicates that the attempted operation is not supported on the current system or device.

`` enumerator CUDA_ERROR_SYSTEM_NOT_READY ``

This error indicates that the system is not yet ready to start any CUDA work.

To continue using CUDA, verify the system configuration is in a valid state and all required driver daemons are actively running. More information about this error can be found in the system specific user guide.

`` enumerator CUDA_ERROR_SYSTEM_DRIVER_MISMATCH ``

This error indicates that there is a mismatch between the versions of the display driver and the CUDA driver.

Refer to the compatibility documentation for supported versions.

`` enumerator CUDA_ERROR_COMPAT_NOT_SUPPORTED_ON_DEVICE ``

This error indicates that the system was upgraded to run with forward compatibility but the visible hardware detected by CUDA does not support this configuration.

Refer to the compatibility documentation for the supported hardware matrix or ensure that only supported hardware is visible during initialization via the CUDA_VISIBLE_DEVICES environment variable.

`` enumerator CUDA_ERROR_MPS_CONNECTION_FAILED ``

This error indicates that the MPS client failed to connect to the MPS control daemon or the MPS server.

`` enumerator CUDA_ERROR_MPS_RPC_FAILURE ``

This error indicates that the remote procedural call between the MPS server and the MPS client failed.

`` enumerator CUDA_ERROR_MPS_SERVER_NOT_READY ``

This error indicates that the MPS server is not ready to accept new MPS client requests.

This error can be returned when the MPS server is in the process of recovering from a fatal failure.

`` enumerator CUDA_ERROR_MPS_MAX_CLIENTS_REACHED ``

This error indicates that the hardware resources required to create MPS client have been exhausted.

`` enumerator CUDA_ERROR_MPS_MAX_CONNECTIONS_REACHED ``

This error indicates the the hardware resources required to support device connections have been exhausted.

`` enumerator CUDA_ERROR_MPS_CLIENT_TERMINATED ``

This error indicates that the MPS client has been terminated by the server.

To continue using CUDA, the process must be terminated and relaunched.

`` enumerator CUDA_ERROR_CDP_NOT_SUPPORTED ``

This error indicates that the module is using CUDA Dynamic Parallelism, but the current configuration, like MPS, does not support it.

`` enumerator CUDA_ERROR_CDP_VERSION_MISMATCH ``

This error indicates that a module contains an unsupported interaction between different versions of CUDA Dynamic Parallelism.

`` enumerator CUDA_ERROR_STREAM_CAPTURE_UNSUPPORTED ``

This error indicates that the operation is not permitted when the stream is capturing.

`` enumerator CUDA_ERROR_STREAM_CAPTURE_INVALIDATED ``

This error indicates that the current capture sequence on the stream has been invalidated due to a previous error.

`` enumerator CUDA_ERROR_STREAM_CAPTURE_MERGE ``

This error indicates that the operation would have resulted in a merge of two independent capture sequences.

`` enumerator CUDA_ERROR_STREAM_CAPTURE_UNMATCHED ``

This error indicates that the capture was not initiated in this stream.

`` enumerator CUDA_ERROR_STREAM_CAPTURE_UNJOINED ``

This error indicates that the capture sequence contains a fork that was not joined to the primary stream.

`` enumerator CUDA_ERROR_STREAM_CAPTURE_ISOLATION ``

This error indicates that a dependency would have been created which crosses the capture sequence boundary.

Only implicit in-stream ordering dependencies are allowed to cross the boundary.

`` enumerator CUDA_ERROR_STREAM_CAPTURE_IMPLICIT ``

This error indicates a disallowed implicit dependency on a current capture sequence from cudaStreamLegacy.

`` enumerator CUDA_ERROR_CAPTURED_EVENT ``

This error indicates that the operation is not permitted on an event which was last recorded in a capturing stream.

`` enumerator CUDA_ERROR_STREAM_CAPTURE_WRONG_THREAD ``

A stream capture sequence not initiated with the CU_STREAM_CAPTURE_MODE_RELAXED argument to cuStreamBeginCapture was passed to cuStreamEndCapture in a different thread.

`` enumerator CUDA_ERROR_TIMEOUT ``

This error indicates that the timeout specified for the wait operation has lapsed.

`` enumerator CUDA_ERROR_GRAPH_EXEC_UPDATE_FAILURE ``

This error indicates that the graph update was not performed because it included changes which violated constraints specific to instantiated graph update.

`` enumerator CUDA_ERROR_EXTERNAL_DEVICE ``

This indicates that an error has occurred in a device outside of GPU.

It can be a synchronous error w.r.t. CUDA API or an asynchronous error from the external device. In case of asynchronous error, it means that if cuda was waiting for an external device’s signal before consuming shared data, the external device signaled an error indicating that the data is not valid for consumption. This leaves the process in an inconsistent state and any further CUDA work will return the same error. To continue using CUDA, the process must be terminated and relaunched. In case of synchronous error, it means that one or more external devices have encountered an error and cannot complete the operation.

`` enumerator CUDA_ERROR_INVALID_CLUSTER_SIZE ``

Indicates a kernel launch error due to cluster misconfiguration.

`` enumerator CUDA_ERROR_FUNCTION_NOT_LOADED ``

Indiciates a function handle is not loaded when calling an API that requires a loaded function.

`` enumerator CUDA_ERROR_INVALID_RESOURCE_TYPE ``

This error indicates one or more resources passed in are not valid resource types for the operation.

`` enumerator CUDA_ERROR_INVALID_RESOURCE_CONFIGURATION ``

This error indicates one or more resources are insufficient or non-applicable for the operation.

`` enumerator CUDA_ERROR_KEY_ROTATION ``

This error indicates that an error happened during the key rotation sequence.

`` enumerator CUDA_ERROR_STREAM_DETACHED ``

This error indicates that the requested operation is not permitted because the stream is in a detached state.

This can occur if the green context associated with the stream has been destroyed, limiting the stream’s operational capabilities.

`` enumerator CUDA_ERROR_GRAPH_RECAPTURE_FAILURE ``

This error indicates that a graph recapture failed and had to be terminated.

`` enumerator CUDA_ERROR_FABRIC_NOT_READY ``

The GPU fabric is not ready within the bounded wait while the fabric manager probe is still in progress (or not converging in time).

Applications may retry after a delay; for the initialization wait budget, see environment variables such as CUDA_FABRIC_INIT_TIMEOUT_MS. The CUDA Runtime uses the same value as ::cudaErrorFabricNotReady.

`` enumerator CUDA_ERROR_UNKNOWN ``

This indicates that an unknown internal error has occurred.

`` enum CUsharedMemoryMode ``

Shared memory related attributes for use with cuLaunchKernelEx.

_Values:_

`` enumerator CU_SHARED_MEMORY_MODE_DEFAULT ``

The default to use for shared memory on launch - uses current function attribute for CU_FUNC_ATTRIBUTE_MAX_DYNAMIC_SHARED_SIZE_BYTES.

`` enumerator CU_SHARED_MEMORY_MODE_REQUIRE_PORTABLE ``

Specifies that the dynamic shared size bytes requested must be a portable size within the bounds of CU_DEVICE_ATTRIBUTE_MAX_SHARED_MEMORY_PER_BLOCK.

`` enumerator CU_SHARED_MEMORY_MODE_ALLOW_NON_PORTABLE ``

Specifies that the dynamic shared size bytes requested may be a non-portable size but still within the bounds of CU_DEVICE_ATTRIBUTE_MAX_SHARED_MEMORY_PER_BLOCK_OPTIN.

`` enumerator CU_SHARED_MEMORY_MODE_ALLOW_OVERSIZED_SHARED_MEMORY ``

Specifies that oversized shared memory configurations may be used (with the limitation of only 8kB L1 cache)

`` enumerator CU_SHARED_MEMORY_MODE_PREFER_OVERSIZED_SHARED_MEMORY ``

Specifies that oversized shared memory configurations may be used (with the limitation of only 8kB L1 cache), and prefer an oversized shared memory configuration.

`` enum CUshared_carveout ``

Shared memory carveout configurations.

These may be passed to cuFuncSetAttribute or cuKernelSetAttribute

_Values:_

`` enumerator CU_SHAREDMEM_CARVEOUT_DEFAULT ``

No preference for shared memory or L1 (default)

`` enumerator CU_SHAREDMEM_CARVEOUT_MAX_SHARED ``

Prefer maximum available shared memory, minimum L1 cache.

`` enumerator CU_SHAREDMEM_CARVEOUT_MAX_L1 ``

Prefer maximum available L1 cache, minimum shared memory.

`` enum CUsharedconfig ``

`` Deprecated: ``

Shared memory configurations

_Values:_

`` enumerator CU_SHARED_MEM_CONFIG_DEFAULT_BANK_SIZE ``

set default shared memory bank size

`` enumerator CU_SHARED_MEM_CONFIG_FOUR_BYTE_BANK_SIZE ``

set shared memory bank width to four bytes

`` enumerator CU_SHARED_MEM_CONFIG_EIGHT_BYTE_BANK_SIZE ``

set shared memory bank width to eight bytes

`` enum CUstreamAtomicReductionDataType ``

Atomic reduction data types for ::CUstreamBatchMemOpParams::atomicReduction::dataType.

_Values:_

`` enumerator CU_STREAM_ATOMIC_REDUCTION_UNSIGNED_32 ``

`` enumerator CU_STREAM_ATOMIC_REDUCTION_UNSIGNED_64 ``

`` enum CUstreamAtomicReductionOpType ``

Atomic reduction operation types for ::CUstreamBatchMemOpParams::atomicReduction::reductionOp.

_Values:_

`` enumerator CU_STREAM_ATOMIC_REDUCTION_OP_OR ``

Performs an atomic OR: *(address) = *(address) | value.

`` enumerator CU_STREAM_ATOMIC_REDUCTION_OP_AND ``

Performs an atomic AND: *(address) = *(address) & value.

`` enumerator CU_STREAM_ATOMIC_REDUCTION_OP_ADD ``

Performs an atomic ADD: *(address) = *(address) + value.

`` enum CUstreamBatchMemOpType ``

Operations for cuStreamBatchMemOp.

_Values:_

`` enumerator CU_STREAM_MEM_OP_WAIT_VALUE_32 ``

Represents a cuStreamWaitValue32 operation.

`` enumerator CU_STREAM_MEM_OP_WRITE_VALUE_32 ``

Represents a cuStreamWriteValue32 operation.

`` enumerator CU_STREAM_MEM_OP_WAIT_VALUE_64 ``

Represents a cuStreamWaitValue64 operation.

`` enumerator CU_STREAM_MEM_OP_WRITE_VALUE_64 ``

Represents a cuStreamWriteValue64 operation.

`` enumerator CU_STREAM_MEM_OP_BARRIER ``

Insert a memory barrier of the specified type.

`` enumerator CU_STREAM_MEM_OP_ATOMIC_REDUCTION ``

Perform a atomic reduction.

See CUstreamBatchMemOpParams::atomicReduction

`` enumerator CU_STREAM_MEM_OP_FLUSH_REMOTE_WRITES ``

This has the same effect as CU_STREAM_WAIT_VALUE_FLUSH, but as a standalone operation.

`` enum CUstreamCaptureMode ``

Possible modes for stream capture thread interactions.

For more details see cuStreamBeginCapture and cuThreadExchangeStreamCaptureMode

_Values:_

`` enumerator CU_STREAM_CAPTURE_MODE_GLOBAL ``

`` enumerator CU_STREAM_CAPTURE_MODE_THREAD_LOCAL ``

`` enumerator CU_STREAM_CAPTURE_MODE_RELAXED ``

`` enum CUstreamCaptureStatus ``

Possible stream capture statuses returned by cuStreamIsCapturing.

_Values:_

`` enumerator CU_STREAM_CAPTURE_STATUS_NONE ``

Stream is not capturing.

`` enumerator CU_STREAM_CAPTURE_STATUS_ACTIVE ``

Stream is actively capturing.

`` enumerator CU_STREAM_CAPTURE_STATUS_INVALIDATED ``

Stream is part of a capture sequence that has been invalidated, but not terminated.

`` enum CUstreamCigDataType ``

_Values:_

`` enumerator STREAM_CIG_DATA_TYPE_D3D12_COMMAND_LIST ``

D3D12 Command List Handle.

`` enum CUstreamMemoryBarrier_flags ``

Flags for CUstreamBatchMemOpParams::memoryBarrier.

_Values:_

`` enumerator CU_STREAM_MEMORY_BARRIER_TYPE_SYS ``

System-wide memory barrier.

`` enumerator CU_STREAM_MEMORY_BARRIER_TYPE_GPU ``

Limit memory barrier scope to the GPU.

`` enum CUstreamUpdateCaptureDependencies_flags ``

Flags for cuStreamUpdateCaptureDependencies.

_Values:_

`` enumerator CU_STREAM_ADD_CAPTURE_DEPENDENCIES ``

Add new nodes to the dependency set.

`` enumerator CU_STREAM_SET_CAPTURE_DEPENDENCIES ``

Replace the dependency set with the new nodes.

`` enum CUstreamWaitValue_flags ``

Flags for cuStreamWaitValue32 and cuStreamWaitValue64.

_Values:_

`` enumerator CU_STREAM_WAIT_VALUE_GEQ ``

Wait until (int32_t)(*addr - value) >= 0 (or int64_t for 64 bit values).

Note this is a cyclic comparison which ignores wraparound. (Default behavior.)

`` enumerator CU_STREAM_WAIT_VALUE_EQ ``

Wait until *addr == value.

`` enumerator CU_STREAM_WAIT_VALUE_AND ``

Wait until (*addr & value) != 0.

`` enumerator CU_STREAM_WAIT_VALUE_NOR ``

Wait until ~(*addr | value) != 0.

Support for this operation can be queried with cuDeviceGetAttribute() and CU_DEVICE_ATTRIBUTE_CAN_USE_STREAM_WAIT_VALUE_NOR.

`` enumerator CU_STREAM_WAIT_VALUE_FLUSH ``

Follow the wait operation with a flush of outstanding remote writes.

This means that, if a remote write operation is guaranteed to have reached the device before the wait can be satisfied, that write is guaranteed to be visible to downstream device work. The device is permitted to reorder remote writes internally. For example, this flag would be required if two remote writes arrive in a defined order, the wait is satisfied by the second write, and downstream work needs to observe the first write. Support for this operation is restricted to selected platforms and can be queried with CU_DEVICE_ATTRIBUTE_CAN_FLUSH_REMOTE_WRITES.

`` enum CUstreamWriteValue_flags ``

Flags for cuStreamWriteValue32.

_Values:_

`` enumerator CU_STREAM_WRITE_VALUE_DEFAULT ``

Default behavior.

`` enumerator CU_STREAM_WRITE_VALUE_NO_MEMORY_BARRIER ``

Permits the write to be reordered with writes which were issued before it, as a performance optimization.

Normally, cuStreamWriteValue32 will provide a memory fence before the write, which has similar semantics to __threadfence_system() but is scoped to the stream rather than a CUDA thread. This flag is not supported in the v2 API.

`` enum CUstream_flags ``

Stream creation flags.

_Values:_

`` enumerator CU_STREAM_DEFAULT ``

Default stream flag.

`` enumerator CU_STREAM_NON_BLOCKING ``

Stream does not synchronize with stream 0 (the NULL stream)

`` enum CUsynchronizationPolicy ``

_Values:_

`` enumerator CU_SYNC_POLICY_AUTO ``

`` enumerator CU_SYNC_POLICY_SPIN ``

`` enumerator CU_SYNC_POLICY_YIELD ``

`` enumerator CU_SYNC_POLICY_BLOCKING_SYNC ``

`` enum CUtensorMapDataType ``

Tensor map data type.

_Values:_

`` enumerator CU_TENSOR_MAP_DATA_TYPE_UINT8 ``

`` enumerator CU_TENSOR_MAP_DATA_TYPE_UINT16 ``

`` enumerator CU_TENSOR_MAP_DATA_TYPE_UINT32 ``

`` enumerator CU_TENSOR_MAP_DATA_TYPE_INT32 ``

`` enumerator CU_TENSOR_MAP_DATA_TYPE_UINT64 ``

`` enumerator CU_TENSOR_MAP_DATA_TYPE_INT64 ``

`` enumerator CU_TENSOR_MAP_DATA_TYPE_FLOAT16 ``

`` enumerator CU_TENSOR_MAP_DATA_TYPE_FLOAT32 ``

`` enumerator CU_TENSOR_MAP_DATA_TYPE_FLOAT64 ``

`` enumerator CU_TENSOR_MAP_DATA_TYPE_BFLOAT16 ``

`` enumerator CU_TENSOR_MAP_DATA_TYPE_FLOAT32_FTZ ``

`` enumerator CU_TENSOR_MAP_DATA_TYPE_TFLOAT32 ``

`` enumerator CU_TENSOR_MAP_DATA_TYPE_TFLOAT32_FTZ ``

`` enumerator CU_TENSOR_MAP_DATA_TYPE_16U4_ALIGN8B ``

`` enumerator CU_TENSOR_MAP_DATA_TYPE_16U4_ALIGN16B ``

`` enumerator CU_TENSOR_MAP_DATA_TYPE_16U6_ALIGN16B ``

`` enum CUtensorMapFloatOOBfill ``

Tensor map out-of-bounds fill type.

_Values:_

`` enumerator CU_TENSOR_MAP_FLOAT_OOB_FILL_NONE ``

`` enumerator CU_TENSOR_MAP_FLOAT_OOB_FILL_NAN_REQUEST_ZERO_FMA ``

`` enum CUtensorMapIm2ColWideMode ``

Tensor map Im2Col wide mode.

_Values:_

`` enumerator CU_TENSOR_MAP_IM2COL_WIDE_MODE_W ``

`` enumerator CU_TENSOR_MAP_IM2COL_WIDE_MODE_W128 ``

`` enum CUtensorMapInterleave ``

Tensor map interleave layout type.

_Values:_

`` enumerator CU_TENSOR_MAP_INTERLEAVE_NONE ``

`` enumerator CU_TENSOR_MAP_INTERLEAVE_16B ``

`` enumerator CU_TENSOR_MAP_INTERLEAVE_32B ``

`` enum CUtensorMapL2promotion ``

Tensor map L2 promotion type.

_Values:_

`` enumerator CU_TENSOR_MAP_L2_PROMOTION_NONE ``

`` enumerator CU_TENSOR_MAP_L2_PROMOTION_L2_64B ``

`` enumerator CU_TENSOR_MAP_L2_PROMOTION_L2_128B ``

`` enumerator CU_TENSOR_MAP_L2_PROMOTION_L2_256B ``

`` enum CUtensorMapSwizzle ``

Tensor map swizzling mode of shared memory banks.

_Values:_

`` enumerator CU_TENSOR_MAP_SWIZZLE_NONE ``

`` enumerator CU_TENSOR_MAP_SWIZZLE_32B ``

`` enumerator CU_TENSOR_MAP_SWIZZLE_64B ``

`` enumerator CU_TENSOR_MAP_SWIZZLE_128B ``

`` enumerator CU_TENSOR_MAP_SWIZZLE_128B_ATOM_32B ``

`` enumerator CU_TENSOR_MAP_SWIZZLE_128B_ATOM_32B_FLIP_8B ``

`` enumerator CU_TENSOR_MAP_SWIZZLE_128B_ATOM_64B ``

`` enum CUuserObjectRetain_flags ``

Flags for retaining user object references for graphs.

_Values:_

`` enumerator CU_GRAPH_USER_OBJECT_MOVE ``

Transfer references from the caller rather than creating new references.

`` enum CUuserObject_flags ``

Flags for user objects for graphs.

_Values:_

`` enumerator CU_USER_OBJECT_NO_DESTRUCTOR_SYNC ``

Indicates the destructor execution is not synchronized by any CUDA handle.

`` enum cl_context_flags ``

NVCL context scheduling flags.

_Values:_

`` enumerator NVCL_CTX_SCHED_AUTO ``

Automatic scheduling.

`` enumerator NVCL_CTX_SCHED_SPIN ``

Set spin as default scheduling.

`` enumerator NVCL_CTX_SCHED_YIELD ``

Set yield as default scheduling.

`` enumerator NVCL_CTX_SCHED_BLOCKING_SYNC ``

Set blocking synchronization as default scheduling.

`` enum cl_event_flags ``

NVCL event scheduling flags.

_Values:_

`` enumerator NVCL_EVENT_SCHED_AUTO ``

Automatic scheduling.

`` enumerator NVCL_EVENT_SCHED_SPIN ``

Set spin as default scheduling.

`` enumerator NVCL_EVENT_SCHED_YIELD ``

Set yield as default scheduling.

`` enumerator NVCL_EVENT_SCHED_BLOCKING_SYNC ``

Set blocking synchronization as default scheduling.

##  6.5.3. Typedefs

`` typedef CUDA_ARRAY3D_DESCRIPTOR_v2 CUDA_ARRAY3D_DESCRIPTOR ``

`` typedef CUDA_ARRAY_DESCRIPTOR_v2 CUDA_ARRAY_DESCRIPTOR ``

`` typedef CUDA_ARRAY_MEMORY_REQUIREMENTS_v1 CUDA_ARRAY_MEMORY_REQUIREMENTS ``

`` typedef CUDA_ARRAY_SPARSE_PROPERTIES_v1 CUDA_ARRAY_SPARSE_PROPERTIES ``

`` typedef CUDA_BATCH_MEM_OP_NODE_PARAMS_v1 CUDA_BATCH_MEM_OP_NODE_PARAMS ``

`` typedef CUDA_EXTERNAL_MEMORY_BUFFER_DESC_v1 CUDA_EXTERNAL_MEMORY_BUFFER_DESC ``

`` typedef CUDA_EXTERNAL_MEMORY_HANDLE_DESC_v1 CUDA_EXTERNAL_MEMORY_HANDLE_DESC ``

`` typedef CUDA_EXTERNAL_MEMORY_MIPMAPPED_ARRAY_DESC_v1 CUDA_EXTERNAL_MEMORY_MIPMAPPED_ARRAY_DESC ``

`` typedef CUDA_EXTERNAL_SEMAPHORE_HANDLE_DESC_v1 CUDA_EXTERNAL_SEMAPHORE_HANDLE_DESC ``

`` typedef CUDA_EXTERNAL_SEMAPHORE_SIGNAL_PARAMS_v1 CUDA_EXTERNAL_SEMAPHORE_SIGNAL_PARAMS ``

`` typedef CUDA_EXTERNAL_SEMAPHORE_WAIT_PARAMS_v1 CUDA_EXTERNAL_SEMAPHORE_WAIT_PARAMS ``

`` typedef CUDA_EXT_SEM_SIGNAL_NODE_PARAMS_v1 CUDA_EXT_SEM_SIGNAL_NODE_PARAMS ``

`` typedef CUDA_EXT_SEM_WAIT_NODE_PARAMS_v1 CUDA_EXT_SEM_WAIT_NODE_PARAMS ``

`` typedef CUDA_HOST_NODE_PARAMS_v1 CUDA_HOST_NODE_PARAMS ``

`` typedef CUDA_KERNEL_NODE_PARAMS_v2 CUDA_KERNEL_NODE_PARAMS ``

`` typedef CUDA_LAUNCH_PARAMS_v1 CUDA_LAUNCH_PARAMS ``

`` typedef CUDA_MEMCPY2D_v2 CUDA_MEMCPY2D ``

`` typedef CUDA_MEMCPY3D_v2 CUDA_MEMCPY3D ``

`` typedef CUDA_MEMCPY3D_BATCH_OP_v1 CUDA_MEMCPY3D_BATCH_OP ``

`` typedef CUDA_MEMCPY3D_PEER_v1 CUDA_MEMCPY3D_PEER ``

`` typedef CUDA_MEMSET_NODE_PARAMS_v1 CUDA_MEMSET_NODE_PARAMS ``

`` typedef CUDA_MEM_ALLOC_NODE_PARAMS_v1 CUDA_MEM_ALLOC_NODE_PARAMS ``

`` typedef CUDA_POINTER_ATTRIBUTE_P2P_TOKENS_v1 CUDA_POINTER_ATTRIBUTE_P2P_TOKENS ``

`` typedef CUDA_RESOURCE_DESC_v1 CUDA_RESOURCE_DESC ``

`` typedef CUDA_RESOURCE_VIEW_DESC_v1 CUDA_RESOURCE_VIEW_DESC ``

`` typedef CUDA_TEXTURE_DESC_v1 CUDA_TEXTURE_DESC ``

`` typedef CUaccessPolicyWindow_v1 CUaccessPolicyWindow ``

Access policy window.

`` typedef struct CUarray_st *CUarray ``

CUDA array.

`` typedef CUarrayMapInfo_v1 CUarrayMapInfo ``

`` typedef void (*CUasyncCallback)(CUasyncNotificationInfo *info, void *userData, CUasyncCallbackHandle callback) ``

CUDA async notification callback.

Param info

Information describing what actions to take as a result of this notification.

Param userData

Pointer to user defined data provided at callback registration.

Param callback

The callback handle associated with this specific callback.

`` typedef struct CUasyncCallbackEntry_st *CUasyncCallbackHandle ``

CUDA async notification callback handle.

`` typedef struct CUIcheckpointOperation_st *CUcheckpointOperationHandle ``

Handle for a CUDA custom storage checkpoint or restore operation awaiting completion.

`` typedef struct CUctx_st *CUcontext ``

A regular context handle.

`` typedef CUdevice_v1 CUdevice ``

CUDA device.

`` typedef int CUdevice_v1 ``

CUDA device.

`` typedef CUdeviceptr_v2 CUdeviceptr ``

CUDA device pointer.

`` typedef unsigned int CUdeviceptr_v2 ``

CUDA device pointer CUdeviceptr is defined as an unsigned integer type whose size matches the size of a pointer on the target platform.

`` typedef CUdevprop_v1 CUdevprop ``

`` typedef CUeglFrame_v1 CUeglFrame ``

`` typedef struct CUeglStreamConnection_st *CUeglStreamConnection ``

CUDA EGLSream Connection.

`` typedef struct CUevent_st *CUevent ``

CUDA event.

`` typedef CUexecAffinityParam_v1 CUexecAffinityParam ``

Execution Affinity Parameters.

`` typedef CUexecAffinitySmCount_v1 CUexecAffinitySmCount ``

`` typedef CUextent3D_v1 CUextent3D ``

`` typedef struct CUextMemory_st *CUexternalMemory ``

CUDA external memory.

`` typedef struct CUextSemaphore_st *CUexternalSemaphore ``

CUDA external semaphore.

`` typedef struct CUfunc_st *CUfunction ``

CUDA function.

`` typedef struct CUgraph_st *CUgraph ``

CUDA graph.

`` typedef cuuint64_t CUgraphConditionalHandle ``

CUDA graph conditional handle.

`` typedef struct CUgraphDeviceUpdatableNode_st *CUgraphDeviceNode ``

CUDA graph device node handle.

`` typedef struct CUgraphExec_st *CUgraphExec ``

CUDA executable graph.

`` typedef CUgraphExecUpdateResultInfo_v1 CUgraphExecUpdateResultInfo ``

`` typedef struct CUgraphNode_st *CUgraphNode ``

CUDA graph node.

`` typedef struct CUgraphicsResource_st *CUgraphicsResource ``

CUDA graphics interop resource.

`` typedef struct CUgreenCtx_st *CUgreenCtx ``

A green context handle. This handle can be used safely from only one CPU thread at a time. Created via cuGreenCtxCreate

`` typedef void (*CUhostFn)(void *userData) ``

CUDA host function.

Param userData

Argument value passed to the function

`` typedef CUipcEventHandle_v1 CUipcEventHandle ``

`` typedef CUipcMemHandle_v1 CUipcMemHandle ``

`` typedef struct CUkern_st *CUkernel ``

CUDA kernel.

`` typedef CUlaunchAttributeID CUkernelNodeAttrID ``

`` typedef CUkernelNodeAttrValue_v1 CUkernelNodeAttrValue ``

`` typedef CUlaunchAttributeValue CUkernelNodeAttrValue_v1 ``

`` typedef struct CUlib_st *CUlibrary ``

CUDA library.

`` typedef struct CUlinkState_st *CUlinkState ``

`` typedef CUmemAccessDesc_v1 CUmemAccessDesc ``

`` typedef CUmemAllocationProp_v1 CUmemAllocationProp ``

`` typedef CUmemFabricHandle_v1 CUmemFabricHandle ``

`` typedef CUmemGenericAllocationHandle_v1 CUmemGenericAllocationHandle ``

`` typedef unsigned long long CUmemGenericAllocationHandle_v1 ``

`` typedef CUmemLocation_v1 CUmemLocation ``

`` typedef CUmemPoolProps_v1 CUmemPoolProps ``

`` typedef CUmemPoolPtrExportData_v1 CUmemPoolPtrExportData ``

`` typedef CUmemcpy3DOperand_v1 CUmemcpy3DOperand ``

`` typedef CUmemcpyAttributes_v1 CUmemcpyAttributes ``

`` typedef struct CUmemPoolHandle_st *CUmemoryPool ``

CUDA memory pool.

`` typedef struct CUmipmappedArray_st *CUmipmappedArray ``

CUDA mipmapped array.

`` typedef struct CUmod_st *CUmodule ``

CUDA module.

`` typedef CUmulticastObjectProp_v1 CUmulticastObjectProp ``

`` typedef size_t (*CUoccupancyB2DSize)(int blockSize) ``

Block size to per-block dynamic shared memory mapping for a certain kernel.

Param blockSize

Block size of the kernel.

Return

The dynamic shared memory needed by a block.

`` typedef CUoffset3D_v1 CUoffset3D ``

`` typedef struct CUstream_st *CUstream ``

CUDA stream.

`` typedef CUlaunchAttributeID CUstreamAttrID ``

`` typedef CUstreamAttrValue_v1 CUstreamAttrValue ``

`` typedef CUlaunchAttributeValue CUstreamAttrValue_v1 ``

`` typedef CUstreamBatchMemOpParams_v1 CUstreamBatchMemOpParams ``

`` typedef void (*CUstreamCallback)(CUstream hStream, CUresult status, void *userData) ``

CUDA stream callback.

Param hStream

The stream the callback was added to, as passed to cuStreamAddCallback. May be NULL.

Param status

CUDA_SUCCESS or any persistent error on the stream.

Param userData

User parameter provided at registration.

`` typedef CUsurfObject_v1 CUsurfObject ``

An opaque value that represents a CUDA surface object.

`` typedef unsigned long long CUsurfObject_v1 ``

An opaque value that represents a CUDA surface object.

`` typedef struct CUsurfref_st *CUsurfref ``

CUDA surface reference.

`` typedef CUtexObject_v1 CUtexObject ``

An opaque value that represents a CUDA texture object.

`` typedef unsigned long long CUtexObject_v1 ``

An opaque value that represents a CUDA texture object.

`` typedef struct CUtexref_st *CUtexref ``

CUDA texture reference.

`` typedef struct CUuserObject_st *CUuserObject ``

CUDA user object for graphs.
