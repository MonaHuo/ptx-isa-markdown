<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/group__CUDART__HIGHLEVEL.html

#  6.1. C++ API Routines

This section describes the C++ high level API functions of the CUDA runtime application programming interface. To use these functions, your application needs to be compiled with the `nvcc` compiler.

C++-style interface built on top of CUDA runtime API

Classes

__cudaOccupancyB2DHelper

Helper functor for cudaOccupancyMaxPotentialBlockSize.

##  6.1.1. Functions

`` template<class T>__host__ cudaChannelFormatDesc cudaCreateChannelDesc(void) ``

Returns a channel descriptor using the specified format.

Returns a channel descriptor with format `f` and number of bits of each component `x`, `y`, `z`, and `w`. The cudaChannelFormatDesc is defined as:

```cpp
struct cudaChannelFormatDesc {
  int x, y, z, w;
  enum cudaChannelFormatKind f;
};
```

where cudaChannelFormatKind is one of cudaChannelFormatKindSigned, cudaChannelFormatKindUnsigned, cudaChannelFormatKindFloat, cudaChannelFormatKindSignedNormalized8X1, cudaChannelFormatKindSignedNormalized8X2, cudaChannelFormatKindSignedNormalized8X4, cudaChannelFormatKindUnsignedNormalized8X1, cudaChannelFormatKindUnsignedNormalized8X2, cudaChannelFormatKindUnsignedNormalized8X4, cudaChannelFormatKindSignedNormalized16X1, cudaChannelFormatKindSignedNormalized16X2, cudaChannelFormatKindSignedNormalized16X4, cudaChannelFormatKindUnsignedNormalized16X1, cudaChannelFormatKindUnsignedNormalized16X2, cudaChannelFormatKindUnsignedNormalized16X4, cudaChannelFormatKindUnsignedNormalized1010102 or cudaChannelFormatKindNV12. cudaChannelFormatKindUnsigned8Packed422, cudaChannelFormatKindUnsigned8Packed444, cudaChannelFormatKindUnsigned8SemiPlanar420, cudaChannelFormatKindUnsigned16SemiPlanar420, cudaChannelFormatKindUnsigned8SemiPlanar422, cudaChannelFormatKindUnsigned16SemiPlanar422, cudaChannelFormatKindUnsigned8SemiPlanar444, cudaChannelFormatKindUnsigned16SemiPlanar444, cudaChannelFormatKindUnsigned8Planar420, cudaChannelFormatKindUnsigned16Planar420, cudaChannelFormatKindUnsigned8Planar422, cudaChannelFormatKindUnsigned16Planar422, cudaChannelFormatKindUnsigned8Planar444, and cudaChannelFormatKindUnsigned16Planar444.

The format is specified by the template specialization.

The template function specializes for the following scalar types: char, signed char, unsigned char, short, unsigned short, int, unsigned int, long, unsigned long, and float. The template function specializes for the following vector types: char{1|2|4}, uchar{1|2|4}, short{1|2|4}, ushort{1|2|4}, int{1|2|4}, uint{1|2|4}, long{1|2|4}, ulong{1|2|4}, float{1|2|4}. The template function specializes for following cudaChannelFormatKind enum values: cudaChannelFormatKind{Uns|S}ignedNormalized{8|16}X{1|2|4}, cudaChannelFormatKindUnsignedNormalized1010102 cudaChannelFormatKindNV12, cudaChannelFormatKindUnsigned8Packed422, cudaChannelFormatKindUnsigned8Packed444, cudaChannelFormatKindUnsigned8SemiPlanar420, cudaChannelFormatKindUnsigned16SemiPlanar420, cudaChannelFormatKindUnsigned8SemiPlanar422, cudaChannelFormatKindUnsigned16SemiPlanar422, cudaChannelFormatKindUnsigned8SemiPlanar444, cudaChannelFormatKindUnsigned16SemiPlanar444, cudaChannelFormatKindUnsigned8Planar420, cudaChannelFormatKindUnsigned16Planar420, cudaChannelFormatKindUnsigned8Planar422, cudaChannelFormatKindUnsigned16Planar422, cudaChannelFormatKindUnsigned8Planar444, and cudaChannelFormatKindUnsigned16Planar444.

Invoking the function on a type without a specialization defaults to creating a channel format of kind cudaChannelFormatKindNone

See also

cudaCreateChannelDesc (Low level), cudaGetChannelDesc,

Returns

Channel descriptor with format `f`

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<char>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<char1>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<char2>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<char4>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindNV12>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindSignedBlockCompressed4>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindSignedBlockCompressed5>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindSignedBlockCompressed6H>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindSignedNormalized16X1>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindSignedNormalized16X2>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindSignedNormalized16X4>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindSignedNormalized8X1>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindSignedNormalized8X2>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindSignedNormalized8X4>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsigned16Planar420>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsigned16Planar422>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsigned16Planar444>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsigned16SemiPlanar420>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsigned16SemiPlanar422>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsigned16SemiPlanar444>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsigned8Packed422>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsigned8Packed444>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsigned8Planar420>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsigned8Planar422>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsigned8Planar444>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsigned8SemiPlanar420>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsigned8SemiPlanar422>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsigned8SemiPlanar444>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsignedBlockCompressed1>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsignedBlockCompressed1SRGB>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsignedBlockCompressed2>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsignedBlockCompressed2SRGB>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsignedBlockCompressed3>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsignedBlockCompressed3SRGB>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsignedBlockCompressed4>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsignedBlockCompressed5>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsignedBlockCompressed6H>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsignedBlockCompressed7>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsignedBlockCompressed7SRGB>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsignedNormalized1010102>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsignedNormalized16X1>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsignedNormalized16X2>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsignedNormalized16X4>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsignedNormalized8X1>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsignedNormalized8X2>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<cudaChannelFormatKindUnsignedNormalized8X4>(void) ``

Warning

doxygenfunction: Unable to resolve function “cudaCreateChannelDesc< float >” with arguments “(void)”. Candidate function could not be parsed. Parsing error is Error when parsing function declaration. If the function has no return type: Error in declarator or parameters-and-qualifiers Invalid C++ declaration: Expected identifier in nested name, got keyword: else [error at 15] template<> else __host__ cudaChannelFormatDesc cudaCreateChannelDesc< float > (void) —————^ If the function has a return type: Invalid C++ declaration: Expected identifier in nested name, got keyword: else [error at 15] template<> else __host__ cudaChannelFormatDesc cudaCreateChannelDesc< float > (void) —————^

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<float1>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<float2>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<float4>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<int>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<int1>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<int2>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<int4>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<long>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<long1>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<long2>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<long4>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<short>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<short1>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<short2>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<short4>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<signed char>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<uchar1>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<uchar2>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<uchar4>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<uint1>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<uint2>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<uint4>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<ulong1>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<ulong2>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<ulong4>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<unsigned char>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<unsigned int>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<unsigned long>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<unsigned short>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<ushort1>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<ushort2>(void) ``

`` template<>__host__ cudaChannelFormatDesc cudaCreateChannelDesc<ushort4>(void) ``

`` __host__ cudaChannelFormatDesc cudaCreateChannelDescHalf(void) ``

`` __host__ cudaChannelFormatDesc cudaCreateChannelDescHalf1(void) ``

`` __host__ cudaChannelFormatDesc cudaCreateChannelDescHalf2(void) ``

`` __host__ cudaChannelFormatDesc cudaCreateChannelDescHalf4(void) ``

`` __host__ cudaChannelFormatDesc cudaCreateChannelDescNV12(void) ``

`` __host__ cudaError_t cudaEventCreate(cudaEvent_t *event, unsigned int flags) ``

Creates an event object with the specified flags.

Creates an event object with the specified flags. Valid flags include:

  * cudaEventDefault: Default event creation flag.

  * cudaEventBlockingSync: Specifies that event should use blocking synchronization. A host thread that uses cudaEventSynchronize() to wait on an event created with this flag will block until the event actually completes.

  * cudaEventDisableTiming: Specifies that the created event does not need to record timing data. Events created with this flag specified and the cudaEventBlockingSync flag not specified will provide the best performance when used with cudaStreamWaitEvent() and cudaEventQuery().

See also

cudaEventCreate (C API), cudaEventCreateWithFlags, cudaEventRecord, cudaEventQuery, cudaEventSynchronize, cudaEventDestroy, cudaEventElapsedTime, cudaStreamWaitEvent

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **event** – - Newly created event

  * **flags** – - Flags for new event

Returns

cudaSuccess, cudaErrorInvalidValue, cudaErrorLaunchFailure, cudaErrorMemoryAllocation

`` template<class T>__host__ cudaError_t cudaFuncGetAttributes(struct cudaFuncAttributes *attr, T *entry) ``

Find out attributes for a given function.

This function obtains the attributes of a function specified via `entry`. The parameter `entry` must be a pointer to a function that executes on the device. The parameter specified by `entry` must be declared as a `__global__` function. The fetched attributes are placed in `attr`. If the specified function does not exist, then cudaErrorInvalidDeviceFunction is returned.

Note that some function attributes such as maxThreadsPerBlock may vary based on the device that is currently being used.

cudaLaunchKernel (C++ API), cudaFuncSetCacheConfig (C++ API), cudaFuncGetAttributes (C API), ::cudaSetDoubleForDevice, ::cudaSetDoubleForHost

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Note

The API can also be used with a kernel cudaKernel_t by querying the handle using cudaLibraryGetKernel() or cudaGetKernel and then passing it to the API by casting to void*. The symbol `entryFuncAddr` passed to cudaGetKernel should be a symbol that is registered with the same CUDA Runtime instance.

Note

Passing a symbol that belongs that belongs to a different runtime instance will result in undefined behavior. The only type that can be reliably passed to a different runtime instance is cudaKernel_t

Parameters

  * **attr** – - Return pointer to function’s attributes

  * **entry** – - Function to get attributes of

Returns

cudaSuccess, cudaErrorInvalidDeviceFunction

`` template<class T>__host__ cudaError_t cudaFuncGetName(const char **name, T *func) ``

Returns the function name for a device entry function pointer.

Returns in `**name` the function name associated with the symbol `func` . The function name is returned as a null-terminated string. This API may return a mangled name if the function is not declared as having C linkage. If `**name` is NULL, cudaErrorInvalidValue is returned. If `func` is not a device entry function, cudaErrorInvalidDeviceFunction is returned.

cudaFuncGetName (C API)

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Note

