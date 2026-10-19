
# Sistema de monitoramento dos níveis de água do reservatório

from colorama import Fore, Style, init

# Inicializa o Colorama para exibir as mensagens coloridas
init(autoreset=True)

# Lista com as situações dos cinco níveis do reservatório
niveis = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

# Define a cor da mensagem conforme o nível informado
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE

# Percorre os cinco níveis e exibe as mensagens coloridas
for nivel in range(1, 6):
    cor = definir_cor(nivel)
    mensagem = niveis[nivel - 1]
    print(cor + mensagem + Style.RESET_ALL)
