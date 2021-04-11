# gRPC demo


## 安装
pip install grpcio

pip install grpcio-tools


## 编译
cd python_grpc 
 
python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. proto/helloworld.proto
