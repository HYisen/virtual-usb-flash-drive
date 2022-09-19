from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
print("hint: use ftp://{ip}".format(ip=ip))
s.close()

authorizer = DummyAuthorizer()
path = "."
authorizer.add_user("user", "password", path, perm="elradfmw")
authorizer.add_anonymous(path)

handler = FTPHandler
handler.authorizer = authorizer
handler.banner = "Welcome to Alex's FTP Server"

server = FTPServer((ip, 21), handler)
server.serve_forever()
