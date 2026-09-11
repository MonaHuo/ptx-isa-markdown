<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUmemDecompressParams.html

#  7.79. CUmemDecompressParams

Defined in cuda.h

`` struct CUmemDecompressParams ``

Structure describing the parameters that compose a single decompression operation.

Public Members

`` size_t srcNumBytes ``

The number of bytes to be read and decompressed from ::CUmemDecompressParams_st.src.

`` size_t dstNumBytes ``

The number of bytes that the decompression operation will be expected to write to ::CUmemDecompressParams_st.dst.

This value is optional; if present, it may be used by the CUDA driver as a heuristic for scheduling the individual decompression operations.

`` cuuint32_t *dstActBytes ``

After the decompression operation has completed, the actual number of bytes written to CUmemDecompressParams.dst will be recorded as a 32-bit unsigned integer in the memory at this address.

`` const void *src ``

Pointer to a buffer of at least ::CUmemDecompressParams_st.srcNumBytes compressed bytes.

`` void *dst ``

Pointer to a buffer where the decompressed data will be written.

The number of bytes written to this location will be recorded in the memory pointed to by ::CUmemDecompressParams_st.dstActBytes

`` CUmemDecompressAlgorithm algo ``

The decompression algorithm to use.

`` unsigned char padding[20] ``
