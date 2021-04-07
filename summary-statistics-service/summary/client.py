from __future__ import print_function

import grpc

import summary_api_pb2
import summary_api_pb2_grpc

import pandas as pd
import sys


def run(port, uri):
    with grpc.insecure_channel('localhost:{}'.format(port)) as channel:
        stub = summary_api_pb2_grpc.DocumentSummarizerStub(channel)
        my_doc_source = summary_api_pb2.DocumentSource(http_uri=uri)
        html = pd.read_csv(my_doc_source.http_uri, index_col=0)
        content = html.to_json().encode('utf-8')
        my_doc = summary_api_pb2.Document(content=b'', source=my_doc_source)
        # inputs
        my_params_for_aggregation = "AccountTypeName"
        my_exclude = "10"
        #send request and catch response
        response = stub.SummarizeDocument(summary_api_pb2.SummarizeDocumentRequest(document=my_doc, params_for_aggregation = my_params_for_aggregation,  exclude = my_exclude))
    print("client received: " + response.content.decode())

if __name__ == '__main__':
    port = sys.argv[1] if len(sys.argv) > 1 else 50052
    uri = sys.argv[2] if len(sys.argv) > 2 else 'https://raw.githubusercontent.com/e-conomic/hiring-assignments/master/machinelearningteam/summary-statistics-service/test.csv'
    run(port, uri)