The API can also be used with a kernel cudaKernel_t by querying the handle using cudaLibraryGetKernel() or cudaGetKernel and then passing it to the API by casting to void*. The symbol `entryFuncAddr` passed to cudaGetKernel should be a symbol that is registered with the same CUDA Runtime instance.

Note

Passing a symbol that belongs that belongs to a different runtime instance will result in undefined behavior. The only type that can be reliably passed to a different runtime instance is cudaKernel_t

Parameters

  * **name** – - The returned name of the function

  * **func** – - The function pointer to retrieve name for

Returns

cudaSuccess, cudaErrorInvalidValue, cudaErrorInvalidDeviceFunction

`` template<class T>__host__ cudaError_t cudaFuncSetAttribute(T *func, enum cudaFuncAttribute attr, int value) ``

Set attributes for a given function.

This function sets the attributes of a function specified via `entry`. The parameter `entry` must be a pointer to a function that executes on the device. The parameter specified by `entry` must be declared as a `__global__` function. The enumeration defined by `attr` is set to the value defined by `value`. If the specified function does not exist, then cudaErrorInvalidDeviceFunction is returned. If the specified attribute cannot be written, or if the value is incorrect, then cudaErrorInvalidValue is returned.

Valid values for `attr` are:

  * cudaFuncAttributeMaxDynamicSharedMemorySize \- The requested maximum size in bytes of dynamically-allocated shared memory. The sum of this value and the function attribute ::sharedSizeBytes cannot exceed the device attribute cudaDevAttrMaxSharedMemoryPerBlockOptin. The maximal size of requestable dynamic shared memory may differ by GPU architecture.

  * cudaFuncAttributePreferredSharedMemoryCarveout \- On devices where the L1 cache and shared memory use the same hardware resources, this sets the shared memory carveout preference, in percent of the total shared memory. See cudaDevAttrMaxSharedMemoryPerMultiprocessor. This is only a hint, and the driver can choose a different ratio if required to execute the function.

  * cudaFuncAttributeRequiredClusterWidth: The required cluster width in blocks. The width, height, and depth values must either all be 0 or all be positive. The validity of the cluster dimensions is checked at launch time. If the value is set during compile time, it cannot be set at runtime. Setting it at runtime will return cudaErrorNotPermitted.

  * cudaFuncAttributeRequiredClusterHeight: The required cluster height in blocks. The width, height, and depth values must either all be 0 or all be positive. The validity of the cluster dimensions is checked at launch time. If the value is set during compile time, it cannot be set at runtime. Setting it at runtime will return cudaErrorNotPermitted.

  * cudaFuncAttributeRequiredClusterDepth: The required cluster depth in blocks. The width, height, and depth values must either all be 0 or all be positive. The validity of the cluster dimensions is checked at launch time. If the value is set during compile time, it cannot be set at runtime. Setting it at runtime will return cudaErrorNotPermitted.

  * cudaFuncAttributeNonPortableClusterSizeAllowed: Indicates whether the function can be launched with non-portable cluster size. 1 is allowed, 0 is disallowed.

  * cudaFuncAttributeClusterSchedulingPolicyPreference: The block scheduling policy of a function. The value type is cudaClusterSchedulingPolicy.

cudaLaunchKernel (C++ API), cudaFuncSetCacheConfig (C++ API), cudaFuncGetAttributes (C API), ::cudaSetDoubleForDevice, ::cudaSetDoubleForHost

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Note

The API can also be used with a kernel cudaKernel_t by querying the handle using cudaLibraryGetKernel() or cudaGetKernel and then passing it to the API by casting to void*. The symbol `entryFuncAddr` passed to cudaGetKernel should be a symbol that is registered with the same CUDA Runtime instance.

Note

Passing a symbol that belongs that belongs to a different runtime instance will result in undefined behavior. The only type that can be reliably passed to a different runtime instance is cudaKernel_t

Parameters

  * **entry** – - Function to get attributes of

  * **attr** – - Attribute to set

  * **value** – - Value to set

Returns

cudaSuccess, cudaErrorInvalidDeviceFunction, cudaErrorInvalidValue

`` template<class T>__host__ cudaError_t cudaFuncSetCacheConfig(T *func, enum cudaFuncCache cacheConfig) ``

Sets the preferred cache configuration for a device function.

On devices where the L1 cache and shared memory use the same hardware resources, this sets through `cacheConfig` the preferred cache configuration for the function specified via `func`. This is only a preference. The runtime will use the requested configuration if possible, but it is free to choose a different configuration if required to execute `func`.

`func` must be a pointer to a function that executes on the device. The parameter specified by `func` must be declared as a `__global__` function. If the specified function does not exist, then cudaErrorInvalidDeviceFunction is returned.

This setting does nothing on devices where the size of the L1 cache and shared memory are fixed.

Launching a kernel with a different preference than the most recent preference setting may insert a device-side synchronization point.

The supported cache configurations are:

  * cudaFuncCachePreferNone: no preference for shared memory or L1 (default)

  * cudaFuncCachePreferShared: prefer larger shared memory and smaller L1 cache

  * cudaFuncCachePreferL1: prefer larger L1 cache and smaller shared memory

cudaLaunchKernel (C++ API), cudaFuncSetCacheConfig (C API), cudaFuncGetAttributes (C++ API), ::cudaSetDoubleForDevice, ::cudaSetDoubleForHost, ::cudaThreadGetCacheConfig, ::cudaThreadSetCacheConfig

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **func** – - device function pointer

  * **cacheConfig** – - Requested cache configuration

Returns

cudaSuccess, cudaErrorInvalidDeviceFunction

`` template<class T>__host__ cudaError_t cudaFuncSetSharedMemConfig(T *func, enum cudaSharedMemConfig config) ``

`` template<class T>__host__ cudaError_t cudaGetKernel(cudaKernel_t *kernelPtr, T *func) ``

Get pointer to device kernel that matches entry function `entryFuncAddr`.

Returns in `kernelPtr` the device kernel corresponding to the entry function `entryFuncAddr`.

See also

cudaGetKernel (C API)

Parameters

  * **kernelPtr** – - Returns the device kernel

  * **entryFuncAddr** – - Address of device entry function to search kernel for

Returns

cudaSuccess

`` template<class T>__host__ cudaError_t cudaGetSymbolAddress(void **devPtr, const T &symbol) ``

Finds the address associated with a CUDA symbol.

Returns in `*devPtr` the address of symbol `symbol` on the device. `symbol` can either be a variable that resides in global or constant memory space. If `symbol` cannot be found, or if `symbol` is not declared in the global or constant memory space, `*devPtr` is unchanged and the error cudaErrorInvalidSymbol is returned.

See also

cudaGetSymbolAddress (C API), cudaGetSymbolSize (C++ API)

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **devPtr** – - Return device pointer associated with symbol

  * **symbol** – - Device symbol reference

Returns

cudaSuccess, cudaErrorInvalidSymbol, cudaErrorNoKernelImageForDevice

`` template<class T>__host__ cudaError_t cudaGetSymbolSize(size_t *size, const T &symbol) ``

Finds the size of the object associated with a CUDA symbol.

Returns in `*size` the size of symbol `symbol`. `symbol` must be a variable that resides in global or constant memory space. If `symbol` cannot be found, or if `symbol` is not declared in global or constant memory space, `*size` is unchanged and the error cudaErrorInvalidSymbol is returned.

See also

cudaGetSymbolAddress (C++ API), cudaGetSymbolSize (C API)

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **size** – - Size of object associated with symbol

  * **symbol** – - Device symbol reference

Returns

cudaSuccess, cudaErrorInvalidSymbol, cudaErrorNoKernelImageForDevice

`` template<class T>__host__ cudaError_t cudaGraphAddMemcpyNodeFromSymbol(cudaGraphNode_t *pGraphNode, cudaGraph_t graph, const cudaGraphNode_t *pDependencies, size_t numDependencies, void *dst, const T &symbol, size_t count, size_t offset, enum cudaMemcpyKind kind) ``

Creates a memcpy node to copy from a symbol on the device and adds it to a graph.

Creates a new memcpy node to copy from `symbol` and adds it to `graph` with `numDependencies` dependencies specified via `pDependencies`. It is possible for `numDependencies` to be 0, in which case the node will be placed at the root of the graph. `pDependencies` may not have any duplicate entries. A handle to the new node will be returned in `pGraphNode`.

When the graph is launched, the node will copy `count` bytes from the memory area pointed to by `offset` bytes from the start of symbol `symbol` to the memory area pointed to by `dst`. The memory areas may not overlap. `symbol` is a variable that resides in global or constant memory space. `kind` can be either cudaMemcpyDeviceToHost, cudaMemcpyDeviceToDevice, or cudaMemcpyDefault. Passing cudaMemcpyDefault is recommended, in which case the type of transfer is inferred from the pointer values. However, cudaMemcpyDefault is only allowed on systems that support unified virtual addressing.

Memcpy nodes have some additional restrictions with regards to managed memory, if the system contains at least one device which has a zero value for the device attribute cudaDevAttrConcurrentManagedAccess.

See also

cudaMemcpyFromSymbol, cudaGraphAddMemcpyNode, cudaGraphAddMemcpyNodeToSymbol, cudaGraphMemcpyNodeGetParams, cudaGraphMemcpyNodeSetParams, cudaGraphMemcpyNodeSetParamsFromSymbol, cudaGraphMemcpyNodeSetParamsToSymbol, cudaGraphCreate, cudaGraphDestroyNode, cudaGraphAddChildGraphNode, cudaGraphAddEmptyNode, cudaGraphAddKernelNode, cudaGraphAddHostNode, cudaGraphAddMemsetNode

Note

Graph objects are not threadsafe. More here.

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **pGraphNode** – - Returns newly created node

  * **graph** – - Graph to which to add the node

  * **pDependencies** – - Dependencies of the node

  * **numDependencies** – - Number of dependencies

  * **dst** – - Destination memory address

  * **symbol** – - Device symbol address

  * **count** – - Size in bytes to copy

  * **offset** – - Offset from start of symbol in bytes

  * **kind** – - Type of transfer

Returns

cudaSuccess, cudaErrorInvalidValue

`` template<class T>__host__ cudaError_t cudaGraphAddMemcpyNodeToSymbol(cudaGraphNode_t *pGraphNode, cudaGraph_t graph, const cudaGraphNode_t *pDependencies, size_t numDependencies, const T &symbol, const void *src, size_t count, size_t offset, enum cudaMemcpyKind kind) ``

Creates a memcpy node to copy to a symbol on the device and adds it to a graph.

