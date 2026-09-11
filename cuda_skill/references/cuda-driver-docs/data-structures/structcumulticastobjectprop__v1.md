<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUmulticastObjectProp__v1.html

#  7.86. CUmulticastObjectProp_v1

Defined in cuda.h

`` struct CUmulticastObjectProp_v1 ``

Specifies the properties for a multicast object.

Public Members

`` unsigned int numDevices ``

The number of devices in the multicast team that will bind memory to this object.

`` size_t size ``

The maximum amount of memory that can be bound to this multicast object per device.

`` unsigned long long handleTypes ``

Bitmask of exportable handle types (see CUmemAllocationHandleType) for this object.

`` unsigned long long flags ``

Flags for future use, must be zero now.
