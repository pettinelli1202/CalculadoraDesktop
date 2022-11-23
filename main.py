from tkinter import *
from tkinter import ttk

#cor
cor1 = '#89FFFB' #azul claro
cor2 = '#292929' #preto medio
cor3 = '#424242' #cinza medio
cor4 = '#FFA143' #laranja
cor5 = '#292725' #preto puro
cor6 = '#FFFFFF' #branco

#iniciando janela
janela = Tk()
janela.title('Calculadora')
janela.geometry('235x309')
janela.config(bg=cor1)
janela.resizable(0,0)
janela.config(cursor='hand2')

frame_tela = Frame(janela, width=235, height=50, bg=cor2)
frame_tela.grid(row=0, column=0)
frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

botao_valores = '' #variavel de todos valores botoes
valor_texto = StringVar() # label

def entrada_valores(evento):

    global botao_valores
    botao_valores = botao_valores + str(evento)
    valor_texto.set(botao_valores) #passando valor para tela

def calculo():
    global botao_valores
    resultado = eval(botao_valores)
    valor_texto.set(str(resultado))
    botao_valores = str(resultado)

def limpar_tela():
    global botao_valores
    botao_valores=''
    valor_texto.set('')

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Verdana 17'), bg=cor1, fg=cor5) #fg cor tela teclado
app_label.place(x=0, y=0)


def entrar_cursor(event): #função enter cursor do botão
    b_igual.config(bg=cor4)

def sair_cursor(event): #funcao leave cursor do botão
    b_igual.config(bg=cor3)

b_cle = Button(frame_corpo, command=limpar_tela, text='C', width= 11, height=2, bg=cor3, fg=cor6, font=('Verdana 13'), relief=RAISED, overrelief=RIDGE)
b_cle.place(x=0, y=0)
b_por = Button(frame_corpo, command=lambda:entrada_valores('%'), text='%', width= 5, height=2, bg=cor3, fg=cor6, font=('Verdana 13'), relief=RAISED, overrelief=RIDGE)
b_por.place(x=118, y=0)
b_div = Button(frame_corpo, command=lambda:entrada_valores('/'), text='/', width= 5, height=2, bg=cor3, fg=cor6, font=('Verdana 13 bold'), relief=RAISED, overrelief=RIDGE)
b_div.place(x=177, y=0)

b_set = Button(frame_corpo, command=lambda:entrada_valores('7'), text='7', width= 5, height=2, bg=cor2,fg=cor6, font=('Verdana 13'), relief=RAISED, overrelief=RIDGE)
b_set.place(x=0, y=52)
b_oit = Button(frame_corpo, command=lambda:entrada_valores('8'), text='8', width= 5, height=2, bg=cor2,fg=cor6, font=('Verdana 13'), relief=RAISED, overrelief=RIDGE)
b_oit.place(x=59, y=52)
b_nov = Button(frame_corpo, command=lambda:entrada_valores('9'), text='9', width= 5, height=2, bg=cor2,fg=cor6, font=('Verdana 13'), relief=RAISED, overrelief=RIDGE)
b_nov.place(x=118, y=52)
b_mult = Button(frame_corpo, command=lambda:entrada_valores('*'), text='*', width= 5, height=2, bg=cor3,fg=cor6, font=('Verdana 13 bold'), relief=RAISED, overrelief=RIDGE)
b_mult.place(x=177, y=52)

b_qua = Button(frame_corpo, command=lambda:entrada_valores('4'), text='4', width= 5, height=2, bg=cor2,fg=cor6, font=('Verdana 13'), relief=RAISED, overrelief=RIDGE)
b_qua.place(x=0, y=104)
b_cin = Button(frame_corpo, command=lambda:entrada_valores('5'), text='5', width= 5, height=2, bg=cor2,fg=cor6, font=('Verdana 13'), relief=RAISED, overrelief=RIDGE)
b_cin.place(x=59, y=104)
b_sei = Button(frame_corpo, command=lambda:entrada_valores('6'), text='6', width= 5, height=2, bg=cor2,fg=cor6, font=('Verdana 13'), relief=RAISED, overrelief=RIDGE)
b_sei.place(x=118, y=104)
b_sub = Button(frame_corpo, command=lambda:entrada_valores('-'), text='-', width= 5, height=2, bg=cor3, fg=cor6, font=('Verdana 13 bold'), relief=RAISED, overrelief=RIDGE)
b_sub.place(x=177, y=104)

b_um = Button(frame_corpo, command=lambda:entrada_valores('1'), text='1', width= 5, height=2, bg=cor2,fg=cor6, font=('Verdana 13'), relief=RAISED, overrelief=RIDGE)
b_um.place(x=0, y=156)
b_dois = Button(frame_corpo, command=lambda:entrada_valores('2'), text='2', width= 5, height=2, bg=cor2,fg=cor6, font=('Verdana 13'), relief=RAISED, overrelief=RIDGE)
b_dois.place(x=59, y=156)
b_tres = Button(frame_corpo, command=lambda:entrada_valores('3'), text='3', width= 5, height=2, bg=cor2,fg=cor6, font=('Verdana 13'), relief=RAISED, overrelief=RIDGE)
b_tres.place(x=118, y=156)
b_adic = Button(frame_corpo, command=lambda:entrada_valores('+'), text='+', width= 5, height=2, bg=cor3, fg=cor6, font=('Verdana 13 bold'), relief=RAISED, overrelief=RIDGE)
b_adic.place(x=177, y=156)

b_zero = Button(frame_corpo, command=lambda:entrada_valores('0'), text='0', width= 11, height=2, bg=cor2,fg=cor6, font=('Verdana 13'), relief=RAISED, overrelief=RIDGE)
b_zero.place(x=0, y=205)
b_pont = Button(frame_corpo, command=lambda:entrada_valores('.'), text='.', width= 5, height=2, bg=cor2,fg=cor6, font=('Verdana 13'), relief=RAISED, overrelief=RIDGE)
b_pont.place(x=118, y=205)
b_igual = Button(frame_corpo, command=calculo, text='=', width= 5, height=2, bg=cor3, fg=cor6, font=('Verdana 13 bold'), relief=RAISED, overrelief=RIDGE)
b_igual.place(x=177, y=205)
b_igual.bind('<Enter>', entrar_cursor)
b_igual.bind('<Leave>', sair_cursor)

janela.mainloop()