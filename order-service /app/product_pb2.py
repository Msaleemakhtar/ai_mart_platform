# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: product.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rproduct.proto\x12\x07product\"\xb7\x02\n\x07Product\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\x01\x12\x0e\n\x06\x65xpiry\x18\x05 \x01(\t\x12\r\n\x05\x62rand\x18\x06 \x01(\t\x12\x0e\n\x06weight\x18\x07 \x01(\x01\x12\x13\n\x0b\x63\x61tegory_id\x18\x08 \x01(\x05\x12\x0b\n\x03sku\x18\t \x01(\t\x12\x16\n\x0estock_quantity\x18\n \x01(\x05\x12\x15\n\rreorder_level\x18\x0b \x01(\x05\x12\x12\n\nmeta_title\x18\x0c \x01(\t\x12\x18\n\x10meta_description\x18\r \x01(\t\x12\x15\n\rmeta_keywords\x18\x0e \x01(\t\x12)\n\toperation\x18\x0f \x01(\x0e\x32\x16.product.OperationType\"1\n\x0bProductList\x12\"\n\x08products\x18\x01 \x03(\x0b\x32\x10.product.Product*3\n\rOperationType\x12\n\n\x06\x43REATE\x10\x00\x12\n\n\x06UPDATE\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'product_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _OPERATIONTYPE._serialized_start=391
  _OPERATIONTYPE._serialized_end=442
  _PRODUCT._serialized_start=27
  _PRODUCT._serialized_end=338
  _PRODUCTLIST._serialized_start=340
  _PRODUCTLIST._serialized_end=389
# @@protoc_insertion_point(module_scope)