Creates a new memcpy node to copy to `symbol` and adds it to `graph` with `numDependencies` dependencies specified via `pDependencies`. It is possible for `numDependencies` to be 0, in which case the node will be placed at the root of the graph. `pDependencies` may not have any duplicate entries. A handle to the new node will be returned in `pGraphNode`.

When the graph is launched, the node will copy `count` bytes from the memory area pointed to by `src` to the memory area pointed to by `offset` bytes from the start of symbol `symbol`. The memory areas may not overlap. `symbol` is a variable that resides in global or constant memory space. `kind` can be either cudaMemcpyHostToDevice, cudaMemcpyDeviceToDevice, or cudaMemcpyDefault. Passing cudaMemcpyDefault is recommended, in which case the type of transfer is inferred from the pointer values. However, cudaMemcpyDefault is only allowed on systems that support unified virtual addressing.

Memcpy nodes have some additional restrictions with regards to managed memory, if the system contains at least one device which has a zero value for the device attribute cudaDevAttrConcurrentManagedAccess.

See also

cudaMemcpyToSymbol, cudaGraphAddMemcpyNode, cudaGraphAddMemcpyNodeFromSymbol, cudaGraphMemcpyNodeGetParams, cudaGraphMemcpyNodeSetParams, cudaGraphMemcpyNodeSetParamsToSymbol, cudaGraphMemcpyNodeSetParamsFromSymbol, cudaGraphCreate, cudaGraphDestroyNode, cudaGraphAddChildGraphNode, cudaGraphAddEmptyNode, cudaGraphAddKernelNode, cudaGraphAddHostNode, cudaGraphAddMemsetNode

Note

Graph objects are not threadsafe. More here.

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **pGraphNode** – - Returns newly created node

  * **graph** – - Graph to which to add the node

  * **pDependencies** – - Dependencies of the node

  * **numDependencies** – - Number of dependencies

  * **symbol** – - Device symbol address

  * **src** – - Source memory address

  * **count** – - Size in bytes to copy

  * **offset** – - Offset from start of symbol in bytes

  * **kind** – - Type of transfer

Returns

cudaSuccess, cudaErrorInvalidValue

`` template<class T>__host__ cudaError_t cudaGraphExecMemcpyNodeSetParamsFromSymbol(cudaGraphExec_t hGraphExec, cudaGraphNode_t node, void *dst, const T &symbol, size_t count, size_t offset, enum cudaMemcpyKind kind) ``

Sets the parameters for a memcpy node in the given graphExec to copy from a symbol on the device.

Updates the work represented by `node` in `hGraphExec` as though `node` had contained the given params at instantiation. `node` must remain in the graph which was used to instantiate `hGraphExec`. Changed edges to and from `node` are ignored.

`symbol` and `dst` must be allocated from the same contexts as the original source and destination memory. The instantiation-time memory operands must be 1-dimensional. Zero-length operations are not supported.

The modifications only affect future launches of `hGraphExec`. Already enqueued or running launches of `hGraphExec` are not affected by this call. `node` is also not modified by this call.

Returns cudaErrorInvalidValue if the memory operands’ mappings changed or the original memory operands are multidimensional.

See also

cudaGraphAddMemcpyNode, cudaGraphAddMemcpyNodeFromSymbol, cudaGraphMemcpyNodeSetParams, cudaGraphMemcpyNodeSetParamsFromSymbol, cudaGraphInstantiate, cudaGraphExecMemcpyNodeSetParams, cudaGraphExecMemcpyNodeSetParamsToSymbol, cudaGraphExecKernelNodeSetParams, cudaGraphExecMemsetNodeSetParams, cudaGraphExecHostNodeSetParams

Note

Graph objects are not threadsafe. More here.

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **hGraphExec** – - The executable graph in which to set the specified node

  * **node** – - Memcpy node from the graph which was used to instantiate graphExec

  * **dst** – - Destination memory address

  * **symbol** – - Device symbol address

  * **count** – - Size in bytes to copy

  * **offset** – - Offset from start of symbol in bytes

  * **kind** – - Type of transfer

Returns

cudaSuccess, cudaErrorInvalidValue

`` template<class T>__host__ cudaError_t cudaGraphExecMemcpyNodeSetParamsToSymbol(cudaGraphExec_t hGraphExec, cudaGraphNode_t node, const T &symbol, const void *src, size_t count, size_t offset, enum cudaMemcpyKind kind) ``

Sets the parameters for a memcpy node in the given graphExec to copy to a symbol on the device.

Updates the work represented by `node` in `hGraphExec` as though `node` had contained the given params at instantiation. `node` must remain in the graph which was used to instantiate `hGraphExec`. Changed edges to and from `node` are ignored.

`src` and `symbol` must be allocated from the same contexts as the original source and destination memory. The instantiation-time memory operands must be 1-dimensional. Zero-length operations are not supported.

The modifications only affect future launches of `hGraphExec`. Already enqueued or running launches of `hGraphExec` are not affected by this call. `node` is also not modified by this call.

Returns cudaErrorInvalidValue if the memory operands’ mappings changed or the original memory operands are multidimensional.

See also

cudaGraphAddMemcpyNode, cudaGraphAddMemcpyNodeToSymbol, cudaGraphMemcpyNodeSetParams, cudaGraphMemcpyNodeSetParamsToSymbol, cudaGraphInstantiate, cudaGraphExecMemcpyNodeSetParams, cudaGraphExecMemcpyNodeSetParamsFromSymbol, cudaGraphExecKernelNodeSetParams, cudaGraphExecMemsetNodeSetParams, cudaGraphExecHostNodeSetParams

Note

Graph objects are not threadsafe. More here.

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **hGraphExec** – - The executable graph in which to set the specified node

  * **node** – - Memcpy node from the graph which was used to instantiate graphExec

  * **symbol** – - Device symbol address

  * **src** – - Source memory address

  * **count** – - Size in bytes to copy

  * **offset** – - Offset from start of symbol in bytes

  * **kind** – - Type of transfer

Returns

cudaSuccess, cudaErrorInvalidValue

`` __host__ cudaError_t cudaGraphExecUpdate(cudaGraphExec_t hGraphExec, cudaGraph_t hGraph, cudaGraphNode_t *hErrorNode_out, enum cudaGraphExecUpdateResult *updateResult_out) ``

`` __host__ cudaError_t cudaGraphInstantiate(cudaGraphExec_t *pGraphExec, cudaGraph_t graph, cudaGraphNode_t *pErrorNode, char *pLogBuffer, size_t bufferSize) ``

Creates an executable graph from a graph.

Instantiates `graph` as an executable graph. The graph is validated for any structural constraints or intra-node constraints which were not previously validated. If instantiation is successful, a handle to the instantiated graph is returned in `pGraphExec`.

If there are any errors, diagnostic information may be returned in `pErrorNode` and `pLogBuffer`. This is the primary way to inspect instantiation errors. The output will be null terminated unless the diagnostics overflow the buffer. In this case, they will be truncated, and the last byte can be inspected to determine if truncation occurred.

See also

cudaGraphInstantiateWithFlags, cudaGraphCreate, cudaGraphUpload, cudaGraphLaunch, cudaGraphExecDestroy

Note

Graph objects are not threadsafe. More here.

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **pGraphExec** – - Returns instantiated graph

  * **graph** – - Graph to instantiate

  * **pErrorNode** – - In case of an instantiation error, this may be modified to indicate a node contributing to the error

  * **pLogBuffer** – - A character buffer to store diagnostic messages

  * **bufferSize** – - Size of the log buffer in bytes

Returns

cudaSuccess, cudaErrorInvalidValue

`` template<class T>__host__ cudaError_t cudaGraphMemcpyNodeSetParamsFromSymbol(cudaGraphNode_t node, void *dst, const T &symbol, size_t count, size_t offset, enum cudaMemcpyKind kind) ``

Sets a memcpy node’s parameters to copy from a symbol on the device.

Sets the parameters of memcpy node `node` to the copy described by the provided parameters.

When the graph is launched, the node will copy `count` bytes from the memory area pointed to by `offset` bytes from the start of symbol `symbol` to the memory area pointed to by `dst`. The memory areas may not overlap. `symbol` is a variable that resides in global or constant memory space. `kind` can be either cudaMemcpyDeviceToHost, cudaMemcpyDeviceToDevice, or cudaMemcpyDefault. Passing cudaMemcpyDefault is recommended, in which case the type of transfer is inferred from the pointer values. However, cudaMemcpyDefault is only allowed on systems that support unified virtual addressing.

See also

cudaMemcpyFromSymbol, cudaGraphMemcpyNodeSetParams, cudaGraphMemcpyNodeSetParamsToSymbol, cudaGraphAddMemcpyNode, cudaGraphMemcpyNodeGetParams

Note

Graph objects are not threadsafe. More here.

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **node** – - Node to set the parameters for

  * **dst** – - Destination memory address

  * **symbol** – - Device symbol address

  * **count** – - Size in bytes to copy

  * **offset** – - Offset from start of symbol in bytes

  * **kind** – - Type of transfer

Returns

cudaSuccess, cudaErrorInvalidValue

`` template<class T>__host__ cudaError_t cudaGraphMemcpyNodeSetParamsToSymbol(cudaGraphNode_t node, const T &symbol, const void *src, size_t count, size_t offset, enum cudaMemcpyKind kind) ``

Sets a memcpy node’s parameters to copy to a symbol on the device.

Sets the parameters of memcpy node `node` to the copy described by the provided parameters.

When the graph is launched, the node will copy `count` bytes from the memory area pointed to by `src` to the memory area pointed to by `offset` bytes from the start of symbol `symbol`. The memory areas may not overlap. `symbol` is a variable that resides in global or constant memory space. `kind` can be either cudaMemcpyHostToDevice, cudaMemcpyDeviceToDevice, or cudaMemcpyDefault. Passing cudaMemcpyDefault is recommended, in which case the type of transfer is inferred from the pointer values. However, cudaMemcpyDefault is only allowed on systems that support unified virtual addressing.

See also

cudaMemcpyToSymbol, cudaGraphMemcpyNodeSetParams, cudaGraphMemcpyNodeSetParamsFromSymbol, cudaGraphAddMemcpyNode, cudaGraphMemcpyNodeGetParams

Note

Graph objects are not threadsafe. More here.

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **node** – - Node to set the parameters for

  * **symbol** – - Device symbol address

  * **src** – - Source memory address

  * **count** – - Size in bytes to copy

  * **offset** – - Offset from start of symbol in bytes

  * **kind** – - Type of transfer

