<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__LAUNCH__PARAMS__v1.html

#  7.27. CUDA_LAUNCH_PARAMS_v1

Defined in cuda.h

`` struct CUDA_LAUNCH_PARAMS_v1 ``

Kernel launch parameters.

Public Members

`` CUfunction function ``

Kernel to launch.

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

`` void **kernelParams ``

Array of pointers to kernel parameters.
