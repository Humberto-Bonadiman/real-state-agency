# Boas vindas ao repositório do projeto Real State Agency

---

## Descrição do projeto

Neste projeto eu desenvolvi um sistema de banco de dados com 3 entidades: Imóveis(Properties), Anúcios(Adverts) e Reservas(Bookings). Um imóvel pode ter
diversos anúncios, mas um anúncio é referente apenas a um imóvel. Um anúncio pode ter
várias reservas, mas uma reserva se refere a apenas um anúncio.
<br/>
Para montar este sistema eu utilizei o Django Rest Framework juntamente com o banco de dados SQLite e criei os arquivos Dockerfile e docker-compose.yml para rodar a aplicação com o Docker.

---

## Instalação do projeto localmente

Após cada um dos passos, haverá um exemplo do comando a ser digitado para fazer o que está sendo pedido.

1. Realize o clone do projeto no diretório de sua preferência e depois acesse o diretório:
```javascript
  git clone git@github.com:humberto-bonadiman/real-state-agency.git
  cd real-state-agency
```

2. Crie o ambiente virtual para o projeto:
```javascript
  python3 -m venv .venv && source .venv/bin/activate
```

3. Instale as dependências:
```javascript
  python3 -m pip install -r requirements.txt
```

4. Aplique as migrations do projeto:
```javascript
  python manage.py makemigrations
  python manage.py migrate
```

5. Rode o projeto:
```javascript
  python manage.py runserver
```

---

## Utilizar o seed

Para já criar alguns dados no banco de dados utilize o comando abaixo:
```javascript
python manage.py loaddata properties/seed/0001_properties.json
```

## Comandos para utilizar o Docker

Para criar e iniciar os contêineres:
</br>
Obs.: Com o comando abaixo o docker fica rodando no terminal.
```javascript
  docker-compose up
```

Para criar e iniciar os contêineres em stand-by:
```javascript
  docker-compose up -d
```

Para realizar apenas a etapa de build das imagens que serão utilizadas:
```javascript
  docker-compose build
```

Para paralisar e remover todos os contêineres e seus componentes como rede, imagem e volume:
```javascript
  docker-compose down
```

Para remover as imagens criadas após o comando **docker-compose down** você pode fazer remover pelos id. Por exemplo, se você possuir duas imagens com os ids 66ee964ad49b e 55caede2ba47 você pode usar o comando abaixo pegando somente os dois primeiros caracteres do id:
```javascript
  docker rmi -f 66 55
```

---

## Testes

Para executar os testes certifique-se de que você está com o ambiente virtual ativado.
**Executar os testes**
```javascript
  python manage.py test
```

**Executar os testes da camada model**
```javascript
  python manage.py test properties.tests.models.tests
```

**Executar os testes da camada view**
```javascript
  python manage.py test properties.tests.views.tests
```

**Executar os testes de uma classe específica** -> <Django app name>.path.to.file.ClassName
```javascript
  python manage.py test properties.tests.views.tests.GetAllPropertiesTest
```

## Ambiente Virtual

O Python oferece um recurso chamado de ambiente virtual que permite sua máquina rodar, sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Caso precise desativar o ambiente virtual, execute o comando "deactivate". 
  Lembre-se de ativar novamente quando voltar a trabalhar no projeto.
