<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/group__CUDART__D3D9.html

#  6.9. Direct3D 9 Interoperability

This section describes the Direct3D 9 interoperability functions of the CUDA runtime application programming interface. Note that mapping of Direct3D 9 resources is performed with the graphics API agnostic, resource mapping interface described in Graphics Interopability.

##  6.9.1. Enumerations

`` enum cudaD3D9DeviceList ``

CUDA devices corresponding to a D3D9 device.

_Values:_

`` enumerator cudaD3D9DeviceListAll ``

The CUDA devices for all GPUs used by a D3D9 device.

`` enumerator cudaD3D9DeviceListCurrentFrame ``

The CUDA devices for the GPUs used by a D3D9 device in its currently rendering frame.

`` enumerator cudaD3D9DeviceListNextFrame ``

The CUDA devices for the GPUs to be used by a D3D9 device in the next frame

##  6.9.2. Functions

`` __host__ cudaError_t cudaD3D9GetDevice(int *device, const char *pszAdapterName) ``

Gets the device number for an adapter.

Returns in `*device` the CUDA-compatible device corresponding to the adapter name `pszAdapterName` obtained from ::EnumDisplayDevices or ::IDirect3D9::GetAdapterIdentifier(). If no device on the adapter with name `pszAdapterName` is CUDA-compatible then the call will fail.

See also

cudaD3D9SetDirect3DDevice, cudaGraphicsD3D9RegisterResource, ::cuD3D9GetDevice

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **device** – - Returns the device corresponding to pszAdapterName

  * **pszAdapterName** – - D3D9 adapter to get device for

Returns

cudaSuccess, cudaErrorInvalidValue, cudaErrorUnknown

`` __host__ cudaError_t cudaD3D9GetDevices(unsigned int *pCudaDeviceCount, int *pCudaDevices, unsigned int cudaDeviceCount, IDirect3DDevice9 *pD3D9Device, enum cudaD3D9DeviceList deviceList) ``

Gets the CUDA devices corresponding to a Direct3D 9 device.

Returns in `*pCudaDeviceCount` the number of CUDA-compatible devices corresponding to the Direct3D 9 device `pD3D9Device`. Also returns in `*pCudaDevices` at most `cudaDeviceCount` of the the CUDA-compatible devices corresponding to the Direct3D 9 device `pD3D9Device`.

If any of the GPUs being used to render `pDevice` are not CUDA capable then the call will return cudaErrorNoDevice.

See also

cudaGraphicsUnregisterResource, cudaGraphicsMapResources, cudaGraphicsSubResourceGetMappedArray, cudaGraphicsResourceGetMappedPointer, ::cuD3D9GetDevices

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **pCudaDeviceCount** – - Returned number of CUDA devices corresponding to `pD3D9Device`

  * **pCudaDevices** – - Returned CUDA devices corresponding to `pD3D9Device`

  * **cudaDeviceCount** – - The size of the output device array `pCudaDevices`

  * **pD3D9Device** – - Direct3D 9 device to query for CUDA devices

  * **deviceList** – - The set of devices to return. This set may be cudaD3D9DeviceListAll for all devices, cudaD3D9DeviceListCurrentFrame for the devices used to render the current frame (in SLI), or cudaD3D9DeviceListNextFrame for the devices used to render the next frame (in SLI).

Returns

cudaSuccess, cudaErrorNoDevice, cudaErrorUnknown

`` __host__ cudaError_t cudaD3D9GetDirect3DDevice(IDirect3DDevice9 **ppD3D9Device) ``

Gets the Direct3D device against which the current CUDA context was created.

Returns in `*ppD3D9Device` the Direct3D device against which this CUDA context was created in cudaD3D9SetDirect3DDevice().

See also

cudaD3D9SetDirect3DDevice, ::cuD3D9GetDirect3DDevice

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

**ppD3D9Device** – - Returns the Direct3D device for this thread

Returns

cudaSuccess, cudaErrorInvalidGraphicsContext, cudaErrorUnknown

`` __host__ cudaError_t cudaD3D9SetDirect3DDevice(IDirect3DDevice9 *pD3D9Device, int device = -1) ``

Sets the Direct3D 9 device to use for interoperability with a CUDA device.

Records `pD3D9Device` as the Direct3D 9 device to use for Direct3D 9 interoperability with the CUDA device `device` and sets `device` as the current device for the calling host thread.

This function will immediately initialize the primary context on `device` if needed.

If `device` has already been initialized then this call will fail with the error cudaErrorSetOnActiveProcess. In this case it is necessary to reset `device` using cudaDeviceReset() before Direct3D 9 interoperability on `device` may be enabled.

