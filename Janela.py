from tkinter import *
from Automato import *

class Janela():
    def __init__(self, master=None): #__init__ igual main() no java
        # primeiro container
        self.tamEntry = 20

        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer["padx"] = 30
        self.primeiroContainer.pack(side=LEFT)

        # segundo container
        self.segundoContainer = Frame(master)
        self.segundoContainer['pady'] = 5
        self.segundoContainer['padx'] = 20
        self.segundoContainer.pack(side=LEFT, fill=Y)

        #terceiro container
        self.terceiroContainer = Frame(master)
        self.terceiroContainer['pady'] = 5
        self.terceiroContainer['padx'] = 20
        self.terceiroContainer.pack(side=BOTTOM)

        #label geral do primeiro container
        self.labelPriCont = Label(self.primeiroContainer)
        self.labelPriCont.pack()

        lblTexto = Label(self.labelPriCont, text="Insira seu automato aqui: ")
        lblTexto.pack()
        #caixa de texto
        self.text = Text(self.labelPriCont, height=26, width=40)

        #scrollbar
        scroll = Scrollbar(self.labelPriCont, command=self.text.yview)
        #configura o text para inserir o scrollbar e o scrollbar para mostrar o texto da caixa de texto
        self.text.configure(yscrollcommand=scroll.set)
        #empacota o text
        self.text.pack(side=LEFT)
        #empacota o scroll
        scroll.pack(side=RIGHT, fill=Y)

        self.lblExemplo = Label(self.segundoContainer)
        self.lblExemplo.pack(anchor=N)
        textEmxemplo = Message(self.lblExemplo, text="Preencha a caixa de texto com o seu automato da seguinte forma:")
        textEmxemplo['width'] = 400
        textEmxemplo.pack(side=TOP, anchor=W)

        textEmxemplo2 = Message(self.lblExemplo, text="(Estado): Transiçao 1 - Transiçao 2")
        textEmxemplo2['width'] = 300
        textEmxemplo2.pack(side=TOP, anchor=W)

        textEmxemplo3 = Message(self.lblExemplo, text="Transiçao 1 equivale ao valor do primeiro simbolo, Transiçao 2 ao valor do segundo simbolo e assim por diante. Exemplo: ")
        textEmxemplo3['width'] = 400
        textEmxemplo3.pack(side=TOP, anchor=W)

        textEmxemplo4 = Message(self.lblExemplo, text="Simbolos: 0,1\n Automato:\nq0: q1 - q2\nq1: q0 - q2\nq2: q2 - q1")
        textEmxemplo4['width'] = 400
        textEmxemplo4.pack(side=TOP, anchor=W)

        textEmxemplo5 = Message(self.lblExemplo, text="Preencha os campos corretamente. O nao preenchimento, ou preechimento errado dos campos resultara em erro ou mau funcionamento!")
        textEmxemplo5['width'] = 400
        textEmxemplo5.pack(side=TOP, anchor=W)

        # label para colocar todos os labels do segundo container
        self.lblTdsLbl = Label(self.segundoContainer)
        self.lblTdsLbl.pack(side=LEFT, anchor=N)

        #Label dos Simbolos
        lblSimbolos = Label(self.lblTdsLbl, text="Simbolos: ", font=self.fontePadrao)
        lblSimbolos.pack()

        #Label dos estados
        lblEstados = Label(self.lblTdsLbl, text="Estados: ", font=self.fontePadrao)
        lblEstados.pack()

        # Label do numero de estados
        lblNumEstados = Label(self.lblTdsLbl, text="Numero de estados: ", font=self.fontePadrao)
        # lblNumEstados['pady'] = 5
        lblNumEstados.pack()

        # label do Estado Inicial
        lblEstInicial = Label(self.lblTdsLbl, text="Estado Inicial: ", font=self.fontePadrao)
        # lblEstInicial['pady'] = 5
        lblEstInicial.pack()

        # label do estado final
        lblEstFinal = Label(self.lblTdsLbl, text="Estado Final:  ", font=self.fontePadrao)
        # lblEstFinal['pady'] = 5
        lblEstFinal.pack()

        # label para colocar todos os entrys do segundo container
        self.lblTdsEntrys = Label(self.segundoContainer)
        self.lblTdsEntrys.pack(side=LEFT, anchor=N)

        #Entry simbolos
        self.entrySimbolos = Entry(self.lblTdsEntrys)
        self.entrySimbolos['width'] = self.tamEntry
        #self.entrySimbolos.insert(0,"0,1")
        self.entrySimbolos.pack()

        #Entry estados
        self.entryEstados = Entry(self.lblTdsEntrys)
        self.entryEstados['width'] = self.tamEntry
       # self.entryEstados.insert(0, "q0,q1,q2")
        self.entryEstados.pack()

        # Entry para colocar o numero de estados (Entry eh uma especie de JText do Java)
        self.entryNumEstados = Entry(self.lblTdsEntrys)
        self.entryNumEstados['width'] = self.tamEntry
        #self.entryNumEstados.insert(0,3)
        self.entryNumEstados.pack()

        # Entry do Estado Inicial
        self.entryEstInicial = Entry(self.lblTdsEntrys)
        self.entryEstInicial['width'] = self.tamEntry
        #self.entryEstInicial.insert(0,"q0")
        self.entryEstInicial.pack()

        # entry do estado final
        self.entryEstFinal = Entry(self.lblTdsEntrys)
        self.entryEstFinal['width'] = self.tamEntry
        #self.entryEstFinal.insert(0,"q2")
        self.entryEstFinal.pack()

        #botao conferir
        self.btnConferir = Button(self.segundoContainer, text="OK", font=self.fontePadrao)
        self.btnConferir['command'] = lambda : self.telaTransicoes()
        self.btnConferir['width'] = 10
        self.btnConferir.pack(side=BOTTOM, anchor=S) #empacota o botao


    #desempacota os pacotes. Os pacotes continuam existindo, porem invisiveis ao usuario
    def retiraInicio(self):
        self.labelPriCont.pack_forget()
        self.lblTdsEntrys.pack_forget()
        self.lblTdsLbl.pack_forget()
        self.btnConferir.pack_forget()
        self.lblExemplo.pack_forget()

    def telaInicial(self): #metodo para voltar a tela inicial
        #desempacota os pacotes da tela de transiçao e empacota novamente os pacotes da tela inicial
        self.lblTransicoes.pack_forget()
        self.lblInfos.pack_forget()
        self.btnVoltar.pack_forget()
        self.lblResultado.pack_forget()
        self.lblResultado2.pack_forget()
        self.lblTeste.pack_forget()
        root.geometry("800x400+200+200") #redimensiona a janela

        self.labelPriCont.pack()
        self.lblExemplo.pack(anchor=N)
        self.lblTdsLbl.pack(side=LEFT, anchor=N)
        self.lblTdsEntrys.pack(side=LEFT, anchor=N)

        #self.terceiroContainer.pack(side=BOTTOM)
        self.btnConferir.pack(side=BOTTOM, anchor=S)

    def separaLinhas(self): #metodo que separa as linhas do texto, cada linha e um item de uma lista
        #self.retiraInicio()
        texto = str(self.text.get("1.0", "end-1c")) #pega o texto da primeira linha ate a ultima escrita no Text
        texto = texto.splitlines() #sepada as linhas e adiciona em um vetor
        return texto

    def telaTransicoes(self): #tela onde mostra as informaçoes referentes ao automato
        self.retiraInicio() #retira a tela inicial
        #declaraçao das partes graficas
        self.lblResultado = Message(self.terceiroContainer)
        self.lblResultado2 = Label(self.terceiroContainer)
        self.primeiroContainer.pack(fill=Y)
        self.segundoContainer.pack(fill=Y)
        self.terceiroContainer.pack(fill=Y)
        #root.geometry("650x200+100+100") #redimenciona a janela

        #cria um objeto Automato e preenche os dados
        self.automato = Automato()
        self.automato.simbolos = self.entrySimbolos.get().split(",") #pega o texto do entry simbolos, separa pelas ',' e adiciona em uma lista(vetor)
        self.automato.estados = self.entryEstados.get().split(",") #pega o texto do entry estados e separa pelas ',' e adiociona em uma lista
        num = self.entryNumEstados.get()
        if num.isdigit(): #verifica se o conteudo do entry NumEstados e um digito
            self.automato.numEstados = int(num) #transforma para inteiro
        self.automato.estadoInicial = self.entryEstInicial.get() #estado inicial do automato
        self.automato.estadosFinais = self.entryEstFinal.get().split(",") #estados finais

        quantSimb = len(self.automato.simbolos) #quantidade de simbolos

        self.transicoes = self.automato.geraAutomato(self.separaLinhas()) #gera as transiçoes do automato

        #declaraçao das demais partes da interface grafica (tabela de transiçoes
        self.lblTransicoes = Label(self.primeiroContainer) #novo label, para colocar os demais itens
        self.lblTransicoes.pack()

        lblTabela = Label(self.lblTransicoes, text="Tabela de Transiçao:") #label com o texto informando a tabela de transiçao
        lblTabela.pack()
       # print(self.transicoes)
        #exibe as transiçoes na tela
        for i in self.automato.estados: #percorre os estados
            for e in range(quantSimb): #percorre os destinos de cada estado

                aux = self.transicoes[i]
                # preenche com espços vazios se o tamanho da lista aux for maior q a quantidade de simbolos
                #(caso haja um automato com algum estado com mais transiçoes do que outros)

               # print(self.automato.simbolos[e])
                #if quantSimb > len(aux):
                    #for x in range(quantSimb - len(aux)):
                       # aux.append("")

                self.mostraEstado(i, self.automato.simbolos[e], self.juntaString(aux[e])) #chama o metodo mostraEstado
        #declaraçao da parte grafica referente as informaçoes
        self.lblInfos = Label(self.segundoContainer)
        self.lblInfos.pack(anchor=N)

        #Declaraçao dos labels de cada informaçao, chamando o metodo retornando o resultado referente a cada informaçao
        lblTipoAut = Label(self.lblInfos, text="Tipo de Automato: {}".format(self.automato.tipoAutomato(self.transicoes)))
        lblTipoAut.pack(anchor=W)

        lblSimbolos = Label(self.lblInfos, text="Simbolos: {}".format(self.juntaString(self.automato.simbolos)))
        lblSimbolos.pack(anchor=W)

        lblNumEstados = Label(self.lblInfos, text="Numero de Estados: {}".format(self.automato.numEstados))
        lblNumEstados.pack(anchor=W)

        lblEstados = Label(self.lblInfos, text="Estados: {}".format(self.juntaString(self.automato.estados)))
        lblEstados.pack(anchor=W)

        lblEstadoInicial = Label(self.lblInfos, text="Estado Inicial: {}".format(self.automato.estadoInicial))
        lblEstadoInicial.pack(anchor=W)

        lblEstadoFinal = Label(self.lblInfos, text="Estado Final: {}".format(self.juntaString(self.automato.estadosFinais)))
        lblEstadoFinal.pack(anchor=W)

        #botao voltar
        self.btnVoltar = Button(self.primeiroContainer, text="Voltar")  # botao voltar
        self.btnVoltar['command'] = lambda: self.telaInicial() #chama o metodo telaInicial()
        self.btnVoltar.pack(side=BOTTOM)

        #empacota o terceiro container
        self.terceiroContainer.pack(side=LEFT)

        # cria um novo label para colocar os itens referentes ao teste da sentenca
        self.lblTeste = Label(self.terceiroContainer)
        self.lblTeste.pack(side=TOP)

        #se o automato for deterministo, mostra a tela para testar a sentença
        if (self.automato.tipoAutomato(self.transicoes) == "Deterministico"):
            lblSentenca = Label(self.lblTeste, text="Testar Sentença:")
            lblSentenca.pack(anchor=W)

            entrySentenca = Entry(self.lblTeste)
            entrySentenca['width'] = self.tamEntry
            entrySentenca.pack(side=LEFT)

            btnTestar = Button(self.lblTeste, text="Testar")

            btnTestar['command'] = lambda : self.formataRsultado(entrySentenca.get())
            btnTestar.pack()
        else: #se nao for deterministo, mostra uma mensagem informando que nao eh possivel testar a sentenca
            lblSentenca = Message(self.lblTeste, text="Automato nao deterministico, nao eh possivel testar sentença!")
            lblSentenca['width'] = 150
            lblSentenca.pack(anchor=W)

    #metodo para mostrar as transiçoes de cada estado na tabela de transiçoes. Recebe como parametro o estado, o valor e o destino
    def mostraEstado(self, estado, valor, destino):
        lbl0 = Label(self.lblTransicoes)
        lbl0.pack(anchor=W)

        lbl1 = Label(lbl0, text="({}, {}) = {}".format(estado, valor, destino))
        lbl1.pack(anchor=W)

    #concatena os itens de uma lista em uma string
    def juntaString(self, lista):
        a = ""
        for i in lista:
            a = a + i + ", "
        return a[:-2]
    #metodo para formatar o resultado obtido atraves do metodo verificaSentenca da classe Automato.
    def formataRsultado(self, senteca):
        #chama o metodo verificaSentenca, passando como parametro a sentenca, as transiçoes, o estado inicial, o estado final e os simbolos
        sent = self.automato.verificaSentenca(senteca, self.transicoes, self.automato.estadoInicial, self.automato.estadosFinais, self.automato.simbolos)

        resultado = "" #inicia uma nova string vazia
        #percorre a lista sent, concatenando os itens na string resultado + '->'
        for a in sent:
            resultado += a + " -> "

        resultado = resultado[:-4] #retira os quatro ultimos caracteres(' -> ')

        #preenchimento das informaçoes dos labels referentes ao resultado da sentenca
        self.lblResultado['text'] = resultado
        self.lblResultado['width'] = 200
        self.lblResultado.pack(anchor=W)

        self.lblResultado2['width'] = self.tamEntry

        #faz a verificao se a sentença eh aceita ou rejetida
        if (len(sent) != len(senteca) +1): #a lista sent deve ter o numero de itens igual o tamanho da sentença +1 (estado inicial)
            self.lblResultado2['text'] = "Sentença rejeitada"
        elif (sent[-1] in self.automato.estadosFinais): #o ultimo item da lista sent deve ser um estado final(lista dos estados finais)
            self.lblResultado2['text'] = "Sentença aceita"
        else: #se nao passar no teste, a sentença eh rejeitada
            self.lblResultado2['text'] = "Sentença rejeitada"

        self.lblResultado2.pack()

#inicializaçao da janela
root = Tk()
Janela(root)
root.title("Simulador de Automato Finito") #seta o titulo
#root.geometry("800x400+200+200")
root.mainloop() #inicia o loop
