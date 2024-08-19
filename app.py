import mysql.connector
from funcoes import obter_entrada_valida, validar_salario, validar_emprestimo, analisar_credito
from banco_dados import inserir_historico_credito, consultar_historico_credito  # Importa também consultar_historico_credito

# Lógica principal do programa
nome = input("Digite seu nome: ")

# Define os limites mínimo e máximo do empréstimo
limite_minimo_emprestimo = 500.00
limite_maximo_emprestimo = 50000.00

while True:
    salario = obter_entrada_valida("Digite o valor do seu salário: R$ ")
    if not validar_salario(salario):
        print("O salário deve ser um valor positivo. Por favor, tente novamente.")
        continue

    emprestimo = obter_entrada_valida("Digite o valor do empréstimo desejado: R$ ")
    if not validar_emprestimo(emprestimo, limite_minimo_emprestimo, limite_maximo_emprestimo):
        print("O valor do empréstimo está fora dos limites permitidos. Por favor, tente novamente.")
        continue

    break

# Chama a função analisar_credito e obtém o resultado da análise
resultado_analise = analisar_credito(nome, salario, emprestimo)

# Exibe a mensagem de resultado da análise
print(resultado_analise['mensagem'])

# Se o crédito foi aprovado, insere o histórico (opcional)
if resultado_analise['aprovado']:
    novo_historico = 'bom'  # Ou 'regular', dependendo da sua lógica
    try:
        inserir_historico_credito(nome, novo_historico)
    except mysql.connector.Error as erro:
        print(f"Erro ao inserir o histórico de crédito: {erro}")