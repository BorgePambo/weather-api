Previsão do Tempo - Projeto com OpenWeatherMap API

Este projeto utiliza a API OpenWeatherMap para obter previsões do tempo em tempo real e exibi-las de forma estruturada. Ele foi desenvolvido em Python e utiliza as bibliotecas requests e pandas para buscar e processar os dados.
Funcionalidades

    Consulta à API do OpenWeatherMap: O projeto faz uma requisição à API para obter as previsões do tempo de uma cidade específica, baseada nas coordenadas de latitude e longitude.
    Processamento dos dados: Os dados retornados pela API são processados e organizados em um DataFrame usando a biblioteca pandas.
    Conversão para unidades de temperatura: A temperatura é obtida em Celsius através do parâmetro units=metric na URL da API.
    Salvamento dos dados: O DataFrame com as previsões é salvo em um arquivo CSV, dentro de uma pasta chamada clean, para facilitar o armazenamento e análise posterior.
    Exibição das previsões: As previsões são mostradas de forma clara e concisa, com detalhes como a data e hora, temperatura, descrição do clima, umidade, pressão atmosférica e vento.

Estrutura do Projeto

    API OpenWeatherMap: A requisição é feita através da API para obter as previsões do tempo.
    Pandas DataFrame: Os dados são armazenados e manipulados em um DataFrame para facilitar a análise.
    CSV de saída: O DataFrame é salvo em um arquivo CSV dentro de uma pasta chamada clean.

Como Usar

    1. Instalar as dependências: Antes de rodar o projeto, instale as dependências necessárias:

    2. pip install requests pandas
    
    3. Obter sua chave da API: Crie uma conta na OpenWeatherMap e obtenha sua chave da API (API key).

    4. Alterar as coordenadas: No código, altere as coordenadas (latitude e longitude) para a cidade desejada. Exemplo para São Paulo:
        lat = -23.5505
        lon = -46.6333

    5. Rodar o código: Execute o script Python. O script fará a requisição à API, processará os dados e salvará as previsões no arquivo CSV dentro da pasta clean.

    6. Visualizar os dados: O arquivo CSV gerado estará disponível na pasta clean com o nome previsao_tmp.csv. Você pode abrir esse arquivo para visualizar as previsões salvas.

  Colunas do CSV:
  
    Data: Data e hora da previsão.
    Temperatura (°C): Temperatura prevista em graus Celsius.
    Descrição: Descrição do clima (por exemplo, "céu limpo", "nuvens dispersas").
    Umidade (%): Umidade relativa do ar em porcentagem.
    Pressão (hPa): Pressão atmosférica em hectopascais.
    Temp_min (°C): Temperatura mínima prevista.
    Temp_max (°C): Temperatura máxima prevista.
    Vento (m/s): Velocidade do vento em metros por segundo.

Dependências

    requests: Para realizar a requisição à API.
    pandas: Para manipulação e análise dos dados.
    
Considerações Finais

    Este projeto oferece uma maneira simples de obter e analisar as previsões do tempo utilizando a OpenWeatherMap API. 
    O arquivo CSV gerado pode ser utilizado para análises posteriores ou até mesmo importado para outras ferramentas para visualização de dados.
