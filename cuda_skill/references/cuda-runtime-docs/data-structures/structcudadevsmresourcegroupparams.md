<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaDevSmResourceGroupParams.html

#  7.11. cudaDevSmResourceGroupParams

`` struct cudaDevSmResourceGroupParams ``

Input data for splitting SMs.

Public Members

`` unsigned int coscheduledSmCount ``

The amount of co-scheduled SMs grouped together for locality purposes.

`` unsigned int flags ``

Combination of `cudaDevSmResourceGroup_flags` values to indicate this this group is created.

`` unsigned int localityDomainId ``

Locality domain that the SM must be located on.

Only valid if cudaDevSmResourceGroupLocalityDomainId is set in flags

`` unsigned int preferredCoscheduledSmCount ``

When possible, combine co-scheduled groups together into larger groups of this size.

`` unsigned int reserved[11] ``

`` unsigned int smCount ``

The amount of SMs available in this resource.
