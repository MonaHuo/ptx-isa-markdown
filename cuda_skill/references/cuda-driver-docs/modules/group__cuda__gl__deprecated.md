<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/group__CUDA__GL__DEPRECATED.html

#  6.31.1. OpenGL Interoperability [DEPRECATED]

This section describes deprecated OpenGL interoperability functionality.

##  6.31.1.1. Enumerations

`` enum CUGLmap_flags ``

Flags to map or unmap a resource.

_Values:_

`` enumerator CU_GL_MAP_RESOURCE_FLAGS_NONE ``

`` enumerator CU_GL_MAP_RESOURCE_FLAGS_READ_ONLY ``

`` enumerator CU_GL_MAP_RESOURCE_FLAGS_WRITE_DISCARD ``

##  6.31.1.2. Functions

`` CUresult cuGLCtxCreate(CUcontext *pCtx, unsigned int Flags, CUdevice device) ``

Create a CUDA context for interoperability with OpenGL.

`` Deprecated: ``

This function is deprecated as of Cuda 5.0.

This function is deprecated and should no longer be used. It is no longer necessary to associate a CUDA context with an OpenGL context in order to achieve maximum interoperability performance.

See also

cuCtxCreate, cuGLInit, cuGLMapBufferObject, cuGLRegisterBufferObject, cuGLUnmapBufferObject, cuGLUnregisterBufferObject, cuGLMapBufferObjectAsync, cuGLUnmapBufferObjectAsync, cuGLSetBufferObjectMapFlags, cuWGLGetDevice

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **pCtx** – - Returned CUDA context

  * **Flags** – - Options for CUDA context creation

  * **device** – - Device on which to create the context

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_OUT_OF_MEMORY

`` CUresult cuGLInit(void) ``

Initializes OpenGL interoperability.

`` Deprecated: ``

This function is deprecated as of Cuda 3.0.

Initializes OpenGL interoperability. This function is deprecated and calling it is no longer required. It may fail if the needed OpenGL driver facilities are not available.

See also

cuGLMapBufferObject, cuGLRegisterBufferObject, cuGLUnmapBufferObject, cuGLUnregisterBufferObject, cuGLMapBufferObjectAsync, cuGLUnmapBufferObjectAsync, cuGLSetBufferObjectMapFlags, cuWGLGetDevice

Note

Note that this function may also return error codes from previous, asynchronous launches.

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_UNKNOWN

`` CUresult cuGLMapBufferObject(CUdeviceptr *dptr, size_t *size, GLuint buffer) ``

Maps an OpenGL buffer object.

`` Deprecated: ``

This function is deprecated as of Cuda 3.0.

Maps the buffer object specified by `buffer` into the address space of the current CUDA context and returns in `*dptr` and `*size` the base pointer and size of the resulting mapping.

There must be a valid OpenGL context bound to the current thread when this function is called. This must be the same context, or a member of the same shareGroup, as the context that was bound when the buffer was registered.

All streams in the current CUDA context are synchronized with the current GL context.

See also

cuGraphicsMapResources

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **dptr** – - Returned mapped base pointer

  * **size** – - Returned size of mapping

  * **buffer** – - The name of the buffer object to map

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_MAP_FAILED

`` CUresult cuGLMapBufferObjectAsync(CUdeviceptr *dptr, size_t *size, GLuint buffer, CUstream hStream) ``

Maps an OpenGL buffer object.

`` Deprecated: ``

This function is deprecated as of Cuda 3.0.

Maps the buffer object specified by `buffer` into the address space of the current CUDA context and returns in `*dptr` and `*size` the base pointer and size of the resulting mapping.

There must be a valid OpenGL context bound to the current thread when this function is called. This must be the same context, or a member of the same shareGroup, as the context that was bound when the buffer was registered.

Stream `hStream` in the current CUDA context is synchronized with the current GL context.

See also

cuGraphicsMapResources

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **dptr** – - Returned mapped base pointer

  * **size** – - Returned size of mapping

  * **buffer** – - The name of the buffer object to map

  * **hStream** – - Stream to synchronize

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE, CUDA_ERROR_MAP_FAILED

`` CUresult cuGLRegisterBufferObject(GLuint buffer) ``

