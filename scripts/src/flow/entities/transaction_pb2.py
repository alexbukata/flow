# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flow/entities/transaction.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flow.entities import event_pb2 as flow_dot_entities_dot_event__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x66low/entities/transaction.proto\x12\rflow.entities\x1a\x19\x66low/entities/event.proto\"\xd0\x03\n\x0bTransaction\x12\x0e\n\x06script\x18\x01 \x01(\x0c\x12\x11\n\targuments\x18\x02 \x03(\x0c\x12\x1a\n\x12reference_block_id\x18\x03 \x01(\x0c\x12\x11\n\tgas_limit\x18\x04 \x01(\x04\x12<\n\x0cproposal_key\x18\x05 \x01(\x0b\x32&.flow.entities.Transaction.ProposalKey\x12\r\n\x05payer\x18\x06 \x01(\x0c\x12\x13\n\x0b\x61uthorizers\x18\x07 \x03(\x0c\x12@\n\x12payload_signatures\x18\x08 \x03(\x0b\x32$.flow.entities.Transaction.Signature\x12\x41\n\x13\x65nvelope_signatures\x18\t \x03(\x0b\x32$.flow.entities.Transaction.Signature\x1aG\n\x0bProposalKey\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x0e\n\x06key_id\x18\x02 \x01(\r\x12\x17\n\x0fsequence_number\x18\x03 \x01(\x04\x1a?\n\tSignature\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x0e\n\x06key_id\x18\x02 \x01(\r\x12\x11\n\tsignature\x18\x03 \x01(\x0c*c\n\x11TransactionStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\r\n\tFINALIZED\x10\x02\x12\x0c\n\x08\x45XECUTED\x10\x03\x12\n\n\x06SEALED\x10\x04\x12\x0b\n\x07\x45XPIRED\x10\x05\x42P\n\x1corg.onflow.protobuf.entitiesZ0github.com/onflow/flow/protobuf/go/flow/entitiesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flow.entities.transaction_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034org.onflow.protobuf.entitiesZ0github.com/onflow/flow/protobuf/go/flow/entities'
  _globals['_TRANSACTIONSTATUS']._serialized_start=544
  _globals['_TRANSACTIONSTATUS']._serialized_end=643
  _globals['_TRANSACTION']._serialized_start=78
  _globals['_TRANSACTION']._serialized_end=542
  _globals['_TRANSACTION_PROPOSALKEY']._serialized_start=406
  _globals['_TRANSACTION_PROPOSALKEY']._serialized_end=477
  _globals['_TRANSACTION_SIGNATURE']._serialized_start=479
  _globals['_TRANSACTION_SIGNATURE']._serialized_end=542
# @@protoc_insertion_point(module_scope)
