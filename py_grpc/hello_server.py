# coding: utf-8
# @date: 2020-02-14


"""
服务端
"""

import grpc
import random
from concurrent import futures
import helloworld_pb2
import helloworld_pb2_grpc


# 实现定义的方法
class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloResponse(message='Hello {msg}'.format(msg=request.name))

    # 写法一
    # def GetDeptUser(self, request, context):
    #     # 普通字段使用点号获取
    #     dept_id = request.dept_id
    #     dept_name = request.dept_name
    #     uid_list = request.uid_list
    #     if dept_id <= 0 or dept_name == '' or len(uid_list) <= 0:
    #         return helloworld_pb2.GetDeptUserResponse()
    #     print('dept_id is {0}, dept_name is {1}'.format(dept_id, dept_name))
    #     user_list = []
    #     user_map = {}
    #     for id_ in uid_list:
    #         uid = id_ + random.randint(0, 1000)
    #         letters = 'qwertyuiopasdfghjklzxcvbnm'
    #         name = "".join(random.sample(letters, 10))
    #         user = helloworld_pb2.BasicUser()
    #         user.id = uid
    #         user.name = name
    #         user_list.append(user) # 与正常的添加操作差不多
    #         user_map[uid] = user
    #     return helloworld_pb2.GetDeptUserResponse(user_list=user_list, user_map=user_map)

    # 写法二：先定义对象，再赋值
    def GetDeptUser(self, request, context):
        rsp = helloworld_pb2.GetDeptUserResponse()
        dept_id = request.dept_id
        dept_name = request.dept_name
        uid_list = request.uid_list
        if dept_id <= 0 or dept_name == '' or len(uid_list) <= 0:
            return rsp
        print('dept_id is {0}, dept_name is {1}'.format(dept_id, dept_name))

        user_list = []
        for id_ in uid_list:
            uid = id_ + random.randint(0, 1000)
            letters = 'qwertyuiopasdfghjklzxcvbnm'
            name = "".join(random.sample(letters, 10))
            user = helloworld_pb2.BasicUser()
            user.id = uid
            user.name = name
            user_list.append(user)
            # 注意map的写法：rsp.user_map[uid] = user 的写法会报错
            rsp.user_map[uid].id = uid
            rsp.user_map[uid].name = name
        # 注意map的写法：rsp.user_map = user_map，或者 rsp.user_map.update(user_map) 都会报错
        rsp.user_list.extend(user_list)
        return rsp


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)

    server.add_insecure_port('[::]:50054')
    server.start()
    print('gRPC 服务端已开启，端口为50054...')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
