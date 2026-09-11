<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUmemAccessDesc__v1.html

#  7.77. CUmemAccessDesc_v1

Defined in cuda.h

`` struct CUmemAccessDesc_v1 ``

Memory access descriptor.

Public Members

`` CUmemLocation location ``

Location on which the request is to change it’s accessibility.

`` CUmemAccess_flags flags ``

::CUmemProt accessibility flags to set on the request
