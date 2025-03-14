class Stack:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek (self):
        if not self.is_empty(): 
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
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
    
def infija_a_postfija(expresion):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    salida = []
    operadores = Stack()

    tokens = expresion.split()
    for token in tokens:
        if token.isnumeric():
            salida.append(token)
        elif token == '(':
            operadores.push(token)
        elif token == ')':
            while not operadores.is_empty() and operadores.peek() != '(':
                salida.append(operadores.pop())
            operadores.pop()
        elif token in precedencia:  # Solo evaluar operadores
            while (not operadores.is_empty() and operadores.peek() in precedencia and 
                precedencia[operadores.peek()] >= precedencia[token]):
                salida.append(operadores.pop())
            operadores.push(token)
    
       # else:
        #    while (not operadores.is_empty() and precedencia[operadores.peek()] >= precedencia[token]):
         #       salida.append(operadores.pop())
          #  operadores.push(token)

    while not operadores.is_empty():
        salida.append(operadores.pop())

    return ' '.join(salida)

expresion_1 = "(3 + 2) * (8 / 4)"
expresion_2 = "((3 + 2) * (8 / 4)"
expresion_3 = "3 + 5 * (2 - 8)"

print("expresion 1 balanceada: ", validar_parentesis(expresion_1))
print("expresion 2 balanceada: ", validar_parentesis(expresion_2))
print("conversion a postfija: ", infija_a_postfija(expresion_3))     


    

