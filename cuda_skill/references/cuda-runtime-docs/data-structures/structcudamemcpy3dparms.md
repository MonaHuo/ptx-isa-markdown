<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaMemcpy3DParms.html

#  7.56. cudaMemcpy3DParms

`` struct cudaMemcpy3DParms ``

CUDA 3D memory copying parameters.

Public Members

`` cudaArray_t dstArray ``

Destination memory address.

`` struct cudaPos dstPos ``

Destination position offset.

`` struct cudaPitchedPtr dstPtr ``

Pitched destination memory address.

`` struct cudaExtent extent ``

Requested memory copy size.

`` enum cudaMemcpyKind kind ``

Type of transfer.

`` cudaArray_t srcArray ``

Source memory address.

`` struct cudaPos srcPos ``

Source position offset.

`` struct cudaPitchedPtr srcPtr ``

Pitched source memory address.
