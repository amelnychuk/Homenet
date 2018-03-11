from __future__ import print_function, unicode_literals

import soco




import os
import sys
import time
import socket
from threading import Thread
from random import choice
try:
    # Python 3
    from urllib.parse import quote
    from http.server import SimpleHTTPRequestHandler
    from socketserver import TCPServer
    print('Running as python 3')
except ImportError:
    # Python 2
    from urllib import quote
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from SocketServer import TCPServer
    print('Running as python 2')

from soco.discovery import by_name, discover

class HttpServer(Thread):
    """A simple HTTP Server in its own thread"""

    def __init__(self, port):
        super(HttpServer, self).__init__()
        os.chdir("./mp3/Notifications")
        self.daemon = True
        handler = SimpleHTTPRequestHandler
        self.httpd = TCPServer(("", port), handler)

    def run(self):
        """Start the server"""
        print('Start HTTP server')
        self.httpd.serve_forever()

    def stop(self):
        """Stop the server"""
        print('Stop HTTP server')
        self.httpd.socket.close()


def detect_ip_address():
    """Return the local ip-address"""
    # Rather hackish way to get the local ip-address, recipy from
    # https://stackoverflow.com/a/166589
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address