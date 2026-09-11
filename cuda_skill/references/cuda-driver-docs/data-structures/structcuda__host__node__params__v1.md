<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__HOST__NODE__PARAMS__v1.html

#  7.22. CUDA_HOST_NODE_PARAMS_v1

Defined in cuda.h

`` struct CUDA_HOST_NODE_PARAMS_v1 ``

Host node parameters.

Public Members

`` CUhostFn fn ``

The function to call when the node executes.

`` void *userData ``

Argument to pass to the function.
