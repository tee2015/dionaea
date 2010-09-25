#********************************************************************************
#*                               Dionaea
#*                           - catches bugs -
#*
#*
#*
#* Copyright (C) 2009  Paul Baecher & Markus Koetter & Mark Schloesser
#* 
#* This program is free software; you can redistribute it and/or
#* modify it under the terms of the GNU General Public License
#* as published by the Free Software Foundation; either version 2
#* of the License, or (at your option) any later version.
#* 
#* This program is distributed in the hope that it will be useful,
#* but WITHOUT ANY WARRANTY; without even the implied warranty of
#* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#* GNU General Public License for more details.
#* 
#* You should have received a copy of the GNU General Public License
#* along with this program; if not, write to the Free Software
#* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#* 
#* 
#*             contact nepenthesdev@gmail.com  
#*
#*******************************************************************************/


from dionaea.core import connection
class echo(connection):
	def __init__ (self, proto=None):
		print("echo init")
		connection.__init__(self,proto)
	def handle_established(self):
		print("new connection to serve!")
		self.send('welcome to reverse world!\n')
	def handle_io_in(self,data):
		print('py_io_in\n')
		self.send(data[::-1][1:] + b'\n')
		return len(data)

#
#e = echo(proto='tcp')
#e.bind('0.0.0.0',4713,'')
#e.listen()

