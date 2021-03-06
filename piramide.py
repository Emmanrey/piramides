class piram():
    def __init__(self):
        self.num = 1
        self.pisos = 1

    def construir(self):
        self.num = self.tipo_letras()
        self.pisos = self.pisos_letras()
        for i in range (0, self.pisos):
            for j in range(0, i+1):
                letra = chr(self.num)
                print(letra, end = " ")
            self.num = self.num + 1
            print("\r")

    def inversa(self):
        self.num = self.tipo_letras()
        self.pisos = self.pisos_letras()
        for i in range (0, self.pisos):
            for j in range(self.pisos, i, -1):
                letra = chr(self.num)
                print(letra, end = " ")
            self.num = self.num + 1
            print("\r")
    
    def asteriscos(self):
        self.pisos = int(input("Pisos: "))
        for i in range (0, self.pisos):
            for j in range(0, i+1):
                print("*", end = " ")
            print("\r")

    def asteriscos_invertido(self):
        self.pisos = int(input("Pisos: "))
        for i in range (0, self.pisos):
            for j in range(self.pisos, i, -1):
                print("*", end = " ")
            print("\r")

    def asteriscos_centrados(self):
        self.pisos = int(input("Pisos: "))
        rango = self.pisos
        for x in range(rango):
            print(' '*(rango-x-1), '*'*(2*x+1))

    def tipo_letras(self):
        tipo = input("Mayusculas o Minusculas: ").lower()
        dato = tipo.split('u')[0]
        if (dato == "may"):
            return 65
        elif (dato == "min"):
            return 97
        else:
            print("Error")
            return 0

    def pisos_letras(self):
        pisos = int(input("Pisos: "))
        return pisos