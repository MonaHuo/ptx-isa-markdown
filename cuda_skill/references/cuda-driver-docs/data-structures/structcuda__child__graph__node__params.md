<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__CHILD__GRAPH__NODE__PARAMS.html

#  7.7. CUDA_CHILD_GRAPH_NODE_PARAMS

Defined in cuda.h

`` struct CUDA_CHILD_GRAPH_NODE_PARAMS ``

Child graph node parameters.

Public Members

`` CUgraph graph ``

The child graph to clone into the node for node creation, or a handle to the graph owned by the node for node query.

The graph must not contain conditional nodes. Graphs containing memory allocation or memory free nodes must set the ownership to be moved to the parent.

`` CUgraphChildGraphNodeOwnership ownership ``

The ownership relationship of the child graph node.
