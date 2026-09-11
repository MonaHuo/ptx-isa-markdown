<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUgraphExecUpdateResultInfo__v1.html

#  7.67. CUgraphExecUpdateResultInfo_v1

Defined in cuda.h

`` struct CUgraphExecUpdateResultInfo_v1 ``

Result information returned by cuGraphExecUpdate.

Public Members

`` CUgraphExecUpdateResult result ``

Gives more specific detail when a cuda graph update fails.

`` CUgraphNode errorNode ``

The “to node” of the error edge when the topologies do not match.

The error node when the error is associated with a specific node. NULL when the error is generic.

`` CUgraphNode errorFromNode ``

The from node of error edge when the topologies do not match.

Otherwise NULL.
