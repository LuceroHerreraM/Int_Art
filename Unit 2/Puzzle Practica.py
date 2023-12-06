from collections import deque

# Clase que define un nodo en el 8-puzzle.
class Nodo:
    def __init__(self, estado, padre, movimiento, profundidad, piezas_correctas):
        self.estado = estado
        self.padre = padre
        self.movimiento = movimiento
        self.profundidad = profundidad
        self.piezas_correctas = piezas_correctas

    def mover(self, direccion):
        nuevo_estado = list(self.estado)
        ind = nuevo_estado.index(0)
        if direccion == "arriba" and ind not in [6, 7, 8]:
            nuevo_estado[ind], nuevo_estado[ind + 3] = nuevo_estado[ind + 3], nuevo_estado[ind]
        elif direccion == "abajo" and ind not in [0, 1, 2]:
            nuevo_estado[ind], nuevo_estado[ind - 3] = nuevo_estado[ind - 3], nuevo_estado[ind]
        elif direccion == "derecha" and ind not in [0, 3, 6]:
            nuevo_estado[ind], nuevo_estado[ind - 1] = nuevo_estado[ind - 1], nuevo_estado[ind]
        elif direccion == "izquierda" and ind not in [2, 5, 8]:
            nuevo_estado[ind], nuevo_estado[ind + 1] = nuevo_estado[ind + 1], nuevo_estado[ind]
        else:
            return None
        return tuple(nuevo_estado)

    def encontrar_sucesores(self):
        sucesores = []
        movimientos = ["arriba", "abajo", "derecha", "izquierda"]
        for movimiento in movimientos:
            sucesor = self.mover(movimiento)
            if sucesor:
                sucesores.append(Nodo(sucesor, self, movimiento, self.profundidad + 1, calcular_heuristica(sucesor)))
        return sucesores

    def encontrar_camino(self, estado_inicial):
        camino = []
        nodo_actual = self
        while nodo_actual.profundidad >= 1:
            camino.append(nodo_actual)
            nodo_actual = nodo_actual.padre
        camino.reverse()
        return camino

    def imprimir_nodo(self):
        renglon = 0
        for i, pieza in enumerate(self.estado):
            print(pieza, end=" ")
            renglon += 1
            if renglon == 3:
                print()
                renglon = 0

    def coordenadas_numero(self, numero):
        estado = list(self.estado)
        if numero in estado:
            indice = estado.index(numero)
            fila = indice // 3
            columna = indice % 3
            return fila, columna
        return None

def calcular_heuristica(estado):
    estado_correcto = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    piezas_correctas = sum(1 for a, b in zip(estado, estado_correcto) if a == b)
    return piezas_correctas

# Algoritmo Breadth First Search.
def bfs(estado_inicial, estado_meta):
    visitados = set()
    frontera = deque()
    frontera.append(Nodo(estado_inicial, None, None, 0, calcular_heuristica(estado_inicial)))
    while frontera:
        nodo = frontera.popleft()
        if nodo.estado not in visitados:
            visitados.add(nodo.estado)
        else:
            continue
        if nodo.estado == estado_meta:
            print("\n¡Se encontró la meta!")
            return nodo.encontrar_camino(estado_inicial)
        else:
            frontera.extend(nodo.encontrar_sucesores())

def main():
    estado_meta = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    estado_inicial = (7, 2, 1, 4, 5, 3, 8, 6, 0)

    print("Este programa encuentra la solución al 8-puzzle utilizando el algoritmo Breadth First Search (BFS).")
    print("El estado inicial del juego es:")
    nodo_inicial = Nodo(estado_inicial, None, None, 0, calcular_heuristica(estado_inicial))
    nodo_inicial.imprimir_nodo()
    coordenadas_7 = nodo_inicial.coordenadas_numero(7)
    if coordenadas_7:
        print(f"El número 7 está ubicado en {coordenadas_7}")
    nodos_camino = bfs(estado_inicial, estado_meta)
    if nodos_camino:
        print("El camino tiene", len(nodos_camino), "movimientos.")
        imprimir_camino = input("¿Desea saber el proceso? s/n: ")

        if imprimir_camino.lower() == "s":
            print("\nEstado inicial:")
            nodo_inicial.imprimir_nodo()
            print("Piezas correctas:", calcular_heuristica(estado_inicial), "\n")
            input("Presione \"enter\" para continuar.")

            for nodo in nodos_camino:
                print("\nSiguiente movimiento:", nodo.movimiento)
                print("Estado actual:")
                nodo.imprimir_nodo()
                coordenadas_7 = nodo.coordenadas_numero(7)
                if coordenadas_7:
                    print(f"El número 7 está ubicado en {coordenadas_7}")
                print("Piezas correctas en puzzle:", nodo.piezas_correctas, "\n")
                input("Presione \"enter\" para continuar.")
    else:
        print("No hay un camino con esas condiciones.")

if __name__ == "__main__":
    main()
