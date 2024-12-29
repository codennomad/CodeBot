CodeBot: Assistente Virtual Inteligente
CodeBot é um assistente virtual que utiliza IA para responder perguntas sobre uma variedade de tópicos como tecnologia, ciências, geografia, literatura, história, mitologia e neurociências. Ele pode interagir com conteúdo de sites, PDFs e vídeos do YouTube para fornecer respostas personalizadas.

Funcionalidades
Respostas Inteligentes: Gera respostas com base em um modelo avançado de linguagem (Llama 3.1-70B Versatile).
Carregamento de Conteúdo: Carrega dados de sites, PDFs e vídeos do YouTube para enriquecer as respostas.
Interação Dinâmica: Permite uma conversa contínua e adaptativa com o usuário.
Personalização: Ajuste o comportamento do bot com base nas interações do usuário.
Tecnologias Utilizadas
Python: Linguagem principal para desenvolvimento.
LangChain: Framework para integração de dados externos com modelos de linguagem.
Groq API: Utilizada para acesso ao modelo Llama 3.1-70B Versatile.
Tkinter (Futuro): Para criar uma interface gráfica com o usuário (em desenvolvimento).
dotenv: Para gestão de variáveis de ambiente.
Document Loaders: Ferramentas para carregar conteúdo de sites, PDFs e vídeos.
Como Usar
Clone o repositório:

bash
Copiar código
git clone https://github.com/usuario/codebot.git
cd codebot
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Crie um arquivo .env e adicione sua chave da API do Groq:

plaintext
Copiar código
GROQ_API_KEY=your_api_key_here
Execute o script:

bash
Copiar código
python codebot.py
Interaja com o bot, fazendo perguntas e carregando dados de sites, PDFs ou vídeos do YouTube.

Contribuindo
Contribuições são bem-vindas! Se você tem ideias para melhorar o CodeBot, sinta-se à vontade para abrir issues ou enviar pull requests.

Licença
Este projeto é licenciado sob a MIT License.
