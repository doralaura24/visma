# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import summary_api_pb2 as summary__api__pb2


class DocumentSummarizerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SummarizeDocument = channel.unary_unary(
                '/summary_statistics.DocumentSummarizer/SummarizeDocument',
                request_serializer=summary__api__pb2.SummarizeDocumentRequest.SerializeToString,
                response_deserializer=summary__api__pb2.SummarizeDocumentReply.FromString,
                )


class DocumentSummarizerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SummarizeDocument(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DocumentSummarizerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SummarizeDocument': grpc.unary_unary_rpc_method_handler(
                    servicer.SummarizeDocument,
                    request_deserializer=summary__api__pb2.SummarizeDocumentRequest.FromString,
                    response_serializer=summary__api__pb2.SummarizeDocumentReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'summary_statistics.DocumentSummarizer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DocumentSummarizer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SummarizeDocument(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/summary_statistics.DocumentSummarizer/SummarizeDocument',
            summary__api__pb2.SummarizeDocumentRequest.SerializeToString,
            summary__api__pb2.SummarizeDocumentReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
