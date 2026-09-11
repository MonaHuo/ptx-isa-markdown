<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaLaunchAttribute.html

#  7.43. cudaLaunchAttribute

`` struct cudaLaunchAttribute ``

Launch attribute.

Public Members

`` cudaLaunchAttributeID id ``

Attribute to set.

`` char pad[8 - sizeof(cudaLaunchAttributeID)] ``

`` cudaLaunchAttributeValue val ``

Value of the attribute.
