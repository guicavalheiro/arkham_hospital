import hospital.corpo_medico.medicos as medicos

class CorpoMedico:
    
    def __init__(self):
        self.corpo_medico = {}
        self.especialidades = []
    
    # Métodos de criação
    
    def insere_especialidade(self, especialidade):
        self.especialidades.append(especialidade)
    
    def criar_medico(self, nome, crm, especialidade):
        medico = medicos.Medicos(nome, crm, especialidade)
        self.corpo_medico[medico.crm] = medico