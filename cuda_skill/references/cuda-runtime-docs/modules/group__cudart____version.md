<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/group__CUDART____VERSION.html

#  6.38. Version Management

##  6.38.1. Functions

`` __host__ cudaError_t cudaDriverGetVersion(int *driverVersion) ``

Returns the latest version of CUDA supported by the driver.

Returns in `*driverVersion` the latest version of CUDA supported by the driver. The version is returned as (1000 major + 10 minor). For example, CUDA 9.2 would be represented by 9020. If no driver is installed, then 0 is returned as the driver version.

This function automatically returns cudaErrorInvalidValue if `driverVersion` is NULL.

See also

cudaRuntimeGetVersion, ::cuDriverGetVersion

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

**driverVersion** – - Returns the CUDA driver version.

Returns

cudaSuccess, cudaErrorInvalidValue

`` __host__ cudaError_t cudaRuntimeGetVersion(int *runtimeVersion) ``

Returns the CUDA Runtime version.

Returns in `*runtimeVersion` the version number of the current CUDA Runtime instance. The version is returned as (1000 major + 10 minor). For example, CUDA 9.2 would be represented by 9020.

As of CUDA 12.0, this function no longer initializes CUDA. The purpose of this API is solely to return a compile-time constant stating the CUDA Toolkit version in the above format.

As of CUDA 13.0, on Windows, the `runtimeVersion` may not be the same as the CUDA Toolkit version the app was built with. Windows will use the CUDA Runtime packaged with the display driver, and that version will be reported.

This function automatically returns cudaErrorInvalidValue if the `runtimeVersion` argument is NULL.

See also

cudaDriverGetVersion, ::cuDriverGetVersion

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

**runtimeVersion** – - Returns the CUDA Runtime version.

Returns

cudaSuccess, cudaErrorInvalidValue
