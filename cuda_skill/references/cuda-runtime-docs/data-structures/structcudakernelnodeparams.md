<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaKernelNodeParams.html

#  7.41. cudaKernelNodeParams

`` struct cudaKernelNodeParams ``

CUDA GPU kernel node parameters.

Public Members

`` dim3 blockDim ``

Block dimensions.

`` void **extra ``

Pointer to kernel arguments in the “extra” format.

`` void *func ``

Kernel to launch.

`` dim3 gridDim ``

Grid dimensions.

`` void **kernelParams ``

Array of pointers to individual kernel arguments.

`` unsigned int sharedMemBytes ``

Dynamic shared-memory size per thread block in bytes.
