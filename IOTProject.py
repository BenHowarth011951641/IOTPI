from http.server import BaseHTTPRequestHandler, HTTPServer
from time import sleep
import time
import board
import neopixel
import threading

hostName = "192.168.248.169"
serverPort = 8080

pixel_pin = board.D18
 
num_pixels = 100
 
ORDER = "BRG"

enabled = True
color = 255

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness = 1.0, auto_write = False, pixel_order = ORDER)
 
def wheel(pos):
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        global color, enabled
        self.send_response(200)
        color = self.path[1:]
        print(color)
        updateLights(color)
        self.send_header("Content-type", "text/html")
        self.end_headers()

def updateLights(color):
    pixels.fill(tuple(int(color[i: i+2], 16) for i in (0, 2, 4)))
    pixels.show()

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
