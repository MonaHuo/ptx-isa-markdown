<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__EXTERNAL__MEMORY__HANDLE__DESC__v1.html

#  7.12. CUDA_EXTERNAL_MEMORY_HANDLE_DESC_v1

Defined in cuda.h

`` struct CUDA_EXTERNAL_MEMORY_HANDLE_DESC_v1 ``

External memory handle descriptor.

Public Members

`` CUexternalMemoryHandleType type ``

Type of the handle.

`` int fd ``

File descriptor referencing the memory object.

Valid when type is CU_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_FD

`` void *handle ``

Valid NT handle.

Must be NULL if ‘name’ is non-NULL

`` const void *name ``

Name of a valid memory object.

Must be NULL if ‘handle’ is non-NULL.

`` struct CUDA_EXTERNAL_MEMORY_HANDLE_DESC_v1::[anonymous]::[anonymous] win32 ``

Win32 handle referencing the semaphore object.

Valid when type is one of the following:

  * CU_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32

  * CU_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_KMT

  * CU_EXTERNAL_MEMORY_HANDLE_TYPE_D3D12_HEAP

  * CU_EXTERNAL_MEMORY_HANDLE_TYPE_D3D12_RESOURCE

  * CU_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_RESOURCE

  * CU_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_RESOURCE_KMT Exactly one of ‘handle’ and ‘name’ must be non-NULL. If type is one of the following: CU_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_KMT CU_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_RESOURCE_KMT then ‘name’ must be NULL.

`` const void *nvSciBufObject ``

A handle representing an NvSciBuf Object.

Valid when type is CU_EXTERNAL_MEMORY_HANDLE_TYPE_NVSCIBUF

`` union CUDA_EXTERNAL_MEMORY_HANDLE_DESC_v1::[anonymous] handle ``

`` unsigned long long size ``

Size of the memory allocation.

`` unsigned int flags ``

Flags must either be zero or CUDA_EXTERNAL_MEMORY_DEDICATED.

`` unsigned int reserved[16] ``
