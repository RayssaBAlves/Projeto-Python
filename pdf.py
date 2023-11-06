from fpdf import FPDF

class PDF(FPDF):

    def doc_title(self, label):
        self.set_font('helvetica', 'B', size=16)
        self.cell(0, 10, label, 0, 1, 'L')
        self.ln()

    def doc_text(self, text):
        self.set_font('helvetica', '', size=12)
        self.multi_cell(0, 7, text)
        self.ln()

    def doc_img(self, img, x, y, w, h):
        self.image(img, x, y, w, h)

pdf = PDF()
pdf.add_page()

pdf.doc_title("Desigualdade na educação brasileira")
pdf.doc_text("A desigualdade na educação brasileira é um desafio persistente que reflete profundas disparidades sociais e econômicas no país. Enquanto algumas regiões desfrutam de instituições educacionais de alta qualidade e acesso a recursos, outras enfrentam carências alarmantes. Essa discrepância se reflete em níveis de aprendizado desiguais, onde crianças de famílias mais abastadas tendem a obter uma educação de maior qualidade em comparação com aquelas de origens menos privilegiadas. A falta de infraestrutura adequada, professores bem preparados e materiais educacionais de qualidade contribuem para esse cenário desigual. Reduzir a desigualdade na educação requer esforços coordenados do governo, da sociedade civil e da comunidade educacional para garantir que todas as crianças tenham acesso a oportunidades educacionais de qualidade, independentemente de sua origem socioeconômica. Isso é fundamental para construir um Brasil mais justo e inclusivo.")

pdf.doc_title("Por que existe essa desigualdade?")
pdf.doc_text("A desigualdade na educação brasileira é profundamente influenciada por questões de renda, raça e marginalização de grupos vulneráveis. Famílias de baixa renda frequentemente enfrentam dificuldades para proporcionar um ambiente propício à educação de seus filhos, enquanto a falta de investimento público adequado contribui para a escassez de recursos nas escolas de comunidades mais carentes. Além disso, a questão racial desempenha um papel significativo, com estudantes negros e indígenas frequentemente enfrentando discriminação e falta de oportunidades educacionais. Essa marginalização é agravada pela perpetuação de estereótipos e preconceitos, que limitam o acesso a educação de qualidade para esses grupos. Para enfrentar essa desigualdade, é crucial adotar políticas que ataquem raízes profundas do problema, promovam inclusão racial, econômica e social, e assegurem a equidade na educação para todos os brasileiros.")

pdf.doc_title("")
pdf.doc_text("")
#pdf.doc_img("grafico.jpg", 80, 115, 60, 60)

pdf.doc_title("")
pdf.doc_text("")
#pdf.doc_img("grafico.jpg", 80, 115, 60, 60)

pdf.doc_title("")
pdf.doc_text("Em um país diverso como o Brasil, a desigualdade na educação é um desafio complexo e multifacetado, enraizado em questões de renda, raça e marginalização. Combater essa disparidade requer um compromisso contínuo com políticas públicas que garantam acesso igualitário a oportunidades educacionais de qualidade para todos os cidadãos, independentemente de sua origem socioeconômica ou racial. Além disso, a promoção da conscientização e da inclusão é essencial para desafiar estereótipos prejudiciais e preconceitos. A construção de uma sociedade mais justa e equitativa começa com uma educação que capacite a todos os brasileiros a atingir seu potencial máximo. É um desafio, mas um que o país deve enfrentar de forma determinada, pois somente assim poderemos criar um futuro mais igualitário e próspero para todos. AAAA")

#pdf.doc_img("grafico.jpg", 80, 115, 60, 60)
pdf.ln(65)

#pdf.doc_text("Python é uma linguagem de propósito geral de alto nível, multiparadigma, suporta o paradigma orientado a objetos, imperativo, funcional e procedural. Possui tipagem dinâmica e uma de suas principais características é permitir a fácil leitura do código e exigir poucas linhas de código se comparado ao mesmo programa em outras linguagens.")

pdf.output("teste.pdf")