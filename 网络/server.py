import  socket

sk = socket.socket() #创建套接字
sk.bind(("127.0.0.1",8000))  #绑定ip和端口号
sk.listen()  #监听，等着别人给我发短信

conn,addr = sk.accept() #接受到别人的电话连接
ret = conn.recv(1024)  #接受的字符大小
print(ret)

conn.send(b"nihao")  #和别人说话
conn.close()  #挂电话
sk.close()#关手机