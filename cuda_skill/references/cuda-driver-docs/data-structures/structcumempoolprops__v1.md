<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUmemPoolProps__v1.html

#  7.82. CUmemPoolProps_v1

Defined in cuda.h

`` struct CUmemPoolProps_v1 ``

Specifies the properties of allocations made from the pool.

Public Members

`` CUmemAllocationType allocType ``

Allocation type.

Currently must be specified as CU_MEM_ALLOCATION_TYPE_PINNED

`` CUmemAllocationHandleType handleTypes ``

Handle types that will be supported by allocations from the pool.

`` CUmemLocation location ``

Location where allocations should reside.

`` void *win32SecurityAttributes ``

Windows-specific LPSECURITYATTRIBUTES required when CU_MEM_HANDLE_TYPE_WIN32 is specified.

This security attribute defines the scope of which exported allocations may be transferred to other processes. In all other cases, this field is required to be zero.

`` size_t maxSize ``

Maximum pool size.

When set to 0, defaults to a system dependent value.

`` unsigned short usage ``

Bitmask indicating intended usage for the pool.

`` unsigned char gpuDirectRDMACapable ``

Allocation hint for requesting GPUDirect RDMA capable memory.

On devices that support GPUDirect RDMA, this flag indicates that the memory will be used for GPUDirect RDMA. On platforms where the default RDMA path does not support localized allocations, this flag has the following effects:

  * For MPS clients using MLOPart/locality domains, this flag has the effect of disabling localization for the pool. This allows the pool to be used for GPUDirect RDMA with the default RDMA path.

  * For pools that are localized using CUDA locality domain APIs, using this flag will have no effect, but attempting to export the localized memory without forcing PCIe will return an error. To use GPUDirect RDMA with localized pools on platforms where the default RDMA path does not support localized allocations, handles must be acquired with the flag CU_MEM_RANGE_FLAG_DMA_BUF_MAPPING_TYPE_PCIE. Note that CUDA memory pools are only compatible with dma_buf mappings.

`` unsigned char reserved[53] ``

reserved for future use, must be 0
