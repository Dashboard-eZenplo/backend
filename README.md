# Guia de Instalação do Projeto

Este arquivo `README.md` fornece um guia detalhado para configurar o ambiente de desenvolvimento tanto no Windows (utilizando WSL) quanto no macOS. Siga as instruções específicas para o seu sistema operacional para garantir que tudo funcione corretamente.


## 1. Recomendação: Utilização do WSL para Desenvolvimento (Windows)

Para usuários de Windows, recomenda-se fortemente o uso do WSL para configurar o ambiente de desenvolvimento. O WSL permite que você execute um sistema Linux diretamente no Windows, facilitando a instalação e o uso de ferramentas de desenvolvimento que são nativas do Linux.

### 2. Instalação do WSL (Windows)

1. Abra o PowerShell como Administrador.
2. Execute o seguinte comando para instalar o WSL:

    ```powershell
    wsl --install
    ```
3. Reinicie o seu computador para que as alterações tenham efeito.

### 3. Instalação do Ubuntu via Microsoft Store (Windows)

1. Abra a **Microsoft Store** no seu Windows.
2. Pesquise por **Ubuntu** e selecione a versão mais recente (recomenda-se o Ubuntu 20.04 ou 22.04).
3. Clique em **Obter** e, em seguida, **Instalar**.
4. Após a instalação, abra o Ubuntu a partir do menu Iniciar e siga as instruções para configurar seu usuário e senha.
5. Fixe o Ubuntu na barra de tarefas, clicando nele que será aberto o terminal corretamente.

## 4. Instalação do Python 3.10.12 (Windows e macOS)

### No Windows (via WSL/Ubuntu):

0. Instalação do terminal **oh my zsh** que facilitará o desenvolvimento:

    ```wsl
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
    ```
    - Documentação do terminal: https://github.com/ohmyzsh/ohmyzsh/wiki
    - Feche e abra o WSL após instalação para aplicar corretamente as mudanças.

1. Atualize a lista de pacotes:

    ```bash
    sudo apt-get update
    ```

2. Instale o Python 3.10.12:

    ```bash
    sudo apt update
    sudo apt install python3.10
    ```

    - _Caso tenha sido instalada outra versão de python 3.10@:_

    ```bash
    sudo apt install python3.10=3.10.12
    ```

3. Verifique se a instalação foi bem-sucedida:

    ```bash
    python3.10 --version
    ```

### No macOS:

1. **Instale o Homebrew** (se ainda não tiver instalado):

    Abra o terminal e execute:

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. **Instale o Python 3.10.12** via Homebrew:

    ```bash
    brew install python@3.10
    ```

3. **Verifique a instalação**:

    ```bash
    python3.10 --version
    ```

## 5. Clonar o Projeto (Windows e macOS)

Clone o repositório do projeto para sua máquina local:

```bash
git clone https://tools.ages.pucrs.br/dashboard-ezenplo/backend.git
cd backend
```

## 6. Criação do Ambiente Virtual (Windows e macOS)

```bash
python3 -m venv venv
```
### Ative o Ambiente Virtual

- No WSL/Ubuntu ou macOS:

```bash
source venv/bin/activate
```

## 7. Instalar os requirements (Windows e macOS)

Com o ambiente virtual ativado, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

## 8. Baixar o Pre-commit (Windows e macOS)

Instale o pre-commit para garantir a qualidade do código:

```bash
pip install pre-commit
pre-commit install
```

**Agora, seu ambiente de desenvolvimento está configurado e pronto para uso. Lembre-se de SEMPRE ativar o ambiente virtual quando trabalhar no projeto, usando o comando:**
```bash
 source venv/bin/activate.
 ```


---

# Testando localmente

## 1. Rodar a API

Para rodar a API, basta ir ao menu lateral localizado à esquerda e clicar no ícone de **Run and Debug** (ou apertar **CTRL/COMMAND+SHIFT+D**), depois na parte superior esquerda clicar no **play verde** onde está escrito ao lado **Python: FastAPI (Uvicorn)**. Voce perceberá que um terminar vai abrir e passar a apresentar os LOGS da API em tempo real.

## 2. Testar os Endpoints

Para testar os Endpoits, com a API rodando, pode-se tanto utilizar o Postman (ou algum programa similar) como também via browser pelo endereço: **localhost/8000/docs#/**

# GitFlow

## Main
- Não acontece desenvolvimento nesta branch. É a branch de produção, onde o usuário terá acesso.

## Dev
- É a partir de onde as branchs de desenvolvimento serão criadas. Os Merge Requests (MRs) serão abertos para ela.

## Branchs de desenolvimento
- Aonde o desenvolvimento acontece. O nome da branch será padronizado como: **US-[ID da US] - [Breve descrição]**

## Exemplo visual:
Os nomes das branchs da imagem não são os mesmos do projeto, é somente uma representação.
<img src = "https://codigomaromba.com/wp-content/uploads/2019/01/gitflow-1.png?w=640">

