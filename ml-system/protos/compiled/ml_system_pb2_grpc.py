# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ml_system_pb2 as ml__system__pb2


class MlSystemStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HealthcheckReq = channel.unary_unary(
                '/MlSystem/HealthcheckReq',
                request_serializer=ml__system__pb2.HealthCheckInput.SerializeToString,
                response_deserializer=ml__system__pb2.HealthCheckOutout.FromString,
                )
        self.ActionReq = channel.unary_unary(
                '/MlSystem/ActionReq',
                request_serializer=ml__system__pb2.ActionInput.SerializeToString,
                response_deserializer=ml__system__pb2.ActionOutput.FromString,
                )
        self.JobExecutionReq = channel.unary_unary(
                '/MlSystem/JobExecutionReq',
                request_serializer=ml__system__pb2.JobExecutionInput.SerializeToString,
                response_deserializer=ml__system__pb2.JobExecutionOutput.FromString,
                )


class MlSystemServicer(object):
    """Missing associated documentation comment in .proto file."""

    def HealthcheckReq(self, request, context):
        """New Procedures
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ActionReq(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def JobExecutionReq(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MlSystemServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'HealthcheckReq': grpc.unary_unary_rpc_method_handler(
                    servicer.HealthcheckReq,
                    request_deserializer=ml__system__pb2.HealthCheckInput.FromString,
                    response_serializer=ml__system__pb2.HealthCheckOutout.SerializeToString,
            ),
            'ActionReq': grpc.unary_unary_rpc_method_handler(
                    servicer.ActionReq,
                    request_deserializer=ml__system__pb2.ActionInput.FromString,
                    response_serializer=ml__system__pb2.ActionOutput.SerializeToString,
            ),
            'JobExecutionReq': grpc.unary_unary_rpc_method_handler(
                    servicer.JobExecutionReq,
                    request_deserializer=ml__system__pb2.JobExecutionInput.FromString,
                    response_serializer=ml__system__pb2.JobExecutionOutput.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MlSystem', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MlSystem(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def HealthcheckReq(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MlSystem/HealthcheckReq',
            ml__system__pb2.HealthCheckInput.SerializeToString,
            ml__system__pb2.HealthCheckOutout.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ActionReq(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MlSystem/ActionReq',
            ml__system__pb2.ActionInput.SerializeToString,
            ml__system__pb2.ActionOutput.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def JobExecutionReq(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MlSystem/JobExecutionReq',
            ml__system__pb2.JobExecutionInput.SerializeToString,
            ml__system__pb2.JobExecutionOutput.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
