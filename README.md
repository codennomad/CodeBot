# CodeBot

CodeBot é um assistente virtual inteligente que combina conhecimento em diversas áreas como tecnologia, ciências, literatura, neurociências, mitologia, história, geografia e muito mais. Ele é projetado para interagir com documentos, como sites, PDFs e vídeos do YouTube, e fornecer respostas personalizadas para o usuário.

## Funcionalidades

- **Chat Interativo**: O CodeBot interage com o usuário e fornece respostas baseadas em documentos carregados (sites, PDFs ou vídeos do YouTube).
- **Carregamento de Documentos**: O usuário pode carregar documentos de diferentes fontes, como:
  - **Sites**: O CodeBot consegue extrair informações de páginas da web.
  - **PDFs**: Permite a leitura de arquivos PDF.
  - **Vídeos do YouTube**: O CodeBot pode processar conteúdo de vídeos para fornecer informações extraídas.
- **Respostas Personalizadas**: O assistente utiliza inteligência artificial para dar respostas com base nas informações carregadas.
- **Curiosidades e Desafios**: Além de responder perguntas, o CodeBot compartilha curiosidades fascinantes e desafios intelectuais.

## Requisitos

- Python 3.8 ou superior
- Bibliotecas:
  - `dotenv`
  - `langchain`
  - `langchain_groq`
  - `langchain_community`
  - `requests`
  - `tkinter` (para interface gráfica)

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/codennomad/CodeBot.git
   cd CodeBot
Instale as dependências necessárias:

bash
Copiar código
pip install -r requirements.txt
Configure suas variáveis de ambiente. Crie um arquivo .env na raiz do projeto e adicione sua chave de API do Groq:

makefile
Copiar código
GROQ_API_KEY=your_api_key_here
Como Usar
Execute o script principal:

bash
Copiar código
python app.py
O CodeBot irá solicitar que você escolha uma fonte de informação para interagir:

Digite 1 para carregar um site.
Digite 2 para carregar um arquivo PDF.
Digite 3 para carregar um vídeo do YouTube.
Após carregar o documento, interaja com o CodeBot, fazendo perguntas. Ele fornecerá respostas com base no conteúdo carregado.

Para finalizar a conversa, digite x.

Contribuição
Contribuições são bem-vindas! Para contribuir:

Faça um fork deste repositório.
Crie uma branch para a sua feature (git checkout -b feature/nome-da-feature).
Comite suas alterações (git commit -am 'Adiciona nova feature').
Envie para o repositório remoto (git push origin feature/nome-da-feature).
Abra um Pull Request.
Licença
Este projeto é licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

markdown
Copiar código

### Explicação do arquivo `README.md`:
- **Nome do Projeto e Descrição**: Fornece uma visão geral do CodeBot, suas funcionalidades e o que ele faz.
- **Funcionalidades**: Explica de maneira clara as funcionalidades que o CodeBot oferece.
- **Requisitos**: Lista as versões do Python e bibliotecas necessárias.
- **Instalação**: Passos para instalar e configurar o projeto no ambiente local.
- **Como Usar**: Instruções detalhadas de como interagir com o CodeBot após a instalação.
- **Contribuição**: Guia para contribuir com o projeto, promovendo a colaboração.
- **Licença**: Informa a licença do projeto (MIT) e fornece um link para o arquivo de licença.

Este arquivo `README.md` pode ser colocado diretamente no repositório do GitHub para fornecer todas as informações essenciais para novos desenvolvedores ou usuários. Se precisar de mais alguma alteração ou adição, me avise!





