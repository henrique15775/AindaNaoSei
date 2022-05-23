import json
import requests

def RequisicaoCep(cep):
    try:
        requisicao = requests.get('http://www.viacep.com.br/ws/%s/json' % cep)
        obj = json.loads(requisicao.text)	
        return obj
    
    except requests.exceptions.JSONDecodeError as e:
        raise SystemExit(e)    