import nodo 

class datoPolinomio(object):
    def __init__(self, valor, termino):
        self.valor = valor
        self.termino = termino

class Polinomio(object):
    def __init__(self):
        self.termino_mayor = None
        self.grado = -1

    @staticmethod
    def agregar_termino(polinomio, termino, valor):
        aux = nodo.Nodo()
        dato = datoPolinomio(valor, termino)
        aux.info = dato
        if (termino > polinomio.grado):
            aux.sig = polinomio.termino_mayor
            polinomio.grado = termino
        else: 
            actual = polinomio.termino_mayor
            while (actual.sig is not None and termino < actual.sig.info.termino):
                actual = actual.sig
            aux.sig = actual.sig
            actual.sig = aux

    @staticmethod
    def modificar_termino(polinomio, termino, valor):
        aux = polinomio.termino_mayor
        while(aux is not None and aux.info.termino != termino):
            aux = aux.sig
        aux.info.valor = valor

    @staticmethod
    def obtener_valor(polinomio, termino):
        aux = polinomio.termino_mayor
        while(aux is not None and aux.info.termino > termino):
            aux = aux.sig
            if (aux is not None and aux.info.termino == termino):
                return aux.info.valor
            else:
                return 0
            
    @staticmethod
    def mostrar(polinomio):
        aux = polinomio.termino_mayor
        pol = ""
        if (aux is not None):
            while(aux is not None):
                signo = "+"
                pol += signo + str(aux.info.valor) + "x^" + str(aux.info.termino)
                aux = aux.sig
        return pol
        
    @staticmethod
    def sumar(polinomio1, polinomio2):
        paux = Polinomio()
        mayor = polinomio1 if (polinomio1.grado > polinomio2.grafo) else polinomio2
        for i in range(0, mayor.grado + 1):
            total = Polinomio.obtener_valor(polinomio1, i) + Polinomio.obtener_valor(polinomio2, i)
            if total != 0:
                Polinomio.agregar_termino(paux, i, total)
        return paux

    @staticmethod
    def multiplicar(polinomio1, polinomio2):
        paux = Polinomio()
        pol1 = polinomio1.temino_mayor
        while pol1 is not None: 
            pol2 = polinomio2.termino_mayor
            while pol2 is not None:
                termino = pol1.info.termino + pol2.info.termino
                valor = pol1.info.valor * pol2.info.valor
                if Polinomio.obtener_valor(paux, termino) != 0:
                    valor += Polinomio.obterner_valor(paux, termino)
                    Polinomio.modificar_termino(paux, termino, valor)
                else:
                    Polinomio.agregar_termino(paux,termino,valor)
                pol2 = pol2.sig
            pol1 = pol1.sig
        return paux