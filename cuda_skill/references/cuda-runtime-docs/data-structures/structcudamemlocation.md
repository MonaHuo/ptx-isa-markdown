<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaMemLocation.html

#  7.51. cudaMemLocation

`` struct cudaMemLocation ``

Specifies a memory location.

To specify a gpu, set type = cudaMemLocationTypeDevice and set id = the gpu’s device ordinal. To specify a cpu NUMA node, set type = cudaMemLocationTypeHostNuma and set id = host NUMA node id.

Public Members

`` union cudaMemLocation::[anonymous] [anonymous] ``

`` unsigned char deviceId ``

Device ID.

`` int id ``

Identifier for cudaMemLocationType::cudaMemLocationTypeDevice, cudaMemLocationType::cudaMemLocationTypeHost, or cudaMemLocationType::cudaMemLocationTypeHostNuma.

`` unsigned char localityDomainId ``

Locality domain ID.

`` struct cudaMemLocation::[anonymous]::[anonymous] localized ``

Identifier for cudaMemLocationType::cudaMemLocationTypeDeviceLocalityDomain.

`` enum cudaMemLocationType type ``

Specifies the location type, which modifies the meaning of id.
