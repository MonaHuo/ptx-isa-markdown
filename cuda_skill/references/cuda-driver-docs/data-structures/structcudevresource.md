<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUdevResource.html

#  7.56. CUdevResource

Defined in cuda.h

`` struct CUdevResource ``

A tagged union describing different resources identified by the type field. This structure should not be directly modified outside of the API that created it.

```cpp
struct {
    CUdevResourceType type;
    union {
        CUdevSmResource sm;
        CUdevWorkqueueConfigResource wqConfig;
        CUdevWorkqueueResource wq;
    };
};
```

  * If `type` is `CU_DEV_RESOURCE_TYPE_INVALID`, this resoure is not valid and cannot be further accessed.

  * If `type` is `CU_DEV_RESOURCE_TYPE_SM`, the CUdevSmResource structure `sm` is filled in. For example, `sm.smCount` will reflect the amount of streaming multiprocessors available in this resource.

  * If `type` is `CU_DEV_RESOURCE_TYPE_WORKQUEUE_CONFIG`, the CUdevWorkqueueConfigResource structure `wqConfig` is filled in.

  * If `type` is `CU_DEV_RESOURCE_TYPE_WORKQUEUE`, the CUdevWorkqueueResource structure `wq` is filled in.
