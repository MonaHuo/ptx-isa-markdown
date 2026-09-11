<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUdevprop__v1.html

#  7.61. CUdevprop_v1

Defined in cuda.h

`` struct CUdevprop_v1 ``

Legacy device properties.

Public Members

`` int maxThreadsPerBlock ``

Maximum number of threads per block.

`` int maxThreadsDim[3] ``

Maximum size of each dimension of a block.

`` int maxGridSize[3] ``

Maximum size of each dimension of a grid.

`` int sharedMemPerBlock ``

Shared memory available per block in bytes.

`` int totalConstantMemory ``

Constant memory available on device in bytes.

`` int SIMDWidth ``

Warp size in threads.

`` int memPitch ``

Maximum pitch in bytes allowed by memory copies.

`` int regsPerBlock ``

32-bit registers available per block

`` int clockRate ``

Clock frequency in kilohertz.

`` int textureAlign ``

Alignment requirement for textures.
