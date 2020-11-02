import random

def data_gen():
    
    dia = random.randint(1, 29)
    mes = random.randint(1, 12)
    ano = random.randint(2015, 2021)
    
    data = f'{dia}/{mes}/{ano}'
    
    hora_ini = random.randint(0, 23)
    mint_ini = '00'
    
    hora_fim = random.randint(0, 23)
    mint_fim = '00'
    
    horario_ini = f'{hora_ini}:{mint_ini}'
    horario_fim = f'{hora_fim}:{mint_fim}'
    
    print(data)
    print(horario_ini)
    print(horario_fim)

def crm_generator():
    
    crm = f'{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}-{random.randint(1, 9)}'
    print(crm)
    
def main():
    #data_gen()
    crm_generator()

def horario():
    
    inicio  = '10:00'
    termino = '13:00'
    
    inicio_int  = int(inicio.split(':')[0])
    termino_int = int(termino.split(':')[0])

    print(inicio_int)
    print(type(inicio_int))
    print()
    
    print(termino_int)
    print(type(termino_int))
    print()
    
    print(termino_int - inicio_int)
    
def date():
    from datetime import datetime
    
    date = str(datetime.date(datetime.now()))
    
    day   = date.split("-")[2]
    month = date.split("-")[1]
    year  = date.split("-")[0]
    
    br_format = f'{day}/{month}/{year}'
    print(br_format)
    
    
    
    
if __name__ == "__main__":
    date()