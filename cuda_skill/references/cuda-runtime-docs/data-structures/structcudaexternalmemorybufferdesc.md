<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaExternalMemoryBufferDesc.html

#  7.20. cudaExternalMemoryBufferDesc

`` struct cudaExternalMemoryBufferDesc ``

External memory buffer descriptor.

Public Members

`` unsigned int flags ``

Flags reserved for future use.

Must be zero.

`` unsigned long long offset ``

Offset into the memory object where the buffer’s base is.

`` unsigned int reserved[16] ``

Must be zero.

`` unsigned long long size ``

Size of the buffer.
