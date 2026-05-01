# ... (Aquí arriba están los reportes del 1 al 10)

    # ----------------------------------------
    # REPORTES 11 AL 15
    # ----------------------------------------
    def distribucion_tiempo_entrega(self):
        conteo = {}
        for e in self.encuestados:
            tiempo = e.tiempo_entrega
            conteo[tiempo] = conteo.get(tiempo, 0) + 1
        
        total = len(self.encuestados)
        print("\nReporte 11 - Distribución de tiempo de entrega:")
        for categoria, cantidad in conteo.items():
            porcentaje = (cantidad / total) * 100
            print(f"  {categoria}: {cantidad} ({porcentaje:.1f}%)")

    def porcentaje_volveria_comprar(self):
        si = sum(1 for e in self.encuestados if e.volveria_comprar.strip().lower() in ["sí", "si"])
        total = len(self.encuestados)
        porcentaje = (si / total) * 100
        print(f"\nReporte 12 - Porcentaje que volvería a comprar: {porcentaje:.1f}%")

    def nps_general(self):
        promotores = sum(1 for e in self.encuestados if e.recomendaria >= 9)
        detractores = sum(1 for e in self.encuestados if e.recomendaria <= 6)
        pasivos = len(self.encuestados) - promotores - detractores
        total = len(self.encuestados)
        
        nps = ((promotores - detractores) / total) * 100
        print(f"\nReporte 13 - NPS General: {nps:.1f}")
        print(f"Reporte 14 - Promotores: {promotores} | Pasivos: {pasivos} | Detractores: {detractores}")

    def nps_por_comida(self):
        datos = {}
        for e in self.encuestados:
            comida = e.comida_preferida
            if comida not in datos:
                datos[comida] = {"promotores": 0, "detractores": 0, "total": 0}
            
            datos[comida]["total"] += 1
            if e.recomendaria >= 9:
                datos[comida]["promotores"] += 1
            elif e.recomendaria <= 6:
                datos[comida]["detractores"] += 1
                
        print("\nReporte 15 - NPS por tipo de comida:")
        for comida, valores in datos.items():
            nps = ((valores["promotores"] - valores["detractores"]) / valores["total"]) * 100
            print(f"  {comida}: {nps:.1f}")