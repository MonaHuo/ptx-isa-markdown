<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUarrayMapInfo__v1.html

#  7.44. CUarrayMapInfo_v1

Defined in cuda.h

`` struct CUarrayMapInfo_v1 ``

Specifies the CUDA array or CUDA mipmapped array memory mapping information.

Public Members

`` CUresourcetype resourceType ``

Resource type.

`` CUmipmappedArray mipmap ``

`` CUarray array ``

`` union CUarrayMapInfo_v1::[anonymous] resource ``

`` CUarraySparseSubresourceType subresourceType ``

Sparse subresource type.

`` unsigned int level ``

For CUDA mipmapped arrays must a valid mipmap level.

For CUDA arrays must be zero

`` unsigned int layer ``

For CUDA layered arrays must be a valid layer index.

Otherwise, must be zero

`` unsigned int offsetX ``

Starting X offset in elements.

`` unsigned int offsetY ``

Starting Y offset in elements.

`` unsigned int offsetZ ``

Starting Z offset in elements.

`` unsigned int extentWidth ``

Width in elements.

`` unsigned int extentHeight ``

Height in elements.

`` unsigned int extentDepth ``

Depth in elements.

`` struct CUarrayMapInfo_v1::[anonymous]::[anonymous] sparseLevel ``

`` unsigned long long offset ``

Offset within mip tail.

Offset within the memory.

`` unsigned long long size ``

Extent in bytes.

`` struct CUarrayMapInfo_v1::[anonymous]::[anonymous] miptail ``

`` union CUarrayMapInfo_v1::[anonymous] subresource ``

`` CUmemOperationType memOperationType ``

Memory operation type.

`` CUmemHandleType memHandleType ``

Memory handle type.

`` CUmemGenericAllocationHandle memHandle ``

`` union CUarrayMapInfo_v1::[anonymous] memHandle ``

`` unsigned int deviceBitMask ``

Device ordinal bit mask.

`` unsigned int flags ``

flags for future use, must be zero now.

`` unsigned int reserved[2] ``

Reserved for future use, must be zero now.