Registers an OpenGL buffer object.

`` Deprecated: ``

This function is deprecated as of Cuda 3.0.

Registers the buffer object specified by `buffer` for access by CUDA. This function must be called before CUDA can map the buffer object. There must be a valid OpenGL context bound to the current thread when this function is called, and the buffer name is resolved by that context.

See also

cuGraphicsGLRegisterBuffer

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

**buffer** – - The name of the buffer object to register.

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_ALREADY_MAPPED

`` CUresult cuGLSetBufferObjectMapFlags(GLuint buffer, unsigned int Flags) ``

Set the map flags for an OpenGL buffer object.

`` Deprecated: ``

This function is deprecated as of Cuda 3.0.

Sets the map flags for the buffer object specified by `buffer`.

Changes to `Flags` will take effect the next time `buffer` is mapped. The `Flags` argument may be any of the following:

  * CU_GL_MAP_RESOURCE_FLAGS_NONE: Specifies no hints about how this resource will be used. It is therefore assumed that this resource will be read from and written to by CUDA kernels. This is the default value.

  * CU_GL_MAP_RESOURCE_FLAGS_READ_ONLY: Specifies that CUDA kernels which access this resource will not write to this resource.

  * CU_GL_MAP_RESOURCE_FLAGS_WRITE_DISCARD: Specifies that CUDA kernels which access this resource will not read from this resource and will write over the entire contents of the resource, so none of the data previously stored in the resource will be preserved.

If `buffer` has not been registered for use with CUDA, then CUDA_ERROR_INVALID_HANDLE is returned. If `buffer` is presently mapped for access by CUDA, then CUDA_ERROR_ALREADY_MAPPED is returned.

There must be a valid OpenGL context bound to the current thread when this function is called. This must be the same context, or a member of the same shareGroup, as the context that was bound when the buffer was registered.

See also

cuGraphicsResourceSetMapFlags

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **buffer** – - Buffer object to unmap

  * **Flags** – - Map flags

Returns

CUDA_SUCCESS, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_HANDLE, CUDA_ERROR_ALREADY_MAPPED, CUDA_ERROR_INVALID_CONTEXT,

`` CUresult cuGLUnmapBufferObject(GLuint buffer) ``

Unmaps an OpenGL buffer object.

`` Deprecated: ``

This function is deprecated as of Cuda 3.0.

Unmaps the buffer object specified by `buffer` for access by CUDA.

There must be a valid OpenGL context bound to the current thread when this function is called. This must be the same context, or a member of the same shareGroup, as the context that was bound when the buffer was registered.

All streams in the current CUDA context are synchronized with the current GL context.

See also

cuGraphicsUnmapResources

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

**buffer** – - Buffer object to unmap

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE

`` CUresult cuGLUnmapBufferObjectAsync(GLuint buffer, CUstream hStream) ``

Unmaps an OpenGL buffer object.

`` Deprecated: ``

This function is deprecated as of Cuda 3.0.

Unmaps the buffer object specified by `buffer` for access by CUDA.

There must be a valid OpenGL context bound to the current thread when this function is called. This must be the same context, or a member of the same shareGroup, as the context that was bound when the buffer was registered.

Stream `hStream` in the current CUDA context is synchronized with the current GL context.

See also

cuGraphicsUnmapResources

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **buffer** – - Name of the buffer object to unmap

  * **hStream** – - Stream to synchronize

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE

`` CUresult cuGLUnregisterBufferObject(GLuint buffer) ``

Unregister an OpenGL buffer object.

`` Deprecated: ``

This function is deprecated as of Cuda 3.0.

Unregisters the buffer object specified by `buffer`. This releases any resources associated with the registered buffer. After this call, the buffer may no longer be mapped for access by CUDA.

There must be a valid OpenGL context bound to the current thread when this function is called. This must be the same context, or a member of the same shareGroup, as the context that was bound when the buffer was registered.

See also

cuGraphicsUnregisterResource

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

**buffer** – - Name of the buffer object to unregister

Returns

CUDA_SUCCESS, CUDA_ERROR_DEINITIALIZED, CUDA_ERROR_NOT_INITIALIZED, CUDA_ERROR_INVALID_CONTEXT, CUDA_ERROR_INVALID_VALUE
