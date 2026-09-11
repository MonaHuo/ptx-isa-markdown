<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaDevSmResource.html

#  7.10. cudaDevSmResource

`` struct cudaDevSmResource ``

Data for SM-related resources All parameters in this structure are OUTPUT only.

Do not write to any of the fields in this structure.

Public Members

`` unsigned int flags ``

The flags set on this SM resource.

For available flags see cudaDevSmResourceGroup_flags.

`` unsigned int localityDomainId ``

Locality domain that the SM must be located on.

Only valid if cudaDevSmResourceConstraintTypeLocalityDomainId is set in flags

`` unsigned int minSmPartitionSize ``

The minimum number of streaming multiprocessors required to partition this resource.

`` unsigned int smCoscheduledAlignment ``

The number of streaming multiprocessors in this resource that are guaranteed to be co-scheduled on the same GPU processing cluster.

smCount will be a multiple of this value, unless the backfill flag is set.

`` unsigned int smCount ``

The amount of streaming multiprocessors available in this resource.
