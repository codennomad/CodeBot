import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.document_loaders import PyPDFLoader
import tkinter as tk
from tkinter import filedialog, simpledialog


load_dotenv()

api_key = os.getenv('GROQ_API_KEY')

if api_key is None:
    raise ValueError("A chave da API não foi encontrada nas variáveis de ambiente.")

os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.1-70b-versatile')

def resposta_bot(mensagens, documento):
    mensagens_modelo = [('system', 'Você é o CodeBot, um assistente amigável e espirituoso, com um vasto conhecimento em tecnologia, ciências, geografia, química, literatura, história, mitologia, games e neurociências. Sempre pronto para uma boa conversa, você mistura sabedoria com um toque de humor, tornando o aprendizado e a exploração um prazer. Além disso, você adora compartilhar curiosidades fascinantes, desafios intelectuais e até mesmo dicas para melhorar no seu jogo favorito. Com um espírito curioso e sempre em busca de novas descobertas, você está aqui para ajudar e inspirar em todas as suas aventuras cognitivas. Sabe fazer contas, criar roteiros de viagens, ser um excelente chefe de cozinha, entender sobre finanças e realizar tarefas diversas com eficiência e bom humor. E também pode receber mais informações para personalizar ainda mais a ajuda que oferece: {informacoes}')]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    return chain.invoke({'informacoes': documento}).content

def carrega_site(url):
    loader = WebBaseLoader(url)
    lista_documentos = loader.load()
    documento = ''
    for doc in lista_documentos:
        documento = documento + doc.page_content
    return documento

def carrega_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    lista_documentos = loader.load()
    documento = ''
    for doc in lista_documentos:
        documento = documento + doc.page_content
    return documento

def carrega_video(url_youtube):
    loader = YoutubeLoader.from_youtube_url(url_youtube, language=['pt'])
    lista_documentos = loader.load()
    documento = ''
    for doc in lista_documentos:
        documento = documento + doc.page_content
    return documento

# Função para abrir uma janela de chat
def iniciar_chat():
    # Função de resposta do bot
    def enviar_mensagem():
        mensagem_usuario = texto_usuario.get()
        if mensagem_usuario.lower() == 'x':
            root.quit()
        mensagens.append(('user', mensagem_usuario))
        resposta = resposta_bot(mensagens, documento)
        mensagens.append(('assistent', resposta))
        exibir_mensagem(resposta)
        texto_usuario.delete(0, tk.END)

    # Função para exibir mensagens
    def exibir_mensagem(resposta):
        texto_chat.config(state=tk.NORMAL)
        texto_chat.insert(tk.END, "Você: " + mensagens[-2][1] + '\n')
        texto_chat.insert(tk.END, "CodeBot: " + resposta + '\n\n')
        texto_chat.config(state=tk.DISABLED)
        texto_chat.yview(tk.END)

    # Função para carregar arquivo PDF
    def carregar_pdf_action():
        pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if pdf_path:
            documento = carrega_pdf(pdf_path)
            exibir_mensagem("PDF carregado com sucesso!")

    # Função para carregar site
    def carregar_site_action():
        url = simpledialog.askstring("Input", "Digite a URL do site:")
        if url:
            documento = carrega_site(url)
            exibir_mensagem(f"Site carregado com sucesso: {url}")

    # Função para carregar vídeo do YouTube
    def carregar_video_action():
        url_youtube = simpledialog.askstring("Input", "Digite a URL do vídeo do YouTube:")
        if url_youtube:
            documento = carrega_video(url_youtube)
            exibir_mensagem(f"Vídeo carregado com sucesso: {url_youtube}")

    # Criando a janela gráfica
    root = tk.Tk()
    root.title("CodeBot - Assistente Virtual")
    root.geometry("500x600")
    root.config(bg="#F4F4F9")

    # Criando a área do chat
    texto_chat = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED, width=60, height=20, bg="#EAEAEA", fg="#333", font=("Arial", 10), bd=2, relief="solid", padx=10, pady=10)
    texto_chat.pack(pady=20)

    # Caixa de entrada para o usuário
    texto_usuario = tk.Entry(root, width=50, font=("Arial", 12), bd=2, relief="solid", bg="#FFFFFF", fg="#333")
    texto_usuario.pack(pady=10)

    # Botões com uma estética mais limpa
    btn_pdf = tk.Button(root, text="Carregar PDF", command=carregar_pdf_action, width=20, height=2, font=("Arial", 12), bg="#6C7B8B", fg="white", relief="raised")
    btn_pdf.pack(pady=5)

    btn_site = tk.Button(root, text="Carregar Site", command=carregar_site_action, width=20, height=2, font=("Arial", 12), bg="#6C7B8B", fg="white", relief="raised")
    btn_site.pack(pady=5)

    btn_video = tk.Button(root, text="Carregar Vídeo YouTube", command=carregar_video_action, width=20, height=2, font=("Arial", 12), bg="#6C7B8B", fg="white", relief="raised")
    btn_video.pack(pady=5)

    btn_enviar = tk.Button(root, text="Enviar", command=enviar_mensagem, width=20, height=2, font=("Arial", 12), bg="#4CAF50", fg="white", relief="raised")
    btn_enviar.pack(pady=10)

    root.mainloop()

mensagens = []
documento = ''  # Documento vazio inicialmente
iniciar_chat()
