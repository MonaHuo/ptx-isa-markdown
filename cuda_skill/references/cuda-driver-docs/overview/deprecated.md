<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/deprecated.html

#  8\. Deprecated List

`` Member CU_CTX_BLOCKING_SYNC ``

This flag was deprecated as of CUDA 4.0 and was replaced with CU_CTX_SCHED_BLOCKING_SYNC.

`` Member CU_CTX_MAP_HOST ``

This flag was deprecated as of CUDA 11.0 and it no longer has any effect. All contexts as of CUDA 3.2 behave as though the flag is enabled.

`` Member CU_DEVICE_P2P_ATTRIBUTE_ACCESS_ACCESS_SUPPORTED ``

use CU_DEVICE_P2P_ATTRIBUTE_CUDA_ARRAY_ACCESS_SUPPORTED instead

`` Member CU_JIT_FMA ``

Enable/Disable the contraction of floating-point multiplies and adds/subtracts into floating-point multiply-add (-fma) operations (1: Enable, default; 0: Disable). Option type: int Applies to: link-time optimization specified with CU_JIT_LTO

`` Member CU_JIT_FTZ ``

Control single-precision denormals (-ftz) support (0: false, default). 1 : flushes denormal values to zero 0 : preserves denormal values Option type: int Applies to: link-time optimization specified with CU_JIT_LTO

`` Member CU_JIT_INPUT_NVVM ``

High-level intermediate code for link-time optimization Applicable options: NVVM compiler options, PTX compiler options

`` Member CU_JIT_LTO ``

Enable link-time optimization (-dlto) for device code (Disabled by default). This option is not supported on 32-bit platforms. Option type: int Applies to: compiler and linker

`` Member CU_JIT_NEW_SM3X_OPT ``

This jit option is deprecated and should not be used.

`` Member CU_JIT_OPTIMIZE_UNUSED_DEVICE_VARIABLES ``

This option serves as a hint to enable the JIT compiler/linker to remove constant (**constant**) and device (**device**) variables unreferenced in device code (Disabled by default). Note that host references to constant and device variables using APIs like cuModuleGetGlobal() with this option specified may result in undefined behavior unless the variables are explicitly specified using CU_JIT_REFERENCED_VARIABLE_NAMES. Option type: int Applies to: link-time optimization specified with CU_JIT_LTO

`` Member CU_JIT_PREC_DIV ``

Control single-precision floating-point division and reciprocals (-prec-div) support (1: true, default). 1 : Enables the IEEE round-to-nearest mode 0 : Enables the fast approximation mode Option type: int Applies to: link-time optimization specified with CU_JIT_LTO

`` Member CU_JIT_PREC_SQRT ``

Control single-precision floating-point square root (-prec-sqrt) support (1: true, default). 1 : Enables the IEEE round-to-nearest mode 0 : Enables the fast approximation mode Option type: int Applies to: link-time optimization specified with CU_JIT_LTO

`` Member CU_JIT_REFERENCED_KERNEL_COUNT ``

Number of entries in CU_JIT_REFERENCED_KERNEL_NAMES array. Option type: unsigned int Applies to: dynamic linker only

`` Member CU_JIT_REFERENCED_KERNEL_NAMES ``

Array of kernel names that should be preserved at link time while others can be removed. Must contain CU_JIT_REFERENCED_KERNEL_COUNT entries. Note that kernel names can be mangled by the compiler in which case the mangled name needs to be specified. Wildcard “*” can be used to represent zero or more characters instead of specifying the full or mangled name. It is important to note that the wildcard “*” is also added implicitly. For example, specifying “foo” will match “foobaz”, “barfoo”, “barfoobaz” and thus preserve all kernels with those names. This can be avoided by providing a more specific name like “barfoobaz”. Option type: const char ** Applies to: dynamic linker only

`` Member CU_JIT_REFERENCED_VARIABLE_COUNT ``

Number of entries in CU_JIT_REFERENCED_VARIABLE_NAMES array. Option type: unsigned int Applies to: link-time optimization specified with CU_JIT_LTO

`` Member CU_JIT_REFERENCED_VARIABLE_NAMES ``

