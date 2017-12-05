# **Chatbot**

<br/>

# **Instalação**

### **1) Dependências para instalar**

```
apt-get update
apt-get install apache2
apt-get install mysql-server mysql-client phpmyadmin
apt-get install virtualenv python3.4 python3-dev python-dev gcc libpq-dev libmysqlclient-dev
```

### **2) Como rodar a aplicação**

1. **Criando um ambiente de virtualização**

    ```
    virtualenv -p /usr/bin/python3 .env
    ```

2. **Ativando o ambiente**

    ```
    source .env/bin/activate
    ```

3. **Instalando os pacotes necessários**

    ```
    pip install -r requirements.txt
    ```

4. **Configurando**

    Entre no arquivo **config.py** e adicione suas credencias do Banco de Dados

5. **Criando banco de dados**

    ```
    mysql -uroot -proot
    create database chatbotdb;
    ```

6. **Executar a aplicação (webservice)**

    ```
    python src/run.py
    ```

7. **Url para acessar a aplicação**

    http://localhost:5000
