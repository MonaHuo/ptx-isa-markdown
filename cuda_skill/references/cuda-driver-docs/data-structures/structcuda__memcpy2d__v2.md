<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__MEMCPY2D__v2.html

#  7.28. CUDA_MEMCPY2D_v2

Defined in cuda.h

`` struct CUDA_MEMCPY2D_v2 ``

2D memory copy parameters

Public Members

`` size_t srcXInBytes ``

Source X in bytes.

`` size_t srcY ``

Source Y.

`` CUmemorytype srcMemoryType ``

Source memory type (host, device, array)

`` const void *srcHost ``

Source host pointer.

`` CUdeviceptr srcDevice ``

Source device pointer.

`` CUarray srcArray ``

Source array reference.

`` size_t srcPitch ``

Source pitch (ignored when src is array)

`` size_t dstXInBytes ``

Destination X in bytes.

`` size_t dstY ``

Destination Y.

`` CUmemorytype dstMemoryType ``

Destination memory type (host, device, array)

`` void *dstHost ``

Destination host pointer.

`` CUdeviceptr dstDevice ``

Destination device pointer.

`` CUarray dstArray ``

Destination array reference.

`` size_t dstPitch ``

Destination pitch (ignored when dst is array)

`` size_t WidthInBytes ``

Width of 2D memory copy in bytes.

`` size_t Height ``

Height of 2D memory copy.
