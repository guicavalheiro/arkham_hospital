import json
from datetime import datetime
    
from hospital import sala
from hospital import gerenciador_medico as ger_medico

"""

App, responsável por fazer toda a interação entre classes.

"""

class Adm:

    def __init__(self):
        self.sala = sala.Sala()
        self.ger_medico = ger_medico.CorpoMedico()
    
    def alocar_sala(self):
        
        print("\n------------------------ Alocar Sala ------------------------\n")    
        
        print("Escolha uma das salas abaixo\n")
        self.lista_todas_salas()
        sala = input("\nSala: ")
        sala = self.sala.salas[sala]
        
        print("\nPara esta sala no período desejado, confira abaixo datas já reservadas:")
        self.disponibilidade_futura(sala)
            
        print("\nInsira uma data, no formato 'dd/mm/aaaa'")
        data = input("Data: ")
        
        
        print("\nInsira a hora de início, no formato 'hh:mm'")
        hora_inicio = input("Hora de início: ")
        
        print("\nInsira a hora de termino, no formato 'hh:mm'")
        hora_termino = input("Hora de termino: ")
        
        print("\nInsira o seu CRM, no formato 'xxxxxxxx-x'")
        crm = input("Crm: ")
        medico = self.ger_medico.corpo_medico[crm]
        
        print(f"\nO valor-hora para a sala escolhida é de {sala.custo} R$.\n\nVocê deseja alterar?")
        choice = input("(1) - Sim\n(2) - Não\n\nEscolha: ")
        
        if choice == '1':
            custo = float(input("\nInsira o valor-hora desejado: "))
        else:
            custo = sala.custo
            
        print("\nAlocando...")
        reservou = self.sala.criar_reserva(sala.nome, data, hora_inicio, hora_termino, medico, custo)
        
        if reservou:
            print("\nSala reservada com sucesso!")    
    
    def disponibilidade_futura(self, sala):
        
        for key_reserva in self.sala.reservas:
            reserva = self.sala.reservas[key_reserva]
            
            if reserva.sala.nome == sala.nome:
                print(f"\nSala        : {reserva.sala.nome}")
                print(f"Tipo        : {reserva.sala.tipo}")
                print(f"Data        : {reserva.data}")
                print(f"Hora Início : {reserva.hora_inicio}")
                print(f"Hora Término: {reserva.hora_termino}")
                print(f"Medico      : {reserva.medico.nome}")
                print(f"Custo Total : {reserva.custo_total}")
        
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
                
    def escolher_datas(self):
        
        data_ini = input("\nInsira a data inicial: ")
        data_fim = input("Insira a data final  : ")
        return data_ini, data_fim
    
    def escolher_reserva_para_exclusao(self):
        
        print("\nInsira os detalhes da reserva a ser excluída")
        
        data_reservada     = input("\nInsira a data da reserva: ")
        hora_ini_reservada = input("Insira a hora de inicio : ")
        hora_fim_reservada = input("Insira a hora de termino: ")
        sala_reservada     = input("Insira a sala reservada : ")

        return data_reservada, hora_ini_reservada, hora_fim_reservada, sala_reservada
    
    def excluir_reserva(self, data_reservada, hora_ini_reservada, hora_fim_reservada, sala_reservada):
        
        key_reserva_para_excluir = f'{data_reservada} {hora_ini_reservada} {hora_fim_reservada} {sala_reservada}'
        date = str(datetime.date(datetime.now()))
    
        today_day   = date.split("-")[2]
        today_month = date.split("-")[1]
        today_year  = date.split("-")[0]
        
        data_res_split = data_reservada.split("/")
        data_res_dia = data_res_split[0]
        data_res_mes = data_res_split[1]
        data_res_ano = data_res_split[2]
        
        if data_res_ano > today_year:
            pass

        elif data_res_ano >= today_year and data_res_mes > today_month:
            pass
            
        elif data_res_ano >= today_year and data_res_mes >= today_month and data_res_dia > today_day:
            pass
        
        else:
            print("\nInsira uma data futura válida.")
            return 0

        print("\nExcluindo a seguinte reserva:")
        reserva = self.sala.reservas.pop(key_reserva_para_excluir)
        print(f"\nSala        : {reserva.sala.nome}")
        print(f"Tipo        : {reserva.sala.tipo}")
        print(f"Data        : {reserva.data}")
        print(f"Hora Início : {reserva.hora_inicio}")
        print(f"Hora Término: {reserva.hora_termino}")
        print(f"Medico      : {reserva.medico.nome}")
        print(f"Custo Total : {reserva.custo_total}")
        
            
    def adm_main(self):
        
        print("\n-- Sistema de alocação de salas Arkham Asylum and Hospital --\n")
        while True:
            
            print("\nSelecione uma ação abaixo:")
            print("\n(1) - Reservar sala")
            print("(2) - Listar médicos")
            print("(3) - Listar salas de cirurgia")
            print("(4) - Listar salas de cirurgia por tipo")
            print("(5) - Listar reservas passadas")
            print("(6) - Listar reservas futuras")
            print("(7) - Listar reservas por período")
            print("(8) - Excluir reserva")
            print("(0) - Sair do programa")
            
            acao = input("\nEscolha: ")
            
            if acao == '1':
                self.alocar_sala()
            
            elif acao == '2':
                self.lista_medicos()
            
            elif acao == '3':
                self.lista_todas_salas()
                
            elif acao == '4':
                tipo = self.escolher_tipo()
                self.lista_salas(tipo)
            
            elif acao == '5':
                self.reservas_passadas()
            
            elif acao == '6':
                self.reservas_futuras()
            
            elif acao == '7':
                data_ini, data_fim = self.escolher_datas()
                self.reservas_por_periodo(data_ini, data_fim)
            
            elif acao == '8':
                data_reservada, hora_ini_reservada, hora_fim_reservada, sala_reservada = self.escolher_reserva_para_exclusao()
                self.excluir_reserva(data_reservada, hora_ini_reservada, hora_fim_reservada, sala_reservada)
            
            elif acao == '0':
                break
            
            else:
                print("\nFaça uma escolha válida!")
            
    def insert_data(self):
        
        with open('data/lista_medicos.json') as medicos_json:
            medicos_data = json.load(medicos_json)
        
        with open('data/lista_reservas.json') as reservas_json:
            reservas_data = json.load(reservas_json)
        
        with open('data/lista_salas.json') as salas_json:
            salas_data = json.load(salas_json)
        
        with open('data/lista_especialidades.json') as especialidades_json:
            especialidades_data = json.load(especialidades_json)
        
        for tipo_sala in salas_data:
            for sala in salas_data[tipo_sala]:
                self.sala.criar_sala(tipo_sala, sala)
            
        for lista_especialidades in especialidades_data:
            for especialidade in especialidades_data[lista_especialidades]:
                self.ger_medico.insere_especialidade(especialidade)

        
        for nome_medico in medicos_data:
            medico = medicos_data[nome_medico]
            self.ger_medico.criar_medico(medico['nome'], medico['crm'], medico['especialidade'])

        for tipo_reservado in reservas_data:
            for sala_reservada in reservas_data[tipo_reservado]:
                reserva = reservas_data[tipo_reservado][sala_reservada]
                medico = self.ger_medico.corpo_medico[reserva['medico']]
                self.sala.criar_reserva(sala_reservada, 
                                        reserva['data'], 
                                        reserva['inicio'], 
                                        reserva['termino'], 
                                        medico)

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
    
    def lista_todas_salas(self):
        
        salas = self.sala.salas
        for sala in salas:
            sala = salas[sala]
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
    
    def reservas_por_periodo(self, data_ini, data_fim):
        
        data_ini_splitted = data_ini.split("/")
        ini_ano = data_ini_splitted[2]
        ini_mes = data_ini_splitted[1]
        ini_dia = data_ini_splitted[0]
        
        data_fim_splitted = data_fim.split("/")
        fim_ano = data_fim_splitted[2]
        fim_mes = data_fim_splitted[1]
        fim_dia = data_fim_splitted[0]
        
        reservas_no_periodo = []
        todas_reservas      = self.sala.ordernar_reservas_por_data()
        
        for reserva in todas_reservas:
            
            date = reserva[1]
            date_splitted = date.split("/")
            
            ano = date_splitted[2]
            mes = date_splitted[1]
            dia = date_splitted[0]
            
            print(f'\nData Inicio : {ini_dia}/{ini_mes}/{ini_ano}')
            print(f'Data Termino: {fim_dia}/{fim_mes}/{fim_ano}')
            print(f'Data Analise: {dia}/{mes}/{ano}')
            print(f"if {ano} > {ini_ano} and {ano} < {fim_ano}")
            print(f"elif ({ano} >= {ini_ano} and {ano} <= {fim_ano}) and ({mes} > {ini_mes} and {mes} < {fim_mes})")
            print(f"elif ({ano} >= {ini_ano} and {ano} <= {fim_ano}) and ({mes} => {ini_mes} and {mes} <= {fim_mes}) and ({dia} > {ini_dia} and {dia} < {fim_dia})")
            if (ano > ini_ano and ano < fim_ano):
                print("Entrou no if")
                reservas_no_periodo.append(reserva)

            elif (ano >= ini_ano and ano <= fim_ano) and (mes > ini_mes and mes < fim_mes):
                print("Entrou no elif 1")
                reservas_no_periodo.append(reserva)
                
            elif (ano >= ini_ano and ano <= fim_ano) and (mes >= ini_mes and mes <= fim_mes) and (dia > ini_dia or dia < fim_dia):
                print("Entrou no elif 2")
                reservas_no_periodo.append(reserva)
        
        custo_periodo = 0
        for reserva in reservas_no_periodo:
            reserva = self.sala.reservas[reserva[0]]
            
            print(f"\nSala        : {reserva.sala.nome}")
            print(f"Tipo        : {reserva.sala.tipo}")
            print(f"Data        : {reserva.data}")
            print(f"Hora Início : {reserva.hora_inicio}")
            print(f"Hora Término: {reserva.hora_termino}")
            print(f"Medico      : {reserva.medico.nome}")
            print(f"Custo Total : {reserva.custo_total}")
            
            custo_periodo += reserva.custo_total
        
        print(f"\nCusto total do período {data_ini} - {data_fim}: {custo_periodo}")
    
    def todas_reservas(self):
        
        print()
        for key_reserva in self.sala.reservas:
            
            reserva = self.sala.reservas[key_reserva]
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
        
    def cria_reserva_manual(self, nome_sala, data, hora_ini, hora_fim, medico, custo=False):
        self.sala.criar_reserva(nome_sala, data, hora_ini, hora_fim, medico, custo)
    
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
    adm.adm_main()
    
if __name__ == "__main__":
    main()
