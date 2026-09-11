<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__MEM__ALLOC__NODE__PARAMS__v2.html

#  7.36. CUDA_MEM_ALLOC_NODE_PARAMS_v2

Defined in cuda.h

`` struct CUDA_MEM_ALLOC_NODE_PARAMS_v2 ``

Memory allocation node parameters.

Public Members

`` CUmemPoolProps poolProps ``

in: location where the allocation should reside (specified in ::location).

::handleTypes must be CU_MEM_HANDLE_TYPE_NONE. IPC is not supported.

`` const CUmemAccessDesc *accessDescs ``

in: array of memory access descriptors.

Used to describe peer GPU access

`` size_t accessDescCount ``

in: number of memory access descriptors.

Must not exceed the number of GPUs.

`` size_t bytesize ``

in: size in bytes of the requested allocation

`` CUdeviceptr dptr ``

out: address of the allocation returned by CUDA
