import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

# --- 1. CONFIGURAÇÕES E ESTILO VISUAL ---
st.set_page_config(page_title="Portal Mulher Segura", page_icon="🌸", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FFF0F5 !important; }
    h1, h2, h3, p, span, label, li { color: #8B1C62 !important; }
    [data-testid="stSidebar"] { background-color: #262626 !important; border-right: 2px solid #FF69B4; }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span { color: #FFB6C1 !important; }
    .law-card { background-color: #FFE4E1; padding: 20px; border-radius: 15px; border-left: 6px solid #FF69B4; margin-bottom: 20px; }
    .concientizacao { background-color: #8B1C62; color: white !important; padding: 25px; border-radius: 15px; margin: 20px 0; }
    .concientizacao h2, .concientizacao p { color: white !important; }
    .stButton>button { background-color: #FF69B4 !important; color: white !important; border-radius: 20px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SAÍDA DE EMERGÊNCIA ---
if st.button("❌ SAIR RÁPIDO DO SITE"):
    st.markdown('<meta http-equiv="refresh" content="0;URL=\'https://www.google.com\'" />', unsafe_allow_html=True)

# --- 3. MENU LATERAL (SIDEBAR) ---
with st.sidebar:
    st.title("🆘 Ajuda Imediata")
    # Imagem de União
    st.image("https://www.gov.br/mdh/pt-br/assuntos/noticias/2023/marco/mdhc-lanca-painel-de-dados-sobre-violencia-contra-mulheres/@@images/image", caption="Portal de Proteção", width=150)
    st.error("**190** - Polícia Militar")
    st.error("**180** - Central da Mulher")
    st.divider()
    st.subheader("Sinal Vermelho ✋")
    # Imagem do X na mão corrigida para Wikimedia (mais estável)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Red_cross_hand.svg/200px-Red_cross_hand.svg.png", width=120)
    st.caption("Faça um 'X' na palma da mão se você estiver precisando de ajuda, e amostre pra alguma altoridade e ele irá lhe ajudar")

# --- 4. TÍTULO E DEFINIÇÃO DO FEMINICÍDIO ---
st.title("🛡️ Mulher Segura a Todo Tempo")

col_intro, col_img_intro = st.columns([2, 1])
with col_intro:
    st.subheader("O que é o Feminicídio?")
    st.write("""
    O **feminicídio** é o assassinato brutal de mulheres motivado pelo gênero, muitas vezes resultado de uma cultura de machismo 
    e desigualdade. É o ponto final de um ciclo de violência doméstica, controle e posse, onde a vítima é vista como objeto do agressor.
    Muitas mulheres vivem sob medo constante, silenciadas pela vergonha, culpa ou medo de represálias. A normalização da violência
    doméstica faz com que muitas acreditem que a situação é passageira ou que a culpa é delas. Isso as impede de buscar ajuda, perpetuando o ciclo de agressão.
    O feminicídio é um problema grave e crescente no Brasil, sendo o país com maior número de casos na América Latina. A impunidada
    e a falta de políticas eficazes de proteção às vítimas contribuem para a perpetuação desse crime.
    """)
    st.write("**O que as mulheres passam:** A violência contra as mulheres é um assunto sério e complexo. Muitas mulheres são submetidas a situações de abuso e controle, que podem começar de forma sutil, mas escalam para algo muito mais grave. Imagine ter que lidar com alguém que controla o que você veste, com quem você fala, ou até mesmo onde você vai. Isso é uma realidade para muitas mulheres. E o pior é que, muitas vezes, elas são levadas a acreditar que a culpa é delas. A violência psicológica é um dos tipos mais comuns de agressão, e é frequentemente subestimada. Ela pode incluir manipulação, humilhação, ameaças e isolamento, deixando a vítima sem apoio e vulnerável. É como se estivessem sendo lentamente sufocadas, sem saber como escapar. E, infelizmente, a violência física é uma realidade para muitas mulheres. Agressões, lesões e, em casos extremos, feminicídio são consequências trágicas de um ciclo de violência que não para. Mas não é só isso. A violência sexual, a violência econômica, tudo isso faz parte de um sistema que perpetua a opressão e o medo.")
with col_img_intro:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Emblem-person-woman.svg/120px-Emblem-person-woman.svg.png", caption="Sua vida importa.")

# --- 5. CONSCIENTIZAÇÃO ---
st.markdown("""
    <div class="concientizacao">
        <h2>📢 Não tenha medo: Denunciar salva vidas!</h2>
        <p>O silêncio protege o agressor. O Estado oferece proteção imediata. <b>A culpa NUNCA é sua. Peça ajuda!</b></p>
    </div>
    """, unsafe_allow_html=True)

# --- 6. ABAS ---
tab_leis, tab_ciclo, tab_teste, tab_dados = st.tabs(["⚖️ Leis & Direitos", "🔄 O Ciclo", "🔍 Avaliação de Risco", "📊 Dados de Impacto"])

with tab_leis:
    st.header("Biblioteca Jurídica de Proteção à Mulher")
    
    st.markdown('<div class="law-card">', unsafe_allow_html=True)
    st.subheader("Lei Maria da Penha (11.340/06)")
    st.write("A Lei Maria da Penha é uma lei federal brasileira (Lei nº 11.340/2006) que visa proteger mulheres em situação de violência doméstica e familiar. Ela foi criada em homenagem a Maria da Penha Maia Fernandes, uma biofarmacêutica cearense que sofreu violência doméstica por parte de seu marido durante 23 anos.")
    st.link_button("Acessar Lei", "http://www.planalto.gov.br/ccivil_03/_ato2004-2006/2006/lei/l11340.htm")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="law-card">', unsafe_allow_html=True)
    st.subheader("Lei Mariana Ferrer (14.245/21)")
    st.write("A Lei Mariana Ferrer, também conhecida como Lei nº 14.245/2021, é um marco importante na proteção das vítimas de crimes sexuais no Brasil. Ela foi criada após o caso da influenciadora digital Mariana Ferrer, que denunciou ter sido dopada e estuprada em 2018, e sofreu revitimização durante o julgamento.")
    st.link_button("Acessar Lei", "https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14245.htm")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="law-card">', unsafe_allow_html=True)
    st.subheader("Lei do Minuto Seguinte (12.845/13)")
    st.write("A Lei do Minuto Seguinte, também conhecida como Lei nº 12.845/2013, é uma legislação brasileira que visa proteger e auxiliar as vítimas de violência sexual, garantindo atendimento emergencial, integral e gratuito no Sistema Único de Saúde (SUS).")
    st.link_button("Acessar Lei", "https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/lei/l12845.htm")
    st.markdown('</div>', unsafe_allow_html=True)

with tab_ciclo:
    st.header("Entenda Por Onde Tudo Começa e o Que as Mulheres Passam")
    st.image("https://www.cnj.jus.br/wp-content/uploads/2021/08/ciclo-violencia.png", caption="Fonte: CNJ", use_container_width=True)
    st.write("""
    1.  **Tensão**: A situação começa a esquentar, com agressões verbais, ameaças e um clima de medo. A vítima pode sentir-se ansiosa, tentando evitar o pior. O agressor pode ficar irritado, crítico e controlador.
    2.  **Explosão**: A tensão explode em agressão física ou sexual grave, deixando a vítima em situação de vulnerabilidade extrema. É o momento mais perigoso, com risco de lesões graves ou até morte.
    3.  **Lua de Mel**: O agressor se arrepende, pede desculpas e jura mudar. Muitas vítimas, esperançosas de uma mudança, desistem da denúncia ou voltam para o agressor. Ele pode ser carinhoso e promissor, mas é uma armadilha.
    4.  **Calmaria**: Após a Lua de Mel, pode haver um período de calmaria, onde parece que tudo voltou ao normal. Mas é uma ilusão, a tensão começa a aumentar novamente.
    5.  **Isolamento**: O agressor pode isolar a vítima de amigos, familiares e apoio, tornando-a mais dependente e vulnerável.
    6.  **Culpa e Vergonha**: A vítima pode sentir-se culpada ou envergonhada, acreditando que a violência é sua culpa.
    """)

with tab_teste:
    st.header("Análise de Risco Que Voçe Ja Passou ou Está Passando")
    st.write("Responda com sinceridade essa pesquisa é Totalmente Anônimo")
    r1 = st.checkbox("Ele já ameaçou tirar seus filhos ou sua vida?")
    r2 = st.checkbox("Ele controla suas senhas ou redes sociais?")
    r3 = st.checkbox("Ele te impede de ver amigos ou familiares?")
    r4 = st.checkbox("Ele já destruiu objetos seus propositalmente?")
    r5 = st.checkbox("Ele já te forçou a ter relações sexuais?")
    
    if st.button("Analisar Nível de Risco"):
        pontos = sum([r1, r2, r3, r4, r5])
        if r1 or r5 or pontos >= 3:
            st.error("🚨 RISCO CRÍTICO: Sua vida está em perigo iminente. Ligue 180 ou 190 AGORA.")
        elif pontos >= 1:
            st.warning("⚠️ ALERTA: Você está em uma relação abusiva. Busque apoio psicológico e jurídico.")
        else:
            st.success("✅ Continue se informando sobre seus direitos.")

with tab_dados:
    st.header("📊 Pequisa de Denúcias Feitas e Medidas Tomadas")
    
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
    denuncias = [120, 155, 190, 240, 280, 350]
    medidas = [100, 140, 175, 210, 250, 320]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(meses, denuncias, color='#8B1C62', label='Denúncias (180)')
    ax.bar(meses, medidas, color='#FF69B4', label='Medidas Protetivas', alpha=0.8)
    ax.set_facecolor('#FFF0F5')
    fig.patch.set_facecolor('#FFF0F5')
    ax.legend()
    for s in ax.spines.values(): s.set_visible(False)
    
    st.pyplot(fig)
    
    st.markdown("""
    **Sobre os Dados:**
    Este gráfico ilustra a correlação direta entre o aumento das denúncias e a resposta imediata do Poder Judiciário. 
    A proximidade entre as barras de 'Denúncias' e 'Medidas' demonstra que o Estado está atento: mulheres que denunciam 
    recebem amparo legal. Os números crescentes em 2026 refletem maior confiança nas instituições e a eficácia das campanhas 
    de conscientização como o Sinal Vermelho.
    """)

# --- 7. RODAPÉ ---
st.divider()
st.markdown("<p style='text-align: center;'>Projeto Acadêmico | 2026 🌸</p>", unsafe_allow_html=True)

# Contador de visitas
st.markdown("""
    <div style='text-align: center;'>
        <img src="https://hitwebcounter.com/counter/counter.php?page=portalmulhersegura_final&style=0005&nbdigits=5&type=page&initCount=0" border="0" />
    </div>
""", unsafe_allow_html=True)
