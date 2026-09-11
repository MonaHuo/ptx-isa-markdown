<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaGraphExecUpdateResultInfo.html

#  7.32. cudaGraphExecUpdateResultInfo

`` struct cudaGraphExecUpdateResultInfo ``

Result information returned by cudaGraphExecUpdate.

Public Members

`` cudaGraphNode_t errorFromNode ``

The from node of error edge when the topologies do not match.

Otherwise NULL.

`` cudaGraphNode_t errorNode ``

The “to node” of the error edge when the topologies do not match.

The error node when the error is associated with a specific node. NULL when the error is generic.

`` enum cudaGraphExecUpdateResult result ``

Gives more specific detail when a cuda graph update fails.
