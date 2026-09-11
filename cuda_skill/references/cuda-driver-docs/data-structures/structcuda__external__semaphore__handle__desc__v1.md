<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__EXTERNAL__SEMAPHORE__HANDLE__DESC__v1.html

#  7.14. CUDA_EXTERNAL_SEMAPHORE_HANDLE_DESC_v1

Defined in cuda.h

`` struct CUDA_EXTERNAL_SEMAPHORE_HANDLE_DESC_v1 ``

External semaphore handle descriptor.

Public Members

`` CUexternalSemaphoreHandleType type ``

Type of the handle.

`` int fd ``

File descriptor referencing the semaphore object.

Valid when type is one of the following:

  * CU_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_FD

  * CU_EXTERNAL_SEMAPHORE_HANDLE_TYPE_TIMELINE_SEMAPHORE_FD

`` void *handle ``

Valid NT handle.

Must be NULL if ‘name’ is non-NULL

`` const void *name ``

Name of a valid synchronization primitive.

Must be NULL if ‘handle’ is non-NULL.

`` struct CUDA_EXTERNAL_SEMAPHORE_HANDLE_DESC_v1::[anonymous]::[anonymous] win32 ``

Win32 handle referencing the semaphore object.

Valid when type is one of the following:

  * CU_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_WIN32

  * CU_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_WIN32_KMT

  * CU_EXTERNAL_SEMAPHORE_HANDLE_TYPE_D3D12_FENCE

  * CU_EXTERNAL_SEMAPHORE_HANDLE_TYPE_D3D11_FENCE

  * CU_EXTERNAL_SEMAPHORE_HANDLE_TYPE_D3D11_KEYED_MUTEX

  * CU_EXTERNAL_SEMAPHORE_HANDLE_TYPE_TIMELINE_SEMAPHORE_WIN32 Exactly one of ‘handle’ and ‘name’ must be non-NULL. If type is one of the following:

  * CU_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_WIN32_KMT

  * CU_EXTERNAL_SEMAPHORE_HANDLE_TYPE_D3D11_KEYED_MUTEX_KMT then ‘name’ must be NULL.

`` const void *nvSciSyncObj ``

Valid NvSciSyncObj.

Must be non NULL

`` union CUDA_EXTERNAL_SEMAPHORE_HANDLE_DESC_v1::[anonymous] handle ``

`` unsigned int flags ``

Flags reserved for the future.

Must be zero.

`` unsigned int reserved[16] ``
