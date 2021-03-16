import string

def calcular(cantidad):
    resultado=0

    if cantidad == 2:
      
      x = input("Ingresa el primer valor: ")
      x = float(x)
      operacion =input("Ingresa el numero de la operacion a realizar 1. +, 2. -, 3. *, 4. / : ")
      
      if operacion == 1:
        operacion = "+"
      elif operacion == 2:
        operacion = "-"
      elif operacion == 3:
        operacion = "*"
      elif operacion == 4:
        operacion ="/"

      y = input("Ingresa el segundo valor: ")
      y = float(y)

      resultado = float(resultado)

      if x % x == 1 and y % y ==1:
        x = int(x)
        y = int(y)
        resultado = int(resultado)
      
      if (operacion == "+"):
        resultado = x +  y
      elif operacion == "-":
        resultado = x -  y 
      elif operacion == "*":
        resultado = x *  y 
      else:
        resultado = x / y 

    elif cantidad == 3:

      x = input("Ingresa el primer valor: ")
      x = float(x)

      op1 =input("Ingresa el numero de la operacion a realizar 1. +, 2. -, 3. *, 4. / : ")

      if op1 == 1:
         op1 = "+"
      elif op1 == 2:
         op1 = "-"
      elif op1 == 3:
         op1 = "*"
      elif op1 == 4:
         op1 ="/"

      y = input("Ingresa el segundo valor: ")
      y = float(y)

      op2 =input("Ingresa el numero de la operacion a realizar 1. +, 2. -, 3. *, 4. / : ")

      if op2 == 1:
         op2 = "+"
      elif op2 == 2:
        op2 = "-"
      elif op2 == 3:
        op2 = "*"
      elif op2 == 4:
        op2 ="/"

      z = input("Ingresa el tercer valor: ")
      z = float(z)

      resultado = float(resultado)

      if x % x == 1 and y % y ==1:
        x = int(x)
        y = int(y)
        resultado = int(resultado)

      if op1 == "+" and op2 == "+":
        resultado = x + y + z
      elif op1 == "+" and op2 == "-":
        resultado = x +  y - z
      elif op1 == "+" and op2 == "*":
        resultado = x + y * z
      elif op1 == "+" and op2 == "/":
        resultado = x + y / z

      elif op1 == "-" and op2 == "-":
        resultado = x -  y - z
      elif op1 == "-" and op2 == "+":
        resultado = x -  y + z
      elif op1 == "-" and op2 == "*":
        resultado = (x - y) * z
      elif op1 == "-" and op2 == "/":
        resultado = (x - y) / z

      elif op1 == "*" and op2 == "*":
        resultado = x * y * z
      elif op1 == "*" and op2 == "+":
        resultado = (x * y) + z
      elif op1 == "*" and op2 == "-":
        resultado = (x * y) - z
      elif op1 == "*" and op2 == "/":
        resultado = (x * y) / z

      elif op1 == "/" and op2 == "/":
        resultado = (x / y) / z
      elif op1 == "/" and op2 == "+":
        resultado = (x / y) + z
      elif op1 == "/" and op2 == "-":
        resultado = (x / y) - z
      elif op1 == '/' and op2 == "*":
        resultado = (x / y) * z


    return resultado

if __name__ == "__main__":



 print("Esta calculadora realiza las operaciones una a una. Si deseas calcular aoperaciones aritmeticas con tres numeros se dara prioridad a la operacion entre los dos primeros numeros elegidos y la primera operacion")
 print("A ese resultado se le sumara, restara, multiplicara o dividira, segun sea el caso, el tercer numero ingresado")
 print("Por ejemplo: Primer valor: 4  Primera operacion  : *  Segundo valor: 2  Seunda operacion  : + Tercer valor: 3 Resultado: (4 * 2) + 3 = 11 ")

 print("Cuantos valores desea incluir en el calculo 2 o 3")
 cant = str(input())
 cantidad = int(cant)

 result = calcular(cantidad)


 print("Resultado: ", result)
    
