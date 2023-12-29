# Importando os módulos necessários -------------------------------------------------
import customtkinter
from tkinter import *
from tkinter import BOTH, END, LEFT, Entry, Label, messagebox
from tkcalendar import Calendar
import threading
#------------------------------------------------------------------------------------
# defenir as cores a usar -----------------------------------------------------------
co0 = '#0000FF' # azul para o bg 
co1 = '#FFFFFF' # branco para a letra 
#------------------------------------------------------------------------------------
# Definindo uma classe personalizada para o calendário que herda da classe Calendar
class CustomCalendar(Calendar):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
#-------------------------------------------------------------------------------------
    # Sobrescrevendo o método para formatar os dias da semana
    def formatweekday(self, day, width):
        """Retorna o nome abreviado do dia da semana."""
        return self._cal.locale.day_abbr[day]
#-------------------------------------------------------------------------------------    

# Função para mostrar o calendário quando o botão é clicado---------------------------
def mostrar_calendario():
    # Obtendo a data selecionada a partir da entrada de texto
    data_selecionada = Edata.get()
    ano, mes, dia = map(int, data_selecionada.split('-'))
#-----------------------------------------------------------------------------------------------------------------------    
    # Criando uma instância do calendário personalizado com a data especificada ----------------------------------------
    cal = CustomCalendar(janela, locale='pt_PT', year=ano, month=mes, day=dia, font=('Arial', 16), showweeknumbers=False)
    cal.place(x=10, y=55)
    #-------------------------------------------------------------------------------------------------------------------
    # Adicionando um cabeçalho personalizado com as iniciais dos dias da semana ----------------------------------------
    dias_semana = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']
    for i, dia in enumerate(dias_semana):
        lbl = Label(cal._header, text=dia, background='blue', foreground='white', font=('Arial', 14, 'bold'))
        lbl.pack(side=LEFT, fill=BOTH, expand=True, padx=1, pady=1)
    #-------------------------------------------------------------------------------------------------------------------

# Função para limpar a entrada de texto---------------------------------------------------------------------------------
def limpar_entrada():
    Edata.delete(0, END)  # Limpa o conteúdo da entrada 
#-----------------------------------------------------------------------------------------------------------------------
# Função para sair da aplicação ----------------------------------------------------------------------------------------
def sair_aplicacao():
    resultado = messagebox.askquestion("Sair da Aplicação", "Você realmente deseja sair do programa?")
    if resultado == "yes":
        janela.destroy()  # Destroi a janela, encerrando o programa
#-----------------------------------------------------------------------------------------------------------------------
# Criando a janela principal usando a classe personalizada CTk ---------------------------------------------------------
janela = customtkinter.CTk()
janela.geometry('500x300+100+100')
janela.resizable(False, False)
janela.title('Calendário 1.1.1.2 dev Joel 2023')
janela.config(background=co0)
janela.iconbitmap(r'C:\Users\HP\Desktop\Programas em python\Calendario\calendario 1.1.1.2\icon.ico')
#------------------------------------------------------------------------------------------------------------------------
# Criando uma caixa de entrada para inserir a data ----------------------------------------------------------------------
Edata = customtkinter.CTkEntry(janela, width=485, font=customtkinter.CTkFont('arial 14'),placeholder_text='formato :ano- mes- dia', bg_color=co0)
Edata.place(x=10, y=10)
#------------------------------------------------------------------------------------------------------------------------
# Criando um botão personalizado para mostrar o calendário --------------------------------------------------------------
botao_mostrar_calendario = customtkinter.CTkButton(janela, text="Mostrar Calendário", command=mostrar_calendario, bg_color=co0, text_color=co1)
botao_mostrar_calendario.place(x=10, y=250)
#-------------------------------------------------------------------------------------------------------------------------
# criar um botão a limpar entrada de  dados ------------------------------------------------------------------------------
botao_Limpar_Entrada = customtkinter.CTkButton(janela, text="limpar Entrada", command=limpar_entrada, bg_color=co0, text_color=co1)
botao_Limpar_Entrada.place(x=155, y=250)
#-------------------------------------------------------------------------------------------------------------------------
# criar um botão a limpar entrada de  dados ------------------------------------------------------------------------------
Botao_sair = customtkinter.CTkButton(janela, text="Sair da aplicação", command=sair_aplicacao, bg_color=co0, text_color=co1)
Botao_sair.place(x=300, y=250)
#-------------------------------------------------------------------------------------------------------------------------
# Iniciando o loop principal da interface gráfica ------------------------------------------------------------------------
janela.mainloop()
#-------------------------------------------------------------------------------------------------------------------------