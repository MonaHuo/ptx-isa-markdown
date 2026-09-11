<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUcheckpointRestoreArgs.html

#  7.51. CUcheckpointRestoreArgs

Defined in cuda.h

`` struct CUcheckpointRestoreArgs ``

CUDA checkpoint optional restore arguments.

Public Members

`` CUcheckpointGpuPair *gpuPairs ``

Pointer to array of gpu pairs that indicate how to remap GPUs during restore.

`` unsigned int gpuPairsCount ``

Number of gpu pairs to remap.

`` unsigned int padding0 ``

Padding to align the following fields.

`` CUcheckpointCustomStorageInfo **customStorageInfo_out ``

Optional custom storage; if NULL, GPU memory is restored from host.

`` char reserved[64 - sizeof(CUcheckpointGpuPair*) - 2 * sizeof(unsigned int) - sizeof(CUcheckpointCustomStorageInfo**)] ``

Reserved for future use, must be zeroed; includes alignment before `customStorageInfo`.
