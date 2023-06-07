# 📦 Sistema de Controle de Estoque

O Sistema de Controle de Estoque é uma aplicação web desenvolvida para gerenciar produtos, categorias e estoque de uma loja. Permite adicionar, editar e excluir produtos e categorias, além de exibir o estoque atual. Os dados são armazenados em um banco de dados MySQL local.

## 💻 Ambiente de Desenvolvimento

O projeto foi desenvolvido utilizando as seguintes tecnologias:

- Linguagem de Programação: Python
- Framework Web: Flask
- ORM: Flask-SQLAlchemy
- Banco de Dados: MySQL
- Front-end: HTML, CSS (Bootstrap) e Jinja2 (template engine do Flask)

## 🔧 Instalação e Execução

Siga as etapas abaixo para instalar e executar a aplicação:

1. Clone o repositório para sua máquina local:

```
git clone https://github.com/Well-Alves/MeuEstoque.git
```


2. Acesse o diretório do projeto:

```
cd MeuEstoque
```

3. Crie um ambiente virtual:

```
python3 -m venv venv
```

4. Ative o ambiente virtual:
- No Linux/Mac:
  ```
  source venv/bin/activate
  ```
- No Windows (PowerShell):
  ```
  venv\Scripts\Activate.ps1
  ```

5. Instale as dependências do projeto:

```
pip install -r requirements.txt
```

6. Configure o banco de dados:
- Crie um banco de dados MySQL local.
- No arquivo app.py, atualize as configurações do banco de dados na variável `app.config['SQLALCHEMY_DATABASE_URI']` para apontar para o seu banco de dados local.

7. Execute o aplicativo:

```
python app.py
```

8. Acesse o aplicativo em seu navegador usando o endereço http://localhost:5000.

## 📋 Requisitos de Sistema

Para executar a aplicação, você precisará ter instalado os seguintes componentes:

- Python 3 ou posterior
- MySQL 8 ou posterior

Certifique-se de ter as versões corretas desses componentes instaladas em seu sistema.

## 👥 Contribuição

Se você quiser contribuir para o projeto, siga as etapas abaixo:

1. Faça um fork do repositório.
2. Crie uma nova branch para a sua contribuição.
3. Implemente as alterações desejadas.
4. Execute os testes e certifique-se de que eles passem.
5. Faça commit das suas alterações.
6. Envie um pull request com uma descrição clara das alterações propostas.

Ficaremos felizes em revisar e incorporar suas contribuições!

## 🧹 Práticas de Código Limpo

Durante o desenvolvimento do projeto, foram aplicadas práticas de código limpo, como:

- Utilização de nomes descritivos para variáveis, funções e classes.
- Quebra de linhas adequada para melhor legibilidade.
- Comentários claros e concisos para explicar trechos complexos de código.
- Separação de responsabilidades em diferentes módulos e funções.
- Uso de boas práticas de programação, como evitar duplicação de código.

## 🧪 Testes Automatizados

A aplicação atualmente não possui testes automatizados implementados. É recomendado o desenvolvimento de testes para garantir a qualidade e robustez do sistema. Testes unitários podem ser escritos para cada funcionalidade importante do sistema, bem como testes de integração para verificar o correto funcionamento das diferentes partes da aplicação.

## 🏗️ Padrão de Projeto de Software

Durante o desenvolvimento do projeto, foi aplicado o padrão de projeto MVC (Model-View-Controller) para organizar e separar as diferentes partes da aplicação. O Flask foi utilizado como framework para implementar o MVC, onde os modelos (Model) representam as entidades do banco de dados, as rotas e controladores (Controller) estão implementados nas views, e as templates (View) são utilizadas para renderizar as páginas HTML.
