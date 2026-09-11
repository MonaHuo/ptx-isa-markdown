<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__MEMCPY3D__v2.html

#  7.31. CUDA_MEMCPY3D_v2

Defined in cuda.h

`` struct CUDA_MEMCPY3D_v2 ``

3D memory copy parameters

Public Members

`` size_t srcXInBytes ``

Source X in bytes.

`` size_t srcY ``

Source Y.

`` size_t srcZ ``

Source Z.

`` size_t srcLOD ``

Source LOD.

`` CUmemorytype srcMemoryType ``

Source memory type (host, device, array)

`` const void *srcHost ``

Source host pointer.

`` CUdeviceptr srcDevice ``

Source device pointer.

`` CUarray srcArray ``

Source array reference.

`` void *reserved0 ``

Must be NULL.

`` size_t srcPitch ``

Source pitch (ignored when src is array)

`` size_t srcHeight ``

Source height (ignored when src is array; may be 0 if Depth==1)

`` size_t dstXInBytes ``

Destination X in bytes.

`` size_t dstY ``

Destination Y.

`` size_t dstZ ``

Destination Z.

`` size_t dstLOD ``

Destination LOD.

`` CUmemorytype dstMemoryType ``

Destination memory type (host, device, array)

`` void *dstHost ``

Destination host pointer.

`` CUdeviceptr dstDevice ``

Destination device pointer.

`` CUarray dstArray ``

Destination array reference.

`` void *reserved1 ``

Must be NULL.

`` size_t dstPitch ``

Destination pitch (ignored when dst is array)

`` size_t dstHeight ``

Destination height (ignored when dst is array; may be 0 if Depth==1)

`` size_t WidthInBytes ``

Width of 3D memory copy in bytes.

`` size_t Height ``

Height of 3D memory copy.

`` size_t Depth ``

Depth of 3D memory copy.
