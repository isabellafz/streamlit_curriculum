import streamlit as st   
from pathlib import Path
from PIL import Image


# Configurações estruturais ==============================================

diretorio = Path(__file__).parent if "__file__" in locals() else Path.cwd()
arquivo_css = diretorio / "styles" / "geral.css"
arquivo_pdf = diretorio / "assets" / "Profile.pdf"
arquivo_img = diretorio / "assets" / "foto.jpg"


# Configurações Gerais das Informações ===================================

TITULO = 'Curriculo | Murillo Henrique'
NOME = 'Murillo Henrique Zanchetta Quirino'
DESCRICAO = """
    DevOps Júnior com foco na cloud AWS e Azure, com experiência em Desenvolvimento FullStack, Kubernets, Docker.
    Tenho experiências com as linguagens: Python, Javascript, Typescript.
    E com os Frameworks: Django, Streamlit, Dash, React
"""
EMAIL = 'murillohenriquezquirino@gmail.com'
MIDIA_SOCIAL = {
    'LinkedIn': 'https://www.linkedin.com/in/murillo-zanchetta-69270826a/',
    'GitHub': 'https://github.com/MurilloZanchetta',
    'Instagram': 'https://www.instagram.com/murillo_godoyy/'
}
CURSOS = {
    '🎯 Curso de Django Web Framework e Django Rest Framework',
    '🎯 Desenvolvendo Dashboards em Python',
    '🎯 Aprenda Internet das Coisas na Prática',
    '🎯 Consultor de Software ERP',
    '🎯 AWS na prática',
}

st.set_page_config(
    layout="wide",
    page_title=TITULO
)

# Carregando assets ===================================================

with open(arquivo_css) as c:
    st.markdown('<style>{}</style>'.format(c.read()), unsafe_allow_html=True)
    
    
with open(arquivo_pdf, 'rb') as arquivo_pdf:
    pdfLeitura = arquivo_pdf.read()
    

imagem = Image.open(arquivo_img)



# colunas ============================================================

col1, col2 = st.columns(2, gap='small')
with col1:
    st.image(imagem, width=250)
    
with col2:
    st.title(NOME)
    st.write(DESCRICAO)
    st.download_button(
        label="Download Curriculo",
        data=pdfLeitura,
        file_name=arquivo_pdf.name,
        mime='application/octet-stream'
    )
    
    st.write(':envelope:', '-', EMAIL)
    
# Midias sociais


st.write("#")
colunas = st.columns(len(MIDIA_SOCIAL))

for indice, (plataforma, link) in enumerate(MIDIA_SOCIAL.items()):
    
    colunas[indice].write(f'[{plataforma}]({link})')
    
    
# experiências

st.write('#')

st.subheader('Experiências')

st.write(
    """
        - :chart: Desenvolvimento web com django
        - :chart: Análise de dados com Python
        - :chart: desenvolvimento web com Typescript
        
        """
)


st.write('#')

st.subheader('Skills')

st.write(
    """
        - 🌐 Programação (Python, Javascript)
        - :chart: Análise de Dados
        - 🤖 Experiência em AI
        
    """
)

# historico de trabalho

st.write('#')

st.subheader('Histórico de trabalho')

st.write('---')


st.write('💻', '**Desenvolvedor fullstack / DevOps  | FL Software**')
st.write('01/2023 - no momento')
st.write(
    """
        Desenvolvendo aplicações e ministrando clouds, como: AWS e Azure
    """
)

# Cursos

st.write('#')

st.subheader('Cursos')
st.write('---')


for curso in CURSOS:
    st.write(f'{curso}')