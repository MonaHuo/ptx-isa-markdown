<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaLaunchConfig__t.html

#  7.44. cudaLaunchConfig_t

`` struct cudaLaunchConfig_t ``

CUDA extensible launch configuration.

Public Members

`` cudaLaunchAttribute *attrs ``

List of attributes; nullable if cudaLaunchConfig_t::numAttrs == 0.

`` dim3 blockDim ``

Block dimensions.

`` size_t dynamicSmemBytes ``

Dynamic shared-memory size per thread block in bytes.

`` dim3 gridDim ``

Grid dimensions.

`` unsigned int numAttrs ``

Number of attributes populated in cudaLaunchConfig_t::attrs.

`` cudaStream_t stream ``

Stream identifier.
