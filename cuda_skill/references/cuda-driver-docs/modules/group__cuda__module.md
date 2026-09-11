<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/group__CUDA__MODULE.html

#  6.27. Module Management

This section describes the module management functions of the low-level CUDA driver application programming interface.

##  6.27.1. Enumerations

`` enum CUmoduleLoadingMode ``

CUDA Lazy Loading status.

_Values:_

`` enumerator CU_MODULE_EAGER_LOADING ``

Lazy Kernel Loading is not enabled.

`` enumerator CU_MODULE_LAZY_LOADING ``

Lazy Kernel Loading is enabled.

##  6.27.2. Functions

`` CUresult cuLinkAddData(CUlinkState state, CUjitInputType type, void *data, size_t size, const char *name, unsigned int numOptions, CUjit_option *options, void **optionValues) ``

Add an input to a pending linker invocation.

Ownership of `data` is retained by the caller. No reference is retained to any inputs after this call returns.

This method accepts only compiler options, which are used if the data must be compiled from PTX, and does not accept any of CU_JIT_WALL_TIME, CU_JIT_INFO_LOG_BUFFER, CU_JIT_ERROR_LOG_BUFFER, CU_JIT_TARGET_FROM_CUCONTEXT, or CU_JIT_TARGET.

See also

cuLinkCreate, cuLinkAddFile, cuLinkComplete, cuLinkDestroy

Note

For LTO-IR input, only LTO-IR compiled with toolkits prior to CUDA 12.0 will be accepted

Parameters

  * **state** – A pending linker action.

  * **type** – The type of the input data.

  * **data** – The input data. PTX must be NULL-terminated.

  * **size** – The length of the input data.

  * **name** – An optional name for this input in log messages.

  * **numOptions** – Size of options.

  * **options** – Options to be applied only for this input (overrides options from cuLinkCreate).

  * **optionValues** – Array of option values, each cast to void *.

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_HANDLE, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_INVALID_IMAGE, CUDA_ERROR_INVALID_PTX, CUDA_ERROR_UNSUPPORTED_PTX_VERSION, CUDA_ERROR_OUT_OF_MEMORY, CUDA_ERROR_NO_BINARY_FOR_GPU

`` CUresult cuLinkAddFile(CUlinkState state, CUjitInputType type, const char *path, unsigned int numOptions, CUjit_option *options, void **optionValues) ``

Add a file input to a pending linker invocation.

No reference is retained to any inputs after this call returns.

This method accepts only compiler options, which are used if the input must be compiled from PTX, and does not accept any of CU_JIT_WALL_TIME, CU_JIT_INFO_LOG_BUFFER, CU_JIT_ERROR_LOG_BUFFER, CU_JIT_TARGET_FROM_CUCONTEXT, or CU_JIT_TARGET.

This method is equivalent to invoking cuLinkAddData on the contents of the file.

See also

cuLinkCreate, cuLinkAddData, cuLinkComplete, cuLinkDestroy

Note

For LTO-IR input, only LTO-IR compiled with toolkits prior to CUDA 12.0 will be accepted

Parameters

  * **state** – A pending linker action

  * **type** – The type of the input data

  * **path** – Path to the input file

  * **numOptions** – Size of options

  * **options** – Options to be applied only for this input (overrides options from cuLinkCreate)

  * **optionValues** – Array of option values, each cast to void *

Returns

CUDA_SUCCESS, CUDA_ERROR_FILE_NOT_FOUND CUDA_ERROR_INVALID_HANDLE, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_INVALID_IMAGE, CUDA_ERROR_INVALID_PTX, CUDA_ERROR_UNSUPPORTED_PTX_VERSION, CUDA_ERROR_OUT_OF_MEMORY, CUDA_ERROR_NO_BINARY_FOR_GPU

`` CUresult cuLinkComplete(CUlinkState state, void **cubinOut, size_t *sizeOut) ``

Complete a pending linker invocation.

Completes the pending linker action and returns the cubin image for the linked device code, which can be used with cuModuleLoadData. The cubin is owned by `state`, so it should be loaded before `state` is destroyed via cuLinkDestroy. This call does not destroy `state`.

See also

cuLinkCreate, cuLinkAddData, cuLinkAddFile, cuLinkDestroy, cuModuleLoadData

Parameters

  * **state** – A pending linker invocation

  * **cubinOut** – On success, this will point to the output image

  * **sizeOut** – Optional parameter to receive the size of the generated image

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_HANDLE, CUDA_ERROR_OUT_OF_MEMORY

`` CUresult cuLinkCreate(unsigned int numOptions, CUjit_option *options, void **optionValues, CUlinkState *stateOut) ``

Creates a pending JIT linker invocation.

If the call is successful, the caller owns the returned CUlinkState, which should eventually be destroyed with cuLinkDestroy. The device code machine size (32 or 64 bit) will match the calling application.

Both linker and compiler options may be specified. Compiler options will be applied to inputs to this linker action which must be compiled from PTX. The options CU_JIT_WALL_TIME, CU_JIT_INFO_LOG_BUFFER_SIZE_BYTES, and CU_JIT_ERROR_LOG_BUFFER_SIZE_BYTES will accumulate data until the CUlinkState is destroyed.

