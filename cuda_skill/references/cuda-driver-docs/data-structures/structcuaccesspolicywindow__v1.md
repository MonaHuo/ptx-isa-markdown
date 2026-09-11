<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUaccessPolicyWindow__v1.html

#  7.43. CUaccessPolicyWindow_v1

Defined in cuda.h

`` struct CUaccessPolicyWindow_v1 ``

Specifies an access policy for a window, a contiguous extent of memory beginning at base_ptr and ending at base_ptr + num_bytes.

num_bytes is limited by CU_DEVICE_ATTRIBUTE_MAX_ACCESS_POLICY_WINDOW_SIZE. Partition into many segments and assign segments such that: sum of “hit segments” / window == approx. ratio. sum of “miss segments” / window == approx 1-ratio. Segments and ratio specifications are fitted to the capabilities of the architecture. Accesses in a hit segment apply the hitProp access policy. Accesses in a miss segment apply the missProp access policy.

Public Members

`` void *base_ptr ``

Starting address of the access policy window.

CUDA driver may align it.

`` size_t num_bytes ``

Size in bytes of the window policy.

CUDA driver may restrict the maximum size and alignment.

`` float hitRatio ``

hitRatio specifies percentage of lines assigned hitProp, rest are assigned missProp.

`` CUaccessProperty hitProp ``

CUaccessProperty set for hit.

`` CUaccessProperty missProp ``

CUaccessProperty set for miss.

Must be either NORMAL or STREAMING
