<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaGraphKernelNodeUpdate.html

#  7.34. cudaGraphKernelNodeUpdate

`` struct cudaGraphKernelNodeUpdate ``

Struct to specify a single node update to pass as part of a larger array to cudaGraphKernelNodeUpdatesApply.

Public Members

`` enum cudaGraphKernelNodeField field ``

Which type of update to apply.

Determines how updateData is interpreted

`` uint3 gridDim ``

Grid dimensions.

`` unsigned int isEnabled ``

Node enable/disable data.

Nonzero if the node should be enabled, 0 if it should be disabled

`` cudaGraphDeviceNode_t node ``

Node to update.

`` size_t offset ``

Offset into the parameter buffer at which to apply the update.

`` struct cudaGraphKernelNodeUpdate::[anonymous]::[anonymous] param ``

Kernel parameter data.

`` const void *pValue ``

Kernel parameter data to write in.

`` size_t size ``

Number of bytes to update.

`` union cudaGraphKernelNodeUpdate::[anonymous] updateData ``

Update data to apply.

Which field is used depends on field’s value
