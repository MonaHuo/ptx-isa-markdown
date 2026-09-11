<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUctxCigParam.html

#  7.54. CUctxCigParam

Defined in cuda.h

`` struct CUctxCigParam ``

CIG Context Create Params.

Public Members

`` CUcigDataType sharedDataType ``

Type of shared data from graphics client (D3D12 or Vulkan).

`` void *sharedData ``

Graphics client data handle (ID3D12CommandQueue or Nvidia specific data blob).