Array of variable names (**device** and/or **constant**) that should be preserved at link time while others can be removed. Must contain CU_JIT_REFERENCED_VARIABLE_COUNT entries. Note that variable names can be mangled by the compiler in which case the mangled name needs to be specified. Wildcard “*” can be used to represent zero or more characters instead of specifying the full or mangled name. It is important to note that the wildcard “*” is also added implicitly. For example, specifying “foo” will match “foobaz”, “barfoo”, “barfoobaz” and thus preserve all variables with those names. This can be avoided by providing a more specific name like “barfoobaz”. Option type: const char ** Applies to: link-time optimization specified with CU_JIT_LTO

`` Member cuCtxAttach  (CUcontext *pctx, unsigned int flags) ``

`` Member cuCtxDetach  (CUcontext ctx) ``

`` Member cuCtxGetSharedMemConfig  (CUsharedconfig *pConfig) ``

`` Member cuCtxSetSharedMemConfig  (CUsharedconfig config) ``

`` Member cuD3D10CtxCreate  (CUcontext *pCtx, CUdevice *pCudaDevice, unsigned int Flags, ID3D10Device *pD3DDevice) ``

This function is deprecated as of CUDA 5.0.

`` Member cuD3D10CtxCreateOnDevice  (CUcontext *pCtx, unsigned int flags, ID3D10Device *pD3DDevice, CUdevice cudaDevice) ``

This function is deprecated as of CUDA 5.0.

`` Member cuD3D10GetDirect3DDevice  (ID3D10Device **ppD3DDevice) ``

This function is deprecated as of CUDA 5.0.

`` Member cuD3D10MapResources  (unsigned int count, ID3D10Resource **ppResources) ``

This function is deprecated as of CUDA 3.0.

`` Member cuD3D10RegisterResource  (ID3D10Resource *pResource, unsigned int Flags) ``

This function is deprecated as of CUDA 3.0.

`` Member cuD3D10ResourceGetMappedArray  (CUarray *pArray, ID3D10Resource *pResource, unsigned int SubResource) ``

This function is deprecated as of CUDA 3.0.

`` Member cuD3D10ResourceGetMappedPitch  (size_t *pPitch, size_t *pPitchSlice, ID3D10Resource *pResource, unsigned int SubResource) ``

This function is deprecated as of CUDA 3.0.

`` Member cuD3D10ResourceGetMappedPointer  (CUdeviceptr *pDevPtr, ID3D10Resource *pResource, unsigned int SubResource) ``

This function is deprecated as of CUDA 3.0.

`` Member cuD3D10ResourceGetMappedSize  (size_t *pSize, ID3D10Resource *pResource, unsigned int SubResource) ``

This function is deprecated as of CUDA 3.0.

`` Member cuD3D10ResourceGetSurfaceDimensions  (size_t *pWidth, size_t *pHeight, size_t *pDepth, ID3D10Resource *pResource, unsigned int SubResource) ``

This function is deprecated as of CUDA 3.0.

`` Member cuD3D10ResourceSetMapFlags  (ID3D10Resource *pResource, unsigned int Flags) ``

This function is deprecated as of CUDA 3.0.

`` Member cuD3D10UnmapResources  (unsigned int count, ID3D10Resource **ppResources) ``

This function is deprecated as of CUDA 3.0.

`` Member cuD3D10UnregisterResource  (ID3D10Resource *pResource) ``

This function is deprecated as of CUDA 3.0.

`` Member cuD3D11CtxCreate  (CUcontext *pCtx, CUdevice *pCudaDevice, unsigned int Flags, ID3D11Device *pD3DDevice) ``

This function is deprecated as of CUDA 5.0.

`` Member cuD3D11CtxCreateOnDevice  (CUcontext *pCtx, unsigned int flags, ID3D11Device *pD3DDevice, CUdevice cudaDevice) ``

This function is deprecated as of CUDA 5.0.

`` Member cuD3D11GetDirect3DDevice  (ID3D11Device **ppD3DDevice) ``

This function is deprecated as of CUDA 5.0.

`` Member cuD3D9MapResources  (unsigned int count, IDirect3DResource9 **ppResource) ``

This function is deprecated as of CUDA 3.0.

`` Member cuD3D9RegisterResource  (IDirect3DResource9 *pResource, unsigned int Flags) ``

This function is deprecated as of CUDA 3.0.

`` Member cuD3D9ResourceGetMappedArray  (CUarray *pArray, IDirect3DResource9 *pResource, unsigned int Face, unsigned int Level) ``

This function is deprecated as of CUDA 3.0.

`` Member cuD3D9ResourceGetMappedPitch  (size_t *pPitch, size_t *pPitchSlice, IDirect3DResource9 *pResource, unsigned int Face, unsigned int Level) ``

