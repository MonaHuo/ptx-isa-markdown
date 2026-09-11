<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaMemAccessDesc.html

#  7.46. cudaMemAccessDesc

`` struct cudaMemAccessDesc ``

Memory access descriptor.

Public Members

`` enum cudaMemAccessFlags flags ``

::CUmemProt accessibility flags to set on the request

`` struct cudaMemLocation location ``

Location on which the request is to change it’s accessibility.
