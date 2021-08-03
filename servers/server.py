from flask import Flask
import ssl

server_crt = 'server_cert/server.crt'
server_key = 'server_cert/server.key'
client_crt = 'server_cert/client.crt'


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_cert_chain(certfile=server_crt, keyfile=server_key)
    context.load_verify_locations(cafile=client_crt)
    app.run(ssl_context=context, debug=True)

