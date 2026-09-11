<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUlaunchMemSyncDomainMap.html

#  7.73. CUlaunchMemSyncDomainMap

Defined in cuda.h

`` struct CUlaunchMemSyncDomainMap ``

Memory Synchronization Domain map.

See ::cudaLaunchMemSyncDomain.

By default, kernels are launched in domain 0. Kernel launched with CU_LAUNCH_MEM_SYNC_DOMAIN_REMOTE will have a different domain ID. User may also alter the domain ID with CUlaunchMemSyncDomainMap for a specific stream / graph node / kernel launch. See CU_LAUNCH_ATTRIBUTE_MEM_SYNC_DOMAIN_MAP.

Domain ID range is available through CU_DEVICE_ATTRIBUTE_MEM_SYNC_DOMAIN_COUNT.

Public Members

`` unsigned char default_ ``

The default domain ID to use for designated kernels.

`` unsigned char remote ``

The remote domain ID to use for designated kernels.
