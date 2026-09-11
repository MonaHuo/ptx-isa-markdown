<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaExternalSemaphoreWaitParams.html

#  7.29. cudaExternalSemaphoreWaitParams

`` struct cudaExternalSemaphoreWaitParams ``

External semaphore wait parameters, compatible with driver type.

Public Members

`` struct cudaExternalSemaphoreWaitParams::[anonymous]::[anonymous] fence ``

Parameters for fence objects.

`` void *fence ``

Pointer to NvSciSyncFence.

Valid if cudaExternalSemaphoreHandleType is of type cudaExternalSemaphoreHandleTypeNvSciSync.

`` unsigned int flags ``

Only when cudaExternalSemaphoreSignalParams is used to signal a cudaExternalSemaphore_t of type cudaExternalSemaphoreHandleTypeNvSciSync, the valid flag is cudaExternalSemaphoreSignalSkipNvSciBufMemSync: which indicates that while waiting for the cudaExternalSemaphore_t, no memory synchronization operations should be performed for any external memory object imported as cudaExternalMemoryHandleTypeNvSciBuf.

For all other types of cudaExternalSemaphore_t, flags must be zero.

`` unsigned long long key ``

Value of key to acquire the mutex with.

`` struct cudaExternalSemaphoreWaitParams::[anonymous]::[anonymous] keyedMutex ``

Parameters for keyed mutex objects.

`` union cudaExternalSemaphoreWaitParams::[anonymous]::[anonymous] nvSciSync ``

`` struct cudaExternalSemaphoreWaitParams::[anonymous] params ``

`` unsigned long long reserved ``

`` unsigned int reserved[10] ``

`` unsigned int timeoutMs ``

Timeout in milliseconds to wait to acquire the mutex.

`` unsigned long long value ``

Value of fence to be waited on.
