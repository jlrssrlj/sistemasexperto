# ======================================

# Sistema Experto para Selección de Modalidad de Carrera

# ======================================

def modalidades():
    modalidades = {}
    while True:
        try:
            n = int(input("¿Cuántas modalidades desea evaluar? (ej: 3): "))
            if n <= 0:
                print("Debe ser mayor a 0")
                continue
            break
        except ValueError:
            print("Ingrese un valor valido")

    for i in range(n):
        nombre = input(f"\nIngrese el nombre de la modalidad #{i+1} (ej: Presencial, Virtual, Distancia): ")
        costo = int(input(f"Ingrese el costo total de la carrera en {nombre} (en pesos): "))
        tiempo = int(input(f"Ingrese la duración de la carrera en {nombre} (años): "))
        modalidades[nombre] = {"costo": costo, "tiempo": tiempo}
    return modalidades


# Algoritmo UCS (selecciona el más económico)
"""Algoritmo de búsqueda no informada utilizado para encontrar el camino de costo
mínimo entre un nodo raiz y un nodo destido en un grafo ponderado"""
def ucs(modalidades):
    return min(modalidades.items(), key=lambda x: x[1]["costo"])


# Algoritmo Greedy (selecciona el más rápido)
"""Estrategia de busqueda que consiste en elegir la opcion mas óptima en cada paso local con la 
esperanza de alcanzar una solucion general óptima"""
def greedy(modalidades):
    return min(modalidades.items(), key=lambda x: x[1]["tiempo"])


# Algoritmo A* (balancea costo y tiempo)
"""Algortimo de búsqueda informada utlizado para encontrar el camino de menor coste entre 
un nodo inicial y un nodo objetivo en un grafo"""
def a_star(modalidades):
    return min(modalidades.items(), key=lambda x: x[1]["costo"] + x[1]["tiempo"]*1000000)


# Menú principal
def sistema_experto():
    menu = """Elección de modalidad"""
    print(menu)

    modalidad = modalidades()

    print("\n--- Resultados de los Algoritmos ---")
    mejor_ucs = ucs(modalidad)
    mejor_greedy = greedy(modalidad)
    mejor_a_star = a_star(modalidad)

    print(f"\nMás económico: {mejor_ucs[0]} → Costo: {mejor_ucs[1]['costo']} - Tiempo: {mejor_ucs[1]['tiempo']} años")
    print(f"Más rápido: {mejor_greedy[0]} → Costo: {mejor_greedy[1]['costo']} - Tiempo: {mejor_greedy[1]['tiempo']} años")
    print(f"Balance costo/tiempo: {mejor_a_star[0]} → Costo: {mejor_a_star[1]['costo']} - Tiempo: {mejor_a_star[1]['tiempo']} años")
    

if __name__ == "__main__":
    sistema_experto()