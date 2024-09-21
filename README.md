# API-WeatherHub

A API WeatherHub fornece dados de clima precisos e atualizados para cidades em todo o mundo. Com uma interface fácil de usar e uma política de rate limiting justa, a API WeatherHub é perfeita para desenvolvedores que precisam de dados de clima para seus aplicativos.

Endpoint
`/weather`

Método
`GET`

Parâmetros
`city`: Nome da cidade (obrigatório)
`country`: Nome do país (obrigatório)

Resposta
`weather_data`: Dados de clima em formato JSON

Exemplo de Requisição
`GET /weather?city=São Paulo&country=Brasil`

Exemplo de Resposta
```
{
  "weather": [
    {
      "main": "Clouds",
      "description": "nublado"
    }
  ],
  "main": {
    "temp": 22.5,
    "temp_max": 25.0,
    "temp_min": 20.0
  }
}
```
Autenticação e Autorização
Para implementar autenticação e autorização, a API WeatherHub utiliza o padrão de autenticação básica com tokens.

Política de Rate Limiting
A API WeatherHub tem uma política de rate limiting que permite 10 requisições por minuto, 50 requisições por hora e 200 requisições por dia.

Suporte Técnico e Atendimento ao Cliente
Para oferecer suporte técnico e atendimento ao cliente, a API WeatherHub fornece uma página de suporte com informações sobre como utilizar a API e como contatar o suporte técnico.


