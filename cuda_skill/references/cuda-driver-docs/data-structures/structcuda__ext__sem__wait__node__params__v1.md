<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__EXT__SEM__WAIT__NODE__PARAMS__v1.html

#  7.19. CUDA_EXT_SEM_WAIT_NODE_PARAMS_v1

Defined in cuda.h

`` struct CUDA_EXT_SEM_WAIT_NODE_PARAMS_v1 ``

Semaphore wait node parameters.

Public Members

`` CUexternalSemaphore *extSemArray ``

Array of external semaphore handles.

`` const CUDA_EXTERNAL_SEMAPHORE_WAIT_PARAMS *paramsArray ``

Array of external semaphore wait parameters.

`` unsigned int numExtSems ``

Number of handles and parameters supplied in extSemArray and paramsArray.
