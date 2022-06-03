from random import shuffle

gabarito = ("A", "A", "A", "A", "D", "A", "E", "D", "B", "E", "D", "B", "C", "C", "E", "B", "A", "A", "B", "E", "D", "C", "D", "C", "C")
respostas = []
pontuacao = 0
ordem_questoes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
shuffle(ordem_questoes)
 
# Função que exibirá a pergunta e suas alternativas, e solicitará e registrará a resposta do jogador na lista 'respostas'
def executa_questao(q):
    # Exibe a questão e as alternativas com base no dicionário 'questoes'
    print(questoes[q]["questao"])
    # Solicita o input e converte a letra da resposta para maiúscula, para posterior comparação com a tupla 'gabarito'
    resposta = input("Insira sua resposta: ").upper()
    # Valida se a resposta é uma das cinco alternativas, e, caso não seja, reitera a solicitação de input
    while resposta != "A" and resposta != "B" and resposta != "C" and resposta != "D" and resposta != "E":
        resposta = input("Resposta inválida. Insira apenas a letra da alternativa escolhida: ").upper()
    respostas.append(resposta)
    # Compara a resposta com o gabarito: caso o jogador tenha acertado, exibe uma mensagem e soma a pontuação recebida na pergunta à variável global 'pontuacao'; do contrário, exibe uma mensagem informando que o jogador errou
    # É subtraído 1 do valor de 'q', pois as questões começam no valor 1, e a tupla 'gabarito' inicia no index 0
    if resposta == gabarito[q-1]:
        print("Você acertou!\n")
        global pontuacao
        pontuacao += questoes[q]["pontuacao"]
    else:
        print(f"\nVocê errou! A alternativa correta é {gabarito[q-1]}.\n")
    # Exibe a explicação da resposta da pergunta, obtida do dicionário 'questoes'
    print(questoes[q]["explicacao"])
 
# Função que mostrará os resultados (pontuação e categoria do jogador)
def mostra_resultados():
    print(f"Seu total de pontos foi {pontuacao} de 50.\n")
    if pontuacao == 50:
        print("Parabéns! Você acertou todas as perguntas!")
    elif 37 <= pontuacao < 50:
        print("Muito bem! Você atingiu 75% da pontuação máxima! Tente novamente para acertar todas!")
    elif 25 <= pontuacao < 37:
        print("Quase lá! Você ultrapassou 50% da pontuação máxima! Quero ver acertar a outra metade agora!")
    elif 12 <= pontuacao < 25:
        print("Você chegou a 25% da pontuação máxima. Tente novamente!")
    elif 0 < pontuacao < 12:
        print("Hmmm, acho que você não conhece muito da Marvel. Você terminou com menos de 25% da pontuação máxima. Tente outra vez!")
    elif pontuacao == 0:
        print("Eita, você conseguiu errar todas as perguntas. É melhor pesquisar um pouco antes de tentar o quiz novamente. :D")
    