The data passed in via cuLinkAddData and cuLinkAddFile will be treated as relocatable (-rdc=true to nvcc) when linking the final cubin during cuLinkComplete and will have similar consequences as offline relocatable device code linking.

`optionValues` must remain valid for the life of the CUlinkState if output options are used. No other references to inputs are maintained after this call returns.

See also

cuLinkAddData, cuLinkAddFile, cuLinkComplete, cuLinkDestroy

Note

For LTO-IR input, only LTO-IR compiled with toolkits prior to CUDA 12.0 will be accepted

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **numOptions** – Size of options arrays

  * **options** – Array of linker and compiler options

  * **optionValues** – Array of option values, each cast to void *

  * **stateOut** – On success, this will contain a CUlinkState to specify and complete this action

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_OUT_OF_MEMORY, CUDA_ERROR_JIT_COMPILER_NOT_FOUND

`` CUresult cuLinkDestroy(CUlinkState state) ``

Destroys state for a JIT linker invocation.

See also

cuLinkCreate

Parameters

**state** – State object for the linker invocation

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_HANDLE

`` CUresult cuModuleEnumerateFunctions(CUfunction *functions, unsigned int numFunctions, CUmodule mod) ``

Returns the function handles within a module.

Returns in `functions` a maximum number of `numFunctions` function handles within `mod`. When function loading mode is set to LAZY the function retrieved may be partially loaded. The loading state of a function can be queried using ::cuFunctionIsLoaded. CUDA APIs may load the function automatically when called with partially loaded function handle which may incur additional latency. Alternatively, ::cuFunctionLoad can be used to explicitly load a function. The returned function handles become invalid when the module is unloaded.

See also

cuModuleGetFunction, cuModuleGetFunctionCount, cuFuncIsLoaded, cuFuncLoad

Parameters

  * **functions** – - Buffer where the function handles are returned to

  * **numFunctions** – - Maximum number of function handles may be returned to the buffer

  * **mod** – - Module to query from

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_HANDLE, CUDA_ERROR_INVALID_VALUE

`` CUresult cuModuleGetFunction(CUfunction *hfunc, CUmodule hmod, const char *name) ``

Returns a function handle.

Returns in `*hfunc` the handle of the function of name `name` located in module `hmod`. If no function of that name exists, cuModuleGetFunction() returns CUDA_ERROR_NOT_FOUND.

See also

cuModuleGetGlobal, cuModuleGetTexRef, cuModuleLoad, cuModuleLoadData, cuModuleLoadDataEx, cuModuleLoadFatBinary, cuModuleUnload

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **hfunc** – - Returned function handle

  * **hmod** – - Module to retrieve function from

  * **name** – - Name of function to retrieve

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_NOT_FOUND

`` CUresult cuModuleGetFunctionCount(unsigned int *count, CUmodule mod) ``

Returns the number of functions within a module.

Returns in `count` the number of functions in `mod`.

Parameters

  * **count** – - Number of functions found within the module

  * **mod** – - Module to query

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_HANDLE, CUDA_ERROR_INVALID_VALUE

`` CUresult cuModuleGetGlobal(CUdeviceptr *dptr, size_t *bytes, CUmodule hmod, const char *name) ``

Returns a global pointer from a module.

Returns in `*dptr` and `*bytes` the base pointer and size of the global of name `name` located in module `hmod`. If no variable of that name exists, cuModuleGetGlobal() returns CUDA_ERROR_NOT_FOUND. One of the parameters `dptr` or `bytes` (not both) can be NULL in which case it is ignored.

See also

cuModuleGetFunction, cuModuleGetTexRef, cuModuleLoad, cuModuleLoadData, cuModuleLoadDataEx, cuModuleLoadFatBinary, cuModuleUnload, ::cudaGetSymbolAddress, ::cudaGetSymbolSize

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **dptr** – - Returned global device pointer

  * **bytes** – - Returned global size in bytes

  * **hmod** – - Module to retrieve global from

  * **name** – - Name of global to retrieve

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_NOT_FOUND

`` CUresult cuModuleGetLoadingMode(CUmoduleLoadingMode *mode) ``

Query lazy loading mode.

Returns lazy loading mode Module loading mode is controlled by CUDA_MODULE_LOADING env variable

See also

cuModuleLoad,

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

**mode** – - Returns the lazy loading mode

Returns

CUDA_SUCCESS, CUDA_ERROR_INVALID_VALUE,

`` CUresult cuModuleLoad(CUmodule *module, const char *fname) ``

Loads a compute module.

Takes a filename `fname` and loads the corresponding module `module` into the current context. The CUDA driver API does not attempt to lazily allocate the resources needed by a module; if the memory for functions and data (constant and global) needed by the module cannot be allocated, cuModuleLoad() fails. The file should be a _cubin_ file as output by **nvcc** , or a _PTX_ file either as output by **nvcc** or handwritten, or a _fatbin_ file as output by **nvcc** from toolchain 4.0 or later, or a _Tile_ IR file.

See also

