# Base de Aplicação Flask

- Este é uma base para a criação de aplicações Flask utilizando o SQLAlchemy.

## Instalação
- Entre na página deste repositório > `<> Code` > `Open with GitHub Desktop`. Para isso é necessário já ter o Github Desktop
- Crie um ambiente virtual: python -m venv venv
- Ative o ambiente virtual:
No Windows: venv\Scripts\activate
No Linux ou Mac: source venv/bin/activate
- Instale as dependências: pip install -r requirements.txt
- Execute o arquivo run.py para iniciar a aplicação: python run.py
- Configuração do Banco de Dados:
Este projeto utiliza o PostgreSQL como banco de dados. Para configurá-lo, é necessário definir as seguintes variáveis de ambiente:

DATABASE: nome do banco de dados
PORTA: número da porta do banco de dados (geralmente 5432)
SENHA: senha do banco de dados
Para configurar a conexão com o banco de dados, edite o arquivo config.py e defina o valor da variável SQLALCHEMY_DATABASE_URI de acordo com as suas configurações. Por exemplo:

```python
DATABASE = 'nome-do-banco'
PORTA = '5432'
SENHA = 'senha-do-banco'

DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "sua_chave_secreta_aqui"
SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:{SENHA}@localhost:{PORTA}/{DATABASE}"
```
## Estrutura de Diretórios

- app/models: diretório para os modelos do SQLAlchemy
- app/routes: diretório para as rotas da aplicação
- app/static: diretório para arquivos estáticos (CSS, JS, imagens, etc.)
- app/templates: diretório para os templates HTML da aplicação