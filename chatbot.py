import os
from dotenv import load_dotenv 
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.document_loaders import PyPDFLoader


load_dotenv()

api_key = os.getenv('GROQ_API_KEY')

if api_key is None:
    raise ValueError("A chave da API não foi encontrada nas variáveis de ambiente.")

os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model = 'llama-3.1-70b-versatile')


def resposta_bot(mensagens, documento):
    mensagens_modelo = [('system', 'Você é o CodeBot, um assistente amigável e espirituoso, com um vasto conhecimento em tecnologia, ciências, geografia, química, literatura, história, mitologia, games e neurociências. Sempre pronto para uma boa conversa, você mistura sabedoria com um toque de humor, tornando o aprendizado e a exploração um prazer. Além disso, você adora compartilhar curiosidades fascinantes, desafios intelectuais e até mesmo dicas para melhorar no seu jogo favorito. Com um espírito curioso e sempre em busca de novas descobertas, você está aqui para ajudar e inspirar em todas as suas aventuras cognitivas. Sabe fazer contas, criar roteiros de viagens, ser um excelente chefe de cozinha, entender sobre finanças e realizar tarefas diversas com eficiência e bom humor. E também pode receber mais informações para personalizar ainda mais a ajuda que oferece: {informacoes}')]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat 
    return chain.invoke({'informacoes': documento}).content

def carrega_site():
    url_site = input('Digite a url do site: ')
    loader = WebBaseLoader(url_site)
    lista_documentos = loader.load()
    documento = ''
    for doc in lista_documentos:
        documento = documento + doc.page_content
    return documento

def carrega_pdf():
    #falta adcioinar o modo de adcionar o pdf#
    loader = PyPDFLoader
    lista_documentos = loader.load()
    documento = ''
    for doc in lista_documentos:
        documento = documento + doc.page_content
    return documento
    

def carrega_video():
    url_youtube = input('Digite a url do video: ')
    loader = YoutubeLoader.from_youtube_url(url_youtube, language = ['pt'])
    lista_documentos = loader.load()
    documento = ''
    for doc in lista_documentos:
        documento = documento + doc.page_content
    return documento

print('Bem-vindo ao CodeBot')

texto_selecao = """
Digite 1 se você estiver pronto para bater um papo com um site!
Digite 2 se você estiver pronto para bater um papo com um pdf!
Digite 3 se você estiver pronto para bater um papo com um video de youtube!
\n
"""
while True:
    selecao = input(texto_selecao)
    if selecao == '1':
        documento = carrega_site
        break
    if selecao == '2':
        documento = carrega_pdf
        break
    if selecao == '3':
        documento = carrega_video
        break
    print('Digite um valor entre 1 e 3!\n')

mensagens = []
while True:
    pergunta = input('Usuario: ')
    if pergunta.lower() == 'x':
        break
    mensagens.append(('user', pergunta))
    resposta = resposta_bot(mensagens, documento)
    mensagens.append(('assistent', resposta))
    print(f'Bot: {resposta}')
    
print('Muito Obrigado por usar o CodeBot')



