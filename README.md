# BackEnd do App EventReg

Este projeto faz parte do **MVP do Sprint de Desenvolvimento Full Stack Básico** e tem o nome de EventReg.

O objetivo aqui é realizar o cadastro das pessoas presentes nos eventos organizados pela Solus IT.
A principal coleta desejada são os e-mails dos presentes, que servirão para futuras malas diretas.
O CPF ficou como opcional por causa da LGPD. Se o inscrito (presente) desejar informar, ele será preenchido.
Importante destacar que o App EventReg tata de cadastrar as pessoas presentes em um evento,
porém pessoas não convidadas podem se inscrever no momento do evento.

---
## Como executar 

> Neste App, usamos o ambiente virtual do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).
> Para instalar o venv no Windows, abra um prompt ou use o terminal do VsCode.
> Vá para pasta que está sua aplicação, e execute os seguintes comandos:
>   python -m venv nome_do_ambiente
>   .\env\Scripts\activate
> OBS.: Se der erro de permissão, abra prompt de comando do Windos e digite:
>   SetExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

✔️ Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Importante destacar que foi retirado, neste arquivo, todas as versões das libs, para evitar erros na execução.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

✔️ Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

✔️ Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

⚠️ Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
