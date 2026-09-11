<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUdevSmResource.html

#  7.58. CUdevSmResource

Defined in cuda.h

`` struct CUdevSmResource ``

Data for SM-related resources All parameters in this structure are OUTPUT only. Do not write to any of the fields in this structure.

Public Members

`` unsigned int smCount ``

The amount of streaming multiprocessors available in this resource.

`` unsigned int minSmPartitionSize ``

The minimum number of streaming multiprocessors required to partition this resource.

`` unsigned int smCoscheduledAlignment ``

The number of streaming multiprocessors in this resource that are guaranteed to be co-scheduled on the same GPU processing cluster.

smCount will be a multiple of this value, unless the backfill flag is set.

`` unsigned int flags ``

The flags set on this SM resource.

For possible values see CUdevSmResourceGroup_flags.

`` unsigned int localityDomainId ``

Locality domain that the SM must be located on.

Only valid if CU_DEV_SM_RESOURCE_GROUP_LOCALITY_DOMAIN_ID is set in flags. If the backfill flag is set, SMs may be assigned from other locality domains.
