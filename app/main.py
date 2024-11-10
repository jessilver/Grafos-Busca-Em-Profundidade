from colorama import init, Fore, Style
import texts, funtions, os

init(autoreset=True)

# Limpa a tela antes de exibir o programa

funtions.create_imports_directory()

while True:

    texts.print_menu()

    menu_option = (input(Fore.YELLOW + 'Selecione uma opção: ' + Fore.CYAN))

    if menu_option == '1':

        while True:

            if funtions.is_imports_directory_empty():
                print('\n'+Fore.RED + 'Nenhum arquivo encontrado.\n')
                input(Fore.YELLOW + 'Pressione Enter para coninuar: ')
                break

            files_names, digraphs = funtions.read_all_files_in_imports()
            texts.selectable_digraphs(len(files_names), len(digraphs))

            digraphs_option = (input(Fore.YELLOW + 'Selecione uma opção: ' + Fore.CYAN))

            try:
                digraph = digraphs['digraph_'+digraphs_option]
                print('\n'+Fore.GREEN + 'digraph_'+digraphs_option+'\n')
            except:
                print('\n'+Fore.RED + 'Opção inválida.\n')

            digraph_option = (input(Fore.YELLOW + '0 para sair, Enter para coninuar: ' + Fore.CYAN))

            if digraph_option == '0':
                break

    elif menu_option == '2':
        print('2')

    elif menu_option == '3':
        print('3')

    elif menu_option == '4':
        file_path = input(Fore.YELLOW + 'Digite o caminho do arquivo: ' + Fore.CYAN)
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            print(Fore.GREEN + 'Conteúdo do arquivo:\n\n' + Fore.RESET + content)
            
            save_path = funtions.get_resource_path(os.path.join('imports', os.path.basename(file_path)))
            with open(save_path, 'w') as file:
                file.write(content)

            print(Fore.GREEN + f'Arquivo salvo em: {save_path}\n')
            input(Fore.YELLOW + 'Pressione Enter para coninuar: ')
        except FileNotFoundError:

            print(Fore.RED + 'Arquivo não encontrado.\n')
            input(Fore.YELLOW + 'Pressione Enter para coninuar: ')
        except Exception as e:

            print(Fore.RED + f'Erro ao ler o arquivo: {e}\n')
            input(Fore.YELLOW + 'Pressione Enter para coninuar: ')
    elif menu_option == '0':
        texts.end_program()
        input(Fore.YELLOW + 'Pressione Enter para coninuar: ')
        break
    else:
        print('\n'+Fore.RED + 'Opção inválida.\n')
        mn_option = (input(Fore.YELLOW + '0 para sair, Enter para coninuar: ' + Fore.CYAN))

        if mn_option == '0':
            texts.end_program()
            input(Fore.YELLOW + 'Pressione Enter para coninuar: ')
            break