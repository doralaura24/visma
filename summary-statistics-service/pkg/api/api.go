package api

import (
	"context"
	"fmt"
	"os/exec"

	api "github.com/e-conomic/hiring-assignments/machinelearningteam/summary-statistics-service/proto"
)

// Server is a server implementing the proto API
type Server struct {
	api.UnimplementedDocumentSummarizerServer
}

// SummarizeDocument echoes the document provided in the request
func (s *Server) SummarizeDocument(
	ctx context.Context,
	req *api.SummarizeDocumentRequest,
) (*api.SummarizeDocumentReply, error) {

	/*
		conn, err := grpc.Dial("localhost:50052")
		if err != nil {
			print(err)
		}
		defer conn.Close()
		c := summary_api.NewDocumentSummarizerClient(conn)
		source := summary_api.DocumentSource{HttpUri: "https://raw.githubusercontent.com/e-conomic/hiring-assignments/master/machinelearningteam/summary-statistics-service/test.csv"} //req.Document.Source.HttpUri}
		doc := summary_api.Document{Content: req.Document.Content, Source: &source}
		pyreq := summary_api.SummarizeDocumentRequest{
			Document:             &doc,
			ParamsForAggregation: "",
			Exclude:              ""}
		r, err := c.SummarizeDocument(ctx, &pyreq)
		if err != nil {
			print(err)
		}
		print(r)
	*/

	py_cmd := "C:\\Users\\T440s\\Desktop\\gowspc\\pkg\\mod\\github.com\\e-conomic\\hiring-assignments\\machinelearningteam\\summary-statistics-service\\summary\\client.py"
	cmd := exec.Command("python", py_cmd, "50052", req.Document.Source.HttpUri)
	output, err := cmd.Output()

	if err != nil {
		fmt.Println(err)
	}

	// Echo
	fmt.Println("Received document...")
	fmt.Println(string(output))
	return &api.SummarizeDocumentReply{
		Content: output,
	}, nil
}
