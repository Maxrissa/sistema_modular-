def total_encuestados(encuestados):
    total = len(encuestados)
    print(f"Reporte 1 - Total de encuestados: {total}")


def comida_mas_preferida(encuestados):
    conteo = {}
    for e in encuestados:
        comida = e.comida_preferida
        conteo[comida] = conteo.get(comida, 0) + 1
    mas_preferida = max(conteo, key=lambda c: conteo[c])
    print(
        f"Reporte 2 - Comida rápida más preferida: {mas_preferida} ({conteo[mas_preferida]} votos)"
    )


def encuestados_por_comida(encuestados):
    conteo = {}
    for e in encuestados:
        comida = e.comida_preferida
        conteo[comida] = conteo.get(comida, 0) + 1
    total = len(encuestados)
    print("\nReporte 3 - Cantidad de encuestados por tipo de comida:")
    for comida, cantidad in conteo.items():
        porcentaje = (cantidad / total) * 100
        print(f"  {comida}: {cantidad} ({porcentaje:.1f}%)")


def frecuencia_consumo_comun(encuestados):
    conteo = {}
    for e in encuestados:
        frecuencia = e.frecuencia_consumo
        conteo[frecuencia] = conteo.get(frecuencia, 0) + 1
    mas_comun = max(conteo, key=lambda f: conteo[f])
    print(
        f"Reporte 4 - Frecuencia de consumo más común: {mas_comun} ({conteo[mas_comun]} personas)"
    )


def promedio_gasto_general(encuestados):
    total_gasto = 0.0
    for e in encuestados:
        total_gasto += e.gasto_promedio
    promedio = total_gasto / len(encuestados)
    print(f"Reporte 5 - Promedio de gasto general: ${promedio:.2f}")
