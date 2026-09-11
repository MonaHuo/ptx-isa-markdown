<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaDevWorkqueueConfigResource.html

#  7.12. cudaDevWorkqueueConfigResource

`` struct cudaDevWorkqueueConfigResource ``

Data for workqueue configuration related resources.

Public Members

`` int device ``

The device on which the workqueue resources are available.

`` enum cudaDevWorkqueueConfigScope sharingScope ``

The sharing scope for the workqueue resources.

`` unsigned int wqConcurrencyLimit ``

The expected maximum number of concurrent stream-ordered workloads.
