from tkinter import *

root = Tk()
root.title('calculadora')
root.geometry('408x355')
root.maxsize(408,355)
root.minsize(408,355)

numero1 = ""
numero2 = ""
divisao = FALSE
multiplica = FALSE
subtracao = FALSE
Soma = FALSE

root.configure(background= "#000080")
entrada = Entry(root,width=15,borderwidth=4,relief=FLAT, foreground="#FFFFFF",bg="#000000", font=('futura', 25,'bold'),justify=CENTER)
entrada.grid(row=0,column=0,columnspan=4,pady=2)

#funções da calculadora

def botao_click(num):
    entrada.insert(END,num)
    
def botao_divisao():
    global numero1
    global divisao
    divisao = TRUE
    numero1 = entrada.get()
    entrada.delete(0,END)
    
def botao_multiplica():
     global numero1
     global multiplica
     multiplica = TRUE
     numero1 = entrada.get()
     entrada.delete(0,END)
     
def botao_subtracao():
     global numero1
     global subtracao
     subtracao= TRUE
     numero1 = entrada.get()
     entrada.delete(0,END)
     
def botao_soma():
     global numero1
     global soma
     soma= TRUE
     numero1 = entrada.get()
     entrada.delete(0,END)
     
def botao_clear():
    entrada.delete(0,END)
    
def botao_resposta():
    global subtracao
    global soma
    global multiplica
    global divisao
    numero2 = entrada.get()
    entrada.delete(0,END)
    
    if soma == TRUE:
        entrada.insert(0, int(numero1) + int(numero2))
        soma = FALSE
        
    if multiplica == TRUE:
        entrada.insert(0, int(numero1) * int(numero2))
        multiplica = FALSE
    if subtracao == TRUE:
        entrada.insert(0, int(numero1) - int(numero2))
        subtracao= FALSE
        
    if divisao ==TRUE:
        entrada.insert(0,int(numero1) / int(numero2))
        divisao = FALSE
        
divisao = Button(root,
                 text="/",
                 padx=40,
                 pady=20,
                 command=botao_divisao,
                 fg='#FFFFFF',
                 activeforeground="#FFFFFF",
                 bg='#000080',
                 activebackground='#0000FF',
                 relief=FLAT,
                 font=('futura',12,'bold')
)
divisao.grid(row=0,column=4)

#1º fileira

um = Button(root,
                 text="1",
                 padx=40,
                 pady=20,
                 command=lambda: botao_click(1),
                 fg='#FFFFFF',
                 activeforeground="#FFFFFF",
                 bg='#000080',
                 activebackground='#0000FF',
                 relief=FLAT,
                 font=('futura',12,'bold')
)
um.grid(row=3,column=1)
dois = Button(root,
                 text="2",
                 padx=40,
                 pady=20,
                 command=lambda: botao_click(2),
                 fg='#FFFFFF',
                 activeforeground="#FFFFFF",
                 bg='#000080',
                 activebackground='#0000FF',
                 relief=FLAT,
                 font=('futura',12,'bold')
)
dois.grid(row=3,column=2)
tres = Button(root,
                 text="3",
                 padx=40,
                 pady=20,
                 command=lambda: botao_click(3),
                 fg='#FFFFFF',
                 activeforeground="#FFFFFF",
                 bg='#000080',
                 activebackground='#0000FF',
                 relief=FLAT,
                 font=('futura',12,'bold')
)
tres.grid(row=3,column=3)
multiplica = Button(root,
                 text="x",
                 padx=41,
                 pady=20,
                 command=botao_multiplica,
                 fg='#FFFFFF',
                 activeforeground="#FFFFFF",
                 bg='#000080',
                 activebackground='#0000FF',
                 relief=FLAT,
                 font=('futura',12,'bold')
)
multiplica.grid(row=3,column=4)

#segunda fileira

