<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaDeviceProp.html

#  7.14. cudaDeviceProp

`` struct cudaDeviceProp ``

CUDA device properties.

Public Members

`` int accessPolicyMaxWindowSize ``

The maximum value of cudaAccessPolicyWindow::num_bytes.

`` int asyncEngineCount ``

Number of asynchronous engines.

`` int canMapHostMemory ``

Device can map host memory with cudaHostAlloc/cudaHostGetDevicePointer.

`` int canUseHostPointerForRegisteredMem ``

Device can access host registered memory at the same virtual address as the CPU.

`` int clusterLaunch ``

Indicates device supports cluster launch.

`` int computePreemptionSupported ``

Device supports Compute Preemption.

`` int concurrentKernels ``

Device can possibly execute multiple kernels concurrently.

`` int concurrentManagedAccess ``

Device can coherently access managed memory concurrently with the CPU.

`` int cooperativeLaunch ``

Device supports launching cooperative kernels via cudaLaunchCooperativeKernel.

`` int deferredMappingCudaArraySupported ``

1 if the device supports deferred mapping CUDA arrays and CUDA mipmapped arrays

`` int deviceNumaConfig ``

NUMA configuration of a device: value is of type cudaDeviceNumaConfig enum.

`` int deviceNumaId ``

NUMA node ID of the GPU memory.

`` int directManagedMemAccessFromHost ``

Host can directly access managed memory on the device without migration.

`` int ECCEnabled ``

Device has ECC support enabled.

`` int globalL1CacheSupported ``

Device supports caching globals in L1.

`` unsigned int gpuDirectRDMAFlushWritesOptions ``

Bitmask to be interpreted according to the cudaFlushGPUDirectRDMAWritesOptions enum.

`` int gpuDirectRDMASupported ``

1 if the device supports GPUDirect RDMA APIs, 0 otherwise

`` int gpuDirectRDMAWritesOrdering ``

See the cudaGPUDirectRDMAWritesOrdering enum for numerical values.

`` unsigned int gpuPciDeviceID ``

The combined 16-bit PCI device ID and 16-bit PCI vendor ID.

`` unsigned int gpuPciSubsystemID ``

The combined 16-bit PCI subsystem ID and 16-bit PCI subsystem vendor ID.

`` int hostNativeAtomicSupported ``

Link between the device and the host supports native atomic operations.

`` int hostNumaId ``

NUMA ID of the host node closest to the device or -1 when system does not support NUMA.

`` int hostNumaMultinodeIpcSupported ``

1 if the device supports HostNuma location IPC between nodes in a multi-node system.

`` int hostRegisterReadOnlySupported ``

Device supports using the cudaHostRegister flag cudaHostRegisterReadOnly to register memory that must be mapped as read-only to the GPU.

`` int hostRegisterSupported ``

Device supports host memory registration via cudaHostRegister.

`` int integrated ``

Device is integrated as opposed to discrete.

`` int ipcEventSupported ``

Device supports IPC Events.

`` int isMultiGpuBoard ``

Device is on a multi-GPU board.

`` int l2CacheSize ``

Size of L2 cache in bytes.

`` int localL1CacheSupported ``

Device supports caching locals in L1.

`` char luid[8] ``

8-byte locally unique identifier.

Value is undefined on TCC and non-Windows platforms

`` unsigned int luidDeviceNodeMask ``

LUID device node mask.

Value is undefined on TCC and non-Windows platforms

`` int major ``

Major compute capability.

`` int managedMemory ``

Device supports allocating managed memory on this system.

`` int maxBlocksPerMultiProcessor ``

Maximum number of resident blocks per multiprocessor.

`` int maxGridSize[3] ``

Maximum size of each dimension of a grid.

`` int maxSurface1D ``

Maximum 1D surface size.

`` int maxSurface1DLayered[2] ``

Maximum 1D layered surface dimensions.

`` int maxSurface2D[2] ``

Maximum 2D surface dimensions.

`` int maxSurface2DLayered[3] ``

Maximum 2D layered surface dimensions.

`` int maxSurface3D[3] ``

Maximum 3D surface dimensions.

`` int maxSurfaceCubemap ``

Maximum Cubemap surface dimensions.

`` int maxSurfaceCubemapLayered[2] ``

Maximum Cubemap layered surface dimensions.

