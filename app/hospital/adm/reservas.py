class Reservas:
    
    def __init__(self, sala, data, hora_inicio, hora_termino, medico, custo):
        self.sala         = sala
        self.data         = data
        self.hora_inicio  = hora_inicio
        self.hora_termino = hora_termino
        self.medico       = medico
        self.custo_hora   = float(custo)
        self.custo_total  = self.calcular_custo()
    
    def calcular_custo(self):
        
        hora_ini = int(self.hora_inicio.split(":")[0])
        hora_fim = int(self.hora_termino.split(":")[0])
        
        custo_total = (hora_fim - hora_ini) * self.custo_hora
        
        return custo_total
    