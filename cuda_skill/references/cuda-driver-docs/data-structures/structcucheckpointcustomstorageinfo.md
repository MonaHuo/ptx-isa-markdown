<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUcheckpointCustomStorageInfo.html

#  7.47. CUcheckpointCustomStorageInfo

Defined in cuda.h

`` struct CUcheckpointCustomStorageInfo ``

Output from CUDA custom storage checkpoint/restore: per-GPU device pointers and a handle to complete the operation.

Public Members

`` CUcheckpointOperationHandle handle ``

Handle returned that is needed to complete checkpoint or restore.

`` CUcheckpointCustomStoragePerDeviceData *perDeviceData ``

Returned pointer to array of per-device data, one per device.

User should set to NULL

`` unsigned int deviceCount ``

Number of devices (and elements in `perDeviceData` array)