Returns

cudaSuccess, cudaErrorInvalidValue

`` template<class T>__host__ cudaError_t cudaHostAlloc(T **ptr, size_t size, unsigned int flags) ``

`` template<class T>__host__ cudaError_t cudaHostGetDevicePointer(T **pDevice, void *pHost, unsigned int flags) ``

`` template<class T>__host__ cudaError_t cudaLaunchCooperativeKernel(T *func, dim3 gridDim, dim3 blockDim, void **args, size_t sharedMem = 0, cudaStream_t stream = 0) ``

Launches a device function.

The function invokes kernel `func` on `gridDim` (`gridDim.x``gridDim.y``gridDim.z`) grid of blocks. Each block contains `blockDim` (`blockDim.x``blockDim.y``blockDim.z`) threads.

The device on which this kernel is invoked must have a non-zero value for the device attribute cudaDevAttrCooperativeLaunch.

The total number of blocks launched cannot exceed the maximum number of blocks per multiprocessor as returned by cudaOccupancyMaxActiveBlocksPerMultiprocessor (or cudaOccupancyMaxActiveBlocksPerMultiprocessorWithFlags) times the number of multiprocessors as specified by the device attribute cudaDevAttrMultiProcessorCount.

The kernel cannot make use of CUDA dynamic parallelism.

If the kernel has N parameters the `args` should point to array of N pointers. Each pointer, from `args[0]` to `args[N - 1]`, point to the region of memory from which the actual parameter will be copied.

`sharedMem` sets the amount of dynamic shared memory that will be available to each thread block.

`stream` specifies a stream the invocation is associated to.

cudaLaunchCooperativeKernel (C API)

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

This function exhibits asynchronous behavior for most use cases.

Note

This function uses standard default stream semantics.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Note

The API can also be used with a kernel cudaKernel_t by querying the handle using cudaLibraryGetKernel() or cudaGetKernel and then passing it to the API by casting to void*. The symbol `entryFuncAddr` passed to cudaGetKernel should be a symbol that is registered with the same CUDA Runtime instance.

Note

Passing a symbol that belongs that belongs to a different runtime instance will result in undefined behavior. The only type that can be reliably passed to a different runtime instance is cudaKernel_t

Parameters

  * **func** – - Device function symbol

  * **gridDim** – - Grid dimentions

  * **blockDim** – - Block dimentions

  * **args** – - Arguments

  * **sharedMem** – - Shared memory (defaults to 0)

  * **stream** – - Stream identifier (defaults to NULL)

Returns

cudaSuccess, cudaErrorInvalidDeviceFunction, cudaErrorInvalidConfiguration, cudaErrorLaunchFailure, cudaErrorLaunchTimeout, cudaErrorLaunchOutOfResources, cudaErrorSharedObjectInitFailed

`` template<class T>__host__ cudaError_t cudaLaunchKernel(T *func, dim3 gridDim, dim3 blockDim, void **args, size_t sharedMem = 0, cudaStream_t stream = 0) ``

Launches a device function.

The function invokes kernel `func` on `gridDim` (`gridDim.x``gridDim.y``gridDim.z`) grid of blocks. Each block contains `blockDim` (`blockDim.x``blockDim.y``blockDim.z`) threads.

If the kernel has N parameters the `args` should point to array of N pointers. Each pointer, from `args[0]` to `args[N - 1]`, point to the region of memory from which the actual parameter will be copied.

`sharedMem` sets the amount of dynamic shared memory that will be available to each thread block.

`stream` specifies a stream the invocation is associated to.

cudaLaunchKernel (C API)

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

This function exhibits asynchronous behavior for most use cases.

Note

This function uses standard default stream semantics.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Note

The API can also be used with a kernel cudaKernel_t by querying the handle using cudaLibraryGetKernel() or cudaGetKernel and then passing it to the API by casting to void*. The symbol `entryFuncAddr` passed to cudaGetKernel should be a symbol that is registered with the same CUDA Runtime instance.

Note

Passing a symbol that belongs that belongs to a different runtime instance will result in undefined behavior. The only type that can be reliably passed to a different runtime instance is cudaKernel_t

Parameters

  * **func** – - Device function symbol

  * **gridDim** – - Grid dimentions

  * **blockDim** – - Block dimentions

  * **args** – - Arguments

  * **sharedMem** – - Shared memory (defaults to 0)

  * **stream** – - Stream identifier (defaults to NULL)

Returns

cudaSuccess, cudaErrorInvalidDeviceFunction, cudaErrorInvalidConfiguration, cudaErrorLaunchFailure, cudaErrorLaunchTimeout, cudaErrorLaunchOutOfResources, cudaErrorSharedObjectInitFailed, cudaErrorInvalidPtx, cudaErrorUnsupportedPtxVersion, cudaErrorNoKernelImageForDevice, cudaErrorJitCompilerNotFound, cudaErrorJitCompilationDisabled

`` template<typename ...ActTypes>__host__ cudaError_t cudaLaunchKernelEx(const cudaLaunchConfig_t *config, const cudaKernel_t kernel, ActTypes&&... args) ``

Launches a CUDA function with launch-time configuration.

Invokes the kernel `kernel` on `config->gridDim` (`config->gridDim.x``config->gridDim.y``config->gridDim.z`) grid of blocks. Each block contains `config->blockDim` (`config->blockDim.x``config->blockDim.y``config->blockDim.z`) threads.

`config->dynamicSmemBytes` sets the amount of dynamic shared memory that will be available to each thread block.

`config->stream` specifies a stream the invocation is associated to.

Configuration beyond grid and block dimensions, dynamic shared memory size, and stream can be provided with the following two fields of `config:`

`config->attrs` is an array of `config->numAttrs` contiguous cudaLaunchAttribute elements. The value of this pointer is not considered if `config->numAttrs` is zero. However, in that case, it is recommended to set the pointer to NULL. `config->numAttrs` is the number of attributes populating the first `config->numAttrs` positions of the `config->attrs` array.

The kernel arguments should be passed as arguments to this function via the `args` parameter pack.

The C API version of this function, `cudaLaunchKernelExC`, is also available for pre-C++11 compilers and for use cases where the ability to pass kernel parameters via void* array is preferable.

See also

cudaLaunchKernelEx (C API), ::cuLaunchKernelEx

Note

This function uses standard default stream semantics.

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **config** – - Launch configuration

  * **func** – - Kernel to launch

  * **args** – - Parameter pack of kernel parameters

Returns

cudaSuccess, cudaErrorInvalidDeviceFunction, cudaErrorInvalidConfiguration, cudaErrorLaunchFailure, cudaErrorLaunchTimeout, cudaErrorLaunchOutOfResources, cudaErrorSharedObjectInitFailed, cudaErrorInvalidPtx, cudaErrorUnsupportedPtxVersion, cudaErrorNoKernelImageForDevice, cudaErrorJitCompilerNotFound, cudaErrorJitCompilationDisabled

`` template<typename ...ExpTypes, typename ...ActTypes>__host__ cudaError_t cudaLaunchKernelEx(const cudaLaunchConfig_t *config, void (*kernel)(ExpTypes...), ActTypes&&... args) ``

Launches a CUDA function with launch-time configuration.

Invokes the kernel `kernel` on `config->gridDim` (`config->gridDim.x``config->gridDim.y``config->gridDim.z`) grid of blocks. Each block contains `config->blockDim` (`config->blockDim.x``config->blockDim.y``config->blockDim.z`) threads.

`config->dynamicSmemBytes` sets the amount of dynamic shared memory that will be available to each thread block.

`config->stream` specifies a stream the invocation is associated to.

Configuration beyond grid and block dimensions, dynamic shared memory size, and stream can be provided with the following two fields of `config:`

`config->attrs` is an array of `config->numAttrs` contiguous cudaLaunchAttribute elements. The value of this pointer is not considered if `config->numAttrs` is zero. However, in that case, it is recommended to set the pointer to NULL. `config->numAttrs` is the number of attributes populating the first `config->numAttrs` positions of the `config->attrs` array.

The kernel arguments should be passed as arguments to this function via the `args` parameter pack.

The C API version of this function, `cudaLaunchKernelExC`, is also available for pre-C++11 compilers and for use cases where the ability to pass kernel parameters via void* array is preferable.

See also

cudaLaunchKernelEx (C API), ::cuLaunchKernelEx

Note

This function uses standard default stream semantics.

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Note

The API can also be used with a kernel cudaKernel_t by querying the handle using cudaLibraryGetKernel() or cudaGetKernel and then passing it to the API by casting to void*. The symbol `entryFuncAddr` passed to cudaGetKernel should be a symbol that is registered with the same CUDA Runtime instance.

Note

Passing a symbol that belongs that belongs to a different runtime instance will result in undefined behavior. The only type that can be reliably passed to a different runtime instance is cudaKernel_t

Parameters

  * **config** – - Launch configuration

  * **kernel** – - Kernel to launch

  * **args** – - Parameter pack of kernel parameters

Returns

cudaSuccess, cudaErrorInvalidDeviceFunction, cudaErrorInvalidConfiguration, cudaErrorLaunchFailure, cudaErrorLaunchTimeout, cudaErrorLaunchOutOfResources, cudaErrorSharedObjectInitFailed, cudaErrorInvalidPtx, cudaErrorUnsupportedPtxVersion, cudaErrorNoKernelImageForDevice, cudaErrorJitCompilerNotFound, cudaErrorJitCompilationDisabled

`` template<class T>__host__ cudaError_t cudaLibraryGetGlobal(T **dptr, size_t *bytes, cudaLibrary_t library, const char *name) ``

Returns a global device pointer.

Returns in `*dptr` and `*bytes` the base pointer and size of the global with name `name` for the requested library `library` and the current device. If no global for the requested name `name` exists, the call returns cudaErrorSymbolNotFound. One of the parameters `dptr` or `bytes` (not both) can be NULL in which case it is ignored.

See also

cudaLibraryLoadData, cudaLibraryLoadFromFile, cudaLibraryUnload, cudaLibraryGetManaged

Parameters

  * **dptr** – - Returned global device pointer for the requested library

  * **bytes** – - Returned global size in bytes

  * **library** – - Library to retrieve global from

  * **name** – - Name of global to retrieve

Returns

cudaSuccess, cudaErrorCudartUnloading, cudaErrorInitializationError, cudaErrorInvalidValue, cudaErrorInvalidResourceHandle, cudaErrorSymbolNotFound cudaErrorDeviceUninitialized, cudaErrorContextIsDestroyed

