<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaMemcpy3DOperand.html

#  7.55. cudaMemcpy3DOperand

`` struct cudaMemcpy3DOperand ``

Struct representing an operand for copy with cudaMemcpy3DBatchAsync.

Public Members

`` cudaArray_t array ``

`` struct cudaMemcpy3DOperand::[anonymous]::[anonymous] array ``

Struct representing an operand when cudaMemcpy3DOperand::type is cudaMemcpyOperandTypeArray.

`` size_t layerHeight ``

Height of each layer in elements.

`` struct cudaMemLocation locHint ``

Hint location for the operand.

Ignored when the pointers are not managed memory or memory allocated outside CUDA.

`` struct cudaOffset3D offset ``

`` union cudaMemcpy3DOperand::[anonymous] op ``

`` void *ptr ``

`` struct cudaMemcpy3DOperand::[anonymous]::[anonymous] ptr ``

Struct representing an operand when cudaMemcpy3DOperand::type is cudaMemcpyOperandTypePointer.

`` size_t rowLength ``

Length of each row in elements.

`` enum cudaMemcpy3DOperandType type ``
