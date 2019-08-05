import time
from tkinter import *
import winsound

class App(object):
    def __init__(self):

        #Instancia principal
        self.root = Tk()
        self.root.title('Despertador')
        self.root.geometry('200x130')
        self.root.resizable(False, False)

        #Frames
        self.frame1 = Frame(self.root) #Frame do relógio
        self.frame1.pack()
        self.frame2 = Frame(self.root) #Frame do set
        self.frame2.pack()
        self.frame3 = Frame(self.root) #Frame dos botoes
        self.frame3.pack(pady=5)
        self.frame4 = Frame(self.root) #Frame do horario marcado
        self.frame4.pack(pady=5)

        #Relógio
        hora = self.getHora()
        self.relogio = Label(self.frame1, text=hora, font=('Courier', 20, 'bold'))
        self.relogio.pack(side='top')

        #Entry, Botões, Labels
        self.textoEntrada1 = Label(self.frame2, text='Despertar: ', font=('Courier', 10, 'bold'))
        self.textoEntrada1.pack(side='left')

        self.entrada1 = Entry(self.frame2, width=5)
        self.entrada1.pack(side='left')
        self.entrada2 = Entry(self.frame2, width=5)
        self.entrada2.pack(side='left')
        self.entrada3 = Entry(self.frame2, width=5)
        self.entrada3.pack(side='left')

        self.botaoAtivar = Button(self.frame3, text='Ativar', width=10, command=self.setHoraD)
        self.botaoAtivar.pack(side='left', padx=5)
        self.botaoDesativar = Button(self.frame3, text='Desativar', width=10, command=self.desativar)
        self.botaoDesativar.pack()

        self.horarioSettado = Label(self.frame4, text='Horario settado', font=('Courier', 10, 'bold'))
        #self.horarioSettado.pack()

        self.despertar_ativo = False

        #Ação
        self.update()

        self.root.mainloop()

    def getHora(self):
        infos = time.localtime()
        hora = infos[3]
        minuto = infos[4]
        segundos = infos[5]

        if hora < 10:
            hora = '0' + str(hora)

        if minuto < 10:
            minuto = '0' + str(minuto)

        if segundos < 10:
            segundos = '0' + str(segundos)

        horario = f'{hora}:{minuto}:{segundos}'

        return horario

    def update(self):
        hora = self.getHora()
        self.relogio['text'] = hora

        if self.despertar_ativo:
            if hora == self.horarioSettado['text']:
                winsound.PlaySound('alarm_sound.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)


        self.root.after(10, self.update)

    def setHoraD(self):
        try:
            hora = int(self.entrada1.get())
            if hora > 24 or hora < 0:
                raise TimeoutError

            if hora < 10:
                hora = '0' + str(hora)

            minuto = int(self.entrada2.get())
            if minuto > 59 or hora < 0:
                raise TimeoutError

            if minuto < 10:
                minuto = '0' + str(minuto)

            segundos = int(self.entrada3.get())
            if segundos > 59 or segundos < 0:
                raise TimeoutError

            if segundos < 10:
                segundos = '0' + str(segundos)

            despertar = f'{hora}:{minuto}:{segundos}'
            self.horarioSettado['text'] = despertar
            self.despertar_ativo = True
            self.horarioSettado.pack()

        except:
            self.horarioSettado['text'] = 'Error'
            self.horarioSettado.pack()

    def desativar(self):
        self.horarioSettado['text'] = 'None'
        self.despertar_ativo = False
        self.horarioSettado.pack_forget()


if __name__ == '__main__':
    App()
