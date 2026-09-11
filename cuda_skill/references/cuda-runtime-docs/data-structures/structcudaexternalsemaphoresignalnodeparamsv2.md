<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaExternalSemaphoreSignalNodeParamsV2.html

#  7.25. cudaExternalSemaphoreSignalNodeParamsV2

`` struct cudaExternalSemaphoreSignalNodeParamsV2 ``

External semaphore signal node parameters.

Public Members

`` cudaExecutionContext_t ctx ``

CUDA Execution Context.

`` cudaExternalSemaphore_t *extSemArray ``

Array of external semaphore handles.

`` unsigned int numExtSems ``

Number of handles and parameters supplied in extSemArray and paramsArray.

`` const struct cudaExternalSemaphoreSignalParams *paramsArray ``

Array of external semaphore signal parameters.
