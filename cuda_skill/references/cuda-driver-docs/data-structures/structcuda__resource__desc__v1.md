<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__RESOURCE__DESC__v1.html

#  7.39. CUDA_RESOURCE_DESC_v1

Defined in cuda.h

`` struct CUDA_RESOURCE_DESC_v1 ``

CUDA Resource descriptor.

Public Members

`` CUresourcetype resType ``

Resource type.

`` CUarray hArray ``

CUDA array.

`` struct CUDA_RESOURCE_DESC_v1::[anonymous]::[anonymous] array ``

`` CUmipmappedArray hMipmappedArray ``

CUDA mipmapped array.

`` struct CUDA_RESOURCE_DESC_v1::[anonymous]::[anonymous] mipmap ``

`` CUdeviceptr devPtr ``

Device pointer.

`` CUarray_format format ``

Array format.

`` unsigned int numChannels ``

Channels per array element.

`` size_t sizeInBytes ``

Size in bytes.

`` struct CUDA_RESOURCE_DESC_v1::[anonymous]::[anonymous] linear ``

`` size_t width ``

Width of the array in elements.

`` size_t height ``

Height of the array in elements.

`` size_t pitchInBytes ``

Pitch between two rows in bytes.

`` struct CUDA_RESOURCE_DESC_v1::[anonymous]::[anonymous] pitch2D ``

`` int reserved[32] ``

`` struct CUDA_RESOURCE_DESC_v1::[anonymous]::[anonymous] reserved ``

`` union CUDA_RESOURCE_DESC_v1::[anonymous] res ``

`` unsigned int flags ``

Flags (must be zero)
