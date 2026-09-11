<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaExternalSemaphoreSignalParams.html

#  7.26. cudaExternalSemaphoreSignalParams

`` struct cudaExternalSemaphoreSignalParams ``

External semaphore signal parameters, compatible with driver type.

Public Members

`` struct cudaExternalSemaphoreSignalParams::[anonymous]::[anonymous] fence ``

Parameters for fence objects.

`` void *fence ``

Pointer to NvSciSyncFence.

Valid if cudaExternalSemaphoreHandleType is of type cudaExternalSemaphoreHandleTypeNvSciSync.

`` unsigned int flags ``

Only when cudaExternalSemaphoreSignalParams is used to signal a cudaExternalSemaphore_t of type cudaExternalSemaphoreHandleTypeNvSciSync, the valid flag is cudaExternalSemaphoreSignalSkipNvSciBufMemSync: which indicates that while signaling the cudaExternalSemaphore_t, no memory synchronization operations should be performed for any external memory object imported as cudaExternalMemoryHandleTypeNvSciBuf.

For all other types of cudaExternalSemaphore_t, flags must be zero.

`` unsigned long long key ``

`` struct cudaExternalSemaphoreSignalParams::[anonymous]::[anonymous] keyedMutex ``

Parameters for keyed mutex objects.

`` union cudaExternalSemaphoreSignalParams::[anonymous]::[anonymous] nvSciSync ``

`` struct cudaExternalSemaphoreSignalParams::[anonymous] params ``

`` unsigned long long reserved ``

`` unsigned int reserved[12] ``

`` unsigned long long value ``

Value of fence to be signaled.
