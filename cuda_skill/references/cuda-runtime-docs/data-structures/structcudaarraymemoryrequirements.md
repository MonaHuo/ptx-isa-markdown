<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaArrayMemoryRequirements.html

#  7.3. cudaArrayMemoryRequirements

`` struct cudaArrayMemoryRequirements ``

CUDA array and CUDA mipmapped array memory requirements.

Public Members

`` size_t alignment ``

Alignment necessary for mapping the array.

`` unsigned int reserved[4] ``

`` size_t size ``

Total size of the array.
