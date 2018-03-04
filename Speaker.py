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

def play_file(zone, file, port=8000):
    netpath = 'http://{}:{}/{}'.format(detect_ip_address(), port, file)
    print( "netpath: ", netpath)

    zone.volume = 100
    zone.play_uri(uri=netpath)

    #number_in_queue = zone.add_uri_to_queue(netpath)
    #zone.play_from_queue(number_in_queue)

def getZone():
    return list(soco.discover())[0]