Successfully initializing CUDA interoperability with `pD3D9Device` will increase the internal reference count on `pD3D9Device`. This reference count will be decremented when `device` is reset using cudaDeviceReset().

Note that this function is never required for correct functionality. Use of this function will result in accelerated interoperability only when the operating system is Windows Vista or Windows 7, and the device `pD3DDdevice` is not an IDirect3DDevice9Ex. In all other cirumstances, this function is not necessary.

See also

cudaD3D9GetDevice, cudaGraphicsD3D9RegisterResource, cudaDeviceReset

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **pD3D9Device** – - Direct3D device to use for this thread

  * **device** – - The CUDA device to use. This device must be among the devices returned when querying cudaD3D9DeviceListAll from cudaD3D9GetDevices, may be set to -1 to automatically select an appropriate CUDA device.

Returns

cudaSuccess, cudaErrorInitializationError, cudaErrorInvalidValue, cudaErrorSetOnActiveProcess

`` __host__ cudaError_t cudaGraphicsD3D9RegisterResource(struct cudaGraphicsResource **resource, IDirect3DResource9 *pD3DResource, unsigned int flags) ``

Register a Direct3D 9 resource for access by CUDA.

Registers the Direct3D 9 resource `pD3DResource` for access by CUDA.

If this call is successful then the application will be able to map and unmap this resource until it is unregistered through cudaGraphicsUnregisterResource(). Also on success, this call will increase the internal reference count on `pD3DResource`. This reference count will be decremented when this resource is unregistered through cudaGraphicsUnregisterResource().

This call potentially has a high-overhead and should not be called every frame in interactive applications.

The type of `pD3DResource` must be one of the following.

  * ::IDirect3DVertexBuffer9: may be accessed through a device pointer

  * ::IDirect3DIndexBuffer9: may be accessed through a device pointer

  * ::IDirect3DSurface9: may be accessed through an array. Only stand-alone objects of type ::IDirect3DSurface9 may be explicitly shared. In particular, individual mipmap levels and faces of cube maps may not be registered directly. To access individual surfaces associated with a texture, one must register the base texture object.

  * ::IDirect3DBaseTexture9: individual surfaces on this texture may be accessed through an array.

The `flags` argument may be used to specify additional parameters at register time. The valid values for this parameter are

  * cudaGraphicsRegisterFlagsNone: Specifies no hints about how this resource will be used.

  * cudaGraphicsRegisterFlagsSurfaceLoadStore: Specifies that CUDA will bind this resource to a surface reference.

  * cudaGraphicsRegisterFlagsTextureGather: Specifies that CUDA will perform texture gather operations on this resource.

Not all Direct3D resources of the above types may be used for interoperability with CUDA. The following are some limitations.

  * The primary rendertarget may not be registered with CUDA.

  * Resources allocated as shared may not be registered with CUDA.

  * Textures which are not of a format which is 1, 2, or 4 channels of 8, 16, or 32-bit integer or floating-point data cannot be shared.

  * Surfaces of depth or stencil formats cannot be shared.

A complete list of supported formats is as follows:

  * D3DFMT_L8

  * D3DFMT_L16

  * D3DFMT_A8R8G8B8

  * D3DFMT_X8R8G8B8

  * D3DFMT_G16R16

  * D3DFMT_A8B8G8R8

  * D3DFMT_A8

  * D3DFMT_A8L8

  * D3DFMT_Q8W8V8U8

  * D3DFMT_V16U16

  * D3DFMT_A16B16G16R16F

  * D3DFMT_A16B16G16R16

  * D3DFMT_R32F

  * D3DFMT_G16R16F

  * D3DFMT_A32B32G32R32F

  * D3DFMT_G32R32F

  * D3DFMT_R16F

If `pD3DResource` is of incorrect type or is already registered, then cudaErrorInvalidResourceHandle is returned. If `pD3DResource` cannot be registered, then cudaErrorUnknown is returned.

See also

cudaD3D9SetDirect3DDevice, cudaGraphicsUnregisterResource, cudaGraphicsMapResources, cudaGraphicsSubResourceGetMappedArray, cudaGraphicsResourceGetMappedPointer, ::cuGraphicsD3D9RegisterResource

Note

Note that this function may also return error codes from previous, asynchronous launches.

Parameters

  * **resource** – - Pointer to returned resource handle

  * **pD3DResource** – - Direct3D resource to register

  * **flags** – - Parameters for resource registration

Returns

cudaSuccess, cudaErrorInvalidDevice, cudaErrorInvalidValue, cudaErrorInvalidResourceHandle, cudaErrorUnknown
