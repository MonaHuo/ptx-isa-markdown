<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUdevResource__st.html

#  7.57. CUdevResource_st

Defined in cuda.h

`` struct CUdevResource_st ``

Public Members

`` CUdevResourceType type ``

Type of resource, dictates which union field was last set.

`` unsigned char _internal_padding[92] ``

`` CUdevSmResource sm ``

Resource corresponding to CU_DEV_RESOURCE_TYPE_SM `type`.

`` CUdevWorkqueueConfigResource wqConfig ``

Resource corresponding to CU_DEV_RESOURCE_TYPE_WORKQUEUE_CONFIG `type`.

`` CUdevWorkqueueResource wq ``

Resource corresponding to CU_DEV_RESOURCE_TYPE_WORKQUEUE `type`.

`` unsigned char _oversize[RESOURCE_ABI_BYTES] ``

`` union CUdevResource_st::[anonymous] [anonymous] ``

`` struct CUdevResource_st *nextResource ``
