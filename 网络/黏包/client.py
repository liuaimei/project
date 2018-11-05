#在client端接受命令并执行

import  socket
import  subprocess
sk = socket.socket()
sk.connect(("127.0.0.1",8080))

cmd = sk.recv(1024).decode("gbk")
subprocess.Popen(cmd,shell=True)
