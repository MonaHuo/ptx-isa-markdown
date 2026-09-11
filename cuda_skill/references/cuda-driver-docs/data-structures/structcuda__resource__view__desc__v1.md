<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__RESOURCE__VIEW__DESC__v1.html

#  7.40. CUDA_RESOURCE_VIEW_DESC_v1

Defined in cuda.h

`` struct CUDA_RESOURCE_VIEW_DESC_v1 ``

Resource view descriptor.

Public Members

`` CUresourceViewFormat format ``

Resource view format.

`` size_t width ``

Width of the resource view.

`` size_t height ``

Height of the resource view.

`` size_t depth ``

Depth of the resource view.

`` unsigned int firstMipmapLevel ``

First defined mipmap level.

`` unsigned int lastMipmapLevel ``

Last defined mipmap level.

`` unsigned int firstLayer ``

First layer index.

`` unsigned int lastLayer ``

Last layer index.

`` unsigned int reserved[16] ``
