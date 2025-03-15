import re
class Stack:
    def __init__(self):
        self.items = []
    
    #Agrega un elemento a la pila.
    def push(self, element):
        self.items.append(element)
    
    #Elimina y devuelve el último elemento de la pila
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    #Devuelve el último elemento sin eliminarlo.
    def peek (self):
        if not self.is_empty(): 
            return self.items[-1]
        return None
    
    #Verifica si la pila está vacía.
    def is_empty(self):
        return len(self.items) == 0
    
    
    #Devuelve el tamaño de la pila.
    def size(self):
        return len(self.items)

#valida las expresiones si estan balanceadas    
def validar_parentesis(expresion):
    stack = Stack()
    for char in expresion:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()
    
def tokenizar_expresion(expresion):
    return re.findall(r'\d+|[()+\-*/]', expresion)

# Conversión de infija a postfija
def infija_a_postfija(expresion):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    salida = []
    operadores = Stack()

    tokens = tokenizar_expresion(expresion) 
    for token in tokens:
        if token.isnumeric():
            salida.append(token)
        elif token == '(':
            operadores.push(token)
        elif token == ')':
            while not operadores.is_empty() and operadores.peek() != '(':
                salida.append(operadores.pop())
            operadores.pop()
        elif token in precedencia:
            while (not operadores.is_empty() and operadores.peek() in precedencia and 
                   precedencia[operadores.peek()] >= precedencia[token]):
                salida.append(operadores.pop())
            operadores.push(token)

    while not operadores.is_empty():
        salida.append(operadores.pop())

    return ' '.join(salida)

# Expresiones de prueba
expresion_1 = "(3 + 2) * (8 / 4)"
expresion_2 = "((3 + 2) * (8 / 4)"
expresion_3 = "3 + 5 * (2 - 8)"

print("Expresión 1 balanceada:", validar_parentesis(expresion_1))  
print("Expresión 2 balanceada:", validar_parentesis(expresion_2))  
print("Conversión a postfija:", infija_a_postfija(expresion_3))


    

