<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUcheckpointGpuPair.html

#  7.49. CUcheckpointGpuPair

Defined in cuda.h

`` struct CUcheckpointGpuPair ``

CUDA checkpoint GPU UUID pairs for device remapping during restore.

Public Members

`` CUuuid oldUuid ``

UUID of the GPU that was checkpointed.

`` CUuuid newUuid ``

UUID of the GPU to restore onto.