This function is deprecated as of CUDA 3.0.

`` Member cuD3D9ResourceGetMappedPointer  (CUdeviceptr *pDevPtr, IDirect3DResource9 *pResource, unsigned int Face, unsigned int Level) ``

This function is deprecated as of CUDA 3.0.

`` Member cuD3D9ResourceGetMappedSize  (size_t *pSize, IDirect3DResource9 *pResource, unsigned int Face, unsigned int Level) ``

This function is deprecated as of CUDA 3.0.

`` Member cuD3D9ResourceGetSurfaceDimensions  (size_t *pWidth, size_t *pHeight, size_t *pDepth, IDirect3DResource9 *pResource, unsigned int Face, unsigned int Level) ``

This function is deprecated as of CUDA 3.0.

`` Member cuD3D9ResourceSetMapFlags  (IDirect3DResource9 *pResource, unsigned int Flags) ``

This function is deprecated as of Cuda 3.0.

`` Member cuD3D9UnmapResources  (unsigned int count, IDirect3DResource9 **ppResource) ``

This function is deprecated as of CUDA 3.0.

`` Member cuD3D9UnregisterResource  (IDirect3DResource9 *pResource) ``

This function is deprecated as of CUDA 3.0.

`` Member CUDA_ERROR_CONTEXT_ALREADY_CURRENT ``

This error return is deprecated as of CUDA 3.2. It is no longer an error to attempt to push the active context via cuCtxPushCurrent().

`` Member CUDA_ERROR_PROFILER_ALREADY_STARTED ``

This error return is deprecated as of CUDA 5.0. It is no longer an error to call cuProfilerStart() when profiling is already enabled.

`` Member CUDA_ERROR_PROFILER_ALREADY_STOPPED ``

This error return is deprecated as of CUDA 5.0. It is no longer an error to call cuProfilerStop() when profiling is already disabled.

`` Member CUDA_ERROR_PROFILER_NOT_INITIALIZED ``

This error return is deprecated as of CUDA 5.0. It is no longer an error to attempt to enable/disable the profiling via cuProfilerStart or cuProfilerStop without initialization.

`` Member cuDeviceComputeCapability  (int *major, int *minor, CUdevice dev) ``

`` Member cuDeviceGetProperties  (CUdevprop *prop, CUdevice dev) ``

`` Member cuFuncSetBlockShape  (CUfunction hfunc, int x, int y, int z) ``

`` Member cuFuncSetSharedMemConfig  (CUfunction hfunc, CUsharedconfig config) ``

`` Member cuFuncSetSharedSize  (CUfunction hfunc, unsigned int bytes) ``

`` Member cuGLCtxCreate  (CUcontext *pCtx, unsigned int Flags, CUdevice device) ``

This function is deprecated as of Cuda 5.0.

`` Member cuGLInit  (void) ``

This function is deprecated as of Cuda 3.0.

`` Member cuGLMapBufferObject  (CUdeviceptr *dptr, size_t *size, GLuint buffer) ``

This function is deprecated as of Cuda 3.0.

`` Member cuGLMapBufferObjectAsync  (CUdeviceptr *dptr, size_t *size, GLuint buffer, CUstream hStream) ``

This function is deprecated as of Cuda 3.0.

`` Member cuGLRegisterBufferObject  (GLuint buffer) ``

This function is deprecated as of Cuda 3.0.

`` Member cuGLSetBufferObjectMapFlags  (GLuint buffer, unsigned int Flags) ``

This function is deprecated as of Cuda 3.0.

`` Member cuGLUnmapBufferObject  (GLuint buffer) ``

This function is deprecated as of Cuda 3.0.

`` Member cuGLUnmapBufferObjectAsync  (GLuint buffer, CUstream hStream) ``

This function is deprecated as of Cuda 3.0.

`` Member cuGLUnregisterBufferObject  (GLuint buffer) ``

This function is deprecated as of Cuda 3.0.

`` Member cuLaunch  (CUfunction f) ``

`` Member cuLaunchCooperativeKernelMultiDevice  (CUDA_LAUNCH_PARAMS *launchParamsList, unsigned int numDevices, unsigned int flags) ``

This function is deprecated as of CUDA 11.3.

`` Member cuLaunchGrid  (CUfunction f, int grid_width, int grid_height) ``

`` Member cuLaunchGridAsync  (CUfunction f, int grid_width, int grid_height, CUstream hStream) ``

