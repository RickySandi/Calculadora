import string
class Calculadora:
    def __init__(self, uno, dos):#tres
        self.valor_1 = uno
        self.valor_2 = dos

    def suma_numeros(self):
        return self.valor_1+self.valor_2

    def resta_numeros(self):
        return self.valor_1-self.valor_2

    def multiplicacion_numeros(self):
        return self.valor_1*self.valor_2

    def division_numeros(self):
        try:
             resultado=(self.valor_1/self.valor_2)
        except Exception:
            resultado="No se puede dividir con cero!\n"
        return resultado

def operaciones_2_numeros(_1er_operador):
      operaciones = { 
    '+': calculadora.suma_numeros, 
    '-': calculadora.resta_numeros, 
    '*': calculadora.multiplicacion_numeros, 
    '/': calculadora.division_numeros
      }
      try:
            resultado=operaciones[_1er_operador]()
      except Exception:
            resultado="Operacion Invalida!\n"
      return resultado

def operaciones_3_numeros(_1er_operador_2do_operador):
    operaciones2 = { 
    '+': calculadora2.suma_numeros, 
    '-': calculadora2.resta_numeros, 
    '*': calculadora2.multiplicacion_numeros, 
    '/': calculadora2.division_numeros
      }
    try:
        resultado=operaciones2[_2do_operador]()
    except Exception:
          resultado="Operacion Invalida!\n"
    return resultado
 
print("\nEsta calculadora realiza las operaciones una a una. Si deseas calcular aoperaciones aritmeticas con tres numeros se dara prioridad a la operacion entre los dos valor_1s numeros elegidos y la primera operacion")
print("A ese resultado se le sumara, restara, multiplicara o dividira, segun sea el caso, el tercer numero ingresado")
print("Por ejemplo: Primer valor: 4  Primera operacion  : *  valor_2 valor: 2  Segunda operacion  : + Tercer valor: 3 \nResultado: (4 * 2) + 3 = 11 ")
numero_de_valores=int(input("Cuantos valores desea incluir en el calculo 2 o 3 "))

if numero_de_valores==2:
  valor_1=int(input("Inserta 1er Numero: "))

  print("Operaciones a realizar\n1 - Sumar\n2 - Restar\n3 - Nultiplicar\n4 - Dividir\n")
  
  _1er_operador=input("Seleccione operacion: ")
  
  valor_2=int(input("Inserta 2do Numero: "))
  calculadora=Calculadora(valor_1,valor_2)
  
  resultado_2_numeros=operaciones_2_numeros(_1er_operador)
else:
  valor_1=int(input("Inserta 1er Numero: "))
  
  print("Operaciones a realizar\n1 - Sumar\n2 - Restar\n3 - Nultiplicar\n4 - Dividir\n")
  
  _1er_operador=input("Seleccione operacion: ")
  
  valor_2=int(input("Inserta 2do Numero: "))
  
  calculadora=Calculadora(valor_1,valor_2)
  
  resultado_2_numeros=operaciones_2_numeros(_1er_operador)
  
  print("Operaciones a realizar\n1 - Sumar\n2 - Restar\n3 - Nultiplicar\n4 - Dividir\n")
  
  _2do_operador=input("Seleccione la segunda peracion: ")
  
  valor_3=int(input("Inserta 3er Numero: "))
  
  calculadora2=Calculadora(resultado_2_numeros,valor_3)
  resultado_3_numeros=operaciones_3_numeros(_2do_operador)
  
if numero_de_valores==2:
  print("El resultado es: ",resultado_2_numeros)
else:
  print("El resultado es: ",resultado_3_numeros)

