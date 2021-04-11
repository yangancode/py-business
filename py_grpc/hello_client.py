# coding: utf-8
# @date: 2020-02-14

"""
客户端
"""

import grpc

import helloworld_pb2, helloworld_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50054')

    stub = helloworld_pb2_grpc.GreeterStub(channel)

    response = stub.SayHello(helloworld_pb2.HelloRequest(name='World'))
    print("Greeter client received: " + response.message)

    # 写法一
    response = stub.GetDeptUser(helloworld_pb2.GetDeptUserRequest(dept_id=1, dept_name='dd', uid_list=[1, 2, 3]))
    print(response.user_list)
    print(response.user_map)

    # 写法二
    user_req = helloworld_pb2.GetDeptUserRequest()
    user_req.dept_id = 110
    user_req.dept_name = 'police'
    user_req.uid_list.append(1)
    user_req.uid_list.append(2)
    user_req.uid_list.append(3)
    # 可用extend函数替换
    # user_req.uid_list.extend([1, 2, 3])

    response = stub.GetDeptUser(user_req)
    print(response.user_list)
    print(response.user_map)


if __name__ == '__main__':
    run()
