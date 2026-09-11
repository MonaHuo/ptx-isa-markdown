<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaDevResource.html

#  7.9. cudaDevResource

`` struct cudaDevResource ``

A tagged union describing different resources identified by the type field.

This structure should not be directly modified outside of the API that created it.

```cpp
struct {
    enum cudaDevResourceType type;
    union {
        struct cudaDevSmResource sm;
        struct cudaDevWorkqueueConfigResource wqConfig;
        struct cudaDevWorkqueueResource wq;
    };
};
```

  * If `type` is `cudaDevResourceTypeInvalid`, this resoure is not valid and cannot be further accessed.

  * If `type` is `cudaDevResourceTypeSm`, the cudaDevSmResource structure `sm` is filled in. For example, `sm.smCount` will reflect the amount of streaming multiprocessors available in this resource.

  * If `type` is `cudaDevResourceTypeWorkqueueConfig`, the cudaDevWorkqueueConfigResource structure `wqConfig` is filled in.

  * If `type` is `cudaDevResourceTypeWorkqueue`, the cudaDevWorkqueueResource structure `wq` is filled in.

Public Members

`` union cudaDevResource::[anonymous] [anonymous] ``

`` unsigned char _internal_padding[92] ``

`` unsigned char _oversize[40] ``

`` struct cudaDevResource_st *nextResource ``

`` struct cudaDevSmResource sm ``

Resource corresponding to cudaDevResourceTypeSm `type`.

`` enum cudaDevResourceType type ``

Type of resource, dictates which union field was last set.

`` struct cudaDevWorkqueueResource wq ``

Resource corresponding to cudaDevResourceTypeWorkqueue `type`.

`` struct cudaDevWorkqueueConfigResource wqConfig ``

Resource corresponding to cudaDevResourceTypeWorkqueueConfig `type`.
