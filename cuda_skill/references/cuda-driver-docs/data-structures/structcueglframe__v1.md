<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUeglFrame__v1.html

#  7.62. CUeglFrame_v1

Defined in cudaEGL.h

`` struct CUeglFrame_v1 ``

CUDA EGLFrame structure Descriptor - structure defining one frame of EGL.

Each frame may contain one or more planes depending on whether the surface * is Multiplanar or not.

Public Members

`` CUarray pArray[MAX_PLANES] ``

Array of CUarray corresponding to each plane.

`` void *pPitch[MAX_PLANES] ``

Array of Pointers corresponding to each plane.

`` union CUeglFrame_v1::[anonymous] frame ``

`` unsigned int width ``

Width of first plane.

`` unsigned int height ``

Height of first plane.

`` unsigned int depth ``

Depth of first plane.

`` unsigned int pitch ``

Pitch of first plane.

`` unsigned int planeCount ``

Number of planes.

`` unsigned int numChannels ``

Number of channels for the plane.

`` CUeglFrameType frameType ``

Array or Pitch.

`` CUeglColorFormat eglColorFormat ``

CUDA EGL Color Format.

`` CUarray_format cuFormat ``

CUDA Array Format.
