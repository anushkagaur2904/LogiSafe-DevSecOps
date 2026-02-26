#!/bin/sh
echo "Starting Docker build for LogiSafe"

cd app

docker build -t logisafe-app:latest .

echo "Docker image build completed"
