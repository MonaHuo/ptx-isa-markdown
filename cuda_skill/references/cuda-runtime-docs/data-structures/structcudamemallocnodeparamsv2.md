<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaMemAllocNodeParamsV2.html

#  7.48. cudaMemAllocNodeParamsV2

`` struct cudaMemAllocNodeParamsV2 ``

Memory allocation node parameters.

Public Members

`` size_t accessDescCount ``

in: Number of `accessDescs`s

`` const struct cudaMemAccessDesc *accessDescs ``

in: number of memory access descriptors.

Must not exceed the number of GPUs.

`` size_t bytesize ``

in: size in bytes of the requested allocation

`` void *dptr ``

out: address of the allocation returned by CUDA

`` struct cudaMemPoolProps poolProps ``

in: location where the allocation should reside (specified in ::location).

::handleTypes must be cudaMemHandleTypeNone. IPC is not supported. in: array of memory access descriptors. Used to describe peer GPU access
