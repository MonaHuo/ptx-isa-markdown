<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__EXTERNAL__MEMORY__BUFFER__DESC__v1.html

#  7.11. CUDA_EXTERNAL_MEMORY_BUFFER_DESC_v1

Defined in cuda.h

`` struct CUDA_EXTERNAL_MEMORY_BUFFER_DESC_v1 ``

External memory buffer descriptor.

Public Members

`` unsigned long long offset ``

Offset into the memory object where the buffer’s base is.

`` unsigned long long size ``

Size of the buffer.

`` unsigned int flags ``

Flags reserved for future use.

Must be zero.

`` unsigned int reserved[16] ``
