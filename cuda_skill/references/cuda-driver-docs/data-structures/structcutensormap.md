<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUtensorMap.html

#  7.95. CUtensorMap

Defined in cuda.h

`` struct CUtensorMap ``

Tensor map descriptor.

Requires compiler support for aligning to 128 bytes.

Public Members

`` cuuint64_t opaque[CU_TENSOR_MAP_NUM_QWORDS] ``
