<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/group__CUDART__SURFACE__OBJECT.html

#  6.34. Surface Object Management

This section describes the low level texture object management functions of the CUDA runtime application programming interface.

The surface object API is only supported on devices of compute capability 3.0 or higher.

##  6.34.1. Functions

`` __host__ cudaError_t cudaCreateSurfaceObject(cudaSurfaceObject_t *pSurfObject, const struct cudaResourceDesc *pResDesc) ``

Creates a surface object.

Creates a surface object and returns it in `pSurfObject`. `pResDesc` describes the data to perform surface load/stores on. cudaResourceDesc::resType must be cudaResourceTypeArray and ::cudaResourceDesc::res::array::array must be set to a valid CUDA array handle.

Surface objects are only supported on devices of compute capability 3.0 or higher. Additionally, a surface object is an opaque value, and, as such, should only be accessed through CUDA API calls.

See also

cudaDestroySurfaceObject, ::cuSurfObjectCreate

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **pSurfObject** – - Surface object to create

  * **pResDesc** – - Resource descriptor

Returns

cudaSuccess, cudaErrorInvalidValue, cudaErrorInvalidChannelDescriptor, cudaErrorInvalidResourceHandle

`` __host__ cudaError_t cudaDestroySurfaceObject(cudaSurfaceObject_t surfObject) ``

Destroys a surface object.

Destroys the surface object specified by `surfObject`.

See also

cudaCreateSurfaceObject, ::cuSurfObjectDestroy

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Note

Use of the handle after this call is undefined behavior.

Parameters

**surfObject** – - Surface object to destroy

Returns

cudaSuccess, cudaErrorInvalidValue

`` __host__ cudaError_t cudaGetSurfaceObjectResourceDesc(struct cudaResourceDesc *pResDesc, cudaSurfaceObject_t surfObject) ``

Returns a surface object’s resource descriptor Returns the resource descriptor for the surface object specified by `surfObject`.

See also

cudaCreateSurfaceObject, ::cuSurfObjectGetResourceDesc

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **pResDesc** – - Resource descriptor

  * **surfObject** – - Surface object

Returns

cudaSuccess, cudaErrorInvalidValue
