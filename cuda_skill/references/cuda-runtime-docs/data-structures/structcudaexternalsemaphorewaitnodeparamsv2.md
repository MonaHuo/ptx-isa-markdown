<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaExternalSemaphoreWaitNodeParamsV2.html

#  7.28. cudaExternalSemaphoreWaitNodeParamsV2

`` struct cudaExternalSemaphoreWaitNodeParamsV2 ``

External semaphore wait node parameters.

Public Members

`` cudaExecutionContext_t ctx ``

CUDA Execution Context.

`` cudaExternalSemaphore_t *extSemArray ``

Array of external semaphore handles.

`` unsigned int numExtSems ``

Number of handles and parameters supplied in extSemArray and paramsArray.

`` const struct cudaExternalSemaphoreWaitParams *paramsArray ``

Array of external semaphore wait parameters.
