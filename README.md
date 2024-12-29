# CodeBot - Assistente Virtual com Interface Gráfica e Funcionalidades Avançadas

## Descrição
CodeBot é um assistente virtual projetado para interagir com diferentes tipos de dados, incluindo sites, PDFs e vídeos do YouTube, agora com funcionalidades adicionais. Ele utiliza a API Groq com o modelo Llama 3.1-70B para oferecer respostas informativas e descontraídas a uma ampla gama de perguntas, integrando uma interface gráfica desenvolvida com Tkinter.

Atualmente, o arquivo principal só é acessível como **chatbor2-0** e ainda apresenta alguns erros. Estou trabalhando ativamente para corrigir esses problemas e aprimorar a experiência do usuário.

## Funcionalidades
- **Carregar sites**: Insira uma URL para carregar o conteúdo textual de um site.
- **Carregar PDFs**: Escolha um arquivo PDF local e extraia seu conteúdo.
- **Carregar vídeos do YouTube**: Insira uma URL de vídeo do YouTube para analisar a transcrição.
- **Chat interativo**: Envie mensagens e receba respostas do CodeBot de forma amigável e personalizada.
- **Personalidade única**: O CodeBot combina conhecimento técnico e curiosidades com um toque de humor para tornar as interações mais envolventes.

## Tecnologias Utilizadas
- **Python**
- **Tkinter**: Para criar a interface gráfica.
- **LangChain Groq**: Para integração com o modelo de linguagem.
- **dotenv**: Para gerenciar variáveis de ambiente de forma segura.
- **YouTube e PDF Loaders**: Para carregamento e processamento de conteúdo multimídia.

## Requisitos
1. **Python 3.7 ou superior**
2. Instale as dependências necessárias utilizando o comando:
   ```bash
   pip install python-dotenv langchain-groq langchain langchain-community
   ```
3. Configure a chave da API Groq no arquivo `.env`:
   ```env
   GROQ_API_KEY=Sua_Chave_API
   ```

---

## Como Usar

### Passo 1: Configurar o Ambiente

1. Certifique-se de que todas as dependências estão instaladas.
2. Configure o arquivo `.env` com sua chave da API Groq.

### Passo 2: Executar o CodeBot

1. Execute o script:
   ```bash
   python codebot.py
   ```
2. Escolha a fonte de dados:
   - **1:** Conversar com um site (URL).
   - **2:** Conversar com um documento PDF.
   - **3:** Conversar com um vídeo do YouTube (URL).

### Passo 3: Interagir com o Bot

1. Carregue o documento ou fonte de dados escolhido.
2. Digite perguntas no terminal.
3. Para encerrar, digite `x`.

---

## Estrutura do Código

1. **Carregamento de documentos:**
   - `carrega_site`: Carrega o conteúdo de uma URL.
   - `carrega_pdf`: Carrega o conteúdo de documentos PDF.
   - `carrega_video`: Carrega transcrições de vídeos do YouTube.

2. **Função de resposta:**
   - `resposta_bot`: Processa as mensagens do usuário e retorna respostas baseadas no modelo.

3. **Interface de Terminal:**
   - Oferece uma experiência simples e intuitiva para interagir com o bot.

## Problemas Conhecidos
- Alguns erros podem ocorrer ao carregar determinados tipos de PDFs ou vídeos do YouTube.
- O nome do arquivo atualmente é **chatbor2-0**, o que pode causar confusão. Planejo ajustar isso nas próximas atualizações.
- A interface pode apresentar inconsistências ao lidar com arquivos de grande tamanho.

## Melhorias Planejadas
- Corrigir bugs conhecidos relacionados ao carregamento de vídeos e PDFs.
- Implementar suporte a mais formatos de documentos e arquivos multimídia.
- Melhorar a usabilidade da interface gráfica.
- Alterar o nome do arquivo principal para maior clareza e padronização.

## Contribuições
Contribuições são bem-vindas! Se você encontrar um bug ou tiver sugestões para novas funcionalidades, fique à vontade para abrir um issue ou enviar um pull request no repositório.

---

Obrigado por utilizar o CodeBot! Estou comprometido em continuar aprimorando esta ferramenta. 🚀

