<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUmemcpyAttributes__v1.html

#  7.85. CUmemcpyAttributes_v1

Defined in cuda.h

`` struct CUmemcpyAttributes_v1 ``

Attributes specific to copies within a batch.

For more details on usage see cuMemcpyBatchAsync.

Public Members

`` CUmemcpySrcAccessOrder srcAccessOrder ``

Source access ordering to be observed for copies with this attribute.

`` CUmemLocation srcLocHint ``

Hint location for the source operand.

Ignored when the pointers are not managed memory or memory allocated outside CUDA.

`` CUmemLocation dstLocHint ``

Hint location for the destination operand.

Ignored when the pointers are not managed memory or memory allocated outside CUDA.

`` unsigned int flags ``

Additional flags for copies with this attribute.

See CUmemcpyFlags
