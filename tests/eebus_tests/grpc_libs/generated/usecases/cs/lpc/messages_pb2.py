# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: usecases/cs/lpc/messages.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'usecases/cs/lpc/messages.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common_types import types_pb2 as common__types_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eusecases/cs/lpc/messages.proto\x12\x06\x63s_lpc\x1a\x18\x63ommon_types/types.proto\"\x19\n\x17\x43onsumptionLimitRequest\"G\n\x18\x43onsumptionLimitResponse\x12+\n\nload_limit\x18\x01 \x01(\x0b\x32\x17.common_types.LoadLimit\"I\n\x1aSetConsumptionLimitRequest\x12+\n\nload_limit\x18\x01 \x01(\x0b\x32\x17.common_types.LoadLimit\"\x1d\n\x1bSetConsumptionLimitResponse\" \n\x1ePendingConsumptionLimitRequest\"\xbb\x01\n\x1fPendingConsumptionLimitResponse\x12L\n\x0bload_limits\x18\x01 \x03(\x0b\x32\x37.cs_lpc.PendingConsumptionLimitResponse.LoadLimitsEntry\x1aJ\n\x0fLoadLimitsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.common_types.LoadLimit:\x02\x38\x01\"\\\n$ApproveOrDenyConsumptionLimitRequest\x12\x13\n\x0bmsg_counter\x18\x01 \x01(\x04\x12\x0f\n\x07\x61pprove\x18\x02 \x01(\x08\x12\x0e\n\x06reason\x18\x03 \x01(\t\"\'\n%ApproveOrDenyConsumptionLimitResponse\",\n*FailsafeConsumptionActivePowerLimitRequest\"S\n+FailsafeConsumptionActivePowerLimitResponse\x12\r\n\x05limit\x18\x01 \x01(\x01\x12\x15\n\ris_changeable\x18\x02 \x01(\x08\"U\n-SetFailsafeConsumptionActivePowerLimitRequest\x12\r\n\x05value\x18\x01 \x01(\x01\x12\x15\n\ris_changeable\x18\x02 \x01(\x08\"0\n.SetFailsafeConsumptionActivePowerLimitResponse\" \n\x1e\x46\x61ilsafeDurationMinimumRequest\"V\n\x1f\x46\x61ilsafeDurationMinimumResponse\x12\x1c\n\x14\x64uration_nanoseconds\x18\x01 \x01(\x03\x12\x15\n\ris_changeable\x18\x02 \x01(\x08\"X\n!SetFailsafeDurationMinimumRequest\x12\x1c\n\x14\x64uration_nanoseconds\x18\x01 \x01(\x03\x12\x15\n\ris_changeable\x18\x02 \x01(\x08\"$\n\"SetFailsafeDurationMinimumResponse\"\x17\n\x15StartHeartbeatRequest\"\x18\n\x16StartHeartbeatResponse\"\x16\n\x14StopHeartbeatRequest\"\x17\n\x15StopHeartbeatResponse\"\"\n IsHeartbeatWithinDurationRequest\"?\n!IsHeartbeatWithinDurationResponse\x12\x1a\n\x12is_within_duration\x18\x01 \x01(\x08\"\x1e\n\x1c\x43onsumptionNominalMaxRequest\".\n\x1d\x43onsumptionNominalMaxResponse\x12\r\n\x05value\x18\x01 \x01(\x01\"0\n\x1fSetConsumptionNominalMaxRequest\x12\r\n\x05value\x18\x01 \x01(\x01\"\"\n SetConsumptionNominalMaxResponseBAZ?github.com/enbility/eebus-grpc-api/rpc_services/usecases/cs/lpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'usecases.cs.lpc.messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z?github.com/enbility/eebus-grpc-api/rpc_services/usecases/cs/lpc'
  _globals['_PENDINGCONSUMPTIONLIMITRESPONSE_LOADLIMITSENTRY']._loaded_options = None
  _globals['_PENDINGCONSUMPTIONLIMITRESPONSE_LOADLIMITSENTRY']._serialized_options = b'8\001'
  _globals['_CONSUMPTIONLIMITREQUEST']._serialized_start=68
  _globals['_CONSUMPTIONLIMITREQUEST']._serialized_end=93
  _globals['_CONSUMPTIONLIMITRESPONSE']._serialized_start=95
  _globals['_CONSUMPTIONLIMITRESPONSE']._serialized_end=166
  _globals['_SETCONSUMPTIONLIMITREQUEST']._serialized_start=168
  _globals['_SETCONSUMPTIONLIMITREQUEST']._serialized_end=241
  _globals['_SETCONSUMPTIONLIMITRESPONSE']._serialized_start=243
  _globals['_SETCONSUMPTIONLIMITRESPONSE']._serialized_end=272
  _globals['_PENDINGCONSUMPTIONLIMITREQUEST']._serialized_start=274
  _globals['_PENDINGCONSUMPTIONLIMITREQUEST']._serialized_end=306
  _globals['_PENDINGCONSUMPTIONLIMITRESPONSE']._serialized_start=309
  _globals['_PENDINGCONSUMPTIONLIMITRESPONSE']._serialized_end=496
  _globals['_PENDINGCONSUMPTIONLIMITRESPONSE_LOADLIMITSENTRY']._serialized_start=422
  _globals['_PENDINGCONSUMPTIONLIMITRESPONSE_LOADLIMITSENTRY']._serialized_end=496
  _globals['_APPROVEORDENYCONSUMPTIONLIMITREQUEST']._serialized_start=498
  _globals['_APPROVEORDENYCONSUMPTIONLIMITREQUEST']._serialized_end=590
  _globals['_APPROVEORDENYCONSUMPTIONLIMITRESPONSE']._serialized_start=592
  _globals['_APPROVEORDENYCONSUMPTIONLIMITRESPONSE']._serialized_end=631
  _globals['_FAILSAFECONSUMPTIONACTIVEPOWERLIMITREQUEST']._serialized_start=633
  _globals['_FAILSAFECONSUMPTIONACTIVEPOWERLIMITREQUEST']._serialized_end=677
  _globals['_FAILSAFECONSUMPTIONACTIVEPOWERLIMITRESPONSE']._serialized_start=679
  _globals['_FAILSAFECONSUMPTIONACTIVEPOWERLIMITRESPONSE']._serialized_end=762
  _globals['_SETFAILSAFECONSUMPTIONACTIVEPOWERLIMITREQUEST']._serialized_start=764
  _globals['_SETFAILSAFECONSUMPTIONACTIVEPOWERLIMITREQUEST']._serialized_end=849
  _globals['_SETFAILSAFECONSUMPTIONACTIVEPOWERLIMITRESPONSE']._serialized_start=851
  _globals['_SETFAILSAFECONSUMPTIONACTIVEPOWERLIMITRESPONSE']._serialized_end=899
  _globals['_FAILSAFEDURATIONMINIMUMREQUEST']._serialized_start=901
  _globals['_FAILSAFEDURATIONMINIMUMREQUEST']._serialized_end=933
  _globals['_FAILSAFEDURATIONMINIMUMRESPONSE']._serialized_start=935
  _globals['_FAILSAFEDURATIONMINIMUMRESPONSE']._serialized_end=1021
  _globals['_SETFAILSAFEDURATIONMINIMUMREQUEST']._serialized_start=1023
  _globals['_SETFAILSAFEDURATIONMINIMUMREQUEST']._serialized_end=1111
  _globals['_SETFAILSAFEDURATIONMINIMUMRESPONSE']._serialized_start=1113
  _globals['_SETFAILSAFEDURATIONMINIMUMRESPONSE']._serialized_end=1149
  _globals['_STARTHEARTBEATREQUEST']._serialized_start=1151
  _globals['_STARTHEARTBEATREQUEST']._serialized_end=1174
  _globals['_STARTHEARTBEATRESPONSE']._serialized_start=1176
  _globals['_STARTHEARTBEATRESPONSE']._serialized_end=1200
  _globals['_STOPHEARTBEATREQUEST']._serialized_start=1202
  _globals['_STOPHEARTBEATREQUEST']._serialized_end=1224
  _globals['_STOPHEARTBEATRESPONSE']._serialized_start=1226
  _globals['_STOPHEARTBEATRESPONSE']._serialized_end=1249
  _globals['_ISHEARTBEATWITHINDURATIONREQUEST']._serialized_start=1251
  _globals['_ISHEARTBEATWITHINDURATIONREQUEST']._serialized_end=1285
  _globals['_ISHEARTBEATWITHINDURATIONRESPONSE']._serialized_start=1287
  _globals['_ISHEARTBEATWITHINDURATIONRESPONSE']._serialized_end=1350
  _globals['_CONSUMPTIONNOMINALMAXREQUEST']._serialized_start=1352
  _globals['_CONSUMPTIONNOMINALMAXREQUEST']._serialized_end=1382
  _globals['_CONSUMPTIONNOMINALMAXRESPONSE']._serialized_start=1384
  _globals['_CONSUMPTIONNOMINALMAXRESPONSE']._serialized_end=1430
  _globals['_SETCONSUMPTIONNOMINALMAXREQUEST']._serialized_start=1432
  _globals['_SETCONSUMPTIONNOMINALMAXREQUEST']._serialized_end=1480
  _globals['_SETCONSUMPTIONNOMINALMAXRESPONSE']._serialized_start=1482
  _globals['_SETCONSUMPTIONNOMINALMAXRESPONSE']._serialized_end=1516
# @@protoc_insertion_point(module_scope)
