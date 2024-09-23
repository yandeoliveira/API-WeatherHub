# API-WeatherHub

A API WeatherHub fornece dados de clima precisos e atualizados para cidades em todo o mundo. Com uma interface fácil de usar e uma política de rate limiting justa, a API WeatherHub é perfeita para desenvolvedores que precisam de dados de clima para seus aplicativos.

Ponto final
` /clima `

Método
` OBTER `

Parâmetros
`city`: Nome da cidade (obrigatório)
`country`: Nome do país (obrigatório)Aqui está o arquivo README para a API-WeatherHub:

API-WeatherHub
Visão Geral
A API-WeatherHub é uma API baseada em Flask que fornece dados climáticos atuais para uma cidade e país específicos. A API usa a API do OpenWeatherMap para buscar dados climáticos e converte a temperatura de Kelvin para Celsius.

Pontos de Extremidade
/weather
Método: GET
Parâmetros:
cidade: string (obrigatório)
país: string (obrigatório)
Resposta: Objeto JSON com dados climáticos
Manipulação de Erros:
Retorna um erro 400 se a entrada for inválida (por exemplo, cidade ou país está vazio ou não é uma string)
Retorna um erro 500 se a solicitação da API para o OpenWeatherMap falhar
Funções
kelvin_to_celsius(kelvin: float) -> float
Converte temperatura de Kelvin para Celsius.

get_weather_data(cidade: str, país: str) -> dict
Busca dados climáticos da API do OpenWeatherMap para uma cidade e país específicos.

convert_weather_data(weather_data: dict) -> dict
Converte temperatura de Kelvin para Celsius nos dados climáticos.

validate_input(cidade: str, país: str) -> bool
Valida a entrada cidade e país.

Variáveis de Ambiente
OPENWEATHERMAP_API_KEY: Chave API para a API do OpenWeatherMap
Executando a API
Para executar a API, execute o seguinte comando:

Edit
Copy code
python app.py
Isso iniciará o servidor de desenvolvimento do Flask, e a API estará disponível em http://localhost:5000/weather.

Exemplo de Solicitação
Para buscar dados climáticos para uma cidade e país, envie uma solicitação GET para http://localhost:5000/weather com os seguintes parâmetros:

Edit
Copy code
cidade=Lisboa&país=Portugal
Isso retornará um objeto JSON com os dados climáticos atuais para Lisboa, Portugal.

Resposta
`weather_data`: Dados de clima em formato JSON

Exemplo de Requisição
`GET /weather?city=São Paulo&country=Brasil`

Exemplo de Resposta
```
{
  "clima": [
    {
      "main": "Nuvens",
      "descrição": "nublado"
    }
  ],
  "principal": {
    "temperatura": 22,5,
    "temp_max": 25,0,
    "temp_min": 20,0
  }
}
```
Autenticação e Autorização
Para implementar autenticação e autorização, a API WeatherHub utiliza o padrão de autenticação básica com tokens.

Política de Rate Limiting
A API WeatherHub tem uma política de rate limiting que permite 10 requisições por minuto, 50 requisições por hora e 200 requisições por dia.
