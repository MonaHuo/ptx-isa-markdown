<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaMemcpyNodeParams.html

#  7.59. cudaMemcpyNodeParams

`` struct cudaMemcpyNodeParams ``

Memcpy node parameters.

Public Members

`` struct cudaMemcpy3DParms copyParams ``

Parameters for the memory copy.

`` cudaExecutionContext_t ctx ``

Context in which to run the memcpy.

If NULL will try to use the current context.

`` int flags ``

Must be zero.

`` int reserved ``

Must be zero.
