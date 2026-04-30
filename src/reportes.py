# aca solo se llaman las funciones declaradas en sus reportes
from src.reporte_a import (
    total_encuestados,
    comida_mas_preferida,
    encuestados_por_comida,
    frecuencia_consumo_comun,
    promedio_gasto_general,
)


class AnalizarEncuestados:
    def __init__(self, lista_objetos):
        self.encuestados = lista_objetos

    def total_encuestados(self):
        total_encuestados(self.encuestados)

    def comida_mas_preferida(self):
        comida_mas_preferida(self.encuestados)

    def encuestados_por_comida(self):
        encuestados_por_comida(self.encuestados)

    def frecuencia_consumo_comun(self):
        frecuencia_consumo_comun(self.encuestados)

    def promedio_gasto_general(self):
        promedio_gasto_general(self.encuestados)
