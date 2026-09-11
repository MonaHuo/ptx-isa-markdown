<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaResourceDesc.html

#  7.66. cudaResourceDesc

`` struct cudaResourceDesc ``

CUDA resource descriptor.

Public Members

`` cudaArray_t array ``

CUDA array.

`` struct cudaResourceDesc::[anonymous]::[anonymous] array ``

`` struct cudaChannelFormatDesc desc ``

Channel descriptor.

`` void *devPtr ``

Device pointer.

`` unsigned int flags ``

Flags (must be zero)

`` size_t height ``

Height of the array in elements.

`` struct cudaResourceDesc::[anonymous]::[anonymous] linear ``

`` cudaMipmappedArray_t mipmap ``

CUDA mipmapped array.

`` struct cudaResourceDesc::[anonymous]::[anonymous] mipmap ``

`` struct cudaResourceDesc::[anonymous]::[anonymous] pitch2D ``

`` size_t pitchInBytes ``

Pitch between two rows in bytes.

`` union cudaResourceDesc::[anonymous] res ``

`` int reserved[32] ``

`` struct cudaResourceDesc::[anonymous]::[anonymous] reserved ``

`` enum cudaResourceType resType ``

Resource type.

`` size_t sizeInBytes ``

Size in bytes.

`` size_t width ``

Width of the array in elements.
