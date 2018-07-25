

class Automato:
    def __init__(self):
        self.simbolos = []
        self.estadoInicial = ""
        self.estadosFinais = []
        self.numEstados = 0
        self.estados = []


    def tipoAutomato(self, automato):

        for i in automato: # percorre o dicionario, sendo i as chaves
            for e in automato[i]: # percorre a lista referente a chave i
                # se tiver mais que um item na lista, significa q tem dois estados
                if ((len(e) > 1)): #or "" in e):  #caso for deterministico e tiver transiçao vazia e se tornar AFND, descomentar 'or "" in e):'

                    return "Nao deterministico" #entao eh nao determinisco

        return "Deterministico" #se terminar o loop sem encontrar uma lista(estado) com mais de 1 item, entao ele eh determinisco

    #metodo que gera as transçoes do autmato
    def geraAutomato(self, s):
        #declaraçao das listas
        estados = []
        transicoes = []
        aux = []

        for linha in s: #percorre a lista s
            estados.append(linha.split(":")[0]) # separa a string da linha antes e depois do ":". O conteudo antes de ":" eh inserido em estados
            rotas = linha.split(":")[1] # pega o conteudo depois de ":"
            rotas = rotas.split("-") #separa o conteudo por "-"
            #print(rotas)

            for i in range(len(rotas)):
                rotas0 = rotas[i].strip().split(",") #primeiro o metodo .strip retira os espacos. Apos o metodo .split(",") separa pelas "," e adiciona na variavel rotas0
            #rotas1 = rotas[1].strip().split(",") #rotas1 pega a string na posicao um e separa pelas ","
                h = rotas0[:] #h recebe todo o conteudo de rotas0
                aux.append(h) #insere h na lista aux
            #i= rotas1[:] #i recebe todo o conteudo de rotas1
            #aux.append(i) #insere i na lista aux
            j = aux[:] #j recebe todo o conteudo de aux
            #j = rotas[:]

            transicoes.append(j) #insere j na lista de transicoes
            del rotas0[:] #deleta todo o conteudo de rotas0
                #del rotas1[:] #deleta todo o conteudo de rotas1
            del aux[:] #deleta todo o conteudo de aux
            #del rotas[:]

        #print(transicoes)
        # com a lista dos estados e das transicoes eh feito um dicionario, com os estados como chave e as transicoes como valores
        automato = dict(zip(estados, transicoes))
        #print(automato)

        return automato

    #metodo que faz a verificaçao da sentenca
    def verificaSentenca(self, sentenca, automato, estInicial, estFinal, simbolos):
        sent = [] #declara a lista
        estAtual = estInicial #começa no estado inical
        sent.append(estAtual) #insere o estado inicial na lista
        '''o primeiro for percorre a sentena. O segundo pecorre a lista do dicionario referente ao estado atual do automato, comecando no estado inicial.
        Entao se pega a posiçao do item 'e' na lista de simbolos do automato. Em seguida faz a verificaçao, se a posiçao e a mesma que a do item 'a' na lista
        referente ao estado atual no dicionario de transiçoes. Se as posiçoes forem iguais, e adicionado o estado atual na lista sent e sai do loop do 
        for mais interno.
        '''

        for e in sentenca: #percorre a sentenca
            pos = simbolos.index(e) #pega a posicao de e na lista
            for a in automato[estAtual]: #q0

                '''
                if estAtual in estFinal:
                    #print("HJhj")
                    return sent
                '''


                if pos == automato[estAtual].index(a):
                    estAtual = a[0]
                    #print ("ad ", a, e)
                    sent.append(estAtual)
                    break

        return sent #retorna a lista sent
