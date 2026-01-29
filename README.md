# MLOps -- He HUANG
## Assignment 1: Use FastAPI to build a scoring algorithm
## Assignment 2: Dockerize FastAPI and expose metrics on port 8001
- Dockerfile added at repo root
- FastAPI runs on port 8000
- Metrics exposed on port 8001
- Build: docker build -t mlops-assignment1 .
- Run: docker run -p 8000:8000 -p 8001:8001 mlops-assignment1