`` template<class T>__host__ cudaError_t cudaLibraryGetManaged(T **dptr, size_t *bytes, cudaLibrary_t library, const char *name) ``

Returns a pointer to managed memory.

Returns in `*dptr` and `*bytes` the base pointer and size of the managed memory with name `name` for the requested library `library`. If no managed memory with the requested name `name` exists, the call returns cudaErrorSymbolNotFound. One of the parameters `dptr` or `bytes` (not both) can be NULL in which case it is ignored. Note that managed memory for library `library` is shared across devices and is registered when the library is loaded.

See also

cudaLibraryLoadData, cudaLibraryLoadFromFile, cudaLibraryUnload, cudaLibraryGetGlobal

Parameters

  * **dptr** – - Returned pointer to the managed memory

  * **bytes** – - Returned memory size in bytes

  * **library** – - Library to retrieve managed memory from

  * **name** – - Name of managed memory to retrieve

Returns

cudaSuccess, cudaErrorCudartUnloading, cudaErrorInitializationError, cudaErrorInvalidValue, cudaErrorInvalidResourceHandle, cudaErrorSymbolNotFound

`` template<class T>__host__ cudaError_t cudaLibraryGetUnifiedFunction(T **fptr, cudaLibrary_t library, const char *symbol) ``

Returns a pointer to a unified function.

Returns in `*fptr` the function pointer to a unified function denoted by `symbol`. If no unified function with name `symbol` exists, the call returns cudaErrorSymbolNotFound. If there is no device with attribute cudaDeviceProp::unifiedFunctionPointers present in the system, the call may return cudaErrorSymbolNotFound.

See also

cudaLibraryLoadData, cudaLibraryLoadFromFile, cudaLibraryUnload

Parameters

  * **fptr** – - Returned pointer to a unified function

  * **library** – - Library to retrieve function pointer memory from

  * **symbol** – - Name of function pointer to retrieve

Returns

cudaSuccess, cudaErrorCudartUnloading, cudaErrorInitializationError, cudaErrorInvalidValue, cudaErrorInvalidResourceHandle, cudaErrorSymbolNotFound

`` template<class T>__host__ cudaError_t cudaMalloc(T **devPtr, size_t size) ``

`` template<class T>__host__ cudaError_t cudaMallocAsync(T **ptr, size_t size, cudaStream_t stream) ``

`` __host__ cudaError_t cudaMallocAsync(void **ptr, size_t size, cudaMemPool_t memPool, cudaStream_t stream) ``

Allocate from a pool.

This is an alternate spelling for cudaMallocFromPoolAsync made available through function overloading.

See also

cudaMallocFromPoolAsync, cudaMallocAsync (C API)

`` template<class T>__host__ cudaError_t cudaMallocAsync(T **ptr, size_t size, cudaMemPool_t memPool, cudaStream_t stream) ``

`` template<class T>__host__ cudaError_t cudaMallocFromPoolAsync(T **ptr, size_t size, cudaMemPool_t memPool, cudaStream_t stream) ``

`` template<class T>__host__ cudaError_t cudaMallocHost(T **ptr, size_t size, unsigned int flags = 0) ``

`` __host__ cudaError_t cudaMallocHost(void **ptr, size_t size, unsigned int flags) ``

Allocates page-locked memory on the host.

Allocates `size` bytes of host memory that is page-locked and accessible to the device. The driver tracks the virtual memory ranges allocated with this function and automatically accelerates calls to functions such as cudaMemcpy(). Since the memory can be accessed directly by the device, it can be read or written with much higher bandwidth than pageable memory obtained with functions such as ::malloc(). Allocating excessive amounts of pinned memory may degrade system performance, since it reduces the amount of memory available to the system for paging. As a result, this function is best used sparingly to allocate staging areas for data exchange between host and device.

The `flags` parameter enables different options to be specified that affect the allocation, as follows.

  * cudaHostAllocDefault: This flag’s value is defined to be 0.

  * cudaHostAllocPortable: The memory returned by this call will be considered as pinned memory by all CUDA contexts, not just the one that performed the allocation.

  * cudaHostAllocMapped: Maps the allocation into the CUDA address space. The device pointer to the memory may be obtained by calling cudaHostGetDevicePointer().

  * cudaHostAllocWriteCombined: Allocates the memory as write-combined (WC). WC memory can be transferred across the PCI Express bus more quickly on some system configurations, but cannot be read efficiently by most CPUs. WC memory is a good option for buffers that will be written by the CPU and read by the device via mapped pinned memory or host->device transfers.

All of these flags are orthogonal to one another: a developer may allocate memory that is portable, mapped and/or write-combined with no restrictions.

cudaSetDeviceFlags() must have been called with the cudaDeviceMapHost flag in order for the cudaHostAllocMapped flag to have any effect.

The cudaHostAllocMapped flag may be specified on CUDA contexts for devices that do not support mapped pinned memory. The failure is deferred to cudaHostGetDevicePointer() because the memory may be mapped into other CUDA contexts via the cudaHostAllocPortable flag.

Memory allocated by this function must be freed with cudaFreeHost().

See also

cudaSetDeviceFlags, cudaMallocHost (C API), cudaFreeHost, cudaHostAlloc

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **ptr** – - Device pointer to allocated memory

  * **size** – - Requested allocation size in bytes

  * **flags** – - Requested properties of allocated memory

Returns

cudaSuccess, cudaErrorMemoryAllocation

`` template<class T>__host__ cudaError_t cudaMallocManaged(T **devPtr, size_t size, unsigned int flags = 0x01) ``

Allocates memory that will be automatically managed by the Unified Memory system.

Allocates `size` bytes of managed memory on the device and returns in `*devPtr` a pointer to the allocated memory. If the device doesn’t support allocating managed memory, cudaErrorNotSupported is returned. Support for managed memory can be queried using the device attribute cudaDevAttrManagedMemory. The allocated memory is suitably aligned for any kind of variable. The memory is not cleared. If `size` is 0, cudaMallocManaged returns cudaErrorInvalidValue. The pointer is valid on the CPU and on all GPUs in the system that support managed memory. All accesses to this pointer must obey the Unified Memory programming model.

`flags` specifies the default stream association for this allocation. `flags` must be one of cudaMemAttachGlobal or cudaMemAttachHost. The default value for `flags` is cudaMemAttachGlobal. If cudaMemAttachGlobal is specified, then this memory is accessible from any stream on any device. If cudaMemAttachHost is specified, then the allocation should not be accessed from devices that have a zero value for the device attribute cudaDevAttrConcurrentManagedAccess; an explicit call to cudaStreamAttachMemAsync will be required to enable access on such devices.

If the association is later changed via cudaStreamAttachMemAsync to a single stream, the default association, as specifed during cudaMallocManaged, is restored when that stream is destroyed. For **managed** variables, the default association is always cudaMemAttachGlobal. Note that destroying a stream is an asynchronous operation, and as a result, the change to default association won’t happen until all work in the stream has completed.

Memory allocated with cudaMallocManaged should be released with cudaFree.

Device memory oversubscription is possible for GPUs that have a non-zero value for the device attribute cudaDevAttrConcurrentManagedAccess. Managed memory on such GPUs may be evicted from device memory to host memory at any time by the Unified Memory driver in order to make room for other allocations.

In a multi-GPU system where all GPUs have a non-zero value for the device attribute cudaDevAttrConcurrentManagedAccess, managed memory may not be populated when this API returns and instead may be populated on access. In such systems, managed memory can migrate to any processor’s memory at any time. The Unified Memory driver will employ heuristics to maintain data locality and prevent excessive page faults to the extent possible. The application can also guide the driver about memory usage patterns via cudaMemAdvise. The application can also explicitly migrate memory to a desired processor’s memory via cudaMemPrefetchAsync.

In a multi-GPU system where all of the GPUs have a zero value for the device attribute cudaDevAttrConcurrentManagedAccess and all the GPUs have peer-to-peer support with each other, the physical storage for managed memory is created on the GPU which is active at the time cudaMallocManaged is called. All other GPUs will reference the data at reduced bandwidth via peer mappings over the PCIe bus. The Unified Memory driver does not migrate memory among such GPUs.

In a multi-GPU system where not all GPUs have peer-to-peer support with each other and where the value of the device attribute cudaDevAttrConcurrentManagedAccess is zero for at least one of those GPUs, the location chosen for physical storage of managed memory is system-dependent.

  * On Linux, the location chosen will be device memory as long as the current set of active contexts are on devices that either have peer-to-peer support with each other or have a non-zero value for the device attribute cudaDevAttrConcurrentManagedAccess. If there is an active context on a GPU that does not have a non-zero value for that device attribute and it does not have peer-to-peer support with the other devices that have active contexts on them, then the location for physical storage will be ‘zero-copy’ or host memory. Note that this means that managed memory that is located in device memory is migrated to host memory if a new context is created on a GPU that doesn’t have a non-zero value for the device attribute and does not support peer-to-peer with at least one of the other devices that has an active context. This in turn implies that context creation may fail if there is insufficient host memory to migrate all managed allocations.

  * On Windows, the physical storage is always created in ‘zero-copy’ or host memory. All GPUs will reference the data at reduced bandwidth over the PCIe bus. In these circumstances, use of the environment variable CUDA_VISIBLE_DEVICES is recommended to restrict CUDA to only use those GPUs that have peer-to-peer support. Alternatively, users can also set CUDA_MANAGED_FORCE_DEVICE_ALLOC to a non-zero value to force the driver to always use device memory for physical storage. When this environment variable is set to a non-zero value, all devices used in that process that support managed memory have to be peer-to-peer compatible with each other. The error cudaErrorInvalidDevice will be returned if a device that supports managed memory is used and it is not peer-to-peer compatible with any of the other managed memory supporting devices that were previously used in that process, even if cudaDeviceReset has been called on those devices. These environment variables are described in the CUDA programming guide under the “CUDA environment variables” section.

  * On ARM, managed memory is not available on discrete gpu with Drive PX-2.

See also

cudaMallocPitch, cudaFree, cudaMallocArray, cudaFreeArray, cudaMalloc3D, cudaMalloc3DArray, cudaMallocHost (C API), cudaFreeHost, cudaHostAlloc, cudaDeviceGetAttribute, cudaStreamAttachMemAsync

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **flags** – Memory can be accessed by any stream on any device

  * **devPtr** – - Pointer to allocated device memory

  * **size** – - Requested allocation size in bytes

  * **flags** – - Must be either cudaMemAttachGlobal or cudaMemAttachHost (defaults to cudaMemAttachGlobal)

