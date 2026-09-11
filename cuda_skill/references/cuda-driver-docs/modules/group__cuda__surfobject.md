<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/group__CUDA__SURFOBJECT.html

#  6.39. Surface Object Management

This section describes the surface object management functions of the low-level CUDA driver application programming interface.

The surface object API is only supported on devices of compute capability 3.0 or higher.

##  6.39.1. Functions

`` CUresult cuSurfObjectCreate(CUsurfObject *pSurfObject, const CUDA_RESOURCE_DESC *pResDesc) ``

Creates a surface object.

Creates a surface object and returns it in `pSurfObject`. `pResDesc` describes the data to perform surface load/stores on. CUDA_RESOURCE_DESC::resType must be CU_RESOURCE_TYPE_ARRAY and CUDA_RESOURCE_DESC::res::array::hArray must be set to a valid CUDA array handle. CUDA_RESOURCE_DESC::flags must be set to zero.

Surface objects are only supported on devices of compute capability 3.0 or higher. Additionally, a surface object is an opaque value, and, as such, should only be accessed through CUDA API calls.

See also

cuSurfObjectDestroy, ::cudaCreateSurfaceObject

Parameters

  * **pSurfObject** – - Surface object to create

  * **pResDesc** – - Resource descriptor

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE

`` CUresult cuSurfObjectDestroy(CUsurfObject surfObject) ``

Destroys a surface object.

Destroys the surface object specified by `surfObject`.

See also

cuSurfObjectCreate, ::cudaDestroySurfaceObject

Parameters

**surfObject** – - Surface object to destroy

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE

`` CUresult cuSurfObjectGetResourceDesc(CUDA_RESOURCE_DESC *pResDesc, CUsurfObject surfObject) ``

Returns a surface object’s resource descriptor.

Returns the resource descriptor for the surface object specified by `surfObject`.

See also

cuSurfObjectCreate, ::cudaGetSurfaceObjectResourceDesc

Parameters

  * **pResDesc** – - Resource descriptor

  * **surfObject** – - Surface object

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE
