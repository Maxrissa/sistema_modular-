from src.lector import leer_datos
from src.modelos import Encuestado
from src.reportes import AnalizarEncuestados

datos_crudos = leer_datos("encuestas.csv")
encuestados = [Encuestado(dato) for dato in datos_crudos]

analizador = AnalizarEncuestados(encuestados)

analizador.total_encuestados()
analizador.comida_mas_preferida()
analizador.encuestados_por_comida()
analizador.frecuencia_consumo_comun()
analizador.promedio_gasto_general()

#16 al 20 
analizador.comida_mejor_satisfaccion()
analizador.comida_peor_satisfaccion()
analizador.relacion_precio_recomendacion()
analizador.relacion_tiempo_satisfaccion()
analizador.perfil_predominante()
