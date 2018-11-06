from socket import *
import os,sys

def do_login(s,user,name,addr):
    if (name in user) or name == '管理员':
        s.sendto('该用户已存在！'.encode(),addr)
        return
    s.sendto('OK'.encode(),addr)

    msg = '欢迎%s进入聊天室！'%name 
    for i in user:
        s.sendto(mag.encode(),user[i])
    user[name] = addr   

def do_request(s):
    user = {}
    while True:
        msg,addr = s.recvfrom(1024)
        print('已连接到的地址：',addr)
        msgList = msg.decode().split(' ')

        if msgList[0] = 'L':
            do_login(s,user,msgList[1],addr)
        elif msgList[0] == 'C':
            msg = ' '.join(msgList[2:])
            do_sendOther(s,user,msgList[1],msg)

def main():
    addr = ('0.0.0.0',8888)
    s = socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(addr)

    do_request(s)

if __name__ == '__main__':
    main()
