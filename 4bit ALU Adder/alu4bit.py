def flipList(A):
#Esta funcion recibe una lista y devuelve la lista en reversa
	return A[::-1] 
	
def overflow(a,b,r):
#esta funcion simula el circuito de overflow
	return ((not a) and (not b) and r) or (a and b and (not r)) 

def alu1bit(a,b,c):
#esta funcion simula el circuito de de sumar 1 bit con carry
#devuelve el bit de carry y luego el bit de resultado
	return ((a or b) and c) or (a and b), a ^ b ^ c

def alu4bit(A, B, op):
#esta funcion simula el circuito de sumar y restar 4 bits
#recibe dos listas y un bit definiendo la operacion (0 para sumar y 1 para restar)
#devuelve el resultado en una lista y si hay o no overflow
	nbits = 4
	if len(A)!= nbits or len(B)!= nbits:
		print "Las palabras tienen que ser de %d bits" % nbits 
		return False, False
	carry = [0] * nbits
	res = [0] * nbits
	for i in range(nbits):
		if i:
			c = carry[i-1]
		else:
			c = op
		carry[i], res[i] = alu1bit(A[i],B[i]^op,c)
	return res, overflow(A[nbits-1], B[nbits-1]^op, res[nbits-1])	
