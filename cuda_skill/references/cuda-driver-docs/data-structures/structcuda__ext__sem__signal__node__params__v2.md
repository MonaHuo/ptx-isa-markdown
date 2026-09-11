<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__EXT__SEM__SIGNAL__NODE__PARAMS__v2.html

#  7.18. CUDA_EXT_SEM_SIGNAL_NODE_PARAMS_v2

Defined in cuda.h

`` struct CUDA_EXT_SEM_SIGNAL_NODE_PARAMS_v2 ``

Semaphore signal node parameters.

Public Members

`` CUexternalSemaphore *extSemArray ``

Array of external semaphore handles.

`` const CUDA_EXTERNAL_SEMAPHORE_SIGNAL_PARAMS *paramsArray ``

Array of external semaphore signal parameters.

`` unsigned int numExtSems ``

Number of handles and parameters supplied in extSemArray and paramsArray.

`` CUcontext ctx ``

`` CUgreenCtx gCtx ``

`` union CUDA_EXT_SEM_SIGNAL_NODE_PARAMS_v2::[anonymous] [anonymous] ``
