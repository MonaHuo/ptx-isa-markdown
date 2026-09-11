<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaChildGraphNodeParams.html

#  7.7. cudaChildGraphNodeParams

`` struct cudaChildGraphNodeParams ``

Child graph node parameters.

Public Members

`` cudaGraph_t graph ``

The child graph to clone into the node for node creation, or a handle to the graph owned by the node for node query.

The graph must not contain conditional nodes. Graphs containing memory allocation or memory free nodes must set the ownership to be moved to the parent.

`` enum cudaGraphChildGraphNodeOwnership ownership ``

The ownership relationship of the child graph node.
