<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaPitchedPtr.html

#  7.63. cudaPitchedPtr

`` struct cudaPitchedPtr ``

CUDA Pitched memory pointer.

See also

make_cudaPitchedPtr

Public Members

`` size_t pitch ``

Pitch of allocated memory in bytes.

`` void *ptr ``

Pointer to allocated memory.

`` size_t xsize ``

Logical width of allocation in elements.

`` size_t ysize ``

Logical height of allocation in elements.