`` int maxTexture1D ``

Maximum 1D texture size.

`` int maxTexture1DLayered[2] ``

Maximum 1D layered texture dimensions.

`` int maxTexture1DMipmap ``

Maximum 1D mipmapped texture size.

`` int maxTexture2D[2] ``

Maximum 2D texture dimensions.

`` int maxTexture2DGather[2] ``

Maximum 2D texture dimensions if texture gather operations have to be performed.

`` int maxTexture2DLayered[3] ``

Maximum 2D layered texture dimensions.

`` int maxTexture2DLinear[3] ``

Maximum dimensions (width, height, pitch) for 2D textures bound to pitched memory.

`` int maxTexture2DMipmap[2] ``

Maximum 2D mipmapped texture dimensions.

`` int maxTexture3D[3] ``

Maximum 3D texture dimensions.

`` int maxTexture3DAlt[3] ``

Maximum alternate 3D texture dimensions.

`` int maxTextureCubemap ``

Maximum Cubemap texture dimensions.

`` int maxTextureCubemapLayered[2] ``

Maximum Cubemap layered texture dimensions.

`` int maxThreadsDim[3] ``

Maximum size of each dimension of a block.

`` int maxThreadsPerBlock ``

Maximum number of threads per block.

`` int maxThreadsPerMultiProcessor ``

Maximum resident threads per multiprocessor.

`` int memoryBusWidth ``

Global memory bus width in bits.

`` int memoryPoolsSupported ``

1 if the device supports using the cudaMallocAsync and cudaMemPool family of APIs, 0 otherwise

`` unsigned int memoryPoolSupportedHandleTypes ``

Bitmask of handle types supported with mempool-based IPC.

`` size_t memPitch ``

Maximum pitch in bytes allowed by memory copies.

`` int minor ``

Minor compute capability.

`` int mpsEnabled ``

Indicates if contexts created on this device will be shared via MPS.

`` int multiGpuBoardGroupID ``

Unique identifier for a group of devices on the same multi-GPU board.

`` int multiProcessorCount ``

Number of multiprocessors on device.

`` char name[256] ``

ASCII string identifying device.

`` int pageableMemoryAccess ``

Device supports coherently accessing pageable memory without calling cudaHostRegister on it.

`` int pageableMemoryAccessUsesHostPageTables ``

Device accesses pageable memory via the host’s page tables.

`` int pciBusID ``

PCI bus ID of the device.

`` int pciDeviceID ``

PCI device ID of the device.

`` int pciDomainID ``

PCI domain ID of the device.

`` int persistingL2CacheMaxSize ``

Device’s maximum l2 persisting lines capacity setting in bytes.

`` int regsPerBlock ``

32-bit registers available per block

`` int regsPerMultiprocessor ``

32-bit registers available per multiprocessor

`` int reserved[56] ``

Reserved for future use.

`` size_t reservedSharedMemPerBlock ``

Shared memory reserved by CUDA driver per block in bytes.

`` size_t sharedMemPerBlock ``

Shared memory available per block in bytes.

`` size_t sharedMemPerBlockOptin ``

Per device maximum shared memory per block usable by special opt in.

`` size_t sharedMemPerMultiprocessor ``

Shared memory available per multiprocessor in bytes.

`` int sparseCudaArraySupported ``

1 if the device supports sparse CUDA arrays and sparse CUDA mipmapped arrays, 0 otherwise

`` int streamPrioritiesSupported ``

Device supports stream priorities.

`` size_t surfaceAlignment ``

Alignment requirements for surfaces.

`` int tccDriver ``

1 if device is a Tesla device using TCC driver, 0 otherwise

`` size_t textureAlignment ``

Alignment requirement for textures.

`` size_t texturePitchAlignment ``

Pitch alignment requirement for texture references bound to pitched memory.

`` int timelineSemaphoreInteropSupported ``

External timeline semaphore interop is supported on the device.

`` size_t totalConstMem ``

Constant memory available on device in bytes.

`` size_t totalGlobalMem ``

Global memory available on device in bytes.

`` int unifiedAddressing ``

Device shares a unified address space with the host.

`` int unifiedFunctionPointers ``

Indicates device supports unified pointers.

`` cudaUUID_t uuid ``

16-byte unique identifier

`` int warpSize ``

Warp size in threads.
