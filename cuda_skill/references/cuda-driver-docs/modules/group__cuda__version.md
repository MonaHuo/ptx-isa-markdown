<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/group__CUDA__VERSION.html

#  6.46. Version Management

This section describes the version management functions of the low-level CUDA driver application programming interface.

##  6.46.1. Functions

`` CUresult cuDriverGetVersion(int *driverVersion) ``

Returns the latest CUDA version supported by driver.

Returns in `*driverVersion` the version of CUDA supported by the driver. The version is returned as (1000 * major + 10 * minor). For example, CUDA 9.2 would be represented by 9020.

This function automatically returns CUDA_ERROR_INVALID_VALUE if `driverVersion` is NULL.

See also

::cudaDriverGetVersion, ::cudaRuntimeGetVersion

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

**driverVersion** – - Returns the CUDA driver version

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_VALUE
