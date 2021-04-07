from concurrent import futures
import sys
import grpc

import summary_api_pb2
import summary_api_pb2_grpc

import pandas as pd

from summary_statistics import calculate_frequency


class DocumentSummarizer(summary_api_pb2_grpc.DocumentSummarizerServicer):
    def SummarizeDocument(self, request, context):
        if request.document.content != b'':
            data = pd.read_json(request.document.content.decode())
        else:
            try:
                data = pd.read_csv(request.document.source.http_uri, index_col=0)
                request.document.content = data.to_json().encode('utf-8')
            except Exception as ex:
                raise ValueError("Cannot load html ({})".format(ex))
        if request.params_for_aggregation not in data.columns:
            raise ValueError("Column ({}) is not in list ({})".format(request.params_for_aggregation,','.join(data.columns)))
        if len(data[request.params_for_aggregation].unique()) < int(request.exclude):
            temp_df = calculate_frequency(data, request.params_for_aggregation)
        else:
            raise ValueError("number of categories ({}) more than threshold ({})!".format((len(data[request.params_for_aggregation].unique())), int(request.exclude)) )
        return summary_api_pb2.SummarizeDocumentReply(content=temp_df.reset_index(drop=True).to_json().encode('utf-8'))

def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    summary_api_pb2_grpc.add_DocumentSummarizerServicer_to_server(DocumentSummarizer(), server)
    server.add_insecure_port("localhost:{}".format(port))
    print("start server listening on {}".format(port))
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    port = sys.argv[1] if len(sys.argv) > 1 else 50051
    serve(port)
