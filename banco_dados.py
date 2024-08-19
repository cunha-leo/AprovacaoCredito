import mysql.connector

def conectar_banco_dados():
    """Estabelece a conexão com o banco de dados MySQL."""

    try:
        conexao = mysql.connector.connect(
            host="localhost",  # Substitua pelo host do seu servidor MySQL
            user="root",  # Substitua pelo seu nome de usuário
            password="Cunha@191192",  # Substitua pela sua senha
            database="aprovacao_credito"  # Nome do banco de dados que você criou
        )
        return conexao
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")
        return None


def inserir_historico_credito(nome, historico):
    """Insere um novo registro no histórico de crédito."""

    conexao = conectar_banco_dados()
    if conexao:
        cursor = None  # Inicializa o cursor para evitar o warning
        try:
            cursor = conexao.cursor()

            # Comando SQL para inserir dados (corrigindo o nome da tabela)
            comando_sql = "INSERT INTO historico_credito (nome, historico) VALUES (%s, %s)"
            valores = (nome, historico)

            cursor.execute(comando_sql, valores)
            conexao.commit()
            print(f"Novo registro inserido com sucesso para o usuário {nome}!")

        except mysql.connector.Error as erro:
            print(f"Erro ao inserir registro no histórico de crédito: {erro}")

        finally:  # Garante que o cursor e a conexão sejam fechados, mesmo se ocorrer um erro
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()


# noinspection PyGlobalUndefined
def consultar_historico_credito(nome):
    """Consulta o histórico de crédito de um usuário."""

    conexao = conectar_banco_dados()  # Corrigido o sinal de atribuição
    if conexao:
        try:
            with conexao.cursor() as cursor:  # Usando with para gerenciar o cursor automaticamente

                # Comando SQL para consultar o histórico (corrigindo a sintaxe)
                comando_sql = "SELECT historico FROM historico_credito WHERE nome = %s"
                valores = (nome,)

                cursor.execute(comando_sql, valores)
                resultado = cursor.fetchone()  # Corrigido o sinal de atribuição

                if resultado:
                    return resultado[0]
                else:
                    return None
        except mysql.connector.Error as erro:
            print(f"Erro ao consultar o histórico de crédito: {erro}")
            # Opcional: Você pode lançar a exceção novamente para que seja tratada em outro lugar
            # raise
        finally:
            if conexao:
                conexao.close()

def atualizar_historico_credito(nome, novo_historico):
    """Atualiza o histórico de crédito de um usuário."""

    conexao = conectar_banco_dados()
    if conexao:
        try:
            with conexao.cursor() as cursor:
                # Comando SQL para atualizar o histórico
                comando_sql = "UPDATE historico_credito SET historico = %s WHERE nome = %s"
                valores = (novo_historico, nome)

                cursor.execute(comando_sql, valores)
                conexao.commit()

                if cursor.rowcount > 0:  # Verifica se alguma linha foi afetada
                    print(f"Histórico de crédito do usuário {nome} atualizado com sucesso!")
                else:
                    print(f"Usuário {nome} não encontrado no histórico de crédito.")
        except mysql.connector.Error as erro:
            print(f"Erro ao atualizar o histórico de crédito: {erro}")
        finally:
            if conexao:
                conexao.close()

def excluir_historico_credito(nome):
    """Exclui o registro do histórico de crédito de um usuário."""

    conexao = conectar_banco_dados()
    if conexao:
        try:
            with conexao.cursor() as cursor:
                # Comando SQL para excluir o registro
                comando_sql = "DELETE FROM historico_credito WHERE nome = %s"
                valores = (nome,)

                cursor.execute(comando_sql, valores)
                conexao.commit()

                if cursor.rowcount > 0:
                    print(f"Histórico de crédito do usuário {nome} excluído com sucesso!")
                else:
                    print(f"Usuário {nome} não encontrado no histórico de crédito.")
        except mysql.connector.Error as erro:
            print(f"Erro ao excluir o histórico de crédito: {erro}")
        finally:
            if conexao:
                conexao.close()

# Teste de conexão (opcional)
if __name__ == "__main__":
    conexao = conectar_banco_dados()
    if conexao:
        print("Conexão com o banco de dados estabelecida com sucesso!")
        conexao.close()
    else:
        print("Falha ao conectar ao banco de dados. Verifique suas credenciais e configurações.")