Returns

cudaSuccess, cudaErrorMemoryAllocation, cudaErrorNotSupported, cudaErrorInvalidValue

`` template<class T>__host__ cudaError_t cudaMallocPitch(T **devPtr, size_t *pitch, size_t width, size_t height) ``

`` template<typename T>__host__ cudaError_t cudaMemDiscardAndPrefetchBatchAsync(T **dptrs, size_t *sizes, size_t count, struct cudaMemLocation prefetchLocs, unsigned long long flags, cudaStream_t stream) ``

Performs a batch of memory discard and prefetches asynchronously.

This is an alternate spelling for cudaMemDiscardAndPrefetchBatchAsync made available through function overloading.

The cudaMemLocation specified by `prefetchLocs` are applicable for all the operations in the batch.

See also

cudaMemDiscardAndPrefetchBatchAsync

`` template<typename T>__host__ cudaError_t cudaMemDiscardAndPrefetchBatchAsync(T **dptrs, size_t *sizes, size_t count, struct cudaMemLocation *prefetchLocs, size_t *prefetchLocIdxs, size_t numPrefetchLocs, unsigned long long flags, cudaStream_t stream) ``

Performs a batch of memory discard and prefetches asynchronously.

This is an alternate spelling for cudaMemDiscardAndPrefetchBatchAsync made available through function overloading.

See also

cudaMemDiscardAndPrefetchBatchAsync

`` template<typename T>__host__ cudaError_t cudaMemPrefetchBatchAsync(T **dptrs, size_t *sizes, size_t count, struct cudaMemLocation prefetchLocs, unsigned long long flags, cudaStream_t stream) ``

Performs a batch of memory prefetches asynchronously.

This is an alternate spelling for cudaMemPrefetchBatchAsync made available through function overloading.

The cudaMemLocation specified by `prefetchLocs` are applicable for all the prefetches specified in the batch.

See also

cudaMemPrefetchBatchAsync

`` template<typename T>__host__ cudaError_t cudaMemPrefetchBatchAsync(T **dptrs, size_t *sizes, size_t count, struct cudaMemLocation *prefetchLocs, size_t *prefetchLocIdxs, size_t numPrefetchLocs, unsigned long long flags, cudaStream_t stream) ``

Performs a batch of memory prefetches asynchronously.

This is an alternate spelling for cudaMemPrefetchBatchAsync made available through function overloading.

See also

cudaMemPrefetchBatchAsync

`` template<typename T, typename U>__host__ cudaError_t cudaMemcpyAsync(T dst, U src, const size_t size, struct cudaMemcpyAttributes *attr, cudaStream_t hStream) ``

Performs a memory copy asynchronously.

Allows specifying attributes for the copy.

This is an alternate spelling for cudaMemcpyAsync made available through function overloading.

See also

cudaMemcpyAsync cudaMemcpyBatchAsync cudaMemcpyWithAttributesAsync

`` template<typename T, typename U>__host__ cudaError_t cudaMemcpyBatchAsync(T *const *dsts, U *const *srcs, const size_t *sizes, size_t count, struct cudaMemcpyAttributes *attrs, size_t *attrsIdxs, size_t numAttrs, cudaStream_t hStream) ``

Performs a batch of memory copies asynchronously.

This is an alternate spelling for cudaMemcpyBatchAsync made available through function overloading.

See also

cudaMemcpyBatchAsync

`` template<typename T, typename U>__host__ cudaError_t cudaMemcpyBatchAsync(T *const *dsts, U *const *srcs, const size_t *sizes, size_t count, struct cudaMemcpyAttributes attr, cudaStream_t hStream) ``

Performs a batch of memory copies asynchronously.

This is an alternate spelling for cudaMemcpyBatchAsync made available through function overloading.

The cudaMemcpyAttributes specified by `attr` are applicable for all the copies specified in the batch.

See also

cudaMemcpyBatchAsync

`` template<class T>__host__ cudaError_t cudaMemcpyFromSymbol(void *dst, const T &symbol, size_t count, size_t offset = 0, enum cudaMemcpyKind kind = cudaMemcpyDeviceToHost) ``

Copies data from the given symbol on the device.

Copies `count` bytes from the memory area `offset` bytes from the start of symbol `symbol` to the memory area pointed to by `dst`. The memory areas may not overlap. `symbol` is a variable that resides in global or constant memory space. `kind` can be either cudaMemcpyDeviceToHost or cudaMemcpyDeviceToDevice.

See also

cudaMemcpy, cudaMemcpy2D, cudaMemcpy2DToArray, cudaMemcpy2DFromArray, cudaMemcpy2DArrayToArray, cudaMemcpyToSymbol, cudaMemcpyAsync, cudaMemcpy2DAsync, cudaMemcpy2DToArrayAsync, cudaMemcpy2DFromArrayAsync, cudaMemcpyToSymbolAsync, cudaMemcpyFromSymbolAsync

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

This function exhibits synchronous behavior for most use cases.

Note

Use of a string naming a variable as the `symbol` parameter was deprecated in CUDA 4.1 and removed in CUDA 5.0.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **dst** – - Destination memory address

  * **symbol** – - Device symbol reference

  * **count** – - Size in bytes to copy

  * **offset** – - Offset from start of symbol in bytes

  * **kind** – - Type of transfer

Returns

cudaSuccess, cudaErrorInvalidValue, cudaErrorInvalidSymbol, cudaErrorInvalidMemcpyDirection, cudaErrorNoKernelImageForDevice

`` template<class T>__host__ cudaError_t cudaMemcpyFromSymbolAsync(void *dst, const T &symbol, size_t count, size_t offset = 0, enum cudaMemcpyKind kind = cudaMemcpyDeviceToHost, cudaStream_t stream = 0) ``

Copies data from the given symbol on the device.

Copies `count` bytes from the memory area `offset` bytes from the start of symbol `symbol` to the memory area pointed to by `dst`. The memory areas may not overlap. `symbol` is a variable that resides in global or constant memory space. `kind` can be either cudaMemcpyDeviceToHost or cudaMemcpyDeviceToDevice.

cudaMemcpyFromSymbolAsync() is asynchronous with respect to the host, so the call may return before the copy is complete. The copy can optionally be associated to a stream by passing a non-zero `stream` argument. If `kind` is cudaMemcpyDeviceToHost and `stream` is non-zero, the copy may overlap with operations in other streams.

See also

cudaMemcpy, cudaMemcpy2D, cudaMemcpy2DToArray, cudaMemcpy2DFromArray, cudaMemcpy2DArrayToArray, cudaMemcpyToSymbol, cudaMemcpyFromSymbol, cudaMemcpyAsync, cudaMemcpy2DAsync, cudaMemcpy2DToArrayAsync, cudaMemcpy2DFromArrayAsync, cudaMemcpyToSymbolAsync

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

This function exhibits asynchronous behavior for most use cases.

Note

Use of a string naming a variable as the `symbol` parameter was deprecated in CUDA 4.1 and removed in CUDA 5.0.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **dst** – - Destination memory address

  * **symbol** – - Device symbol reference

  * **count** – - Size in bytes to copy

  * **offset** – - Offset from start of symbol in bytes

  * **kind** – - Type of transfer

  * **stream** – - Stream identifier

Returns

cudaSuccess, cudaErrorInvalidValue, cudaErrorInvalidSymbol, cudaErrorInvalidMemcpyDirection, cudaErrorNoKernelImageForDevice

`` template<class T>__host__ cudaError_t cudaMemcpyToSymbol(const T &symbol, const void *src, size_t count, size_t offset = 0, enum cudaMemcpyKind kind = cudaMemcpyHostToDevice) ``

Copies data to the given symbol on the device.

Copies `count` bytes from the memory area pointed to by `src` to the memory area `offset` bytes from the start of symbol `symbol`. The memory areas may not overlap. `symbol` is a variable that resides in global or constant memory space. `kind` can be either cudaMemcpyHostToDevice or cudaMemcpyDeviceToDevice.

See also

cudaMemcpy, cudaMemcpy2D, cudaMemcpy2DToArray, cudaMemcpy2DFromArray, cudaMemcpy2DArrayToArray, cudaMemcpyFromSymbol, cudaMemcpyAsync, cudaMemcpy2DAsync, cudaMemcpy2DToArrayAsync, cudaMemcpy2DFromArrayAsync, cudaMemcpyToSymbolAsync, cudaMemcpyFromSymbolAsync

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

This function exhibits synchronous behavior for most use cases.

Note

Use of a string naming a variable as the `symbol` parameter was deprecated in CUDA 4.1 and removed in CUDA 5.0.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **symbol** – - Device symbol reference

  * **src** – - Source memory address

  * **count** – - Size in bytes to copy

  * **offset** – - Offset from start of symbol in bytes

  * **kind** – - Type of transfer

Returns

cudaSuccess, cudaErrorInvalidValue, cudaErrorInvalidSymbol, cudaErrorInvalidMemcpyDirection, cudaErrorNoKernelImageForDevice

`` template<class T>__host__ cudaError_t cudaMemcpyToSymbolAsync(const T &symbol, const void *src, size_t count, size_t offset = 0, enum cudaMemcpyKind kind = cudaMemcpyHostToDevice, cudaStream_t stream = 0) ``

Copies data to the given symbol on the device.

Copies `count` bytes from the memory area pointed to by `src` to the memory area `offset` bytes from the start of symbol `symbol`. The memory areas may not overlap. `symbol` is a variable that resides in global or constant memory space. `kind` can be either cudaMemcpyHostToDevice or cudaMemcpyDeviceToDevice.

cudaMemcpyToSymbolAsync() is asynchronous with respect to the host, so the call may return before the copy is complete. The copy can optionally be associated to a stream by passing a non-zero `stream` argument. If `kind` is cudaMemcpyHostToDevice and `stream` is non-zero, the copy may overlap with operations in other streams.

See also

cudaMemcpy, cudaMemcpy2D, cudaMemcpy2DToArray, cudaMemcpy2DFromArray, cudaMemcpy2DArrayToArray, cudaMemcpyToSymbol, cudaMemcpyFromSymbol, cudaMemcpyAsync, cudaMemcpy2DAsync, cudaMemcpy2DToArrayAsync, cudaMemcpy2DFromArrayAsync, cudaMemcpyFromSymbolAsync

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

This function exhibits asynchronous behavior for most use cases.

Note

