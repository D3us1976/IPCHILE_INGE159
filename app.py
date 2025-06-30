import json
import csv
from collections import Counter

# Leer datos desde el archivo JSON
with open('usuarios.json', 'r', encoding='utf-8') as archivo_json:
    datos_usuarios = json.load(archivo_json)

# Inicialización de variables para estadísticas globales
total_visitas = 0
suma_duraciones = 0
contador_contenido = Counter()

# Recorrer los datos para obtener estadísticas
for usuario in datos_usuarios:
    total_visitas += usuario['visitas']
    suma_duraciones += usuario['duracion_promedio']
    contador_contenido[usuario['contenido_mas_visitado']] += 1

# Cálculo de promedio de duración y contenido más visitado
promedio_duracion_global = suma_duraciones / len(datos_usuarios)
contenido_mas_visitado_global = contador_contenido.most_common(1)[0][0]

# Mostrar estadísticas generales
print(f"Total de visitas: {total_visitas}")
print(f"Duración promedio global: {promedio_duracion_global:.2f} minutos")
print(f"Contenido más visitado: {contenido_mas_visitado_global}")

# Crear un archivo CSV con los datos transformados
with open('usuarios.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
    campos = ['id_usuario', 'nombre', 'visitas', 'duracion_promedio', 'contenido_mas_visitado']
    escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
    escritor.writeheader()
    for usuario in datos_usuarios:
        escritor.writerow(usuario)

