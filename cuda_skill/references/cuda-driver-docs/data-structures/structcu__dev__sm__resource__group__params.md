<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCU__DEV__SM__RESOURCE__GROUP__PARAMS.html

#  7.42. CU_DEV_SM_RESOURCE_GROUP_PARAMS

Defined in cuda.h

`` struct CU_DEV_SM_RESOURCE_GROUP_PARAMS ``

Input data for splitting SMs

Public Members

`` unsigned int smCount ``

The amount of SMs available in this resource.

`` unsigned int coscheduledSmCount ``

The amount of co-scheduled SMs grouped together for locality purposes.

`` unsigned int preferredCoscheduledSmCount ``

When possible, combine co-scheduled groups together into larger groups of this size.

`` unsigned int flags ``

The flags set on this SM resource group.

For possible values see CUdevSmResourceGroup_flags.

`` unsigned int localityDomainId ``

Locality domain that the SM must be located on.

Only valid if CU_DEV_SM_RESOURCE_GROUP_LOCALITY_DOMAIN_ID is set in flags

`` unsigned int reserved[11] ``
