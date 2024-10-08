

**API-WeatherHub**         
  
  **Visão Geral:**                                                        
A API-WeatherHub é uma API baseada em Flask que fornece dados climáticos atuais para uma cidade e país específicos. A API utiliza o OpenWeatherMap como fornecedor de dados climáticos e realiza a conversão da temperatura de Kelvin para Celsius.                                    
                                                      
**Pontos de Extremidade**:
 `/weather`
 `Método`: GET

**Parâmetros:**                                             
 `cidade`: string (obrigatório)             
 `país`: string (obrigatório).                 
  **Resposta**: Objeto JSON com dados climáticos

 **Manipulação de Erros:**
 Retorna um erro 400 se a entrada for inválida (por exemplo, cidade ou país está vazio ou não é uma string)
 Retorna um erro 500 se a solicitação da API para o OpenWeatherMap falhar.

**Funções**:  
 `kelvin_to_celsius(kelvin: float) -> float`      
  Converte a temperatura de Kelvin para Celsius.

`get_weather_data(cidade: str, país: str) -> dict`                         
 Busca dados climáticos da API do OpenWeatherMap para uma cidade e país específicos.

`convert_weather_data(weather_data: dict) -> dict`                                  
 Converte a temperatura de Kelvin para Celsius nos dados climáticos.

`validate_input(cidade: str, país: str) -> bool`                                          
 Valida a entrada cidade e país.

**Variáveis de Ambiente:**                        
 `OPENWEATHERMAP_API_KEY`: Chave API para a API do OpenWeatherMap.
 

  **Para executar a API, execute o seguinte comando:**                                       
 ``python app.py``                      
 Isso iniciará o servidor de desenvolvimento do Flask, e a API estará disponível em `um servidor web como VPS`.

**Exemplo de Solicitação:**                               
 Para buscar dados climáticos para uma cidade e país, envie uma solicitação GET para `um servidor web como VPS` com os seguintes parâmetros:
 ```cidade=Lisboa&país=Portugal```
Isso retornará um objeto JSON com os dados climáticos atuais para Lisboa, Portugal.

**Autenticação e Autorização**                   
 Para implementar autenticação e autorização, a API WeatherHub utiliza o padrão de autenticação básica com tokens.

**Política de Rate Limiting**                
 A API WeatherHub tem uma política de rate limiting que permite 10 requisições por minuto, 50 requisições por hora e 200 requisições por dia.
                                                                                                                                    
                                
*Arquivos de código e aplicativo em outra branch do repositório*                                                                                                      
*A API ainda não está hospedada, se possui interesse em adquiri-lá entre em contato pelo próprio GitHub ou acesse o código para poder fazer a hospedagem.*

