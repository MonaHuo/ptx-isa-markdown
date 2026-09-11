<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaHostNodeParamsV2.html

#  7.38. cudaHostNodeParamsV2

`` struct cudaHostNodeParamsV2 ``

CUDA host node parameters.

Public Members

`` cudaExecutionContext_t ctx ``

CUDA Execution Context.

`` cudaHostFn_t fn ``

The function to call when the node executes.

`` unsigned int syncMode ``

The synchronization mode to use for the host task.

`` void *userData ``

Argument to pass to the function.
