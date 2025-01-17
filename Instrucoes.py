from tkinter import*#para toda a interface 
import PIL as p
import PIL.ImageTk as ptk

class Janela_Instrucoes():
    def __init__(self): 
        self.count=1
        self.instrucoes = Toplevel()  # é uma instancia de tk se a janela root for fechada ela tambpem será fechada
        #self.instrucoes.resizable(False, False) # ampliar a janela
        #self.instrucoes.geometry('700x340')
        self.instrucoes.title('Instruções')
        self.instrucoes['bg'] = '#86cee4'
        self.L1=Label(self.instrucoes, text='1/10', font=('helvetica', 20), fg='black',bg= '#f29cc2'  )
        self.L1.pack()
        self.L2=Label(self.instrucoes, font=('helvetica', 16), text='Olá, este programa detecta qual mão você tem a intenção de movimentar,\n através do sinal do seu sinal cerebral! \n Para entender certinho como utilizar este programa, clique em "Próximo" \n e siga as instruções atentamente!',fg='black',bg= '#86cee4',width=70,height=15 )
        self.L2.pack()
        Button(self.instrucoes, text='Próximo', width=20, bg='#f29cc2',fg='black',command=self.Incremento).pack(side=RIGHT)
        Button(self.instrucoes, text='Anterior', width=20, bg='#f29cc2',fg='black',command=self.Decremento).pack(side=LEFT)
        self.BEEG=Button(self.instrucoes, text='', width=20, relief=FLAT, bg='#86cee4',fg='black',command=self.EletrodosEEG)
        self.BEEG.pack()
        self.instrucoes.mainloop()
                
    def EletrodosEEG(self):
        self.instrucao3 = Toplevel()
        self.instrucao3.title('Posicionamento dos Eletrodos')
        self.pic = 'Imagens/EEG 10-20.png'
        self.pic1 = p.Image.open(self.pic)
        self.photo = ptk.PhotoImage(self.pic1)
        self.instrucao3.resizable(False, False)
        labelImage = Label(self.instrucao3, image=self.photo)
        labelImage.grid(row=0, column=0)
        
        
    def Comparacao(self):
        self.L1['text'] = '{}/10'.format(self.count)
        if(self.count==1):
            self.L2['text'] = 'Olá, este programa detecta qual mão você tem a intenção de movimentar,\n através do sinal do seu sinal cerebral! \n Para entender certinho como utilizar este programa, clique em "Próximo" \n e siga as instruções atentamente!'
        elif (self.count==2):
            self.L2['text']='Conecte o microcontrolador a entrada USB do computador.'
            self.BEEG['relief']=FLAT
            self.BEEG['bg']='#86cee4'
            self.BEEG['text']=''
        elif (self.count==3):
            self.L2['text']='Recomenda-se que o usuário abra a imagem do posicionamento \n dos eletrodos de EEG clicando o botão amarelo \n\n\n\n Coloque os três eletrodos do sinal de intetesse (CZ, C3 e C4) \n Coloque o eletrodo de redução do artefato (Fz) \n Coloque o eletrodo de referência do circuito em uma das orelhas (A1 ou A2)'
            self.BEEG['relief']=RAISED
            self.BEEG['bg']='#f8ef83'
            self.BEEG['text']='Eletrodos EEG'
        elif (self.count==4):
            self.L2['text']='Caso você queira criar um Data Set para treinar a inteligência artificial \n ou visualizar um Data Set previmente preparado,\n clique em "Data Set" no menu principal e siga as instruções a seguir'
            self.BEEG['relief']=FLAT
            self.BEEG['bg']='#86cee4'
            self.BEEG['text']=''
        elif (self.count==5):
            self.L2['text']='"Data Set":\n\n Para criar seu próprio Data Set, selecione "Iniciar" \n Caso seja necessário parar a execução do treinamento, selecione "Parar" \n Para visualizar o sinal eletroencefalográfico do Data Set, \n preencha o número do usuário que vai de 1 a 9 e a sessão que vai de 1 a 3, \n e selecione "Abrir EEG Data Set"\n'
        elif (self.count==6):
            self.L2['text']='Para visualizar qual mão o usuário teve a intenção de mexer,\n vá em "Operação" no menu principal e siga as instruções.'
        elif (self.count==7):
            self.L2['text']='"Operação Treinamento":\n\n Antes de iniciar a predição é necessário treinar a Inteligência Artificial \n Informe o primeiro e o ultimo sujeito \n que irão compor o intervalor dos dados para o treinamento,\n é possível selecionar apenas um indivíduo escrevendo o seu número nos dois campos \n Caso deseja-se remover o artefato do EOG do sinal, \n marque a checkbox \n Pressione "Treinar IA" para treinar a Inteligência Artificial'
        elif (self.count==8):
            self.L2['text']='"Operação Predição":\n\n Para iniciar as predições, selecione "Iniciar" \n Caso seja necessário parar a execução da predição, selecione "Parar"\n OBS: A luz verde indica que o algoritmo acertou a predição do movimento,\n já a luz vermalha indica que ele errou \n A taxa de acerto mostra quantas predições foram feitas corretamente \n Para visualizar o sinal eletroencefalográfico da inteção de movimento, selecione "Abrir EEG"'
        elif (self.count==9):
            self.L2['text']='Para fazer a conexão do microcontrolador,\n vá em "Conectar Hardware" no menu principal e siga as instruções.'
        elif (self.count==10):  
            self.L2['text']='"Conexão Hardware":\n\n Informe o nome da porta na qual o microcontrlador foi conectado,\n exemplo: "COM3","COM4" e pressione "Iniciar Conexão"\n Para iniciar a leitura dos dados, selecione "Ler Dados"\n Caso seja necessário encerrar a leitura dos dados,\n selecione "Encerrar Leitura"\n Caso deseja-se ler os sinais dos 3 canais do EEG presentes no microcontrolador,\n pressione "Plotar EEG do uC"\n Além disso, é possivel visualizar em tempo real a leitura do sinal analógico \n digitalizado em 10 bits do potenciômetro, no canto inferior direito'
        
    def Incremento(self):
        if ((self.count >=1 )& (self.count <10)):
            self.count=self.count+1
            self.Comparacao()
        
    def Decremento(self):
        if ((self.count >1) & (self.count <=10)):
            self.count=self.count-1
            self.Comparacao()