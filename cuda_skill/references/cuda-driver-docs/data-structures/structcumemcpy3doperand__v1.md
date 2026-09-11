<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUmemcpy3DOperand__v1.html

#  7.84. CUmemcpy3DOperand_v1

Defined in cuda.h

`` struct CUmemcpy3DOperand_v1 ``

Struct representing an operand for copy with cuMemcpy3DBatchAsync.

Public Members

`` CUmemcpy3DOperandType type ``

`` CUdeviceptr ptr ``

`` size_t rowLength ``

Length of each row in elements.

`` size_t layerHeight ``

Height of each layer in elements.

`` CUmemLocation locHint ``

Hint location for the operand.

Ignored when the pointers are not managed memory or memory allocated outside CUDA.

`` struct CUmemcpy3DOperand_v1::[anonymous]::[anonymous] ptr ``

Struct representing an operand when CUmemcpy3DOperand::type is CU_MEMCPY_OPERAND_TYPE_POINTER.

`` CUarray array ``

referenced array

`` CUoffset3D offset ``

offset into the array in elements

`` struct CUmemcpy3DOperand_v1::[anonymous]::[anonymous] array ``

Struct representing an operand when CUmemcpy3DOperand::type is CU_MEMCPY_OPERAND_TYPE_ARRAY.

`` union CUmemcpy3DOperand_v1::[anonymous] op ``
