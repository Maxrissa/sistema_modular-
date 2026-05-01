from src.lector import leer_datos
from src.modelos import Encuestado
from src.reportes import AnalizarEncuestados

datos_crudos = leer_datos("encuestas.csv")
encuestados = [Encuestado(dato) for dato in datos_crudos]

analizador = AnalizarEncuestados(encuestados)
# reportes diego
analizador.total_encuestados()
analizador.comida_mas_preferida()
analizador.encuestados_por_comida()
analizador.frecuencia_consumo_comun()
analizador.promedio_gasto_general()
# reportes DAniella
analizador.promedio_gasto_por_comida()
analizador.satisfaccion_producto()
analizador.satisfaccion_servicio()
analizador.calificacion_general()
analizador.distribucion_precios()

# REPORTES 11 AL 15
reportes_xavi = ReporteC(encuestados)
reportes_xavi.distribucion_tiempo_entrega()
reportes_xavi.porcentaje_volveria_comprar()
reportes_xavi.nps_general()
reportes_xavi.nps_por_comida()

# Reporte 16:
# Calcula cuál es la comida con mayor nivel de satisfacción promedio,
# agrupando los datos por tipo de comida y sacando el promedio de satisfacción del producto.
analizador.comida_mejor_satisfaccion()

# Reporte 17:
# Determina la comida con menor satisfacción promedio,
# usando el mismo cálculo pero seleccionando el valor más bajo.
analizador.comida_peor_satisfaccion()

# Reporte 18:
# Analiza la relación entre la percepción de precios (alto, medio, bajo)
# y el nivel de recomendación (NPS), calculando promedios por categoría.
analizador.relacion_precio_recomendacion()

# Reporte 19:
# Evalúa cómo influye el tiempo de entrega (rápido, normal, lento)
# en la satisfacción del producto, mostrando promedios por tipo de entrega.
analizador.relacion_tiempo_satisfaccion()

# Reporte 20:
# Identifica el perfil predominante del consumidor,
# determinando la comida más preferida y la frecuencia de consumo más común.
analizador.perfil_predominante()
