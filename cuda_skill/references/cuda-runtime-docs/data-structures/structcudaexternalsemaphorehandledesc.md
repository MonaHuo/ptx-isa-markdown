<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaExternalSemaphoreHandleDesc.html

#  7.23. cudaExternalSemaphoreHandleDesc

`` struct cudaExternalSemaphoreHandleDesc ``

External semaphore handle descriptor.

Public Members

`` int fd ``

File descriptor referencing the semaphore object.

Valid when type is one of the following:

  * cudaExternalSemaphoreHandleTypeOpaqueFd

  * cudaExternalSemaphoreHandleTypeTimelineSemaphoreFd

`` unsigned int flags ``

Flags reserved for the future.

Must be zero.

`` void *handle ``

Valid NT handle.

Must be NULL if ‘name’ is non-NULL

`` union cudaExternalSemaphoreHandleDesc::[anonymous] handle ``

`` const void *name ``

Name of a valid synchronization primitive.

Must be NULL if ‘handle’ is non-NULL.

`` const void *nvSciSyncObj ``

Valid NvSciSyncObj.

Must be non NULL

`` unsigned int reserved[16] ``

Must be zero.

`` enum cudaExternalSemaphoreHandleType type ``

Type of the handle.

`` struct cudaExternalSemaphoreHandleDesc::[anonymous]::[anonymous] win32 ``

Win32 handle referencing the semaphore object.

Valid when type is one of the following:

  * cudaExternalSemaphoreHandleTypeOpaqueWin32

  * cudaExternalSemaphoreHandleTypeOpaqueWin32Kmt

  * cudaExternalSemaphoreHandleTypeD3D12Fence

  * cudaExternalSemaphoreHandleTypeD3D11Fence

  * cudaExternalSemaphoreHandleTypeKeyedMutex

  * cudaExternalSemaphoreHandleTypeTimelineSemaphoreWin32 Exactly one of ‘handle’ and ‘name’ must be non-NULL. If type is one of the following: cudaExternalSemaphoreHandleTypeOpaqueWin32Kmt cudaExternalSemaphoreHandleTypeKeyedMutexKmt then ‘name’ must be NULL.
