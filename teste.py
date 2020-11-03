import unittest
from adm import Adm

class TestArkham(unittest.TestCase):
    
    # Objetivo: Reservar uma sala pequena
    # Resultado esperado: True
    def test_cria_reserva_sala_pequena(self):    
        
        adm = Adm()
        adm.insert_data()
        
        dermatologista = adm.ger_medico.corpo_medico['21865952-8']
        self.assertTrue(adm.sala.criar_reserva('reabilitacao', '15/06/2021', '12:00', '15:00', dermatologista))

    # Objetivo: Reservar uma sala grande
    # Resultado esperado: True
    def test_cria_reserva_sala_grande(self):
        
        adm = Adm()
        adm.insert_data()
        
        cardiologista = adm.ger_medico.corpo_medico['99769418-4']
        self.assertTrue(adm.sala.criar_reserva('raio_x', '15/06/2021', '12:00', '15:00', cardiologista))

    
    # Objetivo: Reservar uma sala de alto risco
    # Resultado esperado: True
    def test_cria_reserva_sala_risco(self):
        
        adm = Adm()
        adm.insert_data()
        
        cardiologista = adm.ger_medico.corpo_medico['99769418-4']
        self.assertTrue(adm.sala.criar_reserva('emergencia', '15/06/2021', '12:00', '15:00', cardiologista))

    # Objetivo: Uma dermatologista tentando reservar uma sala grande
    # Resultado esperado: False
    def test_cria_reserva_dermato_sala_grande(self):
        
        adm = Adm()
        adm.insert_data()
        
        dermatologista = adm.ger_medico.corpo_medico['21865952-8']
        self.assertFalse(adm.sala.criar_reserva('ecocardiograma', '15/06/2021', '12:00', '15:00', dermatologista))
    
    # Objetivo: Uma dermatologista tentando reservar uma sala de alto risco
    # Resultado esperado: False
    def test_cria_reserva_dermato_sala_risco(self):
        
        adm = Adm()
        adm.insert_data()
        
        dermatologista = adm.ger_medico.corpo_medico['21865952-8']
        self.assertFalse(adm.sala.criar_reserva('traumatologia', '15/06/2021', '12:00', '15:00', dermatologista))
    
    # Objetivo: Um neurologista tentando reservar uma sala pequena
    # Resultado esperado: False
    def test_cria_reserva_neuro_sala_pequena(self):
        
        adm = Adm()
        adm.insert_data()
        
        neurologista = adm.ger_medico.corpo_medico['42559722-9']
        self.assertFalse(adm.sala.criar_reserva('ambulatorio', '17/06/2021', '12:00', '15:00', neurologista))
    
    # Objetivo: Reservar uma sala em uma data e hora que ela já está reservada
    # Resultado esperado: False
    def test_cria_reserva_repetida(self):
        
        adm = Adm()
        adm.insert_data()
        
        neurologista = adm.ger_medico.corpo_medico['42559722-9']
        self.assertFalse(adm.sala.criar_reserva('traumatologia', '14/05/2021', '12:00', '15:00', neurologista))
    
    # Objetivo: Tentar reservar uma sala de alto risco por menos de 3 horas
    # Resultado esperado: False
    def test_cria_reserva_de_alto_risco_tempo_invalido(self):
        
        adm = Adm()
        adm.insert_data()
        
        neurologista = adm.ger_medico.corpo_medico['42559722-9']
        self.assertFalse(adm.sala.criar_reserva('traumatologia', '15/05/2021', '12:00', '14:00', neurologista))
    
if __name__ == "__main__":
    unittest.main()