Use of a string naming a variable as the `symbol` parameter was deprecated in CUDA 4.1 and removed in CUDA 5.0.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **symbol** – - Device symbol reference

  * **src** – - Source memory address

  * **count** – - Size in bytes to copy

  * **offset** – - Offset from start of symbol in bytes

  * **kind** – - Type of transfer

  * **stream** – - Stream identifier

Returns

cudaSuccess, cudaErrorInvalidValue, cudaErrorInvalidSymbol, cudaErrorInvalidMemcpyDirection, cudaErrorNoKernelImageForDevice

`` template<class T>__host__ cudaError_t cudaOccupancyAvailableDynamicSMemPerBlock(size_t *dynamicSmemSize, T *func, int numBlocks, int blockSize) ``

Returns dynamic shared memory available per block when launching `numBlocks` blocks on SM.

Returns in `*dynamicSmemSize` the maximum size of dynamic shared memory to allow `numBlocks` blocks per SM.

See also

cudaOccupancyMaxPotentialBlockSize

See also

cudaOccupancyMaxPotentialBlockSizeWithFlags

See also

cudaOccupancyMaxActiveBlocksPerMultiprocessor

See also

cudaOccupancyMaxActiveBlocksPerMultiprocessorWithFlags

See also

cudaOccupancyMaxPotentialBlockSizeVariableSMem

See also

cudaOccupancyMaxPotentialBlockSizeVariableSMemWithFlags

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Note

The API can also be used with a kernel cudaKernel_t by querying the handle using cudaLibraryGetKernel() or cudaGetKernel and then passing it to the API by casting to void*. The symbol `entryFuncAddr` passed to cudaGetKernel should be a symbol that is registered with the same CUDA Runtime instance.

Note

Passing a symbol that belongs that belongs to a different runtime instance will result in undefined behavior. The only type that can be reliably passed to a different runtime instance is cudaKernel_t

Parameters

  * **dynamicSmemSize** – - Returned maximum dynamic shared memory

  * **func** – - Kernel function for which occupancy is calculated

  * **numBlocks** – - Number of blocks to fit on SM

  * **blockSize** – - Size of the block

Returns

cudaSuccess, cudaErrorInvalidDevice, cudaErrorInvalidDeviceFunction, cudaErrorInvalidValue, cudaErrorUnknown,

`` template<class T>__host__ cudaError_t cudaOccupancyMaxActiveBlocksPerMultiprocessor(int *numBlocks, T func, int blockSize, size_t dynamicSMemSize) ``

Returns occupancy for a device function.

Returns in `*numBlocks` the maximum number of active blocks per streaming multiprocessor for the device function.

See also

cudaOccupancyMaxActiveBlocksPerMultiprocessorWithFlags

See also

cudaOccupancyMaxPotentialBlockSize

See also

cudaOccupancyMaxPotentialBlockSizeWithFlags

See also

cudaOccupancyMaxPotentialBlockSizeVariableSMem

See also

cudaOccupancyMaxPotentialBlockSizeVariableSMemWithFlags

See also

cudaOccupancyAvailableDynamicSMemPerBlock

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Note

The API can also be used with a kernel cudaKernel_t by querying the handle using cudaLibraryGetKernel() or cudaGetKernel and then passing it to the API by casting to void*. The symbol `entryFuncAddr` passed to cudaGetKernel should be a symbol that is registered with the same CUDA Runtime instance.

Note

Passing a symbol that belongs that belongs to a different runtime instance will result in undefined behavior. The only type that can be reliably passed to a different runtime instance is cudaKernel_t

Parameters

  * **numBlocks** – - Returned occupancy

  * **func** – - Kernel function for which occupancy is calulated

  * **blockSize** – - Block size the kernel is intended to be launched with

  * **dynamicSMemSize** – - Per-block dynamic shared memory usage intended, in bytes

Returns

cudaSuccess, cudaErrorInvalidDevice, cudaErrorInvalidDeviceFunction, cudaErrorInvalidValue, cudaErrorUnknown,

`` template<class T>__host__ cudaError_t cudaOccupancyMaxActiveBlocksPerMultiprocessorWithFlags(int *numBlocks, T func, int blockSize, size_t dynamicSMemSize, unsigned int flags) ``

Returns occupancy for a device function with the specified flags.

Returns in `*numBlocks` the maximum number of active blocks per streaming multiprocessor for the device function.

The `flags` parameter controls how special cases are handled. Valid flags include:

  * cudaOccupancyDefault: keeps the default behavior as cudaOccupancyMaxActiveBlocksPerMultiprocessor

  * cudaOccupancyDisableCachingOverride: suppresses the default behavior on platform where global caching affects occupancy. On such platforms, if caching is enabled, but per-block SM resource usage would result in zero occupancy, the occupancy calculator will calculate the occupancy as if caching is disabled. Setting this flag makes the occupancy calculator to return 0 in such cases. More information can be found about this feature in the “Unified L1/Texture Cache” section of the Maxwell tuning guide.

See also

cudaOccupancyMaxActiveBlocksPerMultiprocessor

See also

cudaOccupancyMaxPotentialBlockSize

See also

cudaOccupancyMaxPotentialBlockSizeWithFlags

See also

cudaOccupancyMaxPotentialBlockSizeVariableSMem

See also

cudaOccupancyMaxPotentialBlockSizeVariableSMemWithFlags

See also

cudaOccupancyAvailableDynamicSMemPerBlock

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Note

The API can also be used with a kernel cudaKernel_t by querying the handle using cudaLibraryGetKernel() or cudaGetKernel and then passing it to the API by casting to void*. The symbol `entryFuncAddr` passed to cudaGetKernel should be a symbol that is registered with the same CUDA Runtime instance.

Note

Passing a symbol that belongs that belongs to a different runtime instance will result in undefined behavior. The only type that can be reliably passed to a different runtime instance is cudaKernel_t

Parameters

  * **numBlocks** – - Returned occupancy

  * **func** – - Kernel function for which occupancy is calulated

  * **blockSize** – - Block size the kernel is intended to be launched with

  * **dynamicSMemSize** – - Per-block dynamic shared memory usage intended, in bytes

  * **flags** – - Requested behavior for the occupancy calculator

Returns

cudaSuccess, cudaErrorInvalidDevice, cudaErrorInvalidDeviceFunction, cudaErrorInvalidValue, cudaErrorUnknown,

`` template<class T>__host__ cudaError_t cudaOccupancyMaxActiveClusters(int *numClusters, T *func, const cudaLaunchConfig_t *config) ``

Given the kernel function (`func`) and launch configuration (`config`), return the maximum number of clusters that could co-exist on the target device in `*numClusters`.

If the function has required cluster size already set (see cudaFuncGetAttributes), the cluster size from config must either be unspecified or match the required size. Without required sizes, the cluster size must be specified in config, else the function will return an error.

Note that various attributes of the kernel function may affect occupancy calculation. Runtime environment may affect how the hardware schedules the clusters, so the calculated occupancy is not guaranteed to be achievable.

See also

cudaFuncGetAttributes

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Note

The API can also be used with a kernel cudaKernel_t by querying the handle using cudaLibraryGetKernel() or cudaGetKernel and then passing it to the API by casting to void*. The symbol `entryFuncAddr` passed to cudaGetKernel should be a symbol that is registered with the same CUDA Runtime instance.

Note

Passing a symbol that belongs that belongs to a different runtime instance will result in undefined behavior. The only type that can be reliably passed to a different runtime instance is cudaKernel_t

Parameters

  * **numClusters** – - Returned maximum number of clusters that could co-exist on the target device

  * **func** – - Kernel function for which maximum number of clusters are calculated

  * **config** – - Launch configuration for the given kernel function

Returns

cudaSuccess, cudaErrorInvalidDeviceFunction, cudaErrorInvalidValue, cudaErrorInvalidClusterSize, cudaErrorUnknown,

`` template<class T>__host__ __device__ cudaError_t cudaOccupancyMaxPotentialBlockSize(int *minGridSize, int *blockSize, T func, size_t dynamicSMemSize = 0, int blockSizeLimit = 0) ``

Returns grid and block size that achieves maximum potential occupancy for a device function.

Returns in `*minGridSize` and `*blocksize` a suggested grid / block size pair that achieves the best potential occupancy (i.e. the maximum number of active warps with the smallest number of blocks).

Use

See also

cudaOccupancyMaxPotentialBlockSizeVariableSMem if the amount of per-block dynamic shared memory changes with different block sizes.

See also

cudaOccupancyMaxPotentialBlockSizeWithFlags

See also

cudaOccupancyMaxActiveBlocksPerMultiprocessor

See also

cudaOccupancyMaxActiveBlocksPerMultiprocessorWithFlags

See also

cudaOccupancyMaxPotentialBlockSizeVariableSMem

See also

cudaOccupancyMaxPotentialBlockSizeVariableSMemWithFlags

See also

cudaOccupancyAvailableDynamicSMemPerBlock

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **minGridSize** – - Returned minimum grid size needed to achieve the best potential occupancy

  * **blockSize** – - Returned block size

  * **func** – - Device function symbol

  * **dynamicSMemSize** – - Per-block dynamic shared memory usage intended, in bytes

  * **blockSizeLimit** – - The maximum block size `func` is designed to work with. 0 means no limit.

Returns

cudaSuccess, cudaErrorInvalidDevice, cudaErrorInvalidDeviceFunction, cudaErrorInvalidValue, cudaErrorUnknown,

`` template<typename UnaryFunction, class T>__host__ __device__ cudaError_t cudaOccupancyMaxPotentialBlockSizeVariableSMem(int *minGridSize, int *blockSize, T func, UnaryFunction blockSizeToDynamicSMemSize, int blockSizeLimit = 0) ``

Returns grid and block size that achieves maximum potential occupancy for a device function.

Returns in `*minGridSize` and `*blocksize` a suggested grid / block size pair that achieves the best potential occupancy (i.e. the maximum number of active warps with the smallest number of blocks).

See also

cudaOccupancyMaxPotentialBlockSizeVariableSMemWithFlags

See also

cudaOccupancyMaxActiveBlocksPerMultiprocessor

See also

cudaOccupancyMaxActiveBlocksPerMultiprocessorWithFlags

See also

cudaOccupancyMaxPotentialBlockSize

See also

cudaOccupancyMaxPotentialBlockSizeWithFlags

See also