quatro = Button(root,
                 text="4",
                 padx=40,
                 pady=20,
                 command=lambda: botao_click(4),
                 fg='#FFFFFF',
                 activeforeground="#FFFFFF",
                 bg='#000080',
                 activebackground='#0000FF',
                 relief=FLAT,
                 font=('futura',12,'bold')
)
quatro.grid(row=2,column=1)
cinco = Button(root,
                 text="5",
                 padx=40,
                 pady=20,
                 command=lambda: botao_click(5),
                 fg='#FFFFFF',
                 activeforeground="#FFFFFF",
                 bg='#000080',
                 activebackground='#0000FF',
                 relief=FLAT,
                 font=('futura',12,'bold')
)
cinco.grid(row=2,column=2)
seis = Button(root,
                 text="6",
                 padx=40,
                 pady=20,
                 command=lambda: botao_click(6),
                 fg='#FFFFFF',
                 activeforeground="#FFFFFF",
                 bg='#000080',
                 activebackground='#0000FF',
                 relief=FLAT,
                 font=('futura',12,'bold')
)
seis.grid(row=2,column=3)
subtracao = Button(root,
                 text="-",
                 padx=43,
                 pady=20,
                 command=botao_subtracao,
                 fg='#FFFFFF',
                 activeforeground="#FFFFFF",
                 bg='#000080',
                 activebackground='#0000FF',
                 relief=FLAT,
                 font=('futura',12,'bold')
)
subtracao.grid(row=2,column=4)

#3º fileira

sete = Button(root,
                 text="7",
                 padx=40,
                 pady=20,
                 command=lambda: botao_click(7),
                 fg='#FFFFFF',
                 activeforeground="#FFFFFF",
                 bg='#000080',
                 activebackground='#0000FF',
                 relief=FLAT,
                 font=('futura',12,'bold')
)
sete.grid(row=1,column=1)
oito = Button(root,
                 text="8",
                 padx=40,
                 pady=20,
                 command=lambda: botao_click(8),
                 fg='#FFFFFF',
                 activeforeground="#FFFFFF",
                 bg='#000080',
                 activebackground='#0000FF',
                 relief=FLAT,
                 font=('futura',12,'bold')
)
oito.grid(row=1,column=2)
nove = Button(root,
                 text="9",
                 padx=40,
                 pady=20,
                 command=lambda: botao_click(9),
                 fg='#FFFFFF',
                 activeforeground="#FFFFFF",
                 bg='#000080',
                 activebackground='#0000FF',
                 relief=FLAT,
                 font=('futura',12,'bold')
)
nove.grid(row=1,column=3)
soma = Button(root,
                 text="+",
                 padx=41,
                 pady=20,
                 command=botao_soma,
                 fg='#FFFFFF',
                 activeforeground="#FFFFFF",
                 bg='#000080',
                 activebackground='#0000FF',
                 relief=FLAT,
                 font=('futura',12,'bold')
)
soma.grid(row=1,column=4)
#4ºfileira
zero = Button(root,
                 text="0",
                 padx=91,
                 pady=20,
                 command=lambda: botao_click(0),
                 fg='#FFFFFF',
                 activeforeground="#FFFFFF",
                 bg='#000080',
                 activebackground='#0000FF',
                 relief=FLAT,
                 font=('futura',12,'bold')
)
zero.grid(row=4,column=1,columnspan=2)
limpar = Button(root,
                 text="C",
                 padx=40,
                 pady=20,
                 command=botao_clear,
                 fg='#FFFFFF',
                 activeforeground="#FFFFFF",
                 bg='#000080',
                 activebackground='#0000FF',
                 relief=FLAT,
                 font=('futura',12,'bold')
)
limpar.grid(row=4,column=3)
resposta = Button(root,
                 text="=",
                 padx=41,
                 pady=20,
                 command=botao_resposta,
                 fg='#FFFFFF',
                 activeforeground="#FFFFFF",
                 bg='#000080',
                 activebackground='#0000FF',
                 relief=FLAT,
                 font=('futura',12,'bold')
)
resposta.grid(row=4,column=4)
root.mainloop()
