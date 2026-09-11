<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__ARRAY3D__DESCRIPTOR__v2.html

#  7.1. CUDA_ARRAY3D_DESCRIPTOR_v2

Defined in cuda.h

`` struct CUDA_ARRAY3D_DESCRIPTOR_v2 ``

3D array descriptor

Public Members

`` size_t Width ``

Width of 3D array.

`` size_t Height ``

Height of 3D array.

`` size_t Depth ``

Depth of 3D array.

`` CUarray_format Format ``

Array format.

`` unsigned int NumChannels ``

Channels per array element.

`` unsigned int Flags ``

Flags.
