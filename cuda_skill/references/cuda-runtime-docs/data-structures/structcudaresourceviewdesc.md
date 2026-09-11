<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaResourceViewDesc.html

#  7.67. cudaResourceViewDesc

`` struct cudaResourceViewDesc ``

CUDA resource view descriptor.

Public Members

`` size_t depth ``

Depth of the resource view.

`` unsigned int firstLayer ``

First layer index.

`` unsigned int firstMipmapLevel ``

First defined mipmap level.

`` enum cudaResourceViewFormat format ``

Resource view format.

`` size_t height ``

Height of the resource view.

`` unsigned int lastLayer ``

Last layer index.

`` unsigned int lastMipmapLevel ``

Last defined mipmap level.

`` unsigned int reserved[16] ``

Must be zero.

`` size_t width ``

Width of the resource view.
