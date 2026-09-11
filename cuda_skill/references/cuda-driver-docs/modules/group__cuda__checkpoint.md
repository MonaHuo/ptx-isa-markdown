<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/group__CUDA__CHECKPOINT.html

#  6.1. CUDA Checkpointing

CUDA API versioning support.

This sections describes the checkpoint and restore functions of the low-level CUDA driver application programming interface.

The CUDA checkpoint and restore API’s provide a way to save and restore GPU state for full process checkpoints when used with CPU side process checkpointing solutions. They can also be used to pause GPU work and suspend a CUDA process to allow other applications to make use of GPU resources.

Checkpoint and restore capabilities are currently restricted to Linux.

##  6.1.1. Functions

`` CUresult cuCheckpointOperationComplete(CUcheckpointOperationHandle handle) ``

Complete a custom-storage checkpoint or restore operation.

After cuCheckpointProcessCheckpoint or cuCheckpointProcessRestore with custom storage, cuCheckpointOperationComplete should be called when the application has finished or enqueued (on a stream) the required copies (for checkpoint, GPU mappings to custom storage and for restore, custom storage into GPU mappings) so the driver can finish the operation.

cuCheckpointOperationComplete will first synchronize on the streams returned by cuCheckpointProcessCheckpoint or cuCheckpointProcessRestore. The driver assumes that the application has completed copying the memory to or from custom storage once synchronization is done. None of the streams returned by cuCheckpointProcessCheckpoint or cuCheckpointProcessRestore should be in stream capture mode; any attempt to do so would result in CUDA_ERROR_STREAM_CAPTURE_UNSUPPORTED. Once the synchronization is done, cuCheckpointOperationComplete will unmap the GPU memory that was mapped on each GPU in a particular cuCheckpointProcessCheckpoint or cuCheckpointProcessRestore operation. cuCheckpointOperationComplete identifies the operation to be completed using `handle`. This handle is set by cuCheckpointProcessCheckpoint or cuCheckpointProcessRestore.

When the call returns successfully, the target process will be in the CU_PROCESS_STATE_CHECKPOINTED state when completing a checkpoint operation or the CU_PROCESS_STATE_LOCKED state when completing a restore operation.

Parameters

**handle** – - CUcheckpointCustomStorageInfo::handle set by a prior cuCheckpointProcessCheckpoint or cuCheckpointProcessRestore call

Returns

CUDA_SUCCESS CUDA_ERROR_INVALID_VALUE CUDA_ERROR_NOT_INITIALIZED CUDA_ERROR_ILLEGAL_STATE CUDA_ERROR_NOT_SUPPORTED

`` CUresult cuCheckpointProcessCheckpoint(int pid, CUcheckpointCheckpointArgs *args) ``

Checkpoint a CUDA process’s GPU memory contents.

Checkpoints a CUDA process specified by `pid`. The GPU memory contents will be brought into host memory or mapped onto the calling process’s GPUs for user-defined behavior. Underlying GPU references are released when checkpointing completes. The process must be in the CU_PROCESS_STATE_LOCKED state to checkpoint.

When CUcheckpointCheckpointArgs::customStorageInfo_out is not NULL, all the GPU memory allocated by the process with `pid` will be mapped onto the calling process’s GPUs so the application can copy the memory to custom storage. Upon return of this call, the pointer referenced by CUcheckpointCheckpointArgs::customStorageInfo_out will point to a CUcheckpointCustomStorageInfo struct allocated and populated by the driver. For each GPU which contains data from the checkpointed process, there is a corresponding entry in the CUcheckpointCustomStoragePerDeviceData array.

  * The device pointers and sizes for the contiguously mapped memory on a particular GPU are set in the CUcheckpointCustomStoragePerDeviceData::devPtr and CUcheckpointCustomStoragePerDeviceData::size fields respectively.

  * A stream belonging to the primary context of a particular GPU is set in CUcheckpointCustomStoragePerDeviceData::stream. The application can use the stream to find out which GPU the memory is mapped on and to enqueue the copies to custom storage.

The application is responsible for copying the mapped data from the GPU at the specified device address to custom storage. When checkpointing to custom storage, the application is expected to call cuCheckpointOperationComplete. The CUcheckpointCustomStorageInfo::handle set by this call should be passed to cuCheckpointOperationComplete in `handle`. The driver synchronizes all the streams in cuCheckpointOperationComplete, at which point the copy to custom storage is considered complete.

When checkpointing to custom storage, the application is expected to retain primary contexts of all the devices used by the process to be checkpointed. Otherwise cuCheckpointProcessCheckpoint will return CUDA_ERROR_INVALID_CONTEXT. Unlike other checkpoint operations, checkpointing to custom storage requires cuInit to have been called before execution. Checkpointing the calling process’s GPU memory to custom storage is not supported. Upon successful return, the target process will be in the CU_PROCESS_STATE_CHECKPOINTING state.

When CUcheckpointCheckpointArgs::customStorageInfo_out is NULL, the GPU memory contents will be brought into host memory by cuCheckpointProcessCheckpoint. The application is not expected to copy the GPU memory contents. The application is also not expected to call cuCheckpointOperationComplete. Upon successful return, the target process will be in the CU_PROCESS_STATE_CHECKPOINTED state.

Parameters

  * **pid** – - The process ID of the CUDA process

  * **args** – - Optional checkpoint operation arguments

Returns

CUDA_SUCCESS CUDA_ERROR_INVALID_VALUE CUDA_ERROR_NOT_INITIALIZED CUDA_ERROR_ILLEGAL_STATE CUDA_ERROR_NOT_SUPPORTED CUDA_ERROR_INVALID_CONTEXT

