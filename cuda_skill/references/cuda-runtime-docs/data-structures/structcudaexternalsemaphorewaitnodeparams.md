<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaExternalSemaphoreWaitNodeParams.html

#  7.27. cudaExternalSemaphoreWaitNodeParams

`` struct cudaExternalSemaphoreWaitNodeParams ``

External semaphore wait node parameters.

Public Members

`` cudaExternalSemaphore_t *extSemArray ``

Array of external semaphore handles.

`` unsigned int numExtSems ``

Number of handles and parameters supplied in extSemArray and paramsArray.

`` const struct cudaExternalSemaphoreWaitParams *paramsArray ``

Array of external semaphore wait parameters.
