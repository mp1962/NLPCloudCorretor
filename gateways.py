import requests

def conect_corretor_estilo(data):
    
    url = 'https://api.nlpcloud.io/v1/gpu/fast-gpt-j/gs-correction'
    headers = {"Content-Type": "application/json", "Authorization": "Token d57cc6ffb6230c3efdb8454068bbb5213655d4e8"}

    text = {
        "text":data
    }

    response = requests.post(url, json=text, headers=headers)
    
    if response.status_code == 200:
        return response.json(), response.status_code
    else:
        return {"Error": response.status_code}, response.status_code