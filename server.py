#!/usr/bin/env python3
import http.server
import socketserver
import socket

class DualStackServer(socketserver.TCPServer):
    address_family = socket.AF_INET6
    allow_reuse_address = True
    
    def server_bind(self):
        self.socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
        self.socket.bind(self.server_address)

if __name__ == '__main__':
    with DualStackServer(('::', 10001), http.server.SimpleHTTPRequestHandler) as httpd:
        print('Serving on port 10001 (IPv4+IPv6)')
        httpd.serve_forever()
