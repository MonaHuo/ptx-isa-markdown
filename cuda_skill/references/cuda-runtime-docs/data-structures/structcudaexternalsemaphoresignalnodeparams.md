<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaExternalSemaphoreSignalNodeParams.html

#  7.24. cudaExternalSemaphoreSignalNodeParams

`` struct cudaExternalSemaphoreSignalNodeParams ``

External semaphore signal node parameters.

Public Members

`` cudaExternalSemaphore_t *extSemArray ``

Array of external semaphore handles.

`` unsigned int numExtSems ``

Number of handles and parameters supplied in extSemArray and paramsArray.

`` const struct cudaExternalSemaphoreSignalParams *paramsArray ``

Array of external semaphore signal parameters.
