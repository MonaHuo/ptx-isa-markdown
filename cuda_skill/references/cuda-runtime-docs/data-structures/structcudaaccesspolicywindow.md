<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaAccessPolicyWindow.html

#  7.2. cudaAccessPolicyWindow

`` struct cudaAccessPolicyWindow ``

Specifies an access policy for a window, a contiguous extent of memory beginning at base_ptr and ending at base_ptr + num_bytes.

Partition into many segments and assign segments such that. sum of “hit segments” / window == approx. ratio. sum of “miss segments” / window == approx 1-ratio. Segments and ratio specifications are fitted to the capabilities of the architecture. Accesses in a hit segment apply the hitProp access policy. Accesses in a miss segment apply the missProp access policy.

Public Members

`` void *base_ptr ``

Starting address of the access policy window.

CUDA driver may align it.

`` enum cudaAccessProperty hitProp ``

::CUaccessProperty set for hit.

`` float hitRatio ``

hitRatio specifies percentage of lines assigned hitProp, rest are assigned missProp.

`` enum cudaAccessProperty missProp ``

::CUaccessProperty set for miss.

Must be either NORMAL or STREAMING.

`` size_t num_bytes ``

Size in bytes of the window policy.

CUDA driver may restrict the maximum size and alignment.
