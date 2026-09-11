<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaGraphRecaptureCallbackData.html

#  7.36. cudaGraphRecaptureCallbackData

`` struct cudaGraphRecaptureCallbackData ``

Struct of user callback data that is invoked when node parameter mismatches are detected while recapturing to an existing graph.

Public Members

`` cudaGraphRecaptureCallback_t callbackFunc ``

Callback function that will be invoked.

`` void *userData ``

Generic pointer that is passed to the callback function.
