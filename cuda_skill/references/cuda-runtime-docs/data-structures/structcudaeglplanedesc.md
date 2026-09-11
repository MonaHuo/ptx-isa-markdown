<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaEglPlaneDesc.html

#  7.16. cudaEglPlaneDesc

`` struct cudaEglPlaneDesc ``

CUDA EGL Plane Descriptor - structure defining each plane of a CUDA EGLFrame.

Public Members

`` struct cudaChannelFormatDesc channelDesc ``

Channel Format Descriptor.

`` unsigned int depth ``

Depth of plane.

`` unsigned int height ``

Height of plane.

`` unsigned int numChannels ``

Number of channels for the plane.

`` unsigned int pitch ``

Pitch of plane.

`` unsigned int reserved[4] ``

Reserved for future use.

`` unsigned int width ``

Width of plane.
