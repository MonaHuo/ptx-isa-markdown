<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__CONDITIONAL__NODE__PARAMS.html

#  7.8. CUDA_CONDITIONAL_NODE_PARAMS

Defined in cuda.h

`` struct CUDA_CONDITIONAL_NODE_PARAMS ``

Conditional node parameters.

Public Members

`` CUgraphConditionalHandle handle ``

Conditional node handle.

Handles must be created in advance of creating the node using cuGraphConditionalHandleCreate.

`` CUgraphConditionalNodeType type ``

Type of conditional node.

`` unsigned int size ``

Size of graph output array.

Allowed values are 1 for CU_GRAPH_COND_TYPE_WHILE, 1 or 2 for CU_GRAPH_COND_TYPE_IF, or any value greater than zero for CU_GRAPH_COND_TYPE_SWITCH.

`` CUgraph *phGraph_out ``

CUDA-owned array populated with conditional node child graphs during creation of the node.

Valid for the lifetime of the conditional node. The contents of the graph(s) are subject to the following constraints:

  * Allowed node types are kernel nodes, empty nodes, child graphs, memsets, memcopies, and conditionals. This applies recursively to child graphs and conditional bodies.

  * All kernels, including kernels in nested conditionals or child graphs at any level, must belong to the same device context.

These graphs may be populated using graph node creation APIs or cuStreamBeginCaptureToGraph.

CU_GRAPH_COND_TYPE_IF: phGraph_out[0] is executed when the condition is non-zero. If `size` == 2, phGraph_out[1] will be executed when the condition is zero. CU_GRAPH_COND_TYPE_WHILE: phGraph_out[0] is executed as long as the condition is non-zero. CU_GRAPH_COND_TYPE_SWITCH: phGraph_out[n] is executed when the condition is equal to n. If the condition >= `size`, no body graph is executed.

`` CUcontext ctx ``

Context on which to run the node.

Must match context used to create the handle and all body nodes.
