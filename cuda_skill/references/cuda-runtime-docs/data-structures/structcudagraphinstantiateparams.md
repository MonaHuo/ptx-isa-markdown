<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaGraphInstantiateParams.html

#  7.33. cudaGraphInstantiateParams

`` struct cudaGraphInstantiateParams ``

Graph instantiation parameters.

Public Members

`` cudaGraphNode_t errNode_out ``

The node which caused instantiation to fail, if any.

`` unsigned long long flags ``

Instantiation flags.

`` cudaGraphInstantiateResult result_out ``

Whether instantiation was successful.

If it failed, the reason why

`` cudaStream_t uploadStream ``

Upload stream.
