<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUstreamCigCaptureParams.html

#  7.93. CUstreamCigCaptureParams

Defined in cuda.h

`` struct CUstreamCigCaptureParams ``

Params for capturing CUDA stream to CIG streamCigParams must be non-NULL.

Public Members

`` CUstreamCigParam *streamCigParams ``

CIG (CUDA in Graphics) parameters for sharing command list data from D3D12 graphics clients.
