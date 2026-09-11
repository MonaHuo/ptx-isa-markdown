<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaTextureDesc.html

#  7.68. cudaTextureDesc

`` struct cudaTextureDesc ``

CUDA texture descriptor.

Public Members

`` enum cudaTextureAddressMode addressMode[3] ``

Texture address mode for up to 3 dimensions.

`` float borderColor[4] ``

Texture Border Color.

`` int disableTrilinearOptimization ``

Disable any trilinear filtering optimizations.

`` enum cudaTextureFilterMode filterMode ``

Texture filter mode.

`` unsigned int maxAnisotropy ``

Limit to the anisotropy ratio.

`` float maxMipmapLevelClamp ``

Upper end of the mipmap level range to clamp access to.

`` float minMipmapLevelClamp ``

Lower end of the mipmap level range to clamp access to.

`` enum cudaTextureFilterMode mipmapFilterMode ``

Mipmap filter mode.

`` float mipmapLevelBias ``

Offset applied to the supplied mipmap level.

`` int normalizedCoords ``

Indicates whether texture reads are normalized or not.

`` enum cudaTextureReadMode readMode ``

Texture read mode.

`` int seamlessCubemap ``

Enable seamless cube map filtering.

`` int sRGB ``

Perform sRGB->linear conversion during texture read.
