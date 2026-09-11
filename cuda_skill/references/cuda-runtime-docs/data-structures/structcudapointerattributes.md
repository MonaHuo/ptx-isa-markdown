<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaPointerAttributes.html

#  7.64. cudaPointerAttributes

`` struct cudaPointerAttributes ``

CUDA pointer attributes.

Public Members

`` union cudaPointerAttributes::[anonymous] [anonymous] ``

Locality domain ordinal for device allocations localized to a locality domain, or -1 when the allocation is not localized to a locality domain.

`` int device ``

The device against which the memory was allocated or registered.

If the memory type is cudaMemoryTypeDevice then this identifies the device on which the memory referred physically resides. If the memory type is cudaMemoryTypeHost or::cudaMemoryTypeManaged then this identifies the device which was current when the memory was allocated or registered (and if that device is deinitialized then this allocation will vanish with that device’s state).

`` void *devicePointer ``

The address which may be dereferenced on the current device to access the memory or NULL if no such address exists.

`` void *hostPointer ``

The address which may be dereferenced on the host to access the memory or NULL if no such address exists.

Note

CUDA doesn’t check if unregistered memory is allocated so this field may contain invalid pointer if an invalid pointer has been passed to CUDA.

`` int localityDomainOrdinal ``

`` long reserved[7] ``

Must be zero.

`` enum cudaMemoryType type ``

The type of memory - cudaMemoryTypeUnregistered, cudaMemoryTypeHost, cudaMemoryTypeDevice or cudaMemoryTypeManaged.

`` long unused ``
