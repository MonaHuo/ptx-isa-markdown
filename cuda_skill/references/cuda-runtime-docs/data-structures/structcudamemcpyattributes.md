<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaMemcpyAttributes.html

#  7.58. cudaMemcpyAttributes

`` struct cudaMemcpyAttributes ``

Attributes specific to copies within a batch.

For more details on usage see cudaMemcpyBatchAsync.

Public Members

`` struct cudaMemLocation dstLocHint ``

Hint location for the destination operand.

Ignored when the pointers are not managed memory or memory allocated outside CUDA.

`` unsigned int flags ``

Additional flags for copies with this attribute.

See cudaMemcpyFlags.

`` enum cudaMemcpySrcAccessOrder srcAccessOrder ``

Source access ordering to be observed for copies with this attribute.

`` struct cudaMemLocation srcLocHint ``

Hint location for the source operand.

Ignored when the pointers are not managed memory or memory allocated outside CUDA.
