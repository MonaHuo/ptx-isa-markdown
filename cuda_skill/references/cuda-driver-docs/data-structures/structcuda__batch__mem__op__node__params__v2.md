<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__BATCH__MEM__OP__NODE__PARAMS__v2.html

#  7.6. CUDA_BATCH_MEM_OP_NODE_PARAMS_v2

Defined in cuda.h

`` struct CUDA_BATCH_MEM_OP_NODE_PARAMS_v2 ``

Batch memory operation node parameters.

Public Members

`` CUcontext ctx ``

Context to use for the operations.

`` unsigned int count ``

Number of operations in paramArray.

`` CUstreamBatchMemOpParams *paramArray ``

Array of batch memory operations.

`` unsigned int flags ``

Flags to control the node.
