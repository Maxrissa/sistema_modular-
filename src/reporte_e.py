# reporte 16
def comida_mejor_satisfaccion(encuestados):
    suma = {}
    conteo = {}

    for e in encuestados:
        comida = e.comida_preferida
        satisfaccion = e.satisfaccion_producto

        suma[comida] = suma.get(comida, 0) + satisfaccion
        conteo[comida] = conteo.get(comida, 0) + 1

    promedios = {}
    for comida in suma:
        promedios[comida] = suma[comida] / conteo[comida]

    mejor = max(promedios, key=promedios.get)

    print(f"Reporte 16 - Comida con mejor satisfacción: {mejor} ({promedios[mejor]:.2f})")

# reporte 17
def comida_peor_satisfaccion(encuestados):
    suma = {}
    conteo = {}

    for e in encuestados:
        comida = e.comida_preferida
        satisfaccion = e.satisfaccion_producto

        suma[comida] = suma.get(comida, 0) + satisfaccion
        conteo[comida] = conteo.get(comida, 0) + 1

    promedios = {}
    for comida in suma:
        promedios[comida] = suma[comida] / conteo[comida]

    peor = min(promedios, key=promedios.get)

    print(f"Reporte 17 - Comida con menor satisfacción: {peor} ({promedios[peor]:.2f})")

# reporte 18
def relacion_precio_recomendacion(encuestados):
    datos = {}

    for e in encuestados:
        precio = e.precio_percepcion
        recomendacion = e.recomendaria

        if precio not in datos:
            datos[precio] = []

        datos[precio].append(recomendacion)

    print("\nReporte 18 - Relación entre precio y recomendación:")
    for precio, lista in datos.items():
        promedio = sum(lista) / len(lista)
        print(f"  {precio}: promedio recomendación = {promedio:.2f}")


# reporte 19 
def relacion_tiempo_satisfaccion(encuestados):
    datos = {}

    for e in encuestados:
        tiempo = e.tiempo_entrega
        satisfaccion = e.satisfaccion_producto

        if tiempo not in datos:
            datos[tiempo] = []

        datos[tiempo].append(satisfaccion)

    print("\nReporte 19 - Relación entre tiempo de entrega y satisfacción:")
    for tiempo, lista in datos.items():
        promedio = sum(lista) / len(lista)
        print(f"  {tiempo}: satisfacción promedio = {promedio:.2f}")

  # reporte 20
  def perfil_predominante(encuestados):
    conteo_comida = {}
    conteo_frecuencia = {}

    for e in encuestados:
        comida = e.comida_preferida
        frecuencia = e.frecuencia_consumo

        conteo_comida[comida] = conteo_comida.get(comida, 0) + 1
        conteo_frecuencia[frecuencia] = conteo_frecuencia.get(frecuencia, 0) + 1

    comida_top = max(conteo_comida, key=conteo_comida.get)
    frecuencia_top = max(conteo_frecuencia, key=conteo_frecuencia.get)

    print("\nReporte 20 - Perfil predominante del consumidor:")
    print(f"  Comida favorita: {comida_top}")
    print(f"  Frecuencia de consumo: {frecuencia_top}")
