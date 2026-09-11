<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/group__CUDA__ERROR.html

#  6.13. Error Handling

This section describes the error handling functions of the low-level CUDA driver application programming interface.

##  6.13.1. Functions

`` CUresult cuGetErrorName(CUresult error, const char **pStr) ``

Gets the string representation of an error code enum name.

Sets `*pStr` to the address of a NULL-terminated string representation of the name of the enum error code `error`. If the error code is not recognized, CUDA_ERROR_INVALID_VALUE will be returned and `*pStr` will be set to the NULL address.

See also

CUresult, ::cudaGetErrorName

Parameters

  * **error** – - Error code to convert to string

  * **pStr** – - Address of the string pointer.

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_VALUE

`` CUresult cuGetErrorString(CUresult error, const char **pStr) ``

Gets the string description of an error code.

Sets `*pStr` to the address of a NULL-terminated string description of the error code `error`. If the error code is not recognized, CUDA_ERROR_INVALID_VALUE will be returned and `*pStr` will be set to the NULL address.

See also

CUresult, ::cudaGetErrorString

Parameters

  * **error** – - Error code to convert to string

  * **pStr** – - Address of the string pointer.

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_VALUE
