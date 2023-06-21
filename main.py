#importando tkinter 
from tkinter import * 
from tkinter import ttk 
from tkinter import font

# cores
cor_display = '#181818' #preta
cor_main = '#181818' #cinza menos escuro
cor_button = '#525252' #cinza escuro
cor_fonte = '#ffffff' #branco


janela = Tk()
janela.title("Calculadora")
janela.geometry("350x450")
janela.config(bg=cor_display)

#Divindo a tela/Frames
frame_display = Frame(janela, width=350, height=100, bg=cor_display)
frame_display.grid(row=0, column=0)

frame_main = Frame(janela, width=350, height=420, bg=cor_main)
frame_main.grid(row=1, column=0)

# Defina o nome e o tamanho da fonte
nome_fonte = "Arial"
tamanho_fonte = 30

# Crie a fonte com o nome e tamanho definidos
fonte = font.Font(family=nome_fonte, size=tamanho_fonte)

#criando label
valor_texto = StringVar()

app_label = Label(frame_display, textvariable=valor_texto, font=fonte, width=14, height=2, padx=7, relief=FLAT, anchor="e", bg=cor_display, fg=cor_fonte)
app_label.place(x=0, y=0)


#Função calcular

def calcular():
    resultado = eval(all_valor)
    
    valor_texto.set(str(resultado))

#Função limpar tela

def clear_display():
    global all_valor
    all_valor = ""
    valor_texto.set("")
    
    #variavel com todos os valores 

all_valor = ''

#Função 
def entrada_valor(event):
    global all_valor
    all_valor = all_valor + str(event) 
        
    #valor para tela 
    valor_texto.set(all_valor)

#Função apagar valor

def apagar_valor():
    global all_valor
    all_valor = all_valor[:-1]
    valor_texto.set(all_valor)

#Criando Botões

#primeira fileira
button_clear = Button(frame_main, text="C", width=8, height=3, bg=cor_button, fg=cor_fonte, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge', command= clear_display) 
button_clear.place(x=0, y=0)
button_porcent = Button(frame_main, text="%", width=8, height=3, bg=cor_button, fg=cor_fonte, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge', command= lambda: entrada_valor('%'))
button_porcent.place(x=90, y=0)
button_div = Button(frame_main, text="÷", width=8, height=3, bg=cor_button, fg=cor_fonte, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge', command= lambda: entrada_valor('/'))
button_div.place(x=180, y=0)
button_apagar = Button(frame_main, text="⌫", width=8, height=3, bg=cor_button, fg=cor_fonte, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge', command= apagar_valor)
button_apagar.place(x=270, y=0)

#segunda fileira
button_num_7 = Button(frame_main, text="7", width=8, height=3, bg=cor_button, fg=cor_fonte, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge', command= lambda: entrada_valor('7')) 
button_num_7.place(x=0, y=70)
button_num_8 = Button(frame_main, text="8", width=8, height=3, bg=cor_button, fg=cor_fonte, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge', command= lambda: entrada_valor('8'))
button_num_8.place(x=90, y=70)
button_num_9 = Button(frame_main, text="9", width=8, height=3, bg=cor_button, fg=cor_fonte, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge', command= lambda: entrada_valor('9'))
button_num_9.place(x=180, y=70)
button_mult = Button(frame_main, text="x", width=8, height=3, bg=cor_button, fg=cor_fonte, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge', command= lambda: entrada_valor('*'))
button_mult.place(x=270, y=70)

#terceira fileira
button_num_4 = Button(frame_main, text="4", width=8, height=3, bg=cor_button, fg=cor_fonte, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge', command= lambda: entrada_valor('4')) 
button_num_4.place(x=0, y=140)
button_num_5 = Button(frame_main, text="5", width=8, height=3, bg=cor_button, fg=cor_fonte, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge', command= lambda: entrada_valor('5'))
button_num_5.place(x=90, y=140)
button_num_6 = Button(frame_main, text="6", width=8, height=3, bg=cor_button, fg=cor_fonte, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge', command= lambda: entrada_valor('6'))
button_num_6.place(x=180, y=140)
button_div = Button(frame_main, text="-", width=8, height=3, bg=cor_button, fg=cor_fonte, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge', command= lambda: entrada_valor('-'))
button_div.place(x=270, y=140)

#quarta fileira
button_num_1 = Button(frame_main, text="1", width=8, height=3, bg=cor_button, fg=cor_fonte, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge', command= lambda: entrada_valor('1')) 
button_num_1.place(x=0, y=210)
button_num_2 = Button(frame_main, text="2", width=8, height=3, bg=cor_button, fg=cor_fonte, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge', command= lambda: entrada_valor('2'))
button_num_2.place(x=90, y=210)
button_num_3 = Button(frame_main, text="3", width=8, height=3, bg=cor_button, fg=cor_fonte, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge', command= lambda: entrada_valor('3'))
button_num_3.place(x=180, y=210)
button_soma = Button(frame_main, text="+", width=8, height=3, bg=cor_button, fg=cor_fonte, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge', command= lambda: entrada_valor('+'))
button_soma.place(x=270, y=210)

#quinta fileira
button_num_0 = Button(frame_main, text="0", width=18, height=3, bg=cor_button, fg=cor_fonte, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge', command= lambda: entrada_valor('0')) 
button_num_0.place(x=0, y=280)
button_ponto = Button(frame_main, text=".", width=8, height=3, bg=cor_button, fg=cor_fonte, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge', command= lambda: entrada_valor('.'))
button_ponto.place(x=180, y=280)
button_igual = Button(frame_main, text="=", width=8, height=3, bg=cor_button, fg=cor_fonte, font=('Ivy 13 bold'), relief=RAISED, overrelief='ridge', command = calcular)
button_igual.place(x=270, y=280)







janela.mainloop()