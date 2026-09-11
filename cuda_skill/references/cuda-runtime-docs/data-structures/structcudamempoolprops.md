<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaMemPoolProps.html

#  7.52. cudaMemPoolProps

`` struct cudaMemPoolProps ``

Specifies the properties of allocations made from the pool.

Public Members

`` enum cudaMemAllocationType allocType ``

Allocation type.

Currently must be specified as cudaMemAllocationTypePinned

`` enum cudaMemAllocationHandleType handleTypes ``

Handle types that will be supported by allocations from the pool.

`` struct cudaMemLocation location ``

Location allocations should reside.

`` size_t maxSize ``

Maximum pool size.

When set to 0, defaults to a system dependent value.

`` unsigned char reserved[54] ``

reserved for future use, must be 0

`` unsigned short usage ``

Bitmask indicating intended usage for the pool.

`` void *win32SecurityAttributes ``

Windows-specific LPSECURITYATTRIBUTES required when cudaMemHandleTypeWin32 is specified.

This security attribute defines the scope of which exported allocations may be tranferred to other processes. In all other cases, this field is required to be zero.
