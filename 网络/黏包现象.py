import  subprocess
res = subprocess.Popen("dir",shell=True,stdout=subprocess.PIPE
                       ,stderr=subprocess.PIPE)

print("stdout:",res.stdout.read().decode("gbk"))

print("stderr:",res.stderr.read().decode("gbk"))
