<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUctxCreateParams.html

#  7.55. CUctxCreateParams

Defined in cuda.h

`` struct CUctxCreateParams ``

Params for creating CUDA context.

Both execAffinityParams and cigParams cannot be non-NULL at the same time. If both are NULL, the context will be created as a regular CUDA context.

Public Members

`` CUexecAffinityParam *execAffinityParams ``

Array of execution affinity parameters to limit context resources (e.g., SM count).

Only supported Volta+ MPS. Mutually exclusive with cigParams.

`` int numExecAffinityParams ``

Number of elements in execAffinityParams array.

Must be 0 if execAffinityParams is NULL.

`` CUctxCigParam *cigParams ``

CIG (CUDA in Graphics) parameters for sharing data from D3D12/Vulkan graphics clients.

Mutually exclusive with execAffinityParams.