`` Member cuModuleGetSurfRef  (CUsurfref *pSurfRef, CUmodule hmod, const char *name) ``

`` Member cuModuleGetTexRef  (CUtexref *pTexRef, CUmodule hmod, const char *name) ``

`` Member cuParamSetf  (CUfunction hfunc, int offset, float value) ``

`` Member cuParamSeti  (CUfunction hfunc, int offset, unsigned int value) ``

`` Member cuParamSetSize  (CUfunction hfunc, unsigned int numbytes) ``

`` Member cuParamSetTexRef  (CUfunction hfunc, int texunit, CUtexref hTexRef) ``

`` Member cuParamSetv  (CUfunction hfunc, int offset, void *ptr, unsigned int numbytes) ``

`` Member cuProfilerInitialize  (const char *configFile, const char *outputFile, CUoutput_mode outputMode) ``

`` Member CUsharedconfig ``

`` Member cuSurfRefGetArray  (CUarray *phArray, CUsurfref hSurfRef) ``

`` Member cuSurfRefSetArray  (CUsurfref hSurfRef, CUarray hArray, unsigned int Flags) ``

`` Member cuTexRefCreate  (CUtexref *pTexRef) ``

`` Member cuTexRefDestroy  (CUtexref hTexRef) ``

`` Member cuTexRefGetAddress  (CUdeviceptr *pdptr, CUtexref hTexRef) ``

`` Member cuTexRefGetAddressMode  (CUaddress_mode *pam, CUtexref hTexRef, int dim) ``

`` Member cuTexRefGetArray  (CUarray *phArray, CUtexref hTexRef) ``

`` Member cuTexRefGetBorderColor  (float *pBorderColor, CUtexref hTexRef) ``

`` Member cuTexRefGetFilterMode  (CUfilter_mode *pfm, CUtexref hTexRef) ``

`` Member cuTexRefGetFlags  (unsigned int *pFlags, CUtexref hTexRef) ``

`` Member cuTexRefGetFormat  (CUarray_format *pFormat, int *pNumChannels, CUtexref hTexRef) ``

`` Member cuTexRefGetMaxAnisotropy  (int *pmaxAniso, CUtexref hTexRef) ``

`` Member cuTexRefGetMipmapFilterMode  (CUfilter_mode *pfm, CUtexref hTexRef) ``

`` Member cuTexRefGetMipmapLevelBias  (float *pbias, CUtexref hTexRef) ``

`` Member cuTexRefGetMipmapLevelClamp  (float *pminMipmapLevelClamp, float *pmaxMipmapLevelClamp, CUtexref hTexRef) ``

`` Member cuTexRefGetMipmappedArray  (CUmipmappedArray *phMipmappedArray, CUtexref hTexRef) ``

`` Member cuTexRefSetAddress  (size_t *ByteOffset, CUtexref hTexRef, CUdeviceptr dptr, size_t bytes) ``

`` Member cuTexRefSetAddress2D  (CUtexref hTexRef, const CUDA_ARRAY_DESCRIPTOR *desc, CUdeviceptr dptr, size_t Pitch) ``

`` Member cuTexRefSetAddressMode  (CUtexref hTexRef, int dim, CUaddress_mode am) ``

`` Member cuTexRefSetArray  (CUtexref hTexRef, CUarray hArray, unsigned int Flags) ``

`` Member cuTexRefSetBorderColor  (CUtexref hTexRef, float *pBorderColor) ``

`` Member cuTexRefSetFilterMode  (CUtexref hTexRef, CUfilter_mode fm) ``

`` Member cuTexRefSetFlags  (CUtexref hTexRef, unsigned int Flags) ``

`` Member cuTexRefSetFormat  (CUtexref hTexRef, CUarray_format fmt, int NumPackedComponents) ``

`` Member cuTexRefSetMaxAnisotropy  (CUtexref hTexRef, unsigned int maxAniso) ``

`` Member cuTexRefSetMipmapFilterMode  (CUtexref hTexRef, CUfilter_mode fm) ``

`` Member cuTexRefSetMipmapLevelBias  (CUtexref hTexRef, float bias) ``

`` Member cuTexRefSetMipmapLevelClamp  (CUtexref hTexRef, float minMipmapLevelClamp, float maxMipmapLevelClamp) ``

`` Member cuTexRefSetMipmappedArray  (CUtexref hTexRef, CUmipmappedArray hMipmappedArray, unsigned int Flags) ``
