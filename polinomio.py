from nodo import Nodo

class datoPolinomio(object):
    def __init__(self, valor, termino):
        self.valor = valor
        self.termino = termino

class Polinomio(object):
    def __init__(self):
        self.termino_mayor = None
        self.grado = -1

    def agregar_termino(polinomio, termino, valor):
        aux = Nodo()
        dato = datoPolinomio(valor, termino)
        aux.info = dato
        if(termino > polinomio.grado):
            aux.sig = polinomio.termino_mayor
            polinomio.termino_mayor = aux
            polinomio.grado = termino
        else: 
            actual = polinomio.termino_mayor
            while(actual.sig is not None and termino < actual.sig.info.termino):
                actual = actual.sig
            aux.sig = actual.sig
            actual.sig = aux

    def modificar_termino(polinomio, termino, valor):
        aux = polinomio.termino_mayor
        while(aux is not None and aux.info.termino != termino):
            aux = aux.sig
        aux.info.valor = valor

    def obtener_valor(polinomio, termino):
        aux = polinomio.termino_mayor
        while(aux is not None and aux.info.termino > termino):
            aux = aux.sig
        if (aux is not None and aux.info.termino == termino):
            return aux.info.valor
        else:
            return 0
            
    def mostrar(polinomio):
        aux = polinomio.termino_mayor
        pol = ""
        if (aux is not None):
            while(aux is not None):
                signo = "+"
                pol += signo + str(aux.info.valor) + "x^" + str(aux.info.termino)
                aux = aux.sig
        return pol
        
    def sumar(polinomio1, polinomio2):
        paux = Polinomio()
        mayor = polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2
        for i in range(0, mayor.grado + 1):
            total = Polinomio.obtener_valor(polinomio1, i) + Polinomio.obtener_valor(polinomio2, i)
            if total != 0:
                Polinomio.agregar_termino(paux, i, total)
        return paux

    def multiplicar(polinomio1, polinomio2):
        paux = Polinomio()
        pol1 = polinomio1.termino_mayor
        while(pol1 is not None): 
            pol2 = polinomio2.termino_mayor
            while(pol2 is not None):
                termino = pol1.info.termino + pol2.info.termino
                valor = pol1.info.valor * pol2.info.valor
                if(Polinomio.obtener_valor(paux, termino) != 0):
                    valor += Polinomio.obtener_valor(paux, termino)
                    Polinomio.modificar_termino(paux, termino, valor)
                else:
                    Polinomio.agregar_termino(paux,termino,valor)
                pol2 = pol2.sig
            pol1 = pol1.sig
        return paux
    
    def eliminar(polinomio, termino):
        aux = polinomio.termino_mayor
        if (aux is not None):
            if (aux.info.termino == termino):
                polinomio.termino_mayor = aux.sig
                aux.sig = None
            else:
                while(aux.sig is not None and aux.sig.info.termino != termino):
                    aux = aux.sig
                if (aux.sig is not None and aux.sig.info.termino == termino):
                    aux.sig = aux.sig.sig

    def existe_termino(polinomio, termino):
        aux = polinomio.termino_mayor
        while(aux is not None and aux.info.termino != termino):
            aux = aux.sig
        if (aux is not None and aux.info.termino == termino):
            return True
        else:
            return False

polinomio1 = Polinomio()
Polinomio.agregar_termino(polinomio1, 3, 5)
print("Polinomio 1: ", Polinomio.mostrar(polinomio1))
Polinomio.agregar_termino(polinomio1, 2, 2)
print("Polinomio 1: ", Polinomio.mostrar(polinomio1))
Polinomio.agregar_termino(polinomio1, 1, 3)
print("Polinomio 1: ", Polinomio.mostrar(polinomio1))
Polinomio.agregar_termino(polinomio1, 0, 4)
print("Polinomio 1: ", Polinomio.mostrar(polinomio1))

polinomio2 = Polinomio()
Polinomio.agregar_termino(polinomio2, 2, 5)
Polinomio.agregar_termino(polinomio2, 1, 6)
Polinomio.agregar_termino(polinomio2, 0, 7)
print("Polinomio 2: ", Polinomio.mostrar(polinomio2))

polinomio3 = Polinomio.sumar(polinomio1, polinomio2)
print("Polinomio 3: ", Polinomio.mostrar(polinomio3))
polinomio4 = Polinomio.multiplicar(polinomio1, polinomio2)
print("Polinomio 4: ", Polinomio.mostrar(polinomio4))
Polinomio.eliminar(polinomio1, 3)
print("Polinomio 1: ", Polinomio.mostrar(polinomio1))

print(Polinomio.existe_termino(polinomio1, 2))