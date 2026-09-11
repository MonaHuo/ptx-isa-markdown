<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUlaunchAttribute.html

#  7.71. CUlaunchAttribute

Defined in cuda.h

`` struct CUlaunchAttribute ``

Launch attribute.

Public Members

`` CUlaunchAttributeID id ``

Attribute to set.

`` char pad[8 - sizeof(CUlaunchAttributeID)] ``

`` CUlaunchAttributeValue value ``

Value of the attribute.
