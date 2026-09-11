<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__EXTERNAL__MEMORY__MIPMAPPED__ARRAY__DESC__v1.html

#  7.13. CUDA_EXTERNAL_MEMORY_MIPMAPPED_ARRAY_DESC_v1

Defined in cuda.h

`` struct CUDA_EXTERNAL_MEMORY_MIPMAPPED_ARRAY_DESC_v1 ``

External memory mipmap descriptor.

Public Members

`` unsigned long long offset ``

Offset into the memory object where the base level of the mipmap chain is.

`` CUDA_ARRAY3D_DESCRIPTOR arrayDesc ``

Format, dimension and type of base level of the mipmap chain.

`` unsigned int numLevels ``

Total number of levels in the mipmap chain.

`` unsigned int reserved[16] ``
