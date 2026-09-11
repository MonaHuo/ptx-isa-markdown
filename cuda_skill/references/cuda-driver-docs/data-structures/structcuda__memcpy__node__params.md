<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__MEMCPY__NODE__PARAMS.html

#  7.32. CUDA_MEMCPY_NODE_PARAMS

Defined in cuda.h

`` struct CUDA_MEMCPY_NODE_PARAMS ``

Memcpy node parameters.

Public Members

`` int flags ``

Must be zero.

`` int reserved ``

Must be zero.

`` CUcontext copyCtx ``

Context on which to run the node.

`` CUDA_MEMCPY3D copyParams ``

Parameters for the memory copy.
