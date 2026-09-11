<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaKernelNodeParamsV2.html

#  7.42. cudaKernelNodeParamsV2

`` struct cudaKernelNodeParamsV2 ``

CUDA GPU kernel node parameters.

Public Members

`` union cudaKernelNodeParamsV2::[anonymous] [anonymous] ``

`` uint3 blockDim ``

Block dimensions.

`` cudaExecutionContext_t ctx ``

Context in which to run the kernel.

If NULL will try to use the current context.

`` cudaFunction_t cuFunc ``

functionType = cudaKernelFucntionTypeFunction

`` void **extra ``

Pointer to kernel arguments in the “extra” format.

`` void *func ``

functionType = cudaKernelFucntionTypeDevice

`` enum cudaKernelFunctionType functionType ``

Type of handle passed in the func/kern/cuFunc union above.

`` uint3 gridDim ``

Grid dimensions.

`` cudaKernel_t kern ``

functionType = cudaKernelFucntionTypeKernel

`` void **kernelParams ``

Array of pointers to individual kernel arguments.

`` unsigned int sharedMemBytes ``

Dynamic shared-memory size per thread block in bytes.
