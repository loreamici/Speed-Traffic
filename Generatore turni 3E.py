import tkinter as tk
import random

window = tk.Tk()
window.geometry("971x600")
window.title("CALCOLATORE NUMERI CASUALI")
window.resizable(False,False)

testo = tk.Canvas(bg='white',height=350,width=500,scrollregion=(-2000,-2000,2500,2350))
scrollx = tk.Scrollbar(testo,orient='horizontal')
scrolly = tk.Scrollbar(testo,orient='vertical')

titolo = tk.Label(window,text="GENERATORE DI TURNI PER LA 3E",font = ("Times New Roman",25))
titolo.place(anchor="n",relx=0.5,y=20,width=540,height=23)

estratti = tk.Label(window,text="Numero persone estratte\nper ogni turno", pady = 150, padx = 10,font = ("Times New Roman",14))
estratti.place(anchor="w",y=280,x=55,width=190,height=45)
n_estratti_input = tk.Entry()
n_estratti_input.place(anchor="w",y=280,x=260,width=50)

massimo = tk.Label(window,text="Numero Massimo", pady = 100, padx = 10,font = ("Times New Roman",14))
massimo.place(anchor="w",x=80,y=210,width=140,height=20)
max_input = tk.Entry()
max_input.place(anchor="w",x=260,y=210,width=50)

minimo = tk.Label(window,text="Numero Minimo", pady = 50, padx = 10,font = ("Times New Roman",14))
minimo.place(anchor="w",y=140,x=80,width=130,height=20)
min_input = tk.Entry()
min_input.place(anchor="w",y=140,x=260,width=50)

turni = tk.Label(window,text="Numero turni\nestratti", pady = 200, padx = 10,font = ("Times New Roman",14))
turni.place(anchor="w",y=350,x=80,width=140,height=45)
n_turni_input = tk.Entry()
n_turni_input.place(anchor="w",x=260,y=350,width=50)


def generatore():
    testo.create_rectangle(-2000, -2000, 2500, 2350, fill="white")
    try:
        text = ''
        if min_input.get() and max_input.get() and n_estratti_input.get() and n_turni_input.get():
            lista = [i for i in range(int(min_input.get()),int(max_input.get())+1)]
            if abs(len(lista)-(int(n_estratti_input.get()) * int(n_turni_input.get()))) >= int(n_estratti_input.get()):
                t = "C'È QUALCHE ERRORE!\nRICONTROLLA QUELLO CHE HAI SCRITTO"
                testo.create_text(250,175,fill="darkblue",font="Times 18 italic bold",text=t,justify='center')
                testo.update
                return text
                
            random.shuffle(lista)
            
            for i in range(int(n_turni_input.get())+1):
                for k in range(int(n_estratti_input.get())):
                    if (i)*(int(n_estratti_input.get()))+k+1 > len(lista):
                        break
                    text += f"{lista[i*int(n_estratti_input.get())+k]}, "
                    
                text = text[:-2]+"\n"

        else:
            text = "NON HAI COMPILATO\nTUTTI GLI SPAZI NECESSARI"

        testo.create_text(250,175,fill="darkblue",font="Times 20 italic bold",text=text,justify='center')
        testo.update
    except:
        t = "C'È QUALCHE ERRORE!\nRICONTROLLA QUELLO CHE HAI SCRITTO"
        testo.create_text(250,175,fill="darkblue",font="Times 18 italic bold",text=t,justify='center')
        testo.update   

 
generatore_button = tk.Button(text = "GENERA TURNI CASUALI",command = generatore)
generatore_button.place(anchor='sw',y=570,x=49,relwidth=0.9,height=50)

scrollx.place(anchor='w',x=1,y=7)
scrollx.config(command=testo.xview)
scrolly.place(anchor='e',x=501,y=15)
scrolly.config(command=testo.yview)
testo.config(xscrollcommand=scrollx.set)
testo.config(yscrollcommand=scrolly.set)
testo.place(y=100,x=400)


if __name__ == "__main__":
    window.mainloop()






        
        












