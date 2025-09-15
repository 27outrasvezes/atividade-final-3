import mysql.connector # type: ignore
 
# 1. Conexão com o banco de dados canes_finance
conexao = mysql.connector.connect(
    host="localhost",     # Servidor do MySQL
    user="root",          # Usuário padrão do XAMPP
    password="",          # Senha (vazia no XAMPP por padrão)
    database="canes_finance"  # Nome do banco importado via create_db.sql
)
 
# 2. Criar cursor
cursor = conexao.cursor()
 
# 3. Receber entrada do usuário
descricao = input("Descrição da transação: ")
valor = float(input("Valor da transação: "))
tipo = input("Tipo (credit/debit): ")
data = input("Data (YYYY-MM-DD): ")
 
# ⚠️ IDs fixos de exemplo (ajuste conforme seus dados existentes no banco)
account_id = 1     # conta 'Conta Banco'
category_id = 1    # categoria 'Venda'
created_by = 1     # usuário admin
 
# 4. Comando SQL para inserir transação
sql = """
INSERT INTO transactions (trx_date, description, amount, trx_type, account_id, category_id, created_by)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""
valores = (data, descricao, valor, tipo, account_id, category_id, created_by)
 
cursor.execute(sql, valores)
 
# 5. Confirmar no banco
conexao.commit()
 
print(f"✅ Transação '{descricao}' registrada com sucesso!")
 
# 6. Fechar cursor e conexão
cursor.close()
conexao.close()
