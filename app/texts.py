from colorama import init, Fore, Style
import os

header = (Fore.YELLOW + 
        '===============================================================================================\n'
        '||                                                                                           ||\n'
        '||' + Fore.GREEN + '                 !!Implementação do Algoritimo de busca em profundidade!!                  ' + Fore.YELLOW + '||\n'
        '||                                                                                           ||\n'
        '===============================================================================================\n')

def print_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(header +
        '||                                                                                           ||\n'
        '||' + Fore.CYAN + ' 1 - Selecionar qual digrafo deseja manipular.                                             ' + Fore.YELLOW + '||\n'
        '||' + Fore.CYAN + ' 2 - Mostrar Digrafo.                                                                      ' + Fore.YELLOW + '||\n'
        '||' + Fore.CYAN + ' 3 - Aplicar Busca em Profundidade.                                                        ' + Fore.YELLOW + '||\n'
        '||' + Fore.CYAN + ' 4 - Adicionar arquivos.                                                                   ' + Fore.YELLOW + '||\n'
        '||' + Fore.RED + ' 0 - Finalizar Progama                                                                     ' + Fore.YELLOW + '||\n'
        '||                                                                                           ||\n'
        '===============================================================================================\n'
    )

def selectable_digraphs(n_archives, n_digraphs):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(header +
        '||                                                                                           ' + Fore.YELLOW + '||\n'
        '||' + Fore.CYAN + ' Arquivos lidos: ' + Fore.BLUE + f'{n_archives}                                                                         ' + Fore.YELLOW + '||\n'
        '||' + Fore.CYAN + ' Digrafos disponíveis: ' + Fore.BLUE + f'{n_digraphs}                                                                   ' + Fore.YELLOW + '||\n'
        '||' + Fore.CYAN + ' Selecione uma opção entre ' + Fore.BLUE + '1' + Fore.YELLOW + ' e ' + Fore.BLUE + f'{n_digraphs}                                                           ' + Fore.YELLOW + '||\n'
        '||' + Fore.RED + ' Digite 0 para voltar ao menu                                                              ' + Fore.YELLOW + '||\n'
        '||                                                                                           ||\n'
        '===============================================================================================\n'
    )

def end_program():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(header +
        '||                                                                                           ||\n'
        '||' + Fore.RED + '                                   Progama Finalizado.                                     ' + Fore.YELLOW + '||\n'
        '||                                                                                           ||\n'
        '===============================================================================================\n'
    )
