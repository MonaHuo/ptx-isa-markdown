<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaFuncAttributes.html

#  7.30. cudaFuncAttributes

`` struct cudaFuncAttributes ``

CUDA function attributes.

Public Members

`` int binaryVersion ``

The binary architecture version for which the function was compiled.

This value is the major binary version * 10 + the minor binary version, so a binary version 1.3 function would return the value 13.

`` int cacheModeCA ``

The attribute to indicate whether the function has been compiled with user specified option “-Xptxas –dlcm=ca” set.

`` int clusterDimMustBeSet ``

If this attribute is set, the kernel must launch with a valid cluster dimension specified.

`` int clusterSchedulingPolicyPreference ``

The block scheduling policy of a function.

See cudaFuncSetAttribute

`` size_t constSizeBytes ``

The size in bytes of user-allocated constant memory required by this function.

`` int deviceNodeUpdateStatus ``

Whether the function can be updated on device.

1 means device node update is supported, 0 is unsupported or driver is too old to check the value.

`` size_t localSizeBytes ``

The size in bytes of local memory used by each thread of this function.

`` int maxDynamicSharedSizeBytes ``

The maximum size in bytes of dynamic shared memory per block for this function.

Any launch must have a dynamic shared memory size smaller than this value.

This attribute is ignored if the sharedMemoryMode function or launch attribute is set.

This attribute cannot be used to access oversized shared memory. Oversized shared memory can only be accessed by setting the shared memory mode.

See cudaFuncSetAttribute

`` int maxThreadsPerBlock ``

The maximum number of threads per block, beyond which a launch of the function would fail.

This number depends on both the function and the device on which the function is currently loaded.

`` int nonPortableClusterSizeAllowed ``

Whether the function can be launched with non-portable cluster size.

1 is allowed, 0 is disallowed. A non-portable cluster size may only function on the specific SKUs the program is tested on. The launch might fail if the program is run on a different hardware platform.

CUDA API provides cudaOccupancyMaxActiveClusters to assist with checking whether the desired size can be launched on the current device.

Portable Cluster Size

A portable cluster size is guaranteed to be functional on all compute capabilities higher than the target compute capability. The portable cluster size for sm_90 is 8 blocks per cluster. This value may increase for future compute capabilities.

The specific hardware unit may support higher cluster sizes that’s not guaranteed to be portable.

See cudaFuncSetAttribute

`` int numRegs ``

The number of registers used by each thread of this function.

`` int preferredShmemCarveout ``

On devices where the L1 cache and shared memory use the same hardware resources, this sets the shared memory carveout preference, in percent of the maximum shared memory.

Refer to cudaDevAttrMaxSharedMemoryPerMultiprocessor. This is only a hint, and the driver can choose a different ratio if required to execute the function.

See cudaFuncSetAttribute

`` int ptxVersion ``

The PTX virtual architecture version for which the function was compiled.

This value is the major PTX version * 10 + the minor PTX version, so a PTX version 1.3 function would return the value 13.

`` int requiredClusterDepth ``

`` int requiredClusterHeight ``

`` int requiredClusterWidth ``

The required cluster width/height/depth in blocks.

The values must either all be 0 or all be positive. The validity of the cluster dimensions is otherwise checked at launch time.

If the value is set during compile time, it cannot be set at runtime. Setting it at runtime should return cudaErrorNotPermitted.

See cudaFuncSetAttribute

`` int reserved[14] ``

Reserved for future use.

`` cudaSharedMemoryMode sharedMemoryMode ``

This controls a kernel’s use of non-portable or oversized shared memory configurations.

See cudaFuncSetAttribute

`` size_t sharedSizeBytes ``

The size in bytes of statically-allocated shared memory per block required by this function.

This does not include dynamically-allocated shared memory requested by the user at runtime.
