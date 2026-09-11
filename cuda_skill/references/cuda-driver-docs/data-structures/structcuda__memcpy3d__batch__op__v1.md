<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__MEMCPY3D__BATCH__OP__v1.html

#  7.29. CUDA_MEMCPY3D_BATCH_OP_v1

Defined in cuda.h

`` struct CUDA_MEMCPY3D_BATCH_OP_v1 ``

Public Members

`` CUmemcpy3DOperand src ``

Source memcpy operand.

`` CUmemcpy3DOperand dst ``

Destination memcpy operand.

`` CUextent3D extent ``

Extents of the memcpy between src and dst.

The width, height and depth components must not be 0.

`` CUmemcpySrcAccessOrder srcAccessOrder ``

Source access ordering to be observed for copy from src to dst.

`` unsigned int flags ``

Additional flags for copies with this attribute.

See CUmemcpyFlags
