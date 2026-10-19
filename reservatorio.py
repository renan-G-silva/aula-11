import colorama

colorama.init()

# Lista com as mensagens
mensagens = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

# Função que devolve a cor conforme o nível
def cor_do_nivel(nivel):
    if nivel == 1:
        return colorama.Fore.RED
    elif nivel == 2:
        return colorama.Fore.YELLOW
    elif nivel == 3:
        return colorama.Fore.GREEN
    elif nivel == 4:
        return colorama.Fore.CYAN
    else:
        return colorama.Fore.BLUE

# Mostra cada mensagem com sua cor
for i in range(len(mensagens)):
    print(cor_do_nivel(i + 1) + mensagens[i])

# Volta o terminal ao normal
print(colorama.Style.RESET_ALL)