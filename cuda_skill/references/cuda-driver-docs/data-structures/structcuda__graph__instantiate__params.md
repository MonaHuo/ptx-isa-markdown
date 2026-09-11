<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__GRAPH__INSTANTIATE__PARAMS.html

#  7.21. CUDA_GRAPH_INSTANTIATE_PARAMS

Defined in cuda.h

`` struct CUDA_GRAPH_INSTANTIATE_PARAMS ``

Graph instantiation parameters.

Public Members

`` cuuint64_t flags ``

Instantiation flags.

`` CUstream hUploadStream ``

Upload stream.

`` CUgraphNode hErrNode_out ``

The node which caused instantiation to fail, if any.

`` CUgraphInstantiateResult result_out ``

Whether instantiation was successful.

If it failed, the reason why
