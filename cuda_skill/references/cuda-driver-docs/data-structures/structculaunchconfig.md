<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUlaunchConfig.html

#  7.72. CUlaunchConfig

Defined in cuda.h

`` struct CUlaunchConfig ``

CUDA extensible launch configuration.

Public Members

`` unsigned int gridDimX ``

Width of grid in blocks.

`` unsigned int gridDimY ``

Height of grid in blocks.

`` unsigned int gridDimZ ``

Depth of grid in blocks.

`` unsigned int blockDimX ``

X dimension of each thread block.

`` unsigned int blockDimY ``

Y dimension of each thread block.

`` unsigned int blockDimZ ``

Z dimension of each thread block.

`` unsigned int sharedMemBytes ``

Dynamic shared-memory size per thread block in bytes.

`` CUstream hStream ``

Stream identifier.

`` CUlaunchAttribute *attrs ``

List of attributes; nullable if CUlaunchConfig::numAttrs == 0.

`` unsigned int numAttrs ``

Number of attributes populated in CUlaunchConfig::attrs.
