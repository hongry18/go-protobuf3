# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\x02pb\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb8\x02\n\x06Person\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x03\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12&\n\x06phones\x18\x04 \x03(\x0b\x32\x16.pb.Person.PhoneNumber\x12\x30\n\x0clast_updated\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a\x41\n\x0bPhoneNumber\x12\x0e\n\x06number\x18\x01 \x01(\t\x12\"\n\x04type\x18\x02 \x01(\x0e\x32\x14.pb.Person.PhoneType\"h\n\tPhoneType\x12\x1a\n\x16PHONE_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11PHONE_TYPE_MOBILE\x10\x01\x12\x13\n\x0fPHONE_TYPE_HOME\x10\x02\x12\x13\n\x0fPHONE_TYPE_WORK\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_PERSON']._serialized_start=52
  _globals['_PERSON']._serialized_end=364
  _globals['_PERSON_PHONENUMBER']._serialized_start=193
  _globals['_PERSON_PHONENUMBER']._serialized_end=258
  _globals['_PERSON_PHONETYPE']._serialized_start=260
  _globals['_PERSON_PHONETYPE']._serialized_end=364
# @@protoc_insertion_point(module_scope)