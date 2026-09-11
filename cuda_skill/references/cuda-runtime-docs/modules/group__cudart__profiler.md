<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/group__CUDART__PROFILER.html

#  6.31. Profiler Control

This section describes the profiler control functions of the CUDA runtime application programming interface.

##  6.31.1. Functions

`` __host__ cudaError_t cudaProfilerStart(void) ``

Enable profiling.

Enables profile collection by the active profiling tool for the current context. If profiling is already enabled, then cudaProfilerStart() has no effect.

cudaProfilerStart and cudaProfilerStop APIs are used to programmatically control the profiling granularity by allowing profiling to be done only on selective pieces of code.

See also

cudaProfilerStop, ::cuProfilerStart

Note

Note that this function may also return error codes from previous, asynchronous launches.

Returns

cudaSuccess

`` __host__ cudaError_t cudaProfilerStop(void) ``

Disable profiling.

Disables profile collection by the active profiling tool for the current context. If profiling is already disabled, then cudaProfilerStop() has no effect.

cudaProfilerStart and cudaProfilerStop APIs are used to programmatically control the profiling granularity by allowing profiling to be done only on selective pieces of code.

See also

cudaProfilerStart, ::cuProfilerStop

Note

Note that this function may also return error codes from previous, asynchronous launches.

Returns

cudaSuccess
