# 🤖 Jinhsi Bot - Wuthering Waves Event Tracker

Este é um para Discord feito em Python que envia mensagens automáticas com **eventos ativos e futuros** do jogo **Wuthering Waves**.

> ⚠️ O bot **não precisa ficar online continuamente**. Basta executá-lo sempre que quiser atualizar as informações no canal.

---

## 📌 Funcionalidades

- Exibe eventos **ativos** com data de término em formato Discord (ex: `Termina em 2 dias`)
- Lista eventos **futuros** que começarão nos próximos 7 dias
- Envia tudo em um **embed bonito** com imagem de banner
- Mensagem enviada automaticamente ao iniciar o bot

---

## 🛠️ Instalação e configuração

### ✅ Pré-requisitos

- Python 3.8 ou superior instalado
- Um bot criado no [Portal de Desenvolvedores do Discord](https://discord.com/developers/applications)
- Permissões do bot: `Send Messages` no canal desejado

---

### 📥 Passo a passo para rodar o bot

1. **Clone este repositório ou baixe os arquivos**

2. **Instale as dependências**:

pip install -r requirements.txt

3. **Crie um arquivo .env na raiz do projeto com o seguinte conteúdo**:
DISCORD_TOKEN=seu_token_aqui
CANAL_ID=id_do_canal

4. **Execute o bot**:
python main.py


Jinhsi-bot/

├── main.py          # Código principal do bot

├── .env             # Arquivo com dados sensíveis (não subir para o GitHub!)

└── requirements.txt # Lista de dependências

💡 **Como adicionar eventos**

Adicione novos eventos ou atualize as datas diretamente nessa lista.

Dentro do arquivo main.py, você verá a lista de eventos no formato:


eventos = [
    {
        "nome": "Nome do Evento",
        "inicio": datetime.datetime(2025, 4, 1, 12, 0, 0),
        "fim": datetime.datetime(2025, 4, 10, 11, 59, 0),
    },
    # Adicione mais eventos aqui
]


🔐**Segurança**
O arquivo .env nunca deve ser compartilhado ou enviado para o GitHub, pois contém o token do seu bot.
Se você pretende usar o Git/GitHub, crie um arquivo .gitignore (ou edite se já existir) e coloque o seguinte comando dentro do .gitignore: 

.env

Isso evita que o .env com seus dados sensíveis vá para o repositório.


📂 **Outros**
Caso você não possua uma IDE como VS Code, PyCharm ou não saiba como utilizar uma, você pode usar o Notepad++ para editar o arquivo main.py com facilidade.

Basta clicar com o botão direito no arquivo e escolher “Editar com Notepad++”.


🧾 **Licença**
Este projeto é de uso pessoal e educativo. Sinta-se livre para modificar e usar como quiser.


Criado com ❤️ por Helm
