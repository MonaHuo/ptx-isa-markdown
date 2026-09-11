<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUcheckpointCheckpointArgs.html

#  7.46. CUcheckpointCheckpointArgs

Defined in cuda.h

`` struct CUcheckpointCheckpointArgs ``

CUDA checkpoint optional checkpoint arguments.

Public Members

`` CUcheckpointCustomStorageInfo **customStorageInfo_out ``

Optional custom storage; if NULL, GPU memory is checkpointed to host.

`` char reserved[64 - sizeof(CUcheckpointCustomStorageInfo*)] ``

Reserved for future use, must be zeroed.
