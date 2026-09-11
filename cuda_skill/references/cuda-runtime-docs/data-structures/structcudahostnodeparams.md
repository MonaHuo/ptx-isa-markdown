<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaHostNodeParams.html

#  7.37. cudaHostNodeParams

`` struct cudaHostNodeParams ``

CUDA host node parameters.

Public Members

`` cudaHostFn_t fn ``

The function to call when the node executes.

`` void *userData ``

Argument to pass to the function.
