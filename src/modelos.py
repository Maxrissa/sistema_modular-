# clase padre
class Encuestado:
    def __init__(self, datos_diccionario):
        # van a ir agregando self.(nombre_columna)
        self.id = datos_diccionario.get("id")
        self.comida_preferida = datos_diccionario.get("comida_preferida")
        self.frecuencia_consumo = int(datos_diccionario.get("frecuencia_consumo"))

    def obtener_id(self):
        return self.id

    def obtener_comida_favorita(self):
        return self.comida_preferida

    def obtener_frecuencia_consumo(self):
        return self.frecuencia_consumo
