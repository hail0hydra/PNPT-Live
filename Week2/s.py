#!/usr/bin/python3

import socket


# sockets can be used to connect two nodes together

HOST = '127.0.0.1'
PORT = 7777

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET = IPv4, SOCK_STREAM = TCP

s.connect((HOST,PORT)) # tuple as arguement
