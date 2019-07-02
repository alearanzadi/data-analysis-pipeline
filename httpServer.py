from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
hostPort = 9000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        rootdir = '.'
        f = open(rootdir + self.path)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(f.read())  
        


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))