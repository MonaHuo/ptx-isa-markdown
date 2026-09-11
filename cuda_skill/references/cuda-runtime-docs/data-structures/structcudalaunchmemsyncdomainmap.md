<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaLaunchMemSyncDomainMap.html

#  7.45. cudaLaunchMemSyncDomainMap

`` struct cudaLaunchMemSyncDomainMap ``

Memory Synchronization Domain map.

See cudaLaunchMemSyncDomain.

By default, kernels are launched in domain 0. Kernel launched with cudaLaunchMemSyncDomainRemote will have a different domain ID. User may also alter the domain ID with cudaLaunchMemSyncDomainMap for a specific stream / graph node / kernel launch. See cudaLaunchAttributeMemSyncDomainMap.

Domain ID range is available through cudaDevAttrMemSyncDomainCount.

Public Members

`` unsigned char default_ ``

The default domain ID to use for designated kernels.

`` unsigned char remote ``

The remote domain ID to use for designated kernels.
