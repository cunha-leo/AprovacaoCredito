def obter_entrada_valida(mensagem, tipo_conversao=float):
    """Obtém uma entrada do usuário e a converte para o tipo especificado,
    com tratamento de erros e mensagens de ajuda. Garante que números de ponto flutuante
    tenham no máximo duas casas decimais..."""

    while True:
        try:
            entrada = input(mensagem)
            valor = tipo_conversao(entrada)

            if tipo_conversao == float:
                valor = round(valor, 2)

            return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite um valor numérico válido.")
            if tipo_conversao == float:
                print("Você pode usar o formato padrão da sua região (ex: 1.000,50 ou 1000.50)")

def validar_salario(salario):
    """Valida se o salário é positivo."""

    if salario <= 0:
        return False
    return True

def validar_emprestimo(emprestimo, limite_minimo, limite_maximo):
    """Valida se o empréstimo está dentro dos limites mínimo e máximo."""

    if emprestimo < limite_minimo or emprestimo > limite_maximo:
        return False
    return True

def analisar_credito(nome, salario, emprestimo):
    """Analisa o crédito com base no salário,
    no valor do empréstimo solicitado e no histórico de crédito."""

    from banco_dados import consultar_historico_credito

    valor_maximo = 5 * salario

    # Formatação de moeda independente do locale
    simbolo_moeda = 'R$'
    separador_milhar = '.'
    separador_decimal = ','

    salario_formatado = f"{simbolo_moeda} {salario:,.2f}".replace(',', separador_decimal).replace('.', separador_milhar)
    emprestimo_formatado = f"{simbolo_moeda} {emprestimo:,.2f}".replace(',', separador_decimal).replace('.', separador_milhar)
    valor_maximo_formatado = f"{simbolo_moeda} {valor_maximo:,.2f}".replace(',', separador_decimal).replace('.', separador_milhar)

    # Consulta o histórico de crédito do usuário
    historico = consultar_historico_credito(nome)

    if emprestimo <= valor_maximo:
        if historico and historico == 'ruim':
            resultado = {
                'aprovado': False,
                'mensagem': f"Infelizmente, {nome}, Crédito NEGADO! Seu histórico de crédito não permite a aprovação.",
                'valor_maximo': valor_maximo
            }
        else:
            resultado = {
                'aprovado': True,
                'mensagem': f"Parabéns, {nome}! Crédito APROVADO!\nSeu salário: {salario_formatado}\nValor do empréstimo solicitado: {emprestimo_formatado}",
                'valor_maximo': valor_maximo
            }
    elif emprestimo > valor_maximo:
        resultado = {
            'aprovado': False,
            'mensagem': f"Infelizmente, {nome}, Crédito NEGADO! O valor solicitado excede o limite máximo.\nO valor máximo de empréstimo que você poderia solicitar é: {valor_maximo_formatado}",
            'valor_maximo': valor_maximo
        }

    return resultado