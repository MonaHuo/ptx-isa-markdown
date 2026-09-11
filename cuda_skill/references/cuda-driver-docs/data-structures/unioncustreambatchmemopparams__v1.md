<!-- CUDA Driver API 13.4 -->
Source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/unionCUstreamBatchMemOpParams__v1.html

# CUstreamBatchMemOpParams_v1

Defined in cuda.h

Structs

CUstreamMemOpAtomicReductionParams_st

CUstreamMemOpFlushRemoteWritesParams_st

CUstreamMemOpMemoryBarrierParams_st

CUstreamMemOpWaitValueParams_st

CUstreamMemOpWriteValueParams_st

`` union CUstreamBatchMemOpParams_v1 ``

Per-operation parameters for cuStreamBatchMemOp.

Public Members

`` CUstreamBatchMemOpType operation ``

Operation.

This is the first field of all the union elemets and acts as a TAG to determine which union member is valid.

`` struct CUstreamBatchMemOpParams_v1::CUstreamMemOpWaitValueParams_st waitValue ``

Params for CU_STREAM_MEM_OP_WAIT_VALUE_32 and CU_STREAM_MEM_OP_WAIT_VALUE_64 operations.

`` struct CUstreamBatchMemOpParams_v1::CUstreamMemOpWriteValueParams_st writeValue ``

Params for CU_STREAM_MEM_OP_WRITE_VALUE_32 and CU_STREAM_MEM_OP_WRITE_VALUE_64 operations.

`` struct CUstreamBatchMemOpParams_v1::CUstreamMemOpFlushRemoteWritesParams_st flushRemoteWrites ``

Params for CU_STREAM_MEM_OP_FLUSH_REMOTE_WRITES operations.

`` struct CUstreamBatchMemOpParams_v1::CUstreamMemOpMemoryBarrierParams_st memoryBarrier ``

Params for CU_STREAM_MEM_OP_BARRIER operations.

`` struct CUstreamBatchMemOpParams_v1::CUstreamMemOpAtomicReductionParams_st atomicReduction ``

`` cuuint64_t pad[6] ``

`` struct CUstreamMemOpAtomicReductionParams_st ``

Public Members

`` CUstreamBatchMemOpType operation ``

`` unsigned int flags ``

Must be 0.

`` CUstreamAtomicReductionOpType reductionOp ``

See CUstreamAtomicReductionOpType.

`` CUstreamAtomicReductionDataType dataType ``

See CUstreamAtomicReductionDataType.

`` CUdeviceptr address ``

The address the atomic operation will be operated on.

`` cuuint64_t value ``

The operand value the atomic operation will operate with.

`` CUdeviceptr alias ``

For driver internal use.

Initial value is unimportant.

`` struct CUstreamMemOpFlushRemoteWritesParams_st ``

Public Members

`` CUstreamBatchMemOpType operation ``

`` unsigned int flags ``

Must be 0.

`` struct CUstreamMemOpMemoryBarrierParams_st ``

Public Members

`` CUstreamBatchMemOpType operation ``

< Only supported in the _v2 API

`` unsigned int flags ``

See CUstreamMemoryBarrier_flags.

`` struct CUstreamMemOpWaitValueParams_st ``

Public Members

`` CUstreamBatchMemOpType operation ``

`` CUdeviceptr address ``

`` cuuint32_t value ``

`` cuuint64_t value64 ``

`` union CUstreamBatchMemOpParams_v1::CUstreamMemOpWaitValueParams_st::[anonymous] [anonymous] ``

`` unsigned int flags ``

See CUstreamWaitValue_flags.

`` CUdeviceptr alias ``

For driver internal use.

Initial value is unimportant.

`` struct CUstreamMemOpWriteValueParams_st ``

Public Members

`` CUstreamBatchMemOpType operation ``

`` CUdeviceptr address ``

`` cuuint32_t value ``

`` cuuint64_t value64 ``

`` union CUstreamBatchMemOpParams_v1::CUstreamMemOpWriteValueParams_st::[anonymous] [anonymous] ``

`` unsigned int flags ``

See CUstreamWriteValue_flags.

`` CUdeviceptr alias ``

For driver internal use.

Initial value is unimportant.
