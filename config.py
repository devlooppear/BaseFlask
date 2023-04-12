DATABASE = 'nome_do_banco'
PORTA = '5432'
SENHA = 'senha_do_banco'

DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "sua_chave_secreta_aqui"
SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:{SENHA}@localhost:{PORTA}/{DATABASE}"
