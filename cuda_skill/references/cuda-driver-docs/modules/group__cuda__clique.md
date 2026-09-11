<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/group__CUDA__CLIQUE.html

#  6.19. Fabric Clique Information

This section describes functions and data structures to retrieve fabric clique information.

Structs

CUcliqueInfo

Fabric clique information.

##  6.19.1. Enumerations

`` enum CUcliqueType ``

Fabric clique types.

_Values:_

`` enumerator CU_CLIQUE_TYPE_UNICAST_POINTER ``

Unicast pointer clique.

`` enumerator CU_CLIQUE_TYPE_MULTICAST_POINTER ``

Multicast pointer clique.

`` enumerator CU_CLIQUE_TYPE_UNICAST_LOGICAL_ENDPOINT ``

Unicast logical endpoint clique.

`` enumerator CU_CLIQUE_TYPE_MULTICAST_LOGICAL_ENDPOINT ``

Multicast logical endpoint clique.

##  6.19.2. Functions

`` CUresult cuDeviceGetCliqueCount(size_t *count, CUdevice dev) ``

Retrieves the number of fabric cliques.

Retrieves the number of fabric cliques that the device is part of.

Parameters

  * **count** – **[out]** Number of fabric cliques that the device is part of.

  * **dev** – **[in]** Device for which the number of fabric cliques is requested.

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_PERMITTED, CUDA_ERROR_NOT_SUPPORTED

`` CUresult cuDeviceGetCliqueInfo(CUcliqueInfo *cliqueInfo, size_t *count, CUdevice dev) ``

Retrieves fabric clique information.

Returns the fabric clique information for the cliques that the device is a part of. User must specify the size of the `cliqueInfo` array in `count`. The same parameter `count` will return the actual number of entries updated in the `cliqueInfo` array.

Parameters

  * **cliqueInfo** – **[out]** Array to store the fabric clique information.

  * **count** – **[inout]** Input: Size of the `cliqueInfo` array. Output: Number of entries updated in the `cliqueInfo` array.

  * **dev** – **[in]** Device for which the clique information is requested.

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_PERMITTED, CUDA_ERROR_NOT_SUPPORTED

`` CUresult cuDeviceGetFabricClusterUuid(CUuuid *uuid, CUdevice dev) ``

Retrieves the fabric cluster UUID.

Retrieves the fabric cluster UUID for the given device.

Parameters

  * **uuid** – **[out]** Fabric cluster UUID.

  * **dev** – **[in]** Device for which the fabric cluster UUID is requested.

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_PERMITTED, CUDA_ERROR_NOT_SUPPORTED
