<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaExternalMemoryHandleDesc.html

#  7.21. cudaExternalMemoryHandleDesc

`` struct cudaExternalMemoryHandleDesc ``

External memory handle descriptor.

Public Members

`` int fd ``

File descriptor referencing the memory object.

Valid when type is cudaExternalMemoryHandleTypeOpaqueFd

`` unsigned int flags ``

Flags must either be zero or cudaExternalMemoryDedicated.

`` void *handle ``

Valid NT handle.

Must be NULL if ‘name’ is non-NULL

`` union cudaExternalMemoryHandleDesc::[anonymous] handle ``

`` const void *name ``

Name of a valid memory object.

Must be NULL if ‘handle’ is non-NULL.

`` const void *nvSciBufObject ``

A handle representing NvSciBuf Object.

Valid when type is cudaExternalMemoryHandleTypeNvSciBuf

`` unsigned int reserved[16] ``

Must be zero.

`` unsigned long long size ``

Size of the memory allocation.

`` enum cudaExternalMemoryHandleType type ``

Type of the handle.

`` struct cudaExternalMemoryHandleDesc::[anonymous]::[anonymous] win32 ``

Win32 handle referencing the semaphore object.

Valid when type is one of the following:

  * cudaExternalMemoryHandleTypeOpaqueWin32

  * cudaExternalMemoryHandleTypeOpaqueWin32Kmt

  * cudaExternalMemoryHandleTypeD3D12Heap

  * cudaExternalMemoryHandleTypeD3D12Resource

  * cudaExternalMemoryHandleTypeD3D11Resource

  * cudaExternalMemoryHandleTypeD3D11ResourceKmt Exactly one of ‘handle’ and ‘name’ must be non-NULL. If type is one of the following: cudaExternalMemoryHandleTypeOpaqueWin32Kmt cudaExternalMemoryHandleTypeD3D11ResourceKmt then ‘name’ must be NULL.
