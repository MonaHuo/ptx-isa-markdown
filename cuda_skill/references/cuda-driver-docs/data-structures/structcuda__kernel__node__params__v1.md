<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__KERNEL__NODE__PARAMS__v1.html

#  7.24. CUDA_KERNEL_NODE_PARAMS_v1

Defined in cuda.h

`` struct CUDA_KERNEL_NODE_PARAMS_v1 ``

GPU kernel node parameters.

Public Members

`` CUfunction func ``

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

`` void **kernelParams ``

Array of pointers to kernel parameters.

`` void **extra ``

Extra options.
