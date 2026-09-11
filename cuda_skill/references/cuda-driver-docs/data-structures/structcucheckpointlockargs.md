<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUcheckpointLockArgs.html

#  7.50. CUcheckpointLockArgs

Defined in cuda.h

`` struct CUcheckpointLockArgs ``

CUDA checkpoint optional lock arguments.

Public Members

`` unsigned int timeoutMs ``

Timeout in milliseconds to attempt to lock the process, 0 indicates no timeout.

`` unsigned int reserved0 ``

Reserved for future use, must be zero.

`` cuuint64_t reserved1[7] ``

Reserved for future use, must be zeroed.
