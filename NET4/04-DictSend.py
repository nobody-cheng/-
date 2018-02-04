from socket import *

import uuid

sock = socket(AF_INET, SOCK_DGRAM)

uuid = str(uuid.uuid1())

d = {'cmd': 'online', 'name': 'tom', 'uuid': uuid}

dstr = str(d)

sock.sendto(dstr.encode(), ('127.0.0.1', 10099))
