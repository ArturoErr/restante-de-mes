def fin_mes(D,M,A):
 if M%2==0:
   f=31-D
 else:
   f=30-D
 print("cantidad de dias para fin de mes:",f)
def fin_año(D,M,A):
 c=0
 cn=12-M
 Md=31-D
 A=1
 for A in range(cn):
    if A%2==0:
      c=c+31
    else:
      c=c+30
 R=c+Md
 print("faltan",R,"dias para fin de año.") 
 dt=365-R
 print("dias transcurridos en el año: ",dt)  
fecha = input("Introduce la fecha dia/mes/año: ")
D=int(fecha[:2])
M=int(fecha[3:5])
A=int(fecha[6:])
while D<=0 or D>31:
  D=int(input("Introduzca una dia correcto: "))
while M<=0 or M>12: 
  M=int(input("Introduzca un mes correcto: "))
while M<=0 or M>12: 
  A=int(input("Introduzca un año correcto: "))
fin_mes(D,M,A)
fin_año(D,M,A)   
print("fecha: ",D,M,A)