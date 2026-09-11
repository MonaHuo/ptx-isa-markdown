<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__ARRAY__SPARSE__PROPERTIES__v1.html

#  7.4. CUDA_ARRAY_SPARSE_PROPERTIES_v1

Defined in cuda.h

`` struct CUDA_ARRAY_SPARSE_PROPERTIES_v1 ``

CUDA array sparse properties.

Public Members

`` unsigned int width ``

Width of sparse tile in elements.

`` unsigned int height ``

Height of sparse tile in elements.

`` unsigned int depth ``

Depth of sparse tile in elements.

`` struct CUDA_ARRAY_SPARSE_PROPERTIES_v1::[anonymous] tileExtent ``

`` unsigned int miptailFirstLevel ``

First mip level at which the mip tail begins.

`` unsigned long long miptailSize ``

Total size of the mip tail.

`` unsigned int flags ``

Flags will either be zero or CU_ARRAY_SPARSE_PROPERTIES_SINGLE_MIPTAIL.

`` unsigned int reserved[4] ``
