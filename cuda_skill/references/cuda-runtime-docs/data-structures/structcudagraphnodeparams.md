<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaGraphNodeParams.html

#  7.35. cudaGraphNodeParams

`` struct cudaGraphNodeParams ``

Graph node parameters.

See cudaGraphAddNode.

Public Members

`` union cudaGraphNodeParams::[anonymous] [anonymous] ``

`` struct cudaMemAllocNodeParamsV2 alloc ``

Memory allocation node parameters.

`` struct cudaConditionalNodeParams conditional ``

Conditional node parameters.

`` struct cudaEventRecordNodeParams eventRecord ``

Event record node parameters.

`` struct cudaEventWaitNodeParams eventWait ``

Event wait node parameters.

`` struct cudaExternalSemaphoreSignalNodeParamsV2 extSemSignal ``

External semaphore signal node parameters.

`` struct cudaExternalSemaphoreWaitNodeParamsV2 extSemWait ``

External semaphore wait node parameters.

`` struct cudaMemFreeNodeParams free ``

Memory free node parameters.

`` struct cudaChildGraphNodeParams graph ``

Child graph node parameters.

`` struct cudaHostNodeParamsV2 host ``

Host node parameters.

`` struct cudaKernelNodeParamsV2 kernel ``

Kernel node parameters.

`` struct cudaMemcpyNodeParams memcpy ``

Memcpy node parameters.

`` struct cudaMemsetParamsV2 memset ``

Memset node parameters.

`` int reserved0[3] ``

Reserved.

Must be zero.

`` long long reserved1[29] ``

Padding.

Unused bytes must be zero.

`` long long reserved2 ``

Reserved bytes.

Must be zero.

`` enum cudaGraphNodeType type ``

Type of the node.
