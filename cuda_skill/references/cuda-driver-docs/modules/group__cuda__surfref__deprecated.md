<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/group__CUDA__SURFREF__DEPRECATED.html

#  6.40. Surface Reference Management [DEPRECATED]

This section describes the surface reference management functions of the low-level CUDA driver application programming interface.

##  6.40.1. Functions

`` CUresult cuSurfRefGetArray(CUarray *phArray, CUsurfref hSurfRef) ``

Passes back the CUDA array bound to a surface reference.

`` Deprecated: ``

Returns in `*phArray` the CUDA array bound to the surface reference `hSurfRef`, or returns CUDA_ERROR_INVALID_VALUE if the surface reference is not bound to any CUDA array.

See also

cuModuleGetSurfRef, cuSurfRefSetArray

Parameters

  * **phArray** – - Surface reference handle

  * **hSurfRef** – - Surface reference handle

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE

`` CUresult cuSurfRefSetArray(CUsurfref hSurfRef, CUarray hArray, unsigned int Flags) ``

Sets the CUDA array for a surface reference.

`` Deprecated: ``

Sets the CUDA array `hArray` to be read and written by the surface reference `hSurfRef`. Any previous CUDA array state associated with the surface reference is superseded by this function. `Flags` must be set to 0. The CUDA_ARRAY3D_SURFACE_LDST flag must have been set for the CUDA array. Any CUDA array previously bound to `hSurfRef` is unbound.

See also

cuModuleGetSurfRef, cuSurfRefGetArray

Parameters

  * **hSurfRef** – - Surface reference handle

  * **hArray** – - CUDA array handle

  * **Flags** – - set to 0

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE
