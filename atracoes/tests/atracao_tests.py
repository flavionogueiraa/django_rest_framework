import requests
from django.test import TestCase

from ..models import Atracao


class AtracaoTests(TestCase):
    def setUp(self):
        Atracao.objects.create(
            nome='Atração de teste',
            descricao='Descrição de teste',
            horario_abertura='10:00',
            horario_fechamento='18:00',
            idade_minima=3
        )
    
    def test_get_in_list(self):
        url = 'http://localhost:8000/atracoes/'
        response = requests.get(url)
        assert response.status_code == 200

    def test_get_in_detail(self):
        # É criado um banco de dados novo?
        # Criamos um novo objeto de exemplo e fazemos um get nele?
        
        url = 'http://localhost:8000/atracoes/5/'
        response = requests.get(url)
        assert response.status_code == 200
    

    def test_post(self):
        url = 'http://localhost:8000/atracoes/'
        body = {
            'nome': 'Atração de testes para o post',
            'descricao': 'Descrição de teste, exemplo',
            'horario_abertura': '05:00',
            'horario_fechamento': '13:00',
            'idade_minima': 18
        }

        response = requests.post(url, data=body)
        assert response.status_code == 201
    
    def test_put(self):
        last_atracao = Atracao.objects.last()
        url = f'http://localhost:8000/atracoes/{last_atracao}/'
        body = {
            'nome': 'Atração de testes para o put',
            'descricao': 'Descrição de teste, exemplo',
            'horario_abertura': '07:00',
            'horario_fechamento': '17:00',
            'idade_minima': 18
        }

        response = requests.put(url, data=body)
        assert response.status_code == 200
    
    def test_delete(self):
        last_atracao = Atracao.objects.last()
        url = f'http://localhost:8000/atracoes/{last_atracao}/'
        response = requests.delete(url)
        assert response.status_code == 204
