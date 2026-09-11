<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/structCUasyncNotificationInfo.html

#  7.45. CUasyncNotificationInfo

Defined in cuda.h

`` struct CUasyncNotificationInfo ``

Information passed to the user via the async notification callback.

Public Members

`` CUasyncNotificationType type ``

The type of notification being sent.

`` unsigned long long bytesOverBudget ``

The number of bytes that the process has allocated above its device memory budget.

`` struct CUasyncNotificationInfo::[anonymous]::[anonymous] overBudget ``

Information about notifications of type `CU_ASYNC_NOTIFICATION_TYPE_OVER_BUDGET`.

`` union CUasyncNotificationInfo::[anonymous] info ``

Information about the notification.

`type` must be checked in order to interpret this field.
