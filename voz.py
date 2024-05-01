import customtkinter as ct
from pyttsx3 import init

janela=ct.CTk()
janela.title("Voz Robótica")
janela.geometry("500x400")
janela.resizable(False, False)

def conversao(txt, diretorio):
    robo = init()

    robo.save_to_file(txt, filename=diretorio)

    robo.runAndWait()

def confirmar():
    info=box.get("1.0", "end")
    if not info.strip():
        lbl_erro.configure(text="Ensira caracteres.")
    else:
        lbl_erro.configure(text="")

        if check_mp3.get() and check_wav.get() == 1:
            lbl_erro.configure(text="Ensira apenas uma opção de extensão de áudio.")
            lbl_erro.place(x=130, y=305)

        elif check_mp3.get() == 1:
            dire=ct.filedialog.askdirectory()
            conversao(info, dire+"/voz.mp3")

        elif check_wav.get() == 1:
            dire=ct.filedialog.askdirectory()
            conversao(info, dire+"/voz.wav")

def sair():
    janela.quit()

box=ct.CTkTextbox(janela, width=500, height=300, border_width=2,border_color="#1ffed8", text_color="dark cyan",
                  scrollbar_button_color="#1ffed8",font=("gothic bold",15))
box.place(x=0)

check_mp3=ct.CTkCheckBox(janela, width=10, height=10, fg_color="#1ffed8", checkbox_width=17,checkbox_height=17,
                        border_color="dark cyan", text=".Mp3")
check_mp3.place(x=5,y=320)

check_wav=ct.CTkCheckBox(janela, width=10, height=10, fg_color="#1ffed8", checkbox_width=17,checkbox_height=17,
                        border_color="dark cyan", text=".Wav")
check_wav.place(x=5,y=360)

lbl_erro=ct.CTkLabel(janela, text="", text_color="red")
lbl_erro.place(x=205, y=305)

btn=ct.CTkButton(janela, width=60, height=25, fg_color="#18ccae", text="Confirmar",text_color="#fffafa",
                command=confirmar).place(x=220,y=350)

btn_sair=ct.CTkButton(janela, width=60, height=25, fg_color="red", text="Sair",text_color="#fffafa",
                command=sair).place(x=430, y=370)

janela.mainloop()

# faça bom uso do código.
