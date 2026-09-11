<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/deprecated.html

#  8\. Deprecated List

`` Member cudaD3D10GetDirect3DDevice  (ID3D10Device **ppD3D10Device) ``

This function is deprecated as of CUDA 5.0.

`` Member cudaD3D10MapResources  (int count, ID3D10Resource **ppResources) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaD3D10RegisterResource  (ID3D10Resource *pResource, unsigned int flags) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaD3D10ResourceGetMappedArray  (cudaArray **ppArray, ID3D10Resource *pResource, unsigned int subResource) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaD3D10ResourceGetMappedPitch  (size_t *pPitch, size_t *pPitchSlice, ID3D10Resource *pResource, unsigned int subResource) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaD3D10ResourceGetMappedPointer  (void **pPointer, ID3D10Resource *pResource, unsigned int subResource) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaD3D10ResourceGetMappedSize  (size_t *pSize, ID3D10Resource *pResource, unsigned int subResource) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaD3D10ResourceGetSurfaceDimensions  (size_t *pWidth, size_t *pHeight, size_t *pDepth, ID3D10Resource *pResource, unsigned int subResource) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaD3D10ResourceSetMapFlags  (ID3D10Resource *pResource, unsigned int flags) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaD3D10SetDirect3DDevice  (ID3D10Device *pD3D10Device, int device=-1) ``

This function is deprecated as of CUDA 5.0.

`` Member cudaD3D10UnmapResources  (int count, ID3D10Resource **ppResources) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaD3D10UnregisterResource  (ID3D10Resource *pResource) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaD3D11GetDirect3DDevice  (ID3D11Device **ppD3D11Device) ``

This function is deprecated as of CUDA 5.0.

`` Member cudaD3D11SetDirect3DDevice  (ID3D11Device *pD3D11Device, int device=-1) ``

This function is deprecated as of CUDA 5.0.

`` Member cudaD3D9MapResources  (int count, IDirect3DResource9 **ppResources) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaD3D9RegisterResource  (IDirect3DResource9 *pResource, unsigned int flags) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaD3D9ResourceGetMappedArray  (cudaArray **ppArray, IDirect3DResource9 *pResource, unsigned int face, unsigned int level) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaD3D9ResourceGetMappedPitch  (size_t *pPitch, size_t *pPitchSlice, IDirect3DResource9 *pResource, unsigned int face, unsigned int level) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaD3D9ResourceGetMappedPointer  (void **pPointer, IDirect3DResource9 *pResource, unsigned int face, unsigned int level) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaD3D9ResourceGetMappedSize  (size_t *pSize, IDirect3DResource9 *pResource, unsigned int face, unsigned int level) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaD3D9ResourceGetSurfaceDimensions  (size_t *pWidth, size_t *pHeight, size_t *pDepth, IDirect3DResource9 *pResource, unsigned int face, unsigned int level) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaD3D9ResourceSetMapFlags  (IDirect3DResource9 *pResource, unsigned int flags) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaD3D9UnmapResources  (int count, IDirect3DResource9 **ppResources) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaD3D9UnregisterResource  (IDirect3DResource9 *pResource) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaDeviceBlockingSync ``

This flag was deprecated as of CUDA 4.0 and replaced with cudaDeviceScheduleBlockingSync.

`` Member cudaDeviceGetSharedMemConfig  (enum cudaSharedMemConfig *pConfig) ``

`` Member cudaDeviceSetSharedMemConfig  (enum cudaSharedMemConfig config) ``

`` Member cudaErrorAddressOfConstant ``

This error return is deprecated as of CUDA 3.1. Variables in constant memory may now have their address taken by the runtime via cudaGetSymbolAddress().

`` Member cudaErrorInvalidDevicePointer ``

This error return is deprecated as of CUDA 10.1.

`` Member cudaErrorInvalidHostPointer ``

This error return is deprecated as of CUDA 10.1.

