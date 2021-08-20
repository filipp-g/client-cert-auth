import socket
import ssl

client_crt = 'servers/client_cert/client.crt'
client_key = 'servers/client_cert/client.key'
server_crt = 'servers/client_cert/server.crt'

ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=server_crt)
ctx.load_cert_chain(certfile=client_crt, keyfile=client_key)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = ctx.wrap_socket(s, server_side=False, server_hostname='localhost')
conn.connect(('127.0.0.1', 5000))

print("SSL established. Peer: {}".format(conn.getpeercert()))
print("Closing connection")
conn.close()
