# CodeBot

**CodeBot** é um assistente virtual inteligente que utiliza a API Groq com o modelo Llama 3.1-70B para oferecer respostas detalhadas e interativas em diversas áreas como tecnologia, ciências, geografia, literatura, história, mitologia, games, neurociências, e muito mais. É projetado para ser amigável, espirituoso e eficiente, proporcionando uma experiência de aprendizado divertida e envolvente.

---

## Funcionalidades

- **Respostas inteligentes:** Fornece respostas precisas baseadas no modelo Llama 3.1-70B.
- **Integração com diferentes fontes:** Permite carregar dados de:
  - Sites
  - Documentos PDF
  - Vídeos do YouTube
- **Interatividade:** Responde a perguntas com base nos documentos carregados.
- **Personalidade amigável:** Torna a experiência de aprendizado mais leve e descontraída.

---

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

---

## Contribuição

1. Faça um fork deste repositório.
2. Crie uma branch para suas alterações (`git checkout -b minha-alteracao`).
3. Commit suas modificações (`git commit -m "Minha alteração"`).
4. Envie para o repositório original (`git push origin minha-alteracao`).
5. Crie um Pull Request.

---

## Licença

Este projeto está licenciado sob a MIT License. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Aproveite e explore as funcionalidades do CodeBot para uma experiência interativa e enriquecedora!

