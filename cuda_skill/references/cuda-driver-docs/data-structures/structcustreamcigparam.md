<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUstreamCigParam.html

#  7.94. CUstreamCigParam

Defined in cuda.h

`` struct CUstreamCigParam ``

CIG Stream Capture Params.

Public Members

`` CUstreamCigDataType streamSharedDataType ``

Type of shared data from graphics client (D3D12).

`` void *streamSharedData ``

Graphics client data handle (ID3D12CommandList/ID3D12GraphicsCommandList).