cuModuleGetFunction, cuModuleGetGlobal, cuModuleGetTexRef, cuModuleLoadData, cuModuleLoadDataEx, cuModuleLoadFatBinary, cuModuleUnload

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **module** – - Returned module

  * **fname** – - Filename of module to load

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_INVALID_PTX, CUDA_ERROR_UNSUPPORTED_PTX_VERSION, CUDA_ERROR_NOT_FOUND, CUDA_ERROR_OUT_OF_MEMORY, CUDA_ERROR_FILE_NOT_FOUND, CUDA_ERROR_NO_BINARY_FOR_GPU, CUDA_ERROR_SHARED_OBJECT_SYMBOL_NOT_FOUND, CUDA_ERROR_SHARED_OBJECT_INIT_FAILED, CUDA_ERROR_JIT_COMPILER_NOT_FOUND

`` CUresult cuModuleLoadData(CUmodule *module, const void *image) ``

Load a module’s data.

Takes a pointer `image` and loads the corresponding module `module` into the current context. The `image` may be a _cubin_ or _fatbin_ as output by **nvcc** , or a NULL-terminated _PTX_ , either as output by **nvcc** or hand-written, or _Tile_ IR data.

See also

cuModuleGetFunction, cuModuleGetGlobal, cuModuleGetTexRef, cuModuleLoad, cuModuleLoadDataEx, cuModuleLoadFatBinary, cuModuleUnload

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **module** – - Returned module

  * **image** – - Module data to load

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_INVALID_PTX, CUDA_ERROR_UNSUPPORTED_PTX_VERSION, CUDA_ERROR_OUT_OF_MEMORY, CUDA_ERROR_NO_BINARY_FOR_GPU, CUDA_ERROR_SHARED_OBJECT_SYMBOL_NOT_FOUND, CUDA_ERROR_SHARED_OBJECT_INIT_FAILED, CUDA_ERROR_JIT_COMPILER_NOT_FOUND

`` CUresult cuModuleLoadDataEx(CUmodule *module, const void *image, unsigned int numOptions, CUjit_option *options, void **optionValues) ``

Load a module’s data with options.

Takes a pointer `image` and loads the corresponding module `module` into the current context. The `image` may be a _cubin_ or _fatbin_ as output by **nvcc** , or a NULL-terminated _PTX_ , either as output by **nvcc** or hand-written, or _Tile_ IR data.

See also

cuModuleGetFunction, cuModuleGetGlobal, cuModuleGetTexRef, cuModuleLoad, cuModuleLoadData, cuModuleLoadFatBinary, cuModuleUnload

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **module** – - Returned module

  * **image** – - Module data to load

  * **numOptions** – - Number of options

  * **options** – - Options for JIT

  * **optionValues** – - Option values for JIT

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_INVALID_PTX, CUDA_ERROR_UNSUPPORTED_PTX_VERSION, CUDA_ERROR_OUT_OF_MEMORY, CUDA_ERROR_NO_BINARY_FOR_GPU, CUDA_ERROR_SHARED_OBJECT_SYMBOL_NOT_FOUND, CUDA_ERROR_SHARED_OBJECT_INIT_FAILED, CUDA_ERROR_JIT_COMPILER_NOT_FOUND

`` CUresult cuModuleLoadFatBinary(CUmodule *module, const void *fatCubin) ``

Load a module’s data.

Takes a pointer `fatCubin` and loads the corresponding module `module` into the current context. The pointer represents a _fat binary_ object, which is a collection of different _cubin_ and/or _PTX_ files, all representing the same device code, but compiled and optimized for different architectures.

Prior to CUDA 4.0, there was no documented API for constructing and using fat binary objects by programmers. Starting with CUDA 4.0, fat binary objects can be constructed by providing the _-fatbin option_ to **nvcc**. More information can be found in the **nvcc** document.

See also

cuModuleGetFunction, cuModuleGetGlobal, cuModuleGetTexRef, cuModuleLoad, cuModuleLoadData, cuModuleLoadDataEx, cuModuleUnload

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **module** – - Returned module

  * **fatCubin** – - Fat binary to load

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_INVALID_PTX, CUDA_ERROR_UNSUPPORTED_PTX_VERSION, CUDA_ERROR_NOT_FOUND, CUDA_ERROR_OUT_OF_MEMORY, CUDA_ERROR_NO_BINARY_FOR_GPU, CUDA_ERROR_SHARED_OBJECT_SYMBOL_NOT_FOUND, CUDA_ERROR_SHARED_OBJECT_INIT_FAILED, CUDA_ERROR_JIT_COMPILER_NOT_FOUND

`` CUresult cuModuleUnload(CUmodule hmod) ``

Unloads a module.

Unloads a module `hmod` from the current context. Attempting to unload a module which was obtained from the Library Management API such as cuLibraryGetModule will return CUDA_ERROR_NOT_PERMITTED.

See also

cuModuleGetFunction, cuModuleGetGlobal, cuModuleGetTexRef, cuModuleLoad, cuModuleLoadData, cuModuleLoadDataEx, cuModuleLoadFatBinary

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Use of the handle after this call is undefined behavior.

Parameters

**hmod** – - Module to unload

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_NOT_PERMITTED
