<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUDA__TEXTURE__DESC__v1.html

#  7.41. CUDA_TEXTURE_DESC_v1

Defined in cuda.h

`` struct CUDA_TEXTURE_DESC_v1 ``

Texture descriptor.

Public Members

`` CUaddress_mode addressMode[3] ``

Address modes.

`` CUfilter_mode filterMode ``

Filter mode.

`` unsigned int flags ``

Flags.

`` unsigned int maxAnisotropy ``

Maximum anisotropy ratio.

`` CUfilter_mode mipmapFilterMode ``

Mipmap filter mode.

`` float mipmapLevelBias ``

Mipmap level bias.

`` float minMipmapLevelClamp ``

Mipmap minimum level clamp.

`` float maxMipmapLevelClamp ``

Mipmap maximum level clamp.

`` float borderColor[4] ``

Border Color.

`` int reserved[12] ``
