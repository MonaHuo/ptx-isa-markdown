<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaMemcpy3DBatchOp.html

#  7.54. cudaMemcpy3DBatchOp

`` struct cudaMemcpy3DBatchOp ``

Public Members

`` struct cudaMemcpy3DOperand dst ``

Destination memcpy operand.

`` struct cudaExtent extent ``

Extents of the memcpy between src and dst.

The width, height and depth components must not be 0.

`` unsigned int flags ``

Additional flags for copy from src to dst.

See cudaMemcpyFlags.

`` struct cudaMemcpy3DOperand src ``

Source memcpy operand.

`` enum cudaMemcpySrcAccessOrder srcAccessOrder ``

Source access ordering to be observed for copy from src to dst.
