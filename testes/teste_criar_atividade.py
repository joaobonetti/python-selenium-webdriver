from selenium import webdriver
from pages.page_criar_atividade import criarAtividade
from utils.login import LoginProfessor

webdriver = webdriver.Chrome(r'd:\Downloads\chromedriver_win32\chromedriver.exe')

url = "https://integra-h.nrc.ice.ufjf.br/"
webdriver.get(url)

login_professor = LoginProfessor(webdriver)

login_professor.realiza_login(
    login = 'testes.professor',
    senha = '6kmfDK'
)

criar_atividade = criarAtividade(webdriver)

# --------- Caso de teste: Criação de atividade padrão -------------#
criar_atividade.caminho()
criar_atividade.ct11_criar_atividade(
    tema        = 'ativividade teste ct11',
    descricao   = 'teste nova atividade',
    vagas       = '30',
    duracao     = '8',
    sala        = '101',
    data        = '12/12/2020',
    hora_inicio = '1000',
    hora_fim    = '1800'
)
# ------------- Caso de teste: Cancelar transação ----------------#
webdriver.get(url)
criar_atividade.caminho()
criar_atividade.ct12_criar_atividade()

# --------------- Caso de teste: Data incoerente -----------------#
webdriver.get(url)
criar_atividade.caminho()
criar_atividade.ct13_criar_atividade(
    tema        = 'teste datas invalidas ct13',
    vagas       = '30',
    duracao     = '8',
    sala        = '102',
    data        = '12/12/2017',
    hora_inicio = '1000',
    hora_fim    = '1800'
)
# --------------- Caso de teste: Hora incoerente -----------------#
webdriver.get(url)
criar_atividade.caminho()
criar_atividade.ct14_criar_atividade(
    tema        = 'teste datas invalidas ct14',
    vagas       = '30',
    duracao     = '1',
    sala        = '103',
    data        = '12/12/2020',
    hora_inicio = '0800',
    hora_fim    = '2200'
)