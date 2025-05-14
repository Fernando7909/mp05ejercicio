import heapq

# Crear una cua de prioritat buida
cua_prioritat = []

# Afegir elements (prioritat, valor)
heapq.heappush(cua_prioritat, (2, "Tasques urgents"))
heapq.heappush(cua_prioritat, (1, "Tasques molt urgents"))
heapq.heappush(cua_prioritat, (3, "Tasques menys urgents"))

# Extreure elements en funció de la prioritat
while len(cua_prioritat) > 0:
    prioritat, tasca = heapq.heappop(cua_prioritat)
    print(f"Tasca: {tasca}, Prioritat: {prioritat}")
