<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__MEMSET__NODE__PARAMS__v1.html

#  7.33. CUDA_MEMSET_NODE_PARAMS_v1

Defined in cuda.h

`` struct CUDA_MEMSET_NODE_PARAMS_v1 ``

Memset node parameters.

Public Members

`` CUdeviceptr dst ``

Destination device pointer.

`` size_t pitch ``

Pitch of destination device pointer.

Unused if height is 1

`` unsigned int value ``

Value to be set.

`` unsigned int elementSize ``

Size of each element in bytes.

Must be 1, 2, or 4.

`` size_t width ``

Width of the row in elements.

`` size_t height ``

Number of rows.
