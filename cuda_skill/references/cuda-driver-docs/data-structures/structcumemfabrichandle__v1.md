<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUmemFabricHandle__v1.html

#  7.80. CUmemFabricHandle_v1

Defined in cuda.h

`` struct CUmemFabricHandle_v1 ``

Fabric handle - An opaque handle representing a memory allocation that can be exported to processes in same or different nodes.

For IPC between processes on different nodes they must be connected via the NVSwitch fabric.

Public Members

`` unsigned char data[CU_IPC_HANDLE_SIZE] ``
