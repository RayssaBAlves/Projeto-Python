from fpdf import FPDF

class PDF(FPDF):

    def doc_title(self, label):
        self.set_font('helvetica', 'B', size=13)
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

pdf.doc_title("Desigualdade na educação")
pdf.doc_text("A desigualdade na educação é um desafio persistente que reflete profundas disparidades sociais e econômicas no país. Enquanto algumas regiões desfrutam de instituições educacionais de alta qualidade e acesso a recursos, outras enfrentam carências alarmantes. Essa discrepância se reflete em níveis de aprendizado desiguais, onde crianças de famílias mais abastadas tendem a obter uma educação de maior qualidade em comparação com aquelas de origens menos privilegiadas. A falta de infraestrutura adequada, professores bem preparados e materiais educacionais de qualidade contribuem para esse cenário desigual. Reduzir a desigualdade na educação requer esforços coordenados do governo, da sociedade civil e da comunidade educacional para garantir que todas as crianças tenham acesso a oportunidades educacionais de qualidade, independentemente de sua origem socioeconômica. Isso é fundamental para construir um Brasil mais justo e inclusivo.")

pdf.doc_title("Por que existe essa desigualdade?")
pdf.doc_text("A desigualdade na educação brasileira é profundamente influenciada por questões de renda, raça e marginalização de grupos vulneráveis. Famílias de baixa renda frequentemente enfrentam dificuldades para proporcionar um ambiente propício à educação de seus filhos, enquanto a falta de investimento público adequado contribui para a escassez de recursos nas escolas de comunidades mais carentes. Além disso, a questão racial desempenha um papel significativo, com estudantes negros e indígenas frequentemente enfrentando discriminação e falta de oportunidades educacionais. Essa marginalização é agravada pela perpetuação de estereótipos e preconceitos, que limitam o acesso a educação de qualidade para esses grupos. Para enfrentar essa desigualdade, é crucial adotar políticas que ataquem raízes profundas do problema, promovam inclusão racial, econômica e social, e assegurem a equidade na educação para todos os brasileiros.")

pdf.doc_title("O Distanciamento das Classes Desfavorecidas das Universidades Públicas")
pdf.doc_text("O acesso de pessoas das classes mais desfavorecidas às universidades públicas é prejudicado por diversas barreiras. A falta de recursos financeiros impede investimentos em educação de qualidade desde cedo. A escassez de suporte educacional em suas comunidades os deixa em desvantagem, sem acesso a programas de tutoria e orientação vocacional. A ausência de representatividade e exemplos inspiradores desmotiva aspirantes ao ensino superior. A distância geográfica e a limitada oferta de cursos em regiões menos privilegiadas dificultam a participação em processos seletivos. A concentração de instituições em áreas urbanas aumenta as barreiras logísticas e financeiras. A falta de acesso à informação sobre bolsas e políticas afirmativas cria um desconhecimento de oportunidades. A complexidade burocrática e falta de clareza nas políticas de inclusão também são obstáculos. Em resumo, o distanciamento resulta de um conjunto complexo de desafios, desde a infância até a falta de informação e representatividade, dificultando o acesso desses jovens às universidades públicas.")
pdf.ln(150)
pdf.doc_img("grafico_01.png", 80, 115, 100, 100)
pdf.ln(65)

pdf.doc_title("O Ensino a Distância como Resposta às Barreiras Sociais no Acesso ao Conhecimento")
pdf.doc_text("A crescente preferência dos estudantes pela modalidade de ensino a distância (EAD) reflete a busca por conciliação entre estudo e trabalho. A flexibilidade oferecida por cursos EAD permite que os alunos organizem seu tempo de estudo de acordo com suas obrigações profissionais, facilitando a gestão equilibrada entre ambas as atividades. Essa abordagem elimina barreiras geográficas, permitindo o acesso a cursos de instituições renomadas sem a necessidade de deslocamento físico. A tecnologia desempenha um papel crucial, oferecendo plataformas interativas e aulas gravadas que se adaptam à rotina agitada dos estudantes. Ao manterem empregos em tempo integral, os alunos podem garantir uma renda estável enquanto buscam avanço acadêmico. Essa opção não apenas facilita a busca por qualificação profissional, mas também democratiza o acesso ao ensino superior, tornando-o mais inclusivo e flexível. Essa tendência representa uma resposta positiva à necessidade contemporânea de equilíbrio entre aprimoramento acadêmico e carreira profissional.")
pdf.ln(65)
pdf.doc_img("ensino_01.png", 80, 115, 100, 100)
pdf.ln(150)
pdf.doc_text("A preferência pelo ensino a distância como forma de conciliar estudo e trabalho reflete a desigualdade no acesso à educação. As barreiras econômicas e geográficas que afetam as classes menos privilegiadas tornam o EAD uma alternativa mais acessível. Enquanto alguns têm a flexibilidade de escolher entre modalidades presenciais e online, outros recorrem ao EAD como uma solução prática diante das limitações impostas pela desigualdade social e econômica, ampliando as oportunidades educacionais para aqueles que enfrentam obstáculos tradicionais.")

pdf.doc_text("Em uma cidade diversa como o São Paulo, a desigualdade na educação é um desafio complexo e multifacetado, enraizado em questões de renda, raça e marginalização. Combater essa disparidade requer um compromisso contínuo com políticas públicas que garantam acesso igualitário a oportunidades educacionais de qualidade para todos os cidadãos, independentemente de sua origem socioeconômica ou racial. Além disso, a promoção da conscientização e da inclusão é essencial para desafiar estereótipos prejudiciais e preconceitos. A construção de uma sociedade mais justa e equitativa começa com uma educação que capacite a todos os brasileiros a atingir seu potencial máximo. É um desafio, mas um que o país deve enfrentar de forma determinada, pois somente assim poderemos criar um futuro mais igualitário e próspero para todos.")

pdf.output("projeto-python.pdf")