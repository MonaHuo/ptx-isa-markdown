<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__BATCH__MEM__OP__NODE__PARAMS__v1.html

#  7.5. CUDA_BATCH_MEM_OP_NODE_PARAMS_v1

Defined in cuda.h

`` struct CUDA_BATCH_MEM_OP_NODE_PARAMS_v1 ``

Batch memory operation node parameters.

Used in the legacy cuGraphAddBatchMemOpNode api. New code should use cuGraphAddNode()

Public Members

`` CUcontext ctx ``

`` unsigned int count ``

`` CUstreamBatchMemOpParams *paramArray ``

`` unsigned int flags ``
