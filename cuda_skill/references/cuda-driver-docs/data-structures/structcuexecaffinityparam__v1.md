<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUexecAffinityParam__v1.html

#  7.63. CUexecAffinityParam_v1

Defined in cuda.h

`` struct CUexecAffinityParam_v1 ``

Execution Affinity Parameters.

Public Members

`` CUexecAffinityType type ``

Type of execution affinity.

`` CUexecAffinitySmCount smCount ``

Value for CU_EXEC_AFFINITY_TYPE_SM_COUNT.

`` union CUexecAffinityParam_v1::[anonymous] param ``
