<!-- CUDA Runtime API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/structcudaAsyncNotificationInfo__t.html

#  7.5. cudaAsyncNotificationInfo_t

`` struct cudaAsyncNotificationInfo_t ``

Information describing an async notification event.

Public Members

`` unsigned long long bytesOverBudget ``

The number of bytes that the process has allocated above its device memory budget.

`` union cudaAsyncNotificationInfo_t::[anonymous] info ``

Information about the notification.

`type` must be checked in order to interpret this field.

`` struct cudaAsyncNotificationInfo_t::[anonymous]::[anonymous] overBudget ``

Information about notifications of type `cudaAsyncNotificationTypeOverBudget`.

`` cudaAsyncNotificationType type ``

The type of notification being sent.
