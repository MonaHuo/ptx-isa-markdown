<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUgraphNodeParams.html

#  7.68. CUgraphNodeParams

Defined in cuda.h

`` struct CUgraphNodeParams ``

Graph node parameters.

See cuGraphAddNode.

Public Members

`` CUgraphNodeType type ``

Type of the node.

`` int reserved0[3] ``

Reserved.

Must be zero.

`` long long reserved1[29] ``

Padding.

Unused bytes must be zero.

`` CUDA_KERNEL_NODE_PARAMS_v3 kernel ``

Kernel node parameters.

`` CUDA_MEMCPY_NODE_PARAMS memcpy ``

Memcpy node parameters.

`` CUDA_MEMSET_NODE_PARAMS_v2 memset ``

Memset node parameters.

`` CUDA_HOST_NODE_PARAMS_v2 host ``

Host node parameters.

`` CUDA_CHILD_GRAPH_NODE_PARAMS graph ``

Child graph node parameters.

`` CUDA_EVENT_WAIT_NODE_PARAMS eventWait ``

Event wait node parameters.

`` CUDA_EVENT_RECORD_NODE_PARAMS eventRecord ``

Event record node parameters.

`` CUDA_EXT_SEM_SIGNAL_NODE_PARAMS_v2 extSemSignal ``

External semaphore signal node parameters.

`` CUDA_EXT_SEM_WAIT_NODE_PARAMS_v2 extSemWait ``

External semaphore wait node parameters.

`` CUDA_MEM_ALLOC_NODE_PARAMS_v2 alloc ``

Memory allocation node parameters.

`` CUDA_MEM_FREE_NODE_PARAMS free ``

Memory free node parameters.

`` CUDA_BATCH_MEM_OP_NODE_PARAMS_v2 memOp ``

MemOp node parameters.

`` CUDA_CONDITIONAL_NODE_PARAMS conditional ``

Conditional node parameters.

`` char asBytes[232] ``

Padding as bytes.

`` union CUgraphNodeParams::[anonymous] [anonymous] ``

`` long long reserved2 ``

Reserved bytes.

Must be zero.
