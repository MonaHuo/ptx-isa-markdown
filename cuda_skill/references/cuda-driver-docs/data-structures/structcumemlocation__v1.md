<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUmemLocation__v1.html

#  7.81. CUmemLocation_v1

Defined in cuda.h

`` struct CUmemLocation_v1 ``

Specifies a memory location.

Public Members

`` CUmemLocationType type ``

Specifies the location type, which modifies the meaning of id.

`` int id ``

Identifier for CUmemLocationType::CU_MEM_LOCATION_TYPE_DEVICE, CUmemLocationType::CU_MEM_LOCATION_TYPE_HOST, CUmemLocationType::CU_MEM_LOCATION_TYPE_HOST_NUMA.

`` unsigned char deviceId ``

Device ID.

`` unsigned char localityDomainId ``

Locality domain ID.

`` struct CUmemLocation_v1::[anonymous]::[anonymous] localized ``

Identifier for CUmemLocationType::CU_MEM_LOCATION_TYPE_DEVICE_LOCALITY_DOMAIN.

`` union CUmemLocation_v1::[anonymous] [anonymous] ``
