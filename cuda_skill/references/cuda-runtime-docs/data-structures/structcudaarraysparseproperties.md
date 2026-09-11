<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaArraySparseProperties.html

#  7.4. cudaArraySparseProperties

`` struct cudaArraySparseProperties ``

Sparse CUDA array and CUDA mipmapped array properties.

Public Members

`` unsigned int depth ``

Tile depth in elements.

`` unsigned int flags ``

Flags will either be zero or cudaArraySparsePropertiesSingleMipTail.

`` unsigned int height ``

Tile height in elements.

`` unsigned int miptailFirstLevel ``

First mip level at which the mip tail begins.

`` unsigned long long miptailSize ``

Total size of the mip tail.

`` unsigned int reserved[4] ``

`` struct cudaArraySparseProperties::[anonymous] tileExtent ``

`` unsigned int width ``

Tile width in elements.
