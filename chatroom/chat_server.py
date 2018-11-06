#coding=utf-8
'''
Chatroom
env:python 3.5
socket and fork
'''
from socket import *
import os,sys

def do_login(s,user,name,addr):
    if (name in user) or name == '管理员':
        s.sendto('该用户已存在'.encode(),addr)
        return
    s.sendto(b'OK',addr)
    #通知其他人
    msg = '\n欢迎 %s 进入聊天室'%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    #将用户加入user
    user[name] = addr

def do_sendOther(s,user,name,msg):
    msg = "%s说：%s"%(name,msg)
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])

def do_quit(s,user,name):
    msg = '\n%s退出了聊天室！'%name
    for i in user:
        if i == name:
            s.sendto(b'EXIT',user[i])
        else:
            s.sendto(msg.encode(),user[i])
    del user[name]

def do_request(s):
    #存储结果{'zhangsan':('127.0.0.1',9999)}
    user = {}
    while True:
        msg,addr = s.recvfrom(1024)
        print('已连接到的地址：',addr)
        msgList = msg.decode().split(' ')
        #区分请求类型
        if msgList[0] == 'L':
            #处理登录函数
            do_login(s,user,msgList[1],addr)
        elif msgList[0] == 'C':
            msg = ' '.join(msgList[2:])
            do_sendOther(s,user,msgList[1],msg)
        elif msgList[0] == 'Q':
            do_quit(s,user,msgList[1])

#创建网络连接
def main():
    ADDR = ('0.0.0.0',8888)
    #创建套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)

    

    pid = os.fork()
    if pid < 0:
        print('创建进程失败！')
        return
    elif pid == 0:
        while True:
            msg = input('管理员消息：')
            msg = 'C 管理员 ' + msg
            s.sendto(msg.encode(),ADDR)
    else:
        #用于接收各种客户端请求，调用相应的函数处理
        do_request(s)

if __name__ == '__main__':
    main()



