import hospital.adm.reservas as res

"""

- CUSTO                   : 1200 REAIS POR HORA
- TEMPO MINIMO DE RESERVA : 3 HORAS 
- OBSERVACAO              : SE INICIO FOR ANTES DAS 10H, CONCEDER DESCONTO DE 10% 

"""

class SalaRisco:
    
    def __init__(self, nome):
        self.nome  = nome
        self.custo = 1200
        self.tipo  = 'risco'
    
    def criar_reserva(self, data, hora_inicio, hora_termino, medico):
        reserva = res.Reservas(data, hora_inicio, hora_termino, medico)
        self.reservas.append(reserva)
        
    def mudar_preco(self, custo):
        self.custo = custo