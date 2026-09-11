<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUcheckpointCustomStoragePerDeviceData.html

#  7.48. CUcheckpointCustomStoragePerDeviceData

Defined in cuda.h

`` struct CUcheckpointCustomStoragePerDeviceData ``

Per-GPU data for zero-copy mapped device memory used with CUDA checkpoint/restore on custom storage.

Public Members

`` CUdeviceptr devPtr ``

Zero-copy mapped device memory pointer for the user to copy to/from.

`` size_t size ``

Size of mapped memory.

`` CUstream stream ``

Stream the user may use for the copy; the CUDA driver synchronizes on this stream before completing checkpoint or restore.
