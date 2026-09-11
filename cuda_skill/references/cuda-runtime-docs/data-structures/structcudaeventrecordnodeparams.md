<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaEventRecordNodeParams.html

#  7.17. cudaEventRecordNodeParams

`` struct cudaEventRecordNodeParams ``

Event record node parameters.

Public Members

`` cudaExecutionContext_t ctx ``

CUDA Execution Context.

`` cudaEvent_t event ``

The event to record when the node executes.
