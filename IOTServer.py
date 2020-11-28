# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "192.168.248.169"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        color = self.path[1:]
        print(color)
        self.send_header("Content-type", "text/html")
        self.end_headers()

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")