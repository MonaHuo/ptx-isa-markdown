<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/group__CUDA__PROFILER.html

#  6.34. Profiler Control

This section describes the profiler control functions of the low-level CUDA driver application programming interface.

##  6.34.1. Functions

`` CUresult cuProfilerStart(void) ``

Enable profiling.

Enables profile collection by the active profiling tool for the current context. If profiling is already enabled, then cuProfilerStart() has no effect.

cuProfilerStart and cuProfilerStop APIs are used to programmatically control the profiling granularity by allowing profiling to be done only on selective pieces of code.

See also

cuProfilerInitialize, cuProfilerStop, ::cudaProfilerStart

Note

Note that this function may also return error codes from previous, asynchronous launches.

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_CONTEXT

`` CUresult cuProfilerStop(void) ``

Disable profiling.

Disables profile collection by the active profiling tool for the current context. If profiling is already disabled, then cuProfilerStop() has no effect.

cuProfilerStart and cuProfilerStop APIs are used to programmatically control the profiling granularity by allowing profiling to be done only on selective pieces of code.

See also

cuProfilerInitialize, cuProfilerStart, ::cudaProfilerStop

Note

Note that this function may also return error codes from previous, asynchronous launches.

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_CONTEXT
