import hospital.adm.reservas as res

"""

- CUSTO                   : 400 REAIS POR HORA
- TEMPO MINIMO DE RESERVA : 2 HORAS 

"""

class SalaPequena:
    
    #def __init__(self, nome, data, hora_inicio, hora_termino):
    def __init__(self, nome):  
        self.nome  = nome
        self.custo = 400
        self.tipo = 'pequena'
    
    def criar_reserva(self, data, hora_inicio, hora_termino, medico):
        reserva = res.Reservas(data, hora_inicio, hora_termino, medico)
        self.reservas.append(reserva)
    
    def mudar_preco(self, custo):
        self.custo = custo