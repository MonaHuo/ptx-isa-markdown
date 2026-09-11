<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__EXTERNAL__SEMAPHORE__SIGNAL__PARAMS__v1.html

#  7.15. CUDA_EXTERNAL_SEMAPHORE_SIGNAL_PARAMS_v1

Defined in cuda.h

`` struct CUDA_EXTERNAL_SEMAPHORE_SIGNAL_PARAMS_v1 ``

External semaphore signal parameters.

Public Members

`` unsigned long long value ``

Value of fence to be signaled.

`` struct CUDA_EXTERNAL_SEMAPHORE_SIGNAL_PARAMS_v1::[anonymous]::[anonymous] fence ``

Parameters for fence objects.

`` void *fence ``

Pointer to NvSciSyncFence.

Valid if CUexternalSemaphoreHandleType is of type CU_EXTERNAL_SEMAPHORE_HANDLE_TYPE_NVSCISYNC.

`` unsigned long long reserved ``

`` union CUDA_EXTERNAL_SEMAPHORE_SIGNAL_PARAMS_v1::[anonymous]::[anonymous] nvSciSync ``

`` unsigned long long key ``

Value of key to release the mutex with.

`` struct CUDA_EXTERNAL_SEMAPHORE_SIGNAL_PARAMS_v1::[anonymous]::[anonymous] keyedMutex ``

Parameters for keyed mutex objects.

`` unsigned int reserved[12] ``

`` struct CUDA_EXTERNAL_SEMAPHORE_SIGNAL_PARAMS_v1::[anonymous] params ``

`` unsigned int flags ``

Only when CUDA_EXTERNAL_SEMAPHORE_SIGNAL_PARAMS is used to signal a CUexternalSemaphore of type CU_EXTERNAL_SEMAPHORE_HANDLE_TYPE_NVSCISYNC, the valid flag is CUDA_EXTERNAL_SEMAPHORE_SIGNAL_SKIP_NVSCIBUF_MEMSYNC which indicates that while signaling the CUexternalSemaphore, no memory synchronization operations should be performed for any external memory object imported as CU_EXTERNAL_MEMORY_HANDLE_TYPE_NVSCIBUF.

For all other types of CUexternalSemaphore, flags must be zero.
