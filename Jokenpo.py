import tkinter as tk
import random

def jogar():
    escolha_usuario = opcao_var.get()
    if escolha_usuario:
        escolha_comp = escolha_computador()
        resultado = verificar_vencedor(escolha_usuario, escolha_comp)
        resultado_label.config(text=f"Computador escolheu: {escolha_comp}\n{resultado}")
    else:
        resultado_label.config(text="Por favor, escolha uma opção!")

def escolha_computador():
    opcoes = ["Pedra", "Papel", "Tesoura"]
    return random.choice(opcoes)

def verificar_vencedor(escolha_usuario, escolha_comp):
    if escolha_usuario == escolha_comp:
        return "Empate!"
    elif (
        (escolha_usuario == "Tesoura" and escolha_comp == "Papel") or
        (escolha_usuario == "Pedra" and escolha_comp == "Tesoura") or
        (escolha_usuario == "Papel" and escolha_comp == "Pedra")
    ):
        return "Você ganhou!"
    else:
        return "Você perdeu!"

janela = tk.Tk()
opcao_var = tk.StringVar()

instrucao_label = tk.Label(janela, text="Escolha uma opção:")
instrucao_label.pack()

opcoes = ["Pedra", "Papel", "Tesoura"]
for opcao in opcoes:
    botao = tk.Radiobutton(janela, text=opcao, variable=opcao_var, value=opcao)
    botao.pack()

jogar_botao = tk.Button(janela, text="Jogar", command=jogar)
jogar_botao.pack()

resultado_label = tk.Label(janela, text="")
resultado_label.pack()

opcao_var.set(None)

janela.title("Jokenpô")
janela.geometry('250x200')
janela.mainloop()
