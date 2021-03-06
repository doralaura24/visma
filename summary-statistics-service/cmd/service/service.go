package main

import (
	"log"
	"net"
	"net/http"

	"github.com/e-conomic/hiring-assignments/machinelearningteam/summary-statistics-service/pkg/api"
	pb "github.com/e-conomic/hiring-assignments/machinelearningteam/summary-statistics-service/proto"
	"github.com/prometheus/client_golang/prometheus/promhttp"
	"google.golang.org/grpc"

	health "github.com/e-conomic/hiring-assignments/machinelearningteam/summary-statistics-service/pkg/health/v1"
	api_health "google.golang.org/grpc/health/grpc_health_v1"
)

const (
	port = ":50051"
)

// starts the Prometheus stats endpoint server
func startPromHTTPServer(port string) {
	http.Handle("/metrics", promhttp.Handler())
	if err := http.ListenAndServe(":"+port, nil); err != nil {
		log.Println("prometheus err", port)
	}
}

func main() {
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	go startPromHTTPServer("50051")

	s := grpc.NewServer()

	// Register: Health
	healthServ := health.NewHealthCheckService()
	api_health.RegisterHealthServer(s, healthServ)

	pb.RegisterDocumentSummarizerServer(s, &api.Server{})
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
