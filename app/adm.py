import json
from datetime import datetime
    
from hospital import sala
from hospital import gerenciador_medico as ger_medico

"""

App, responsável por fazer toda a interação entre classes.
c
"""

class Adm:

    def __init__(self):
        self.sala = sala.Sala()
        self.ger_medico = ger_medico.CorpoMedico()
    
    def alocar_sala(self):
        
        print("\n------------------------ Alocar Sala ------------------------\n")    
        while True:
            print("Escolha a sala")
            sala = input("Sala: ")
            sala = self.sala.salas[sala]
                
            print("\nInsira uma data, no formato 'dd/mm/aaaa'")
            data = input("Data: ")
            
            print("\nInsira a hora de início, no formato 'hh:mm'")
            hora_inicio = input("Hora de início: ")
            
            print("\nInsira a hora de termino, no formato 'hh:mm'")
            hora_termino = input("Hora de termino: ")
            
            print("\nInsira o seu CRM, no formato 'xxxxxxxx-x'")
            crm = input("Crm: ")
            medico = self.ger_medico.corpo_medico[crm]
            
            print("\nAlocando...")
            self.sala.criar_reserva(sala, data, hora_inicio, hora_termino, medico)
            
            break
    
    def escolher_tipo(self):
        
        while True:
            opcao = input("\nEscolha um tipo de sala:\n\n(1) - Pequena\n(2) - Grande\n(3) - Alto Risco")
            
            if opcao == '1':
                return 'pequena'
            
            elif opcao == '2':
                return 'grande'

            elif opcao == '3':
                return 'risco'
            
            else:
                print("\nEscolha uma opção válida!")
            
    def adm_main(self):
        
        print("\n-- Sistema de alocação de salas Arkham Asylum and Hospital --\n")
        while True:
            
            print("Selecione uma ação abaixo:")
            print("\n(1) - Reservar sala")
            print("(2) - Listar médicos")
            print("(3) - Listar salas de cirurgia")
            print("(4) - Listar reservas passadas")
            print("(5) - Listar reservas futuras")
            print("(6) - Listar reservas por período")
            print("(7) - Excluir reserva")
            
            #acao = int(input("Escolha: "))
            acao = 1
            
            if acao == 1:
                self.alocar_sala()
            
            elif acao == 2:
                self.lista_medicos()
            
            elif acao == 3:
                tipo = self.escolher_tipo()
                self.lista_salas(tipo)
            
    
    def insert_data(self):
        
        with open('data/lista_medicos.json') as medicos_json:
            medicos_data = json.load(medicos_json)
        
        with open('data/lista_reservas.json') as reservas_json:
            reservas_data = json.load(reservas_json)
        
        with open('data/lista_salas.json') as salas_json:
            salas_data = json.load(salas_json)
        
        with open('data/lista_especialidades.json') as especialidades_json:
            especialidades_data = json.load(especialidades_json)
            
        # print(medicos_data)
        # print()
        # print(reservas_data)
        # print()
        # print(salas_data)
        
        for tipo_sala in salas_data:
            for sala in salas_data[tipo_sala]:
                self.sala.criar_sala(tipo_sala, sala)
        
        # Print teste para inserção de salas
        # for tipo_sala in self.sala.salas:
        #     sala = self.sala.salas[tipo_sala] 
        #     print(f"\nNome : {sala.nome}")
        #     print(f"Custo: {sala.custo}")
            
        
        for lista_especialidades in especialidades_data:
            for especialidade in especialidades_data[lista_especialidades]:
                self.ger_medico.insere_especialidade(especialidade)
        
        # Print teste para inserção de especialidades
        # print(self.ger_medico.corpo_medico)
        # for especialidade in self.ger_medico.corpo_medico:
        #     print(especialidade)
        
        for nome_medico in medicos_data:
            medico = medicos_data[nome_medico]
            self.ger_medico.criar_medico(medico['nome'], medico['crm'], medico['especialidade'])
        
        # Print teste para inserção de médicos
        # for especialidade in self.ger_medico.corpo_medico:
        #     for crm in self.ger_medico.corpo_medico[especialidade]:
        #         medico = self.ger_medico.corpo_medico[especialidade][crm]
        #         print(f"\nMédico       : {medico.nome}")
        #         print(f"Especialidade: {medico.especialidade}")

        for tipo_reservado in reservas_data:
            for sala_reservada in reservas_data[tipo_reservado]:
                reserva = reservas_data[tipo_reservado][sala_reservada]
                medico = self.ger_medico.corpo_medico[reserva['medico']]
                self.sala.criar_reserva(sala_reservada, 
                                        reserva['data'], 
                                        reserva['inicio'], 
                                        reserva['termino'], 
                                        medico)
        
        # Print teste para inserção de reservas
        # for reserva in self.sala.reservas:
        #     reserva = self.sala.reservas[reserva]
        #     medico  = self.ger_medico.corpo_medico[reserva['medico']]
            
        #     print(f"\nSala   : {reserva['sala'].nome}")
        #     print(f"Data   : {reserva['data']}")
        #     print(f"Inicio : {reserva['hora_inicio']}")
        #     print(f"Termino: {reserva['hora_termino']}")
        #     print(f"Medico : {medico.nome}")            
    
    def lista_medicos(self):
        corpo = self.ger_medico.corpo_medico
        for key_medico in corpo:    
            medico = corpo[key_medico]
            print(f"\nNome         : {medico.nome}")
            print(f"CRM          : {medico.crm}")
            print(f"Especialidade: {medico.especialidade}")
    
    def lista_salas(self, tipo_desejado):
        
        salas = self.sala.salas
        
        for sala in salas:
            sala = salas[sala]
            
            if sala.tipo == tipo_desejado:
                print(sala.nome)
    
    def reservas_passadas(self):
        
        date = str(datetime.date(datetime.now()))
    
        today_day   = date.split("-")[2]
        today_month = date.split("-")[1]
        today_year  = date.split("-")[0]
    
        today = f'{today_day}/{today_month}/{today_year}'
        
        reservas_passadas = []
        todas_reservas    = self.sala.ordernar_reservas_por_data()
        
        for reserva in todas_reservas:
            
            date = reserva[1]
            date_splitted = date.split("/")
            
            ano = date_splitted[2]
            mes = date_splitted[1]
            dia = date_splitted[0]
                
            if ano < today_year:
                reservas_passadas.append(reserva)        

            elif ano <= today_year and mes < today_month:
                reservas_passadas.append(reserva)
                
            elif ano <= today_year and mes <= today_month and dia < today_day:
                reservas_passadas.append(reserva)
        
        print("Todas as reservas já realizadas:")
        for reserva in reservas_passadas:
            reserva = self.sala.reservas[reserva[0]]
            
            print(f"\nSala        : {reserva.sala.nome}")
            print(f"Tipo        : {reserva.sala.tipo}")
            print(f"Data        : {reserva.data}")
            print(f"Hora Início : {reserva.hora_inicio}")
            print(f"Hora Término: {reserva.hora_termino}")
            print(f"Medico      : {reserva.medico.nome}")
            print(f"Custo Total : {reserva.custo_total}")
    
    def reservas_futuras(self):
        
        date = str(datetime.date(datetime.now()))
    
        today_day   = date.split("-")[2]
        today_month = date.split("-")[1]
        today_year  = date.split("-")[0]
    
        today = f'{today_day}/{today_month}/{today_year}'
        
        reservas_passadas = []
        todas_reservas    = self.sala.ordernar_reservas_por_data()
        
        for reserva in todas_reservas:
            
            date = reserva[1]
            date_splitted = date.split("/")
            
            ano = date_splitted[2]
            mes = date_splitted[1]
            dia = date_splitted[0]
                
            if ano > today_year:
                reservas_passadas.append(reserva)        

            elif ano >= today_year and mes > today_month:
                reservas_passadas.append(reserva)
                
            elif ano >= today_year and mes >= today_month and dia > today_day:
                reservas_passadas.append(reserva)
        
        print("Todas as reservas já realizadas:")
        for reserva in reservas_passadas:
            reserva = self.sala.reservas[reserva[0]]
            
            print(f"\nSala        : {reserva.sala.nome}")
            print(f"Tipo        : {reserva.sala.tipo}")
            print(f"Data        : {reserva.data}")
            print(f"Hora Início : {reserva.hora_inicio}")
            print(f"Hora Término: {reserva.hora_termino}")
            print(f"Medico      : {reserva.medico.nome}")
            print(f"Custo Total : {reserva.custo_total}")
        
    def custo_por_sala(self):
        
        custo_dict = {}
        for key_sala in self.sala.salas:
            custo_dict[key_sala] = 0
        
        for key_reserva in self.sala.reservas:
            reserva = self.sala.reservas[key_reserva]
            custo_dict[reserva.sala.nome] += reserva.custo_total
        
        for key_custo in custo_dict:
            print(f"\nSala        : {key_custo}")
            print(f"Custo gerado: {custo_dict[key_custo]}")
    def aux_cria_reserva(self):
        
        neuro = self.ger_medico.corpo_medico['42559722-9']
        self.sala.criar_reserva('traumatologia', '15/06/2021', '12:00', '15:00', neuro)
    
    def teste_aloca_ocupada(self):
        
        # Testando reservar uma sala já reservada numa determinada data
        medico = self.ger_medico.corpo_medico['42559722-9']
        self.sala.criar_reserva('traumatologia', '14/05/2021', '12:00', '15:00', medico)
        
        # Testando reservar uma sala grande/alto risco para um dermatologista
        dermato = self.ger_medico.corpo_medico['21865952-8']
        self.sala.criar_reserva('traumatologia', '15/06/2021', '12:00', '15:00', dermato)
        
        # Testando reservar uma sala pequena para o neurologista
        neuro = self.ger_medico.corpo_medico['42559722-9']
        self.sala.criar_reserva('ambulatorio', '15/06/2021', '12:00', '15:00', neuro)
        
        # Testando reservar uma sala pequena para o cardiologista
        cardio = self.ger_medico.corpo_medico['82233623-7']
        self.sala.criar_reserva('patologia', '15/06/2021', '12:00', '15:00', cardio)
        
        # Testando reservar uma sala pequena por menos de 2 horas
        psiqui = self.ger_medico.corpo_medico['16923694-5']
        self.sala.criar_reserva('ambulatorio', '18/05/2021', '12:00', '13:00', psiqui)
        
        # Testando reservar uma sala grande por menos de 2 horas
        psiqui = self.ger_medico.corpo_medico['16923694-5']
        self.sala.criar_reserva('ecocardiograma', '18/05/2021', '12:00', '13:00', psiqui)
        
        # Testando reservar uma sala de alto risco por menos de 3 horas
        neuro = self.ger_medico.corpo_medico['42559722-9']
        self.sala.criar_reserva('emergencia', '15/06/2021', '12:00', '14:00', neuro)
        
def main():
    adm = Adm()
    adm.insert_data()
    # adm.adm_main()
    
    adm.aux_cria_reserva()
    adm.custo_por_sala()
    
    # adm.reservas_passadas()
    # adm.reservas_futuras()
    
    # adm.lista_reservas()
    # adm.teste_aloca_ocupada()
    # adm.lista_reservas()
    # adm.sala.ordernar_reservas_por_data()
    
    # adm.lista_medicos()
    # adm.lista_salas('pequena')
    
if __name__ == "__main__":
    main()
