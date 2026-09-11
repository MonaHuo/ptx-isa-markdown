<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaExternalMemoryMipmappedArrayDesc.html

#  7.22. cudaExternalMemoryMipmappedArrayDesc

`` struct cudaExternalMemoryMipmappedArrayDesc ``

External memory mipmap descriptor.

Public Members

`` struct cudaExtent extent ``

Dimensions of base level of the mipmap chain.

`` unsigned int flags ``

Flags associated with CUDA mipmapped arrays.

See cudaMallocMipmappedArray

`` struct cudaChannelFormatDesc formatDesc ``

Format of base level of the mipmap chain.

`` unsigned int numLevels ``

Total number of levels in the mipmap chain.

`` unsigned long long offset ``

Offset into the memory object where the base level of the mipmap chain is.

`` unsigned int reserved[16] ``

Must be zero.
