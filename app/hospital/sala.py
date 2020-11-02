import hospital.salas_type.sala_grande  as sala_grande
import hospital.salas_type.sala_pequena as sala_pequena
import hospital.salas_type.sala_risco   as sala_risco
import hospital.adm.reservas            as res

"""

- RESERVAS DEVERÃO SER FEITAS ENTRE 06:00 E 22:00
- TIPOS DE SALA: 1 - GRANDE
                 2 - PEQUENA
                 3 - ALTO RISCO
- DERMATOLOGISTAS SÓ PODEM RESERVAR SALAS PEQUENAS
- CARDIOS E NEUROS SÓ PODEM RESERVAR SALAS GRANDES E DE ALTO RISCO
"""

class Sala:
    
    def __init__(self):
        self.salas = {}
        self.reservas = {}
        
    # Métodos de criação de sala
    
    def criar_sala(self, tipo, nome):
        
        if tipo == 'grande':
            self.criar_sala_grande(nome)
        
        elif tipo == 'pequena':
            self.criar_sala_pequena(nome)
            
        elif tipo == 'risco':
            self.criar_sala_alto_risco(nome)
            
    def criar_sala_grande(self, nome):
        sala = sala_grande.SalaGrande(nome)
        self.salas[nome] = sala
        
    def criar_sala_pequena(self, nome):
        sala = sala_pequena.SalaPequena(nome)
        self.salas[nome] = sala
        
    def criar_sala_alto_risco(self, nome):
        sala = sala_risco.SalaRisco(nome)
        self.salas[nome] = sala
    
    # Métodos de criação de reserva
    
    def criar_reserva(self, sala, data, hora_inicio, hora_termino, medico):
        
        key = f'{data} {hora_inicio} {hora_termino} {sala}'
        
        hora_inicio_int  = int(hora_inicio.split(':')[0])
        hora_termino_int = int(hora_termino.split(':')[0])
        total_horas = hora_termino_int - hora_inicio_int
        
        
        if key in self.reservas:
            self.reserva_falhou(2, key, sala, data, hora_inicio, hora_termino, medico)
            self.reserva_falhou(1, key, sala, data, hora_inicio, hora_termino, medico)
        
        elif (self.salas[sala].tipo == 'pequena' or self.salas[sala].tipo == 'grande') and total_horas < 2:
            self.reserva_falhou(2, key, sala, data, hora_inicio, hora_termino, medico)
            print("\nMotivo: O tempo mínimo de reserva para salas pequenas e grandes é de 2 horas.")
        
        elif self.salas[sala].tipo == 'risco' and total_horas < 3:
            self.reserva_falhou(2, key, sala, data, hora_inicio, hora_termino, medico)
            print("\nMotivo: O tempo mínimo de reserva para salas de alto risco é de 3 horas.")
        
        elif medico.especialidade == 'Dermatologista' and self.salas[sala].tipo != 'pequena':
            self.reserva_falhou(2, key, sala, data, hora_inicio, hora_termino, medico)
            print("\nMotivo: Dermatologistas só podem reservar salas pequenas.")
        
        elif medico.especialidade == 'Neurologista' and self.salas[sala].tipo == 'pequena':
            self.reserva_falhou(2, key, sala, data, hora_inicio, hora_termino, medico)
            print("\nMotivo: Neurologistas podem apenas alugar salas grandes ou de alto risco.")
            
        elif medico.especialidade == 'Cardiologista' and self.salas[sala].tipo == 'pequena':
            self.reserva_falhou(2, key, sala, data, hora_inicio, hora_termino, medico)
            print("\nMotivo: Cardiologistas podem apenas alugar salas grandes ou de alto risco.")
        
        else:
            custo = self.salas[sala].custo
            
            if self.salas[sala].tipo == 'risco' and int(hora_inicio.split(":")[0]) < 10:
                custo *= 0.9
                reserva = res.Reservas(self.salas[sala], data, hora_inicio, hora_termino, medico, custo)
            else:
                reserva = res.Reservas(self.salas[sala], data, hora_inicio, hora_termino, medico, custo)
            
            self.reservas[key] = reserva

    def reserva_falhou(self, error_id, key, sala, data, hora_inicio, hora_termino, medico):
        
        if error_id == 1:
            print("\nMotivo: Data já ocupada pela seguinte reserva:")
            
            reserva = self.reservas[key]
            
            print(f"\nSala        : {reserva.sala.nome}")
            print(f"Tipo        : {reserva.sala.tipo}")
            print(f"Data        : {reserva.data}")
            print(f"Hora Início : {reserva.hora_inicio}")
            print(f"Hora Término: {reserva.hora_termino}")
            print(f"Medico      : {reserva.medico.nome}")
        
        elif error_id == 2:
            print("\nA seguinte tentativa de reserva falhou:")
            
            print(f"\nSala        : {sala}")
            print(f"Tipo        : {self.salas[sala].tipo}")
            print(f"Data        : {data}")
            print(f"Hora Início : {hora_inicio}")
            print(f"Hora Término: {hora_termino}")
            print(f"Médico      : {medico.nome}")
    
    def ordernar_reservas_por_data(self):
        
        res_dict = {}
        for key_reserva in self.reservas:
            reserva = self.reservas[key_reserva]
            res_dict[reserva.data] = key_reserva
        
        res_list = []
        aux_res_dict = res_dict.copy()
        while len(aux_res_dict) > 0:
            
            date_antigo = 100000
            ano_antigo  = 100000
            mes_antigo  = 100000
            dia_antigo  = 100000
            for date in aux_res_dict:
                    
                date_splitted = date.split('/')
                day   = int(date_splitted[0])
                month = int(date_splitted[1])
                year  = int(date_splitted[2])
                
                if year < ano_antigo:
                    date_antigo = date
                    ano_antigo = year
                    mes_antigo = month
                    dia_antigo = day
                
                elif year == ano_antigo and month < mes_antigo:
                    date_antigo = date
                    ano_antigo = year
                    mes_antigo = month
                    dia_antigo = day
                
                elif year == ano_antigo and month == mes_antigo and day < dia_antigo:
                    date_antigo = date
                    ano_antigo = year
                    mes_antigo = month
                    dia_antigo = day
                
            ano_antigo = str(ano_antigo)
            if mes_antigo < 10:
                mes_antigo = f'0{mes_antigo}'
            if dia_antigo < 10:
                dia_antigo = f'0{dia_antigo}'
           
            aux_res_dict.pop(date_antigo)
            res_list.append((res_dict[date_antigo], f'{dia_antigo}/{mes_antigo}/{ano_antigo}'))
            
            # print(len(res_dict))
        
        # for tup in res_list:
        #     print(tup[0], tup[1])
        
        return res_list
        
    # Métodos de alocação de sala
    
    # Métodos de inspeção de sala
    
    