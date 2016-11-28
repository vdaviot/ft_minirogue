# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Server.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/11/28 15:39:44 by vdaviot           #+#    #+#              #
#    Updated: 2016/11/28 15:39:46 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import socket, select, sys, Queue

class		Server():

	def	__init__(self, ip, port):

		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.server.setblocking(0)
		self.server.bind((ip, port))
		self.server.listen(5)
		self.inputs = [self.server]
		self.outputs = []
		self.messages_queue = {}

	def	_waitEvent(self):
		while self.inputs:
			print >>sys.stderr, '\nwaiting for the next event'
			readable, writable, exceptional = select.select(self.inputs, self.outputs, self.inputs)
			for s in readable:
				if s is self.server:
					connection, client_address = s.accept()
					print >>sys.stderr, 'new connection from', client_address
					connection.setblocking(0)
					self.inputs.append(connection)
					self.messages_queue[connection] = Queue.Queue()
				else:
					data = s.recv(1024)
					if data:
						print >>sys.stderr, 'received "%s" from %s' % (data, s.getpeername())
						self.messages_queue[s].put(data)
						if s not in self.outputs:
							self.outputs.append(s)
					else:
						print >>sys.stderr, 'closing', client_address, 'after reading no data'
						if s in self.outputs:
							self.outputs.remove(s)
						self.inputs.remove(s)
						s.close()
						del self.messages_queue[s]
			for s in writable:
				try:
					next_msg = self.messages_queue[s].get_nowait()
				except Queue.Empty:
					print >>sys.stderr, 'output queue for', s.getpeername(), 'is empty'
					self.outputs.remove(s)
				else:
					print >>sys.stderr, 'sending "%s" to %s' % (next_msg, s.getpeername())
					s.send(next_msg)
					
			for s in exceptional:
				print >>sys.stderr, 'handling exceptional condition for', s.getpeername()
				self.inputs.remove(s)
				if s in self.outputs:
					self.outputs.remove(s)
				s.close()
				del self.messages_queue[s]

try:
	server = Server(sys.argv[1], int(sys.argv[2]))
	server._waitEvent()
except:
	print "\nProgram closed."
