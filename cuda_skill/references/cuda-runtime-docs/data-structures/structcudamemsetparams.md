<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaMemsetParams.html

#  7.60. cudaMemsetParams

`` struct cudaMemsetParams ``

CUDA Memset node parameters.

Public Members

`` void *dst ``

Destination device pointer.

`` unsigned int elementSize ``

Size of each element in bytes.

Must be 1, 2, or 4.

`` size_t height ``

Number of rows.

`` size_t pitch ``

Pitch of destination device pointer.

Unused if height is 1

`` unsigned int value ``

Value to be set.

`` size_t width ``

Width of the row in elements.
