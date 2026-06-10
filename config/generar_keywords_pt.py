import json
import random

# ============================================
# CONFIGURAÇÃO
# ============================================
QUANTIDADE_KEYWORDS = 10000

# ============================================
# TÓPICOS EM PORTUGUÊS
# ============================================
topicos = {
    "matematica": {
        "topicos": ["matematica", "calculo", "algebra", "geometria", "trigonometria", 
                   "estatistica", "probabilidade", "derivadas", "integrais", "limites", 
                   "funcoes", "matrizes", "vetores", "equacoes", "logaritmos", 
                   "fracoes", "percentagens", "raizes", "potencias", "polinomios", 
                   "numeros complexos", "equacoes diferenciais", "algebra linear",
                   "trigonometria esferica", "calculo vetorial", "topologia", "teoria dos numeros"]
    },
    "fisica": {
        "topicos": ["fisica", "mecanica", "termodinamica", "eletromagnetismo", "optica", 
                   "acustica", "cinematica", "dinamica", "fluidos", "quantica", 
                   "relatividade", "energia", "trabalho", "potencia", "movimento", 
                   "forcas", "gravidade", "eletricidade", "magnetismo", "ondas",
                   "astrofisica", "cosmologia", "fisica nuclear", "fisica molecular"]
    },
    "quimica": {
        "topicos": ["quimica", "quimica organica", "quimica inorganica", "quimica analitica", 
                   "bioquimica", "reacoes quimicas", "balanceamento", "estequiometria", 
                   "tabela periodica", "ligacoes quimicas", "moleculas", "atomos", 
                   "compostos quimicos", "acidos", "bases", "ph", "solucoes", 
                   "gases", "termoquimica", "quimica quantica", "eletroquimica"]
    },
    "biologia": {
        "topicos": ["biologia", "biologia celular", "biologia molecular", "genetica", 
                   "anatomia", "fisiologia", "ecologia", "evolucao", "botanica", 
                   "zoologia", "microbiologia", "dna", "rna", "proteinas", "enzimas", 
                   "metabolismo", "celulas", "tecidos", "orgaos", "sistemas do corpo",
                   "neurociencia", "imunologia", "embriologia"]
    },
    "programacao": {
        "topicos": ["programacao", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "inteligencia_artificial": {
        "topicos_especiais": ["machine learning", "deep learning", "gpt", "llm"],
        "topicos": ["inteligencia artificial", "redes neurais", "processamento de linguagem natural", 
                   "visao computacional", "chatbots", "transformers", "automacao",
                   "aprendizado de maquina", "aprendizado profundo", "pln", "visao computacional"]
    },
    "ciberseguranca": {
        "topicos": ["ciberseguranca", "hacking etico", "firewalls", "criptografia", 
                   "seguranca da informacao", "teste de penetracao", "malware", "ransomware", 
                   "phishing", "engenharia social", "criptografia", "seguranca de rede",
                   "seguranca web", "seguranca movel", "hacking etico"]
    },
    "culinaria": {
        "topicos": ["culinaria", "receitas faceis", "sobremesas", "confeitaria", "pastelaria", 
                   "comida mexicana", "comida italiana", "comida espanhola", "bebidas", 
                   "cocktails", "cocktails", "harmonizacao", "vinho", "cerveja artesanal",
                   "gastronomia molecular", "culinaria vegetariana", "culinaria vegana"]
    },
    "esportes": {
        "topicos": ["esportes", "futebol", "basquetebol", "tenis", "natacao", "corrida", 
                   "fitness", "academia", "yoga", "pilates", "crossfit", "nutricao esportiva",
                   "treinamento funcional", "calistenia", "boxe", "artes marciais"]
    },
    "negocios": {
        "topicos": ["negocios", "empreendedorismo", "startups", "marketing digital", "vendas", 
                   "financas pessoais", "investimentos", "negocios online", "ecommerce", 
                   "logistica", "lideranca", "gestao empresarial", "recursos humanos",
                   "atendimento ao cliente", "branding", "seo", "sem", "email marketing"]
    }
}

# ============================================
# PREFIXOS
# ============================================
prefixos = [
    "como aprender", "como dominar", "guia completo de", "tutorial de", "curso de",
    "dominar", "entender", "praticar", "resolver problemas de", "exercicios de",
    "introducao a", "conceitos basicos de", "manual de", "teoria de",
    "exemplos de", "fundamentos de", "dicas para aprender", "recursos para estudar",
    "aulas de", "licoes de", "como melhorar em", "como usar"
]

# ============================================
# SUFIXOS
# ============================================
sufixos = [
    "iniciante", "intermediario", "avancado", "profissional", "completo",
    "facil", "rapido", "para iniciantes", "do zero", "passo a passo",
    "com exercicios", "online", "gratis", "certificado", "universitario",
    "para criancas", "para adultos", "intensivo", "pratico", "teorico"
]

# ============================================
# PERGUNTAS
# ============================================
perguntas = [
    "o que e", "como funciona", "para que serve", "onde aprender",
    "quando usar", "por que e importante", "quais sao os beneficios de",
    "quanto tempo leva para aprender", "o que preciso para estudar"
]

# ============================================
# GERACAO DE KEYWORDS
# ============================================
keywords = set()

print("🔄 Gerando keywords em portugues...")

# 1. Combinacoes com prefixos
for prefixo in prefixos:
    for cat_data in topicos.values():
        for topico in cat_data["topicos"]:
            keywords.add(f"{prefixo} {topico}")
        for topico_esp in cat_data.get("topicos_especiais", []):
            keywords.add(f"{prefixo} {topico_esp}")

# 2. Combinacoes com sufixos
for sufixo in sufixos:
    for cat_data in topicos.values():
        for topico in cat_data["topicos"][:15]:
            keywords.add(f"{topico} {sufixo}")
        for topico_esp in cat_data.get("topicos_especiais", []):
            keywords.add(f"{topico_esp} {sufixo}")

# 3. Perguntas
for pergunta in perguntas:
    for cat_data in topicos.values():
        for topico in cat_data["topicos"][:15]:
            keywords.add(f"{pergunta} {topico}")
        for topico_esp in cat_data.get("topicos_especiais", []):
            keywords.add(f"{pergunta} {topico_esp}")

# 4. Verbos + topico
verbos = ["aprender", "dominar", "praticar", "estudar", "compreender", "aplicar"]
for verbo in verbos:
    for cat_data in topicos.values():
        for topico in cat_data["topicos"][:15]:
            keywords.add(f"{verbo} {topico}")

# 5. Comparacoes
for cat_data in topicos.values():
    todos_topicos = cat_data["topicos"] + cat_data.get("topicos_especiais", [])
    if len(todos_topicos) >= 2:
        for _ in range(min(30, len(todos_topicos) * 3)):
            topico1, topico2 = random.sample(todos_topicos, 2)
            keywords.add(f"diferenca entre {topico1} e {topico2}")
            keywords.add(f"{topico1} vs {topico2}")
            keywords.add(f"comparacao {topico1} vs {topico2}")

# 6. Erros comuns
for cat_data in topicos.values():
    for topico in cat_data["topicos"][:10]:
        keywords.add(f"erros comuns em {topico}")
        keywords.add(f"como evitar erros em {topico}")
        keywords.add(f"solucao para problemas de {topico}")

# 7. Cursos e niveis
niveis = ["iniciante", "intermediario", "avancado", "profissional", "intensivo"]
for nivel in niveis:
    for cat_data in topicos.values():
        for topico in cat_data["topicos"][:12]:
            keywords.add(f"curso {nivel} de {topico}")
            keywords.add(f"aulas de {topico} nivel {nivel}")

# 8. Certificacoes e recursos
for cat_data in topicos.values():
    for topico in cat_data["topicos"][:10]:
        keywords.add(f"certificacao em {topico}")
        keywords.add(f"exame de {topico}")
        keywords.add(f"livros de {topico}")
        keywords.add(f"videos de {topico}")

# 9. Dicas
for cat_data in topicos.values():
    for topico in cat_data["topicos"][:10]:
        keywords.add(f"dicas para {topico}")
        keywords.add(f"conselhos para melhorar em {topico}")

# 10. Variacoes numericas
for i in range(1, 2000):
    cat_name = random.choice(list(topicos.keys()))
    topico = random.choice(topicos[cat_name]["topicos"])
    keywords.add(f"licao {i} de {topico}")
    keywords.add(f"capitulo {i} de {topico}")
    keywords.add(f"unidade {i} de {topico}")

# ============================================
# LIMITAR
# ============================================
keywords_lista = sorted(list(keywords))
random.shuffle(keywords_lista)

if len(keywords_lista) < QUANTIDADE_KEYWORDS:
    print(f"⚠ Apenas {len(keywords_lista)} keywords geradas. Repetindo algumas para atingir {QUANTIDADE_KEYWORDS}...")
    while len(keywords_lista) < QUANTIDADE_KEYWORDS:
        keywords_lista.extend(keywords_lista[:min(1000, QUANTIDADE_KEYWORDS - len(keywords_lista))])

keywords_final = keywords_lista[:QUANTIDADE_KEYWORDS]
random.shuffle(keywords_final)

# ============================================
# SALVAR
# ============================================
with open('keywords/pt.json', 'w', encoding='utf-8') as f:
    json.dump(keywords_final, f, indent=2, ensure_ascii=False)

# ============================================
# RELATORIO
# ============================================
print(f"\n✅ {len(keywords_final)} keywords geradas em portugues")
print(f"📁 Salvo em: keywords/pt.json")
print(f"\n📊 Visualizacao (30 primeiras keywords):")
for i, kw in enumerate(keywords_final[:30]):
    print(f"   {i+1}. {kw}")