`` Member cudaErrorMemoryValueTooLarge ``

This error return is deprecated as of CUDA 3.1. Device emulation mode was removed with the CUDA 3.1 release.

`` Member cudaErrorMixedDeviceExecution ``

This error return is deprecated as of CUDA 3.1. Device emulation mode was removed with the CUDA 3.1 release.

`` Member cudaErrorNotYetImplemented ``

This error return is deprecated as of CUDA 4.1.

`` Member cudaErrorPriorLaunchFailure ``

This error return is deprecated as of CUDA 3.1. Device emulation mode was removed with the CUDA 3.1 release.

`` Member cudaErrorProfilerAlreadyStarted ``

This error return is deprecated as of CUDA 5.0. It is no longer an error to call cudaProfilerStart() when profiling is already enabled.

`` Member cudaErrorProfilerAlreadyStopped ``

This error return is deprecated as of CUDA 5.0. It is no longer an error to call cudaProfilerStop() when profiling is already disabled.

`` Member cudaErrorProfilerNotInitialized ``

This error return is deprecated as of CUDA 5.0. It is no longer an error to attempt to enable/disable the profiling via cudaProfilerStart or cudaProfilerStop without initialization.

`` Member cudaErrorSynchronizationError ``

This error return is deprecated as of CUDA 3.1. Device emulation mode was removed with the CUDA 3.1 release.

`` Member cudaErrorTextureFetchFailed ``

This error return is deprecated as of CUDA 3.1. Device emulation mode was removed with the CUDA 3.1 release.

`` Member cudaErrorTextureNotBound ``

This error return is deprecated as of CUDA 3.1. Device emulation mode was removed with the CUDA 3.1 release.

`` Member cudaFuncSetSharedMemConfig  (const void *func, enum cudaSharedMemConfig config) ``

`` Member cudaGetDriverEntryPoint  (const char *symbol, void **funcPtr, unsigned long long flags, enum cudaDriverEntryPointQueryResult *driverStatus=NULL) ``

This function is deprecated as of CUDA 13.0

`` Member cudaGLMapBufferObject  (void **devPtr, GLuint bufObj) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaGLMapBufferObjectAsync  (void **devPtr, GLuint bufObj, cudaStream_t stream) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaGLRegisterBufferObject  (GLuint bufObj) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaGLSetBufferObjectMapFlags  (GLuint bufObj, unsigned int flags) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaGLSetGLDevice  (int device) ``

This function is deprecated as of CUDA 5.0.

`` Member cudaGLUnmapBufferObject  (GLuint bufObj) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaGLUnmapBufferObjectAsync  (GLuint bufObj, cudaStream_t stream) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaGLUnregisterBufferObject  (GLuint bufObj) ``

This function is deprecated as of CUDA 3.0.

`` Member cudaMemcpyArrayToArray  (cudaArray_t dst, size_t wOffsetDst, size_t hOffsetDst, cudaArray_const_t src, size_t wOffsetSrc, size_t hOffsetSrc, size_t count, enum cudaMemcpyKind kind=cudaMemcpyDeviceToDevice) ``

`` Member cudaMemcpyFromArray  (void *dst, cudaArray_const_t src, size_t wOffset, size_t hOffset, size_t count, enum cudaMemcpyKind kind) ``

`` Member cudaMemcpyFromArrayAsync  (void *dst, cudaArray_const_t src, size_t wOffset, size_t hOffset, size_t count, enum cudaMemcpyKind kind, cudaStream_t stream=0) ``

`` Member cudaMemcpyToArray  (cudaArray_t dst, size_t wOffset, size_t hOffset, const void *src, size_t count, enum cudaMemcpyKind kind) ``

`` Member cudaMemcpyToArrayAsync  (cudaArray_t dst, size_t wOffset, size_t hOffset, const void *src, size_t count, enum cudaMemcpyKind kind, cudaStream_t stream=0) ``

`` Member cudaSharedMemConfig ``
