<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUlogicalEndpointProp.html

#  7.76. CUlogicalEndpointProp

Defined in cuda.h

`` struct CUlogicalEndpointProp ``

Properties of a logical endpoint construction.

Public Members

`` CUlogicalEndpointType type ``

Type of the logical endpoint defined in CUlogicalEndpointType.

`` CUdevice device ``

Owner device of the unicast logical endpoint.

`` struct CUlogicalEndpointProp::[anonymous]::[anonymous] unicast ``

`` unsigned int numDevices ``

Number of devices in the multicast logical endpoint team.

`` struct CUlogicalEndpointProp::[anonymous]::[anonymous] multicast ``

`` union CUlogicalEndpointProp::[anonymous] [anonymous] ``

`` unsigned long long size ``

Size of the logical endpoint.

`` unsigned int ipcHandleTypes ``

A bitmask of IPC handle types defined in CUlogicalEndpointIpcHandleType.

`` unsigned int flags ``

A bitmask of flags defined in CUlogicalEndpointFlag.
