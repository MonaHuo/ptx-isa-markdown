<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaEglFrame.html

#  7.15. cudaEglFrame

`` struct cudaEglFrame ``

CUDA EGLFrame Descriptor - structure defining one frame of EGL.

Each frame may contain one or more planes depending on whether the surface is Multiplanar or not. Each plane of EGLFrame is represented by cudaEglPlaneDesc which is defined as:

```cpp
typedef struct cudaEglPlaneDesc_st {
    unsigned int width;
    unsigned int height;
    unsigned int depth;
    unsigned int pitch;
    unsigned int numChannels;
    struct cudaChannelFormatDesc channelDesc;
    unsigned int reserved[4];
} cudaEglPlaneDesc;
```

Public Members

`` cudaEglColorFormat eglColorFormat ``

CUDA EGL Color Format.

`` union cudaEglFrame::[anonymous] frame ``

`` cudaEglFrameType frameType ``

Array or Pitch.

`` cudaArray_t pArray[3] ``

Array of CUDA arrays corresponding to each plane.

`` unsigned int planeCount ``

Number of planes.

`` cudaEglPlaneDesc planeDesc[3] ``

CUDA EGL Plane Descriptor cudaEglPlaneDesc.

`` struct cudaPitchedPtr pPitch[3] ``

Array of Pointers corresponding to each plane.
