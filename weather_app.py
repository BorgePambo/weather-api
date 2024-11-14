import requests
import pandas as pd
import os


api_key = '439dbc280b97639285535ad3ba6eb2dd'

# Defina a latitude e longitude para a cidade desejada
lat = -23.5505
lon = -46.6333

# URL para pegar os dados em Celsius (com "units=metric")
url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"

# Fazer a requisição para a API
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    
    data = response.json()

    
    if 'list' in data:
        # Convertendo os dados de previsão para uma lista de dicionários
        forecasts = []
        for forecast in data['list']:
            forecast_data = {
                'Data': forecast['dt_txt'],
                'Temperatura': forecast['main']['temp'],  
                'Descrição': forecast['weather'][0]['description'],
                'Umidade': forecast['main']['humidity'],  
                'Pressão': forecast['main']['pressure'],  
                'Temp_min': forecast['main']['temp_min'],  
                'Temp_max': forecast['main']['temp_max'],  
                'Vento': forecast['wind']['speed'], 
            }
            forecasts.append(forecast_data)
        
        # Criando o DataFrame
        df = pd.DataFrame(forecasts)

        #print(df)

        outfile = os.makedirs('clean', exist_ok=True)

        df.to_csv(os.path.join('clean', 'previsao_tmp.csv'))
        print('Salvo com sucesso..!')

    else:
        print("Dados de previsão não encontrados.")
else:
    print(f"Erro ao pegar os dados: {response.status_code}")
