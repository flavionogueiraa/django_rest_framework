import requests
from django.test import SimpleTestCase

from ..models import Atracao


class AtracaoTests(SimpleTestCase):
    def test_get_in_list(self):
        url = 'http://localhost:8000/atracoes/'
        response = requests.get(url)
        assert response.status_code == 200

    def test_get_in_detail(self):
        # É criado um banco de dados novo?
        # Criamos um novo objeto de exemplo e fazemos um get nele?
        
        url = 'http://localhost:8000/atracoes/'
        response = requests.get(url)
        assert response.status_code == 200
