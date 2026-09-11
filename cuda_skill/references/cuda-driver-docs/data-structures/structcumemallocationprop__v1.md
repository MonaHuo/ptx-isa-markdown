<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUmemAllocationProp__v1.html

#  7.78. CUmemAllocationProp_v1

Defined in cuda.h

`` struct CUmemAllocationProp_v1 ``

Specifies the allocation properties for a allocation.

Public Members

`` CUmemAllocationType type ``

Allocation type.

`` CUmemAllocationHandleType requestedHandleTypes ``

requested CUmemAllocationHandleType

`` CUmemLocation location ``

Location of allocation.

`` void *win32HandleMetaData ``

Windows-specific POBJECT_ATTRIBUTES required when CU_MEM_HANDLE_TYPE_WIN32 is specified.

This object attributes structure includes security attributes that define the scope of which exported allocations may be transferred to other processes. In all other cases, this field is required to be zero.

`` unsigned char compressionType ``

Allocation hint for requesting compressible memory.

On devices that support Compute Data Compression, compressible memory can be used to accelerate accesses to data with unstructured sparsity and other compressible data patterns. Applications are expected to query allocation property of the handle obtained with cuMemCreate using cuMemGetAllocationPropertiesFromHandle to validate if the obtained allocation is compressible or not. Note that compressed memory may not be mappable on all devices.

`` unsigned char gpuDirectRDMACapable ``

Allocation hint for requesting GPUDirect RDMA capable memory.

On devices with attribute CU_DEVICE_ATTRIBUTE_GPU_DIRECT_RDMA_WITH_CUDA_VMM_SUPPORTED set, this flag indicates that the memory will be used for GPUDirect RDMA. On platforms where the default RDMA path does not support localized allocations, this flag has the following effects:

  * For MPS clients using MLOPart/locality domains, this flag has the effect of disabling localization for the allocation. This allows the allocation to be used for GPUDirect RDMA with the default RDMA path.

  * For allocations that are localized using CUDA locality domain APIs, using this flag will return an error. To use GPUDirect RDMA with localized allocations on platforms where the default RDMA path does not support localized allocations, allocations must explicitly opt-in to using the PCIe (BAR1) path by setting the flag CU_MEM_CREATE_USAGE_GPU_DIRECT_RDMA_OVER_PCIE.

`` unsigned short usage ``

Bitmask indicating intended usage for this allocation.

`` unsigned char reserved[4] ``

`` struct CUmemAllocationProp_v1::[anonymous] allocFlags ``
