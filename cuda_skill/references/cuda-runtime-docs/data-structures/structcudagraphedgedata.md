<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaGraphEdgeData.html

#  7.31. cudaGraphEdgeData

`` struct cudaGraphEdgeData ``

Optional annotation for edges in a CUDA graph.

Note, all edges implicitly have annotations and default to a zero-initialized value if not specified. A zero-initialized struct indicates a standard full serialization of two nodes with memory visibility.

Public Members

`` unsigned char from_port ``

This indicates when the dependency is triggered from the upstream node on the edge.

The meaning is specfic to the node type. A value of 0 in all cases means full completion of the upstream node, with memory visibility to the downstream node or portion thereof (indicated by `to_port`

).

Only kernel nodes define non-zero ports. A kernel node can use the following output port types:

cudaGraphKernelNodePortDefault, cudaGraphKernelNodePortProgrammatic, or cudaGraphKernelNodePortLaunchCompletion.

`` unsigned char reserved[5] ``

These bytes are unused and must be zeroed.

This ensures compatibility if additional fields are added in the future.

`` unsigned char to_port ``

This indicates what portion of the downstream node is dependent on the upstream node or portion thereof (indicated by `from_port`).

The meaning is specific to the node type. A value of 0 in all cases means the entirety of the downstream node is dependent on the upstream work.

Currently no node types define non-zero ports. Accordingly, this field must be set to zero.

`` unsigned char type ``

This should be populated with a value from cudaGraphDependencyType.

(It is typed as char due to compiler-specific layout of bitfields.) See cudaGraphDependencyType.
