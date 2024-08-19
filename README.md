# Sistema de Aprovação de Crédito com Python e MySQL

## Descrição

Este projeto implementa um sistema básico de aprovação de 
crédito em Python, utilizando o banco de dados MySQL para 
armazenar e consultar o histórico de crédito dos usuários.
O sistema solicita informações do usuário, como nome, 
salário e valor do empréstimo desejado, e realiza uma 
análise para determinar se o crédito será aprovado ou 
negado. A análise leva em consideração o salário do 
usuário, o valor do empréstimo, limites pré-definidos e 
o histórico de crédito do usuário, se disponível no banco 
de dados.

## Funcionalidades

* **Obtenção de dados do usuário:** Solicita ao usuário seu nome, salário e valor do empréstimo desejado, com validação de entrada para garantir dados numéricos corretos.
* **Validação de dados:**
    * Verifica se o salário é positivo.
    * Verifica se o valor do empréstimo está dentro dos limites mínimo e máximo permitidos.
* **Análise de crédito:**
    * Calcula o valor máximo de empréstimo permitido com base no salário do usuário.
    * Consulta o histórico de crédito do usuário no banco de dados MySQL.
    * Aprova ou nega o crédito com base no valor do empréstimo, no limite máximo e no histórico de crédito.
* **Inserção de histórico de crédito:**
    * Em caso de aprovação do crédito, insere um novo registro no histórico de crédito do usuário no banco de dados.
* **Formatação de moeda:** Formata os valores monetários de acordo com o locale do Brasil, utilizando o símbolo "R$", ponto como separador de milhar e vírgula como separador decimal.
* **Tratamento de erros:** Implementa tratamento de erros para lidar com possíveis exceções durante a conexão com o banco de dados e a execução de consultas SQL.
* **Modularização:** O código é organizado em módulos (`app.py`, `funcoes.py`, `banco_dados.py`) para facilitar a leitura, compreensão e manutenção.

## Tecnologias utilizadas

* Python 3
* MySQL
* mysql-connector-python

## Como executar o projeto

1. **Pré-requisitos:**
   * **Python 3 instalado**
   * **MySQL instalado e em execução**
   * **Banco de dados criado:** Crie um banco de dados chamado `aprovacao_credito` no MySQL.
   * **Tabela criada:** Crie a tabela `historico_credito` no banco de dados usando o script SQL fornecido (`criar_banco.sql`).
   * **Conector MySQL instalado:** `pip install mysql-connector-python`
   * **Credenciais de acesso:** Configure as credenciais de acesso ao seu banco de dados MySQL (host, usuário, senha) no arquivo `banco_dados.py` ou utilize variáveis de ambiente.

2. **Executar o programa:**
   * Abra um terminal na pasta do projeto.
   * Execute o comando `python app.py`.
   * O programa solicitará o nome do usuário, salário e valor do empréstimo.
   * Após a análise, o programa exibirá a mensagem de aprovação ou negação do crédito.

## Exemplos de código

````python
# Exemplo de uso da função obter_entrada_valida
salario = obter_entrada_valida("Digite o valor do seu salário: R$ ")

# Exemplo de uso da função validar_salario
if not validar_salario(salario):
    print("O salário deve ser um valor positivo.")

# Exemplo de uso da função analisar_credito
resultado_analise = analisar_credito(nome, salario, emprestimo)
print(resultado_analise['mensagem'])
Use o código com cuidado.
````

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para sugerir melhorias, corrigir bugs ou adicionar novas funcionalidades ao projeto.   

## Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.   

## Observações
Este é um projeto de exemplo para fins de aprendizado. Em um sistema real de aprovação de crédito, seria necessário implementar funcionalidades mais complexas, como análise de risco, verificação de documentos, integração com sistemas externos, etc.
Certifique-se de proteger suas credenciais de acesso ao banco de dados, utilizando variáveis de ambiente ou um arquivo de configuração externo.
