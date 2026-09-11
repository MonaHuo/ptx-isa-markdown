<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__EXTERNAL__SEMAPHORE__WAIT__PARAMS__v1.html

#  7.16. CUDA_EXTERNAL_SEMAPHORE_WAIT_PARAMS_v1

Defined in cuda.h

`` struct CUDA_EXTERNAL_SEMAPHORE_WAIT_PARAMS_v1 ``

External semaphore wait parameters.

Public Members

`` unsigned long long value ``

Value of fence to be waited on.

`` struct CUDA_EXTERNAL_SEMAPHORE_WAIT_PARAMS_v1::[anonymous]::[anonymous] fence ``

Parameters for fence objects.

`` void *fence ``

`` unsigned long long reserved ``

`` union CUDA_EXTERNAL_SEMAPHORE_WAIT_PARAMS_v1::[anonymous]::[anonymous] nvSciSync ``

Pointer to NvSciSyncFence.

Valid if CUexternalSemaphoreHandleType is of type CU_EXTERNAL_SEMAPHORE_HANDLE_TYPE_NVSCISYNC.

`` unsigned long long key ``

Value of key to acquire the mutex with.

`` unsigned int timeoutMs ``

Timeout in milliseconds to wait to acquire the mutex.

`` struct CUDA_EXTERNAL_SEMAPHORE_WAIT_PARAMS_v1::[anonymous]::[anonymous] keyedMutex ``

Parameters for keyed mutex objects.

`` unsigned int reserved[10] ``

`` struct CUDA_EXTERNAL_SEMAPHORE_WAIT_PARAMS_v1::[anonymous] params ``

`` unsigned int flags ``

Only when CUDA_EXTERNAL_SEMAPHORE_WAIT_PARAMS is used to wait on a CUexternalSemaphore of type CU_EXTERNAL_SEMAPHORE_HANDLE_TYPE_NVSCISYNC, the valid flag is CUDA_EXTERNAL_SEMAPHORE_WAIT_SKIP_NVSCIBUF_MEMSYNC which indicates that while waiting for the CUexternalSemaphore, no memory synchronization operations should be performed for any external memory object imported as CU_EXTERNAL_MEMORY_HANDLE_TYPE_NVSCIBUF.

For all other types of CUexternalSemaphore, flags must be zero.