cudaOccupancyAvailableDynamicSMemPerBlock

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **minGridSize** – - Returned minimum grid size needed to achieve the best potential occupancy

  * **blockSize** – - Returned block size

  * **func** – - Device function symbol

  * **blockSizeToDynamicSMemSize** – - A unary function / functor that takes block size, and returns the size, in bytes, of dynamic shared memory needed for a block

  * **blockSizeLimit** – - The maximum block size `func` is designed to work with. 0 means no limit.

Returns

cudaSuccess, cudaErrorInvalidDevice, cudaErrorInvalidDeviceFunction, cudaErrorInvalidValue, cudaErrorUnknown,

`` template<typename UnaryFunction, class T>__host__ __device__ cudaError_t cudaOccupancyMaxPotentialBlockSizeVariableSMemWithFlags(int *minGridSize, int *blockSize, T func, UnaryFunction blockSizeToDynamicSMemSize, int blockSizeLimit = 0, unsigned int flags = 0) ``

Returns grid and block size that achieves maximum potential occupancy for a device function.

Returns in `*minGridSize` and `*blocksize` a suggested grid / block size pair that achieves the best potential occupancy (i.e. the maximum number of active warps with the smallest number of blocks).

The `flags` parameter controls how special cases are handled. Valid flags include:

  * cudaOccupancyDefault: keeps the default behavior as cudaOccupancyMaxPotentialBlockSizeVariableSMemWithFlags

  * cudaOccupancyDisableCachingOverride: This flag suppresses the default behavior on platform where global caching affects occupancy. On such platforms, if caching is enabled, but per-block SM resource usage would result in zero occupancy, the occupancy calculator will calculate the occupancy as if caching is disabled. Setting this flag makes the occupancy calculator to return 0 in such cases. More information can be found about this feature in the “Unified L1/Texture Cache” section of the Maxwell tuning guide.

See also

cudaOccupancyMaxPotentialBlockSizeVariableSMem

See also

cudaOccupancyMaxActiveBlocksPerMultiprocessor

See also

cudaOccupancyMaxActiveBlocksPerMultiprocessorWithFlags

See also

cudaOccupancyMaxPotentialBlockSize

See also

cudaOccupancyMaxPotentialBlockSizeWithFlags

See also

cudaOccupancyAvailableDynamicSMemPerBlock

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **minGridSize** – - Returned minimum grid size needed to achieve the best potential occupancy

  * **blockSize** – - Returned block size

  * **func** – - Device function symbol

  * **blockSizeToDynamicSMemSize** – - A unary function / functor that takes block size, and returns the size, in bytes, of dynamic shared memory needed for a block

  * **blockSizeLimit** – - The maximum block size `func` is designed to work with. 0 means no limit.

  * **flags** – - Requested behavior for the occupancy calculator

Returns

cudaSuccess, cudaErrorInvalidDevice, cudaErrorInvalidDeviceFunction, cudaErrorInvalidValue, cudaErrorUnknown,

`` template<class T>__host__ __device__ cudaError_t cudaOccupancyMaxPotentialBlockSizeWithFlags(int *minGridSize, int *blockSize, T func, size_t dynamicSMemSize = 0, int blockSizeLimit = 0, unsigned int flags = 0) ``

Returns grid and block size that achived maximum potential occupancy for a device function with the specified flags.

Returns in `*minGridSize` and `*blocksize` a suggested grid / block size pair that achieves the best potential occupancy (i.e. the maximum number of active warps with the smallest number of blocks).

The `flags` parameter controls how special cases are handle. Valid flags include:

  * cudaOccupancyDefault: keeps the default behavior as cudaOccupancyMaxPotentialBlockSize

  * cudaOccupancyDisableCachingOverride: This flag suppresses the default behavior on platform where global caching affects occupancy. On such platforms, if caching is enabled, but per-block SM resource usage would result in zero occupancy, the occupancy calculator will calculate the occupancy as if caching is disabled. Setting this flag makes the occupancy calculator to return 0 in such cases. More information can be found about this feature in the “Unified L1/Texture Cache” section of the Maxwell tuning guide.

Use

See also

cudaOccupancyMaxPotentialBlockSizeVariableSMem if the amount of per-block dynamic shared memory changes with different block sizes.

See also

cudaOccupancyMaxPotentialBlockSize

See also

cudaOccupancyMaxActiveBlocksPerMultiprocessor

See also

cudaOccupancyMaxActiveBlocksPerMultiprocessorWithFlags

See also

cudaOccupancyMaxPotentialBlockSizeVariableSMem

See also

cudaOccupancyMaxPotentialBlockSizeVariableSMemWithFlags

See also

cudaOccupancyAvailableDynamicSMemPerBlock

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **minGridSize** – - Returned minimum grid size needed to achieve the best potential occupancy

  * **blockSize** – - Returned block size

  * **func** – - Device function symbol

  * **dynamicSMemSize** – - Per-block dynamic shared memory usage intended, in bytes

  * **blockSizeLimit** – - The maximum block size `func` is designed to work with. 0 means no limit.

  * **flags** – - Requested behavior for the occupancy calculator

Returns

cudaSuccess, cudaErrorInvalidDevice, cudaErrorInvalidDeviceFunction, cudaErrorInvalidValue, cudaErrorUnknown,

`` template<class T>__host__ cudaError_t cudaOccupancyMaxPotentialClusterSize(int *clusterSize, T *func, const cudaLaunchConfig_t *config) ``

Given the kernel function (`func`) and launch configuration (`config`), return the maximum cluster size in `*clusterSize`.

The cluster dimensions in `config` are ignored. If func has a required cluster size set (see cudaFuncGetAttributes),`*clusterSize` will reflect the required cluster size.

By default this function will always return a value that’s portable on future hardware. A higher value may be returned if the kernel function allows non-portable cluster sizes.

This function will respect the compile time launch bounds.

See also

cudaFuncGetAttributes

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Note

The API can also be used with a kernel cudaKernel_t by querying the handle using cudaLibraryGetKernel() or cudaGetKernel and then passing it to the API by casting to void*. The symbol `entryFuncAddr` passed to cudaGetKernel should be a symbol that is registered with the same CUDA Runtime instance.

Note

Passing a symbol that belongs that belongs to a different runtime instance will result in undefined behavior. The only type that can be reliably passed to a different runtime instance is cudaKernel_t

Parameters

  * **clusterSize** – - Returned maximum cluster size that can be launched for the given kernel function and launch configuration

  * **func** – - Kernel function for which maximum cluster size is calculated

  * **config** – - Launch configuration for the given kernel function

Returns

cudaSuccess, cudaErrorInvalidDeviceFunction, cudaErrorInvalidValue, cudaErrorUnknown,

`` template<class T>__host__ cudaError_t cudaStreamAttachMemAsync(cudaStream_t stream, T *devPtr, size_t length = 0, unsigned int flags = 0x04) ``

Attach memory to a stream asynchronously.

Enqueues an operation in `stream` to specify stream association of `length` bytes of memory starting from `devPtr`. This function is a stream-ordered operation, meaning that it is dependent on, and will only take effect when, previous work in stream has completed. Any previous association is automatically replaced.

`devPtr` must point to an one of the following types of memories:

  * managed memory declared using the **managed** keyword or allocated with cudaMallocManaged.

  * a valid host-accessible region of system-allocated pageable memory. This type of memory may only be specified if the device associated with the stream reports a non-zero value for the device attribute cudaDevAttrPageableMemoryAccess.

For managed allocations, `length` must be either zero or the entire allocation’s size. Both indicate that the entire allocation’s stream association is being changed. Currently, it is not possible to change stream association for a portion of a managed allocation.

For pageable allocations, `length` must be non-zero.

The stream association is specified using `flags` which must be one of cudaMemAttachGlobal, cudaMemAttachHost or cudaMemAttachSingle. The default value for `flags` is cudaMemAttachSingle If the cudaMemAttachGlobal flag is specified, the memory can be accessed by any stream on any device. If the cudaMemAttachHost flag is specified, the program makes a guarantee that it won’t access the memory on the device from any stream on a device that has a zero value for the device attribute cudaDevAttrConcurrentManagedAccess. If the cudaMemAttachSingle flag is specified and `stream` is associated with a device that has a zero value for the device attribute cudaDevAttrConcurrentManagedAccess, the program makes a guarantee that it will only access the memory on the device from `stream`. It is illegal to attach singly to the NULL stream, because the NULL stream is a virtual global stream and not a specific stream. An error will be returned in this case.

When memory is associated with a single stream, the Unified Memory system will allow CPU access to this memory region so long as all operations in `stream` have completed, regardless of whether other streams are active. In effect, this constrains exclusive ownership of the managed memory region by an active GPU to per-stream activity instead of whole-GPU activity.

Accessing memory on the device from streams that are not associated with it will produce undefined results. No error checking is performed by the Unified Memory system to ensure that kernels launched into other streams do not access this region.

It is a program’s responsibility to order calls to cudaStreamAttachMemAsync via events, synchronization or other means to ensure legal access to memory at all times. Data visibility and coherency will be changed appropriately for all kernels which follow a stream-association change.

If `stream` is destroyed while data is associated with it, the association is removed and the association reverts to the default visibility of the allocation as specified at cudaMallocManaged. For **managed** variables, the default association is always cudaMemAttachGlobal. Note that destroying a stream is an asynchronous operation, and as a result, the change to default association won’t happen until all work in the stream has completed.

See also

cudaStreamCreate, cudaStreamCreateWithFlags, cudaStreamWaitEvent, cudaStreamSynchronize, cudaStreamAddCallback, cudaStreamDestroy, cudaMallocManaged

Note

Note that this function may also return error codes from previous, asynchronous launches.

Note

Note that this function may also return cudaErrorInitializationError, cudaErrorInsufficientDriver or cudaErrorNoDevice if this call tries to initialize internal CUDA RT state.

Note

Note that as specified by cudaStreamAddCallback no CUDA function may be called from callback. cudaErrorNotPermitted may, but is not guaranteed to, be returned as a diagnostic in such case.

Parameters

  * **flags** – Memory can only be accessed by a single stream on the associated device

  * **stream** – - Stream in which to enqueue the attach operation

  * **devPtr** – - Pointer to memory (must be a pointer to managed memory or to a valid host-accessible region of system-allocated memory)

  * **length** – - Length of memory (defaults to zero)

  * **flags** – - Must be one of cudaMemAttachGlobal, cudaMemAttachHost or cudaMemAttachSingle (defaults to cudaMemAttachSingle)

Returns

cudaSuccess, cudaErrorNotReady, cudaErrorInvalidValue, cudaErrorInvalidResourceHandle
