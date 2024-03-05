import psycopg
print(psycopg)
class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

#definição do método: ele recebe um objeto do tipo Usuario
def existe(usuario):
    #Abre a conexão
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="20241_fatec_ipi_pdbi_login_phyton",
        user="postgres",
        passwprd="123456"
    ) as conexao:
        #obtem um cursor
        with conexao.cursor() as cursor:
            #executa o comando
            cursor.execute('SELECT * FROM tb_usuario WHERE login=%s AND senha=%s', (f'{usuario.login}') , (f'{usuario.senha}'))!= none
            result = cursor.fetchone()
            return result != None 
def teste():
    print(existe(Usuario('admin', 'admin')))

    teste()