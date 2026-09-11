<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/group__CUDART__FABRIC.html

#  6.24. Logical Endpoint

This section describes the functions for Logical Endpoint operations management.

##  6.24.1. Functions

`` __device__ cudaError_t cudaFabricOpErrorStatusCount(void *status, cudaFabricOpStatusSource statusSource, unsigned int *count) ``

Get the number of errors for a fabric operation.

Given the pointer to the `status` field obtained from fabric operation completion object, return the total count of errors.

Parameters

  * **status** – - The pointer to the status field obtained from fabric operation completion object

  * **statusSource** – - The type of the fabric operation completion object

  * **count** – - The number of errors in the decoded status field

Returns

cudaSuccess, cudaErrorInvalidValue, cudaErrorNotSupported

`` __device__ cudaError_t cudaFabricOpErrorStatusGet(void *status, cudaFabricOpStatusSource statusSource, unsigned int statusIndex, cudaFabricOpStatusInfo *statusInfo) ``

Get the error status of a fabric operation.

Given a pointer to the `status` field obtained from a fabric operation completion object, retrieves the error at index `statusIndex` in the decoded `status` field and writes it to `statusInfo`.

`statusIndex` must be in the range [0, statusCount), where statusCount is the value returned via the `count` parameter of cudaFabricOpErrorStatusCount.

Parameters

  * **status** – - Pointer to the status field from the fabric operation completion object

  * **statusSource** – - The type of the fabric operation completion object

  * **statusIndex** – - Index of the error to retrieve (0-based; selects which of the decoded errors to return)

  * **statusInfo** – - Pointer to `cudaFabricOpStatusInfo` where the decoded error information is returned

Returns

cudaSuccess, cudaErrorInvalidValue, cudaErrorNotSupported
