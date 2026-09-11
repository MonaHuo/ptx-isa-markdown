<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaMemcpy3DPeerParms.html

#  7.57. cudaMemcpy3DPeerParms

`` struct cudaMemcpy3DPeerParms ``

CUDA 3D cross-device memory copying parameters.

Public Members

`` cudaArray_t dstArray ``

Destination memory address.

`` int dstDevice ``

Destination device.

`` struct cudaPos dstPos ``

Destination position offset.

`` struct cudaPitchedPtr dstPtr ``

Pitched destination memory address.

`` struct cudaExtent extent ``

Requested memory copy size.

`` cudaArray_t srcArray ``

Source memory address.

`` int srcDevice ``

Source device.

`` struct cudaPos srcPos ``

Source position offset.

`` struct cudaPitchedPtr srcPtr ``

Pitched source memory address.
