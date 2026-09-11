<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUdevWorkqueueConfigResource.html

#  7.59. CUdevWorkqueueConfigResource

Defined in cuda.h

`` struct CUdevWorkqueueConfigResource ``

Data for workqueue configuration related resources

Public Members

`` CUdevice device ``

The device on which the workqueue resources are available.

`` unsigned int wqConcurrencyLimit ``

The expected maximum number of concurrent stream-ordered workloads.

`` CUdevWorkqueueConfigScope sharingScope ``

The sharing scope for the workqueue resources.
