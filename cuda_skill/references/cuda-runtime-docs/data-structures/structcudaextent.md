<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaExtent.html

#  7.19. cudaExtent

`` struct cudaExtent ``

CUDA extent.

See also

make_cudaExtent

Public Members

`` size_t depth ``

Depth in elements.

`` size_t height ``

Height in elements.

`` size_t width ``

Width in elements when referring to array memory, in bytes when referring to linear memory.
