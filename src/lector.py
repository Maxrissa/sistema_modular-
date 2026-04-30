# leer datos del csv
import csv


def leer_datos(nombre_archivo):
    with open(nombre_archivo, mode="r", encoding="utf-8") as f:
        return list(csv.DictReader(f))