# Dicionário criado para armazenar os subdicionários de cada questão, que possuem chaves para o texto da questão e suas alternativas, a explicação que será exibida após a resposta, e a pontuação equivalente à questão
questoes = {1: {"questao": "Em que ano a Marvel foi criada?\n\na) 1939 \nb) 1930 \nc) 1942 \nd) 1950 \ne) 1960 \n", "explicacao": "A Marvel Entertainment foi criada em 1939, nos Estados Unidos, por Martin Goodman. A primeira revista em quadrinhos da companhia foi a Marvel Comics, lançada em 31 de agosto de 1939.\n", "pontuacao": 3},
            2: {"questao": "Antigamente, como a Marvel se chamava?\n\na) Timely Comics \nb) Marvel Super-Heroes \nc) Timolye Comics \nd) Marvely Comics \ne) Marvel Super-Heroes Studio \n", "explicacao": "A editora inicialmente não se chamava Marvel, tudo começou com a editora Timely Comics, criada em 1939.\n", "pontuacao": 2},
            3: {"questao": "Qual foi o primeiro Herói criado pela Marvel? \n\na) Tocha Humana e Namor \nb) Capitão América \nc) Mulher Invisível \nd) Homem de Ferro \ne) Hulk \n", "explicacao": "Os primeiros heróis da Marvel/Timely foram o Namor e o Tocha-Humana (o Androide, não o membro do Quarteto Fantástico). Ambos fizeram suas estreias na revista Marvel Comics #1.\n", "pontuacao": 2},
            4: {"questao": "A Fase 1 dos filmes da Marvel se refere a qual ano? \n\na) 2008 a 2012 \nb) 2013 a 2015 \nc) 2016 a 2019 \nd) 2021 a 2023 \ne) Nenhuma das anteriores \n", "explicacao": "O Marvel Studios divide seu universo cinematográfico em etapas, começando a sua Fase 1 em 2008, com Homem de Ferro e terminando em 2012, com o primeiro Vingadores.\n", "pontuacao": 2},
            5: {"questao": "Qual é o nome da armadura criado pelo Tony Stark para derrotar o Hulk?\n\na) Stop-Hulk \nb) Mark Hulk \nc) Hulk Smash \nd) HulkBuster \ne) A armadura não existe \n", "explicacao": "O Mark 44 (XLIV), também conhecido como \"Hulkbuster\", é uma Armadura Modular Extra Pesada criada por Tony Stark e Bruce Banner como uma proteção de segurança no caso de um descontrole incontrolável do Hulk.A armadura foi destaque em Vingadores: Era de Ultron.\n", "pontuacao": 1},
            6: {"questao": "Qual o nome do martelo do Thor?\n\na) Mjölnir \nb) Mijönyer \nc) Mijonier \nd) Mionir \ne) Meonir \n", "explicacao": "O martelo do Thor é conhecido como Mjölnir. No Universo Cinematográfico da Marvel, a origem de Mjölnir nunca foi bem explorada, mas sua aparência e suas utilidades eram bem similares as das HQs. Uma diferença entre o martelo do Thor da MCU e dos quadrinhos, seria que ele não é indestrutível, e a prova disso é que ele foi destroçado sem nenhuma cerimônia por Hela, a Deusa da Morte em Thor: Ragnarok (2017).\n", "pontuacao": 1},
            7: {"questao": "Qual o filme da Marvel que marca o final da Fase 1?\n\na) O Incrível Hulk \nb) Homem de Ferro \nc) Capitão América: O Primeiro Vingador  \nd) Homem de Ferro 2 \ne) Os Vingadores \n", "explicacao": "Os Vingadores (2012), foi um filme marcante para finalizar a fase 1 da MCU. Juntando todos os principais heróis da Marvel em um único filme, deu o resultado de uma bilheteria de US$ 1,5 bilhão.\n", "pontuacao": 2},
            8: {"questao": "Qual é o ator que interpreta o Incrível Hulk?\n\na) Robert Downey Jr \nb) Chris Hemsworth \nc) Jeremy Renner \nd) Mark Ruffalo \ne) Tom Hiddleston \n", "explicacao": "Mark Ruffalo fez um Bruce Banner tão adorado que o povo esquece como foi Edward Norton quem viveu o personagem em O Incrível Hulk (2008). A substituição foi devido a uma má relação entre os diretores e o presidente da Marvel, Kevin Feige com o ator Edward Norton.\n", "pontuacao": 2},
            9: {"questao": "O que será explorado na Fase 4 da Marvel?\n\na) A história do Doutor Estranho \nb) O conceito de Multiverso \nc) A construção de um novo esquadrão dos Vingadores \nd) A aparição de dois novos líderes \ne) O mundo afetado após o Thanos \n", "explicacao": "O Multiverso é a possibilidade de que várias dimensões paralelas coexistem, cada uma com sua variante. O conceito é muito utilizado nos quadrinhos, que explora diversos universos. A Marvel nas HQs, por exemplo, tem a Terra-616, que é o universo primário, onde a maioria de suas histórias acontecem. Assim, eles criaram diversos outros universos alternativos, como o Ultimate (Terra-1610) onde surgiu o personagem Miles Morales do filme Homem-Aranha no Aranhaverso (2019). \n", "pontuacao": 1},
            10: {"questao": "Qual foi a primeira série apresentada pela Marvel que faz parte da Fase 4?\n\na) Hawkeye \nb) Moon Knight \nc) O Falcão e o Soldado Invernal \nd) She-Hulk \ne) WandaVision \n", "explicacao": "A poderosa Feiticeira Escarlate, foi a eleita para dar início ao ambicioso plano da Marvel de expandir seu universo, com a sua série WandaVision (2021).\n", "pontuacao": 2},
            11: {"questao": "Quantas Joias do Infinito existem?\n\na) 10 \nb) 5 \nc) 7 \nd) 6 \ne) 8 \n", "explicacao": "No Universo Cinematográfico Marvel, as Joias do Infinito são referidas como as Pedras do Infinito. Atualmente, apenas uma das seis Joias do Infinito ainda falta ser introduzida - as outras são o Tesseract, o Éter, o Orbe, a Pedra da Mente e o Olho de Agamotto.\n", "pontuacao": 3},
            12: {"questao": "Qual o personagem que foi criado por uma IA e foi ativado por uma Joia do Infinito?\n\na) Ultron \nb) Visão \nc) Inteligência Suprema Kree \nd) Falange \ne) Nenhuma das anteriores \n", "explicacao": "Visão foi um androide nascido do resultado de um corpo sintético de Vibranium criado por Ultron e Helen Cho, ativado pela Joia da Mente. Originalmente sendo um corpo perfeito de Ultron, o corpo foi roubado pelos Vingadores e enviado para Tony Stark e Bruce Banner, que colocaram os remanescentes da I.A. de Tony, J.A.R.V.I.S., dentro deste corpo.\n", "pontuacao": 1},
            13: {"questao": "Em que ano foi lançado o primeiro filme do MCU?\n\na) 2007 \nb) 2010 \nc) 2008 \nd) 2009 \ne) 2006 \n", "explicacao": "O filme foi Homem de Ferro (2008).\n", "pontuacao": 3},
            14: {"questao": "Qual foi o primeiro filme em que o vilão Thanos apareceu?\n\na) Vingadores: Era de Ultron \nb) Vingadores: Guerra Infinita \nc) Os Vingadores \nd) Vingadores Ultimato \ne) Eternos \n", "explicacao": "Thanos aparece pela primeira vez em uma cena pós-créditos de Os Vingadores, onde ele é revelado como o mestre do Outro e benfeitor de Loki, que o enviou à Terra para obtenha o Tesseract.\n", "pontuacao": 2},
            15: {"questao": "Qual é o reino do Pantera Negra?\n\na) Asgard \nb) Ego \nc) Xandar \nd) Sakaar\ne) Wakanda \n", "explicacao": "Wakanda, oficialmente conhecido como Reino de Wakanda, é um pequeno país isolacionista localizado na África, cercado por cadeias de montanhas e uma selva espessa. É uma das nações mais tecnologicamente avançadas da Terra, conhecida por seus ricos depósitos do elemento vibranium.\n", "pontuacao": 1},
            16: {"questao": "Como Nick Fury perdeu o olho?\n\na) Durante uma guerra \nb) Arranhão de gato \nc) Ataque do Loki \nd) Diabetes \ne) Nenhuma das anteriores \n", "explicacao": "Ainda jovem, ele mostra desde o início do filme alguns cortes no olho esquerdo, contudo, o que o fez mesmo perder a visão no MCU foi um ataque do gato Goose — que, na verdade, é um perigoso alienígena da raça Flerken.\n", "pontuacao": 3},
            17: {"questao": "Quais foram os dois heróis apresentados no filme Capitão América: Guerra Civil?\n\na) Homem-Aranha e Pantera Negra \nb) Homem-Aranha e Visão \nc) Homem-Formiga e Visão \nd) Pantera Negra e Homem Formiga \ne) Soldado Invernal e Pantera Negra \n", "explicacao": "Os super-heróis que estreiaram na MCU foram o Homem-Aranha e o Pantera Negra. \n", "pontuacao": 1},
            18: {"questao": "Em quais anos foram lançados os filmes dos Vingadores?\n\na) 2012, 2015, 2018 e 2019 \nb) 2011, 2015, 2019 e 2019 \nc) 2010, 2014, 2018 e 2019 \nd) 2012, 2014, 2017 e 2019\ne) 2011, 2013, 2015 e 2018 \n", "explicacao": "Os Vingadores (2012), Vingadores: Era de Ultron (2015), Vingadores: Guerra Infinita (2018), Vingadores: Ultimato (2019).\n", "pontuacao": 3},
            19: {"questao": "Quais foram os anos que a Marvel lançou apenas 1 filme?\n\na) 2008 e 2010 \nb) 2010 e 2012 \nc) 2010 e 2015 \nd) 2013 e 2014 \ne) 2012 e 2015 \n", "explicacao": "Homem de Ferro 2 (2010) e Os Vingadores (2012).\n", "pontuacao": 3},
            20: {"questao": "Quais dos 6 Vingadores não têm poderes?\n\na) Gavião Arqueiro, Homem de Ferro e Thor \nb) Homem de Ferro, Hulk e Thor \nc) Viúva Negra, Gavião Arqueiro e Capitão América \nd) Viúva Negra, Thor e Gavião Arqueiro \ne) Homem de Ferro, Gavião Arqueiro e Viúva Negra \n", "explicacao": "Homem de Ferro depende de sua armadura, Gavião Arqueiro de sua mira e Viúva Negra de sua habilidade de combate.\n", "pontuacao": 1},
            21: {"questao": "No filme Vingadores: Ultimato, quem teve que morrer para obter a Joia da Alma?\n\na) Gavião Arqueiro \nb) Capitão América \nc) Homem de Ferro \nd) Viúva Negra \ne) Ninguém \n", "explicacao": "Gavião Arqueiro e Viúva Negra vão para Vormir pegar a Joia da Alma, mas percebem que seria necessário um sacrifício para conseguir o artefato. Natasha se voluntariou, mesmo lutando contra a tentativa de Clint Barton ir no lugar dela e acabou morrendo no MCU.\n", "pontuacao": 2},
            22: {"questao": "Sobre que cidade Gavião Arqueiro e Viúva Negra costumam relembrar?\n\na) Praga \nb) Istambul \nc) Budapeste \nd) Nova Iorque \ne) Berlim \n", "explicacao": "A Viúva Negra revela em seu filme Viúva Negra (2021), que Gavião Arqueiro esteve com ela na missão de armar as bombas para matar Dreykov, que comandava a Sala Vermelha, em Budapeste. \n", "pontuacao": 3},
            23: {"questao": "Onde Lady Sif e Volstagg guardam a Joia da Realidade depois que os Elfos Negros tentam roubá-la? \n\na) Vormir \nb) Um cofre em Asgard \nc) Dentro da espada de Sif \nd) Deixaram com o Colecionador \ne) Nenhuma das anteriores \n", "explicacao": "Ela apareceu em Thor: Mundo Sombrio quando Lady Sif e Volstagg a levaram, já em forma de pedra, para o Colecionador guardar. Eles até explicaram que fizeram isso porque seria imprudente manter mais uma Joia no cofre de Odin. Entretanto, em Guardiões da Galáxia, a casa do Colecionador explodiu completamente e, desde então, ela não voltou a aparecer.\n", "pontuacao": 3},
            24: {"questao": "Qual era a profissão do Doutor Estranho antes de se tornar herói?\n\na) Cardiologista \nb) Terapeuta \nc) Neurocirurgião \nd) Cirurgião Plástico \ne) Psicólogo \n", "explicacao": "Anteriormente um brilhante, mas arrogante, neurocirurgião, Strange sofreu um acidente de caro, fazendo com que sua mãos fossem severamente danificadas. Quando a medicina ocidental falhou com ele, Strange embarcou em uma jornada que o levou até Kamar-Taj, onde Strange descobriu a magia e as dimensões alternativas sendo treinado pela Anciã.\n", "pontuacao": 2},
            25: {"questao": "Quais são os integrantes originais dos Vingadores?\n\na) Homem de Ferro, Capitão América, Thor, Hulk, Homem-Aranha e Viúva Negra \nb) Homem de Ferro, Capitão América, Thor, Hulk, Feiticeira Escarlate e Viúva Negra \nc) Homem de Ferro, Capitão América, Thor, Hulk, Viúva Negra e Gavião Arqueiro \nd) Homem de Ferro, Capitão América, Hulk, Agatha Harkness e Doutor Estranho \ne) Homem de Ferro, Capitão América, Thor e Hulk \n", "explicacao": "No filme Os Vingadores, de 2012, os protagonistas introduzidos ao longo dos cinco filmes anteriores se juntam em uma única equipe para enfrentar uma ameaça maior. Os filmes são Homem de Ferro (2008), O Incrível Hulk (2008), Homem de Ferro 2 (2010), Thor (2011) e Capitão América: O Primeiro Vingador (2011). Além dos personagens centrais, a Viúva Negra e o Gavião Arqueiro aparecem como personagens secundários em Homem de Ferro 2 e Thor, respectivamente.\n", "pontuacao": 1}
}
 
# For-loop para execução da função 'executa_questao' no mesmo número de questões disponíveis
# O argumento passado é baseado na lista 'ordem_questoes', que tornará a ordem das questões aleatória
for questao in range(len(questoes)):
    executa_questao(ordem_questoes[questao])
 
mostra_resultados()