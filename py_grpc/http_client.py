# coding: utf-8
# @date: 2021-04-10

"""
"""

import requests

import helloworld_pb2, helloworld_pb2_grpc

if __name__ == '__main__':
    user_req = helloworld_pb2.GetDeptUserRequest()
    user_req.dept_id = 110
    user_req.dept_name = 'police'
    user_req.uid_list.append(1)
    user_req.uid_list.append(2)
    user_req.uid_list.append(3)

    # 如果不是直接用gRPC，而是先经过HTTP，就得进行序列化
    data = user_req.SerializeToString()
    req_url = 'http://127.0.0.1:5001/get_dept_user'

    try:
        response = requests.post(req_url, data=data)
        if response.status_code != 200:
            print('request failed, code: ', response.status_code)

        # 反序列化数据
        rsp = helloworld_pb2.GetDeptUserResponse()
        rsp.ParseFromString(response.content)
        print('rsp: ', rsp.user_list)

    except Exception as e:
        print('request failed, err: ', e)
