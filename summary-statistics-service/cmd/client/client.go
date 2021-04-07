package main

import (
	"context"
	"io/ioutil"
	"log"

	pb "github.com/e-conomic/hiring-assignments/machinelearningteam/summary-statistics-service/proto"

	"google.golang.org/grpc"
)

const (
	host = "localhost:50051"
)

func main() {
	conn, err := grpc.Dial(host, grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	client := pb.NewDocumentSummarizerClient(conn)

	document, err := ioutil.ReadFile("test.csv")
	if err != nil {
		log.Fatal("Couldn't read input document")
	}

	_uri := "https://raw.githubusercontent.com/e-conomic/hiring-assignments/master/machinelearningteam/summary-statistics-service/test.csv"

	ctx := context.Background()
	resp, err := client.SummarizeDocument(ctx, &pb.SummarizeDocumentRequest{
		Document: &pb.Document{
			Content: document,
			Source:  &pb.DocumentSource{HttpUri: _uri},
		},
	})

	ioutil.WriteFile("out.csv", resp.GetContent(), 0644)
}