`` CUresult cuCheckpointProcessGetRestoreThreadId(int pid, int *tid) ``

Returns the restore thread ID for a CUDA process.

Returns in `*tid` the thread ID of the CUDA restore thread for the process specified by `pid`.

Parameters

  * **pid** – - The process ID of the CUDA process

  * **tid** – - Returned restore thread ID

Returns

CUDA_SUCCESS CUDA_ERROR_INVALID_VALUE CUDA_ERROR_NOT_INITIALIZED CUDA_ERROR_NOT_SUPPORTED

`` CUresult cuCheckpointProcessGetState(int pid, CUprocessState *state) ``

Returns the process state of a CUDA process.

Returns in `*state` the current state of the CUDA process specified by `pid`.

Parameters

  * **pid** – - The process ID of the CUDA process

  * **state** – - Returned CUDA process state

Returns

CUDA_SUCCESS CUDA_ERROR_INVALID_VALUE CUDA_ERROR_NOT_INITIALIZED CUDA_ERROR_NOT_SUPPORTED

`` CUresult cuCheckpointProcessLock(int pid, CUcheckpointLockArgs *args) ``

Lock a running CUDA process.

Lock the CUDA process specified by `pid` which will block further CUDA API calls. Process must be in the RUNNING state in order to lock.

Upon successful return the process will be in the LOCKED state.

If timeoutMs is specified and the timeout is reached the process will be left in the RUNNING state upon return.

Parameters

  * **pid** – - The process ID of the CUDA process

  * **args** – - Optional lock operation arguments

Returns

CUDA_SUCCESS CUDA_ERROR_INVALID_VALUE CUDA_ERROR_NOT_INITIALIZED CUDA_ERROR_ILLEGAL_STATE CUDA_ERROR_NOT_SUPPORTED CUDA_ERROR_NOT_READY

`` CUresult cuCheckpointProcessRestore(int pid, CUcheckpointRestoreArgs *args) ``

Restore a CUDA process’s GPU memory contents from its last checkpoint.

Restores a CUDA process specified by `pid` from its last checkpoint. Process must be in the CU_PROCESS_STATE_CHECKPOINTED state to restore.

GPU UUID pairs can be specified in `args` to remap the process old GPUs onto new GPUs. The GPU to restore onto needs to have enough memory and be of the same chip type as the old GPU. If an array of GPU UUID pairs is specified, it must contain every checkpointed GPU.

CUDA process restore requires persistence mode to be enabled or cuInit to have been called before execution.

When CUcheckpointRestoreArgs::customStorageInfo_out is not NULL, all the GPU memory to be restored for the process with `pid` will be mapped onto the calling process’s GPUs so the application can copy the memory back to the GPU.

Upon return of this call, the pointer referenced by CUcheckpointRestoreArgs::customStorageInfo_out will point to a CUcheckpointCustomStorageInfo struct allocated and populated by the driver. For each GPU which contains data from the restored process, there is a corresponding entry in the CUcheckpointCustomStoragePerDeviceData array.

  * The device pointers and sizes for the contiguously mapped memory on a particular GPU are set in the CUcheckpointCustomStoragePerDeviceData::devPtr and CUcheckpointCustomStoragePerDeviceData::size fields respectively.

  * A stream belonging to the primary context of the GPU is set in CUcheckpointCustomStoragePerDeviceData::stream. The application can use the stream to find out which GPU the memory is mapped on and to enqueue the copies from custom storage back to the GPU.

The application is responsible for copying the data from custom storage to the GPU at the specified device address. When restoring from custom storage, the application is expected to call cuCheckpointOperationComplete. The CUcheckpointCustomStorageInfo::handle set by this call should be passed to cuCheckpointOperationComplete in `handle`. The driver synchronizes all the streams in cuCheckpointOperationComplete, at which point the copy from custom storage is considered complete.

When restoring from custom storage, the application is expected to retain primary contexts of all the devices used by the process to be restored. Otherwise cuCheckpointProcessRestore will return CUDA_ERROR_INVALID_CONTEXT

. Restoring the calling process’s

GPU memory from custom storage is not supported. Upon successful return, the target process will be in the

CU_PROCESS_STATE_RESTORING state.

When CUcheckpointRestoreArgs::customStorageInfo_out is NULL, the GPU memory contents will be restored from host memory by cuCheckpointProcessRestore. The application is not expected to copy back the GPU memory contents. The application is also not expected to call cuCheckpointOperationComplete. Upon successful return, the target process will be in the CU_PROCESS_STATE_LOCKED state.

See also

cuInit

Parameters

  * **pid** – - The process ID of the CUDA process

  * **args** – - Optional restore operation arguments

Returns

CUDA_SUCCESS CUDA_ERROR_INVALID_VALUE CUDA_ERROR_NOT_INITIALIZED CUDA_ERROR_ILLEGAL_STATE CUDA_ERROR_NOT_SUPPORTED CUDA_ERROR_INVALID_CONTEXT

`` CUresult cuCheckpointProcessUnlock(int pid, CUcheckpointUnlockArgs *args) ``

Unlock a CUDA process to allow CUDA API calls.

Unlocks a process specified by `pid` allowing it to resume making CUDA API calls. Process must be in the LOCKED state.

Upon successful return the process will be in the RUNNING state.

Parameters

  * **pid** – - The process ID of the CUDA process

  * **args** – - Optional unlock operation arguments

Returns

CUDA_SUCCESS CUDA_ERROR_INVALID_VALUE CUDA_ERROR_NOT_INITIALIZED CUDA_ERROR_ILLEGAL_STATE CUDA_ERROR_NOT_SUPPORTED
