<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/group__CUDA__PROFILER__DEPRECATED.html

#  6.35. Profiler Control [DEPRECATED]

This section describes the profiler control functions of the low-level CUDA driver application programming interface.

##  6.35.1. Functions

`` CUresult cuProfilerInitialize(const char *configFile, const char *outputFile, CUoutput_mode outputMode) ``

Initialize the profiling.

`` Deprecated: ``

Note that this function is deprecated and should not be used. Starting with CUDA 12.0, it always returns error code CUDA_ERROR_NOT_SUPPORTED.

Using this API user can initialize the CUDA profiler by specifying the configuration file, output file and output file format. This API is generally used to profile different set of counters by looping the kernel launch. The `configFile` parameter can be used to select profiling options including profiler counters. Refer to the “Compute Command Line Profiler User Guide” for supported profiler options and counters.

Limitation: The CUDA profiler cannot be initialized with this API if another profiling tool is already active, as indicated by the CUDA_ERROR_PROFILER_DISABLED return code.

Typical usage of the profiling APIs is as follows:

for each set of counters/options

{

cuProfilerInitialize()

; //Initialize profiling, set the counters or options in the config file

…

cuProfilerStart()

;

// code to be profiled

cuProfilerStop()

;

…

cuProfilerStart()

;

// code to be profiled

cuProfilerStop()

;

…

}

See also

cuProfilerStart, cuProfilerStop,

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **configFile** – - Name of the config file that lists the counters/options for profiling.

  * **outputFile** – - Name of the outputFile where the profiling results will be stored.

  * **outputMode** – - outputMode, can be CU_OUT_KEY_VALUE_PAIR or CU_OUT_CSV.

Returns

CUDA_ERROR_NOT_SUPPORTED
