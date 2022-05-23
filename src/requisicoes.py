import requests

def RequisicaoCep(CEP):
        return requests.get("https://viacep.com.br/ws/${CEP}/json/")