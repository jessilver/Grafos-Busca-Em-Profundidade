from colorama import init, Fore, Style
from lib import funtions as base_funtions
from lib import graph as graph_funtions
import texts, os

init(autoreset=True)

# Limpa a tela antes de exibir o programa

base_funtions.create_imports_directory()

while True:

    texts.print_menu()

    menu_option = (input(Fore.YELLOW + 'Selecione uma opção: ' + Fore.CYAN))

    if menu_option == '1':

        while True:

            if base_funtions.is_imports_directory_empty():
                print('\n'+Fore.RED + 'Nenhum arquivo encontrado.\n')
                input(Fore.YELLOW + 'Pressione Enter para coninuar: ')
                break

            files_names, digraphs = base_funtions.read_all_files_in_imports()
            texts.selectable_digraphs(len(files_names), len(digraphs))

            digraphs_option = (input(Fore.YELLOW + 'Selecione uma opção: ' + Fore.CYAN))

            try:
                digraph = digraphs['digraph_'+digraphs_option]
                print('\n'+Fore.GREEN + 'digraph_'+digraphs_option+'\n')

                for i in digraph:
                    print(i)
                print('\n')

                G = None
                G, start = graph_funtions.build_digraph(digraph)

                while True:
                    texts.draw_or_dfs()

                    dfs_option = (input(Fore.YELLOW + 'Selecione uma opção: ' + Fore.CYAN))

                    digraph = digraphs['digraph_'+digraphs_option]
                    print('\n'+Fore.GREEN + 'digraph_'+digraphs_option+'\n')

                    for i in digraph:
                        print(i)

                    if dfs_option == '1':
                        graph_funtions.draw_digraph(G,('digraph_'+digraphs_option))
                        dfs_option = (input('\n'+Fore.YELLOW + '0 para sair, Enter para coninuar: ' + Fore.CYAN))
                    elif dfs_option == '2':

                        node_option = (input('\n'+Fore.YELLOW + 'Selecione um nó de inicio: ' + Fore.CYAN))

                        dfs_result = graph_funtions.dfs(G, node_option)
                        print('\n'+Fore.GREEN + 'Visitados: ' + Fore.RESET + str(dfs_result['visited']))
                        print(Fore.GREEN + 'Tempo de entrada: ' + Fore.RESET + str(dfs_result['entry_time']))
                        print(Fore.GREEN + 'Tempo de saída: ' + Fore.RESET + str(dfs_result['exit_time']))
                        print(Fore.GREEN + 'Arestas de árvore: ' + Fore.RESET + str(dfs_result['tree_edges']))
                        print(Fore.GREEN + 'Arestas de retorno: ' + Fore.RESET + str(dfs_result['back_edges']))
                        print(Fore.GREEN + 'Arestas de avanço: ' + Fore.RESET + str(dfs_result['forward_edges']))
                        print(Fore.GREEN + 'Arestas de cruzamento: ' + Fore.RESET + str(dfs_result['cross_edges'])+'\n')

                        graph_funtions.draw_generated_tree(G, dfs_result)

                        dfs_option = (input('\n'+Fore.YELLOW + '0 para sair, Enter para coninuar: ' + Fore.CYAN))



                    elif dfs_option == '0':
                        break
                    else:
                        print('\n'+Fore.RED + 'Opção inválida.\n')
                        dfs_option = (input(Fore.YELLOW + '0 para sair, Enter para coninuar: ' + Fore.CYAN))


            except:
                print('\n'+Fore.RED + 'Opção inválida.\n')

            digraph_option = (input(Fore.YELLOW + '0 para sair, Enter para coninuar: ' + Fore.CYAN))

            if digraph_option == '0':
                break

    elif menu_option == '2':
        while True:

            if base_funtions.is_imports_directory_empty():
                print('\n'+Fore.RED + 'Nenhum arquivo encontrado.\n')
                input(Fore.YELLOW + 'Pressione Enter para coninuar: ')
                break

            files_names, digraphs = base_funtions.read_all_files_in_imports()
            texts.selectable_digraphs(len(files_names), len(digraphs))

            digraphs_option = (input(Fore.YELLOW + 'Selecione uma opção: ' + Fore.CYAN))

            try:
                digraph = digraphs['digraph_'+digraphs_option]
                print('\n'+Fore.GREEN + 'digraph_'+digraphs_option+'\n')

                for i in digraph:
                    print(i)
                print('\n')

                G = None
                G, _ = graph_funtions.build_digraph(digraph)

                if int(digraphs_option) <= len(digraphs):
                    
                    graph_funtions.draw_digraph(G,('digraph_'+digraphs_option))

                elif digraphs_option == '0':
                    break
                else:
                    trow = Exception('Opção inválida.')

            except:
                print('\n'+Fore.RED + 'Opção inválida.\n')

            digraphs_option = (input(Fore.YELLOW + '0 para sair, Enter para coninuar: ' + Fore.CYAN))

            if digraphs_option == '0':
                break

    elif menu_option == '3':
        while True:

            if base_funtions.is_imports_directory_empty():
                print('\n'+Fore.RED + 'Nenhum arquivo encontrado.\n')
                input(Fore.YELLOW + 'Pressione Enter para coninuar: ')
                break

            files_names, digraphs = base_funtions.read_all_files_in_imports()
            texts.selectable_digraphs(len(files_names), len(digraphs))

            digraphs_option = (input(Fore.YELLOW + 'Selecione uma opção: ' + Fore.CYAN))

            try:
                digraph = digraphs['digraph_'+digraphs_option]
                print('\n'+Fore.GREEN + 'digraph_'+digraphs_option+'\n')

                for i in digraph:
                    print(i)

                node_option = (input('\n'+Fore.YELLOW + 'Selecione um nó de inicio: ' + Fore.CYAN))

                G = None
                G, _ = graph_funtions.build_digraph(digraph)


                if int(digraphs_option) <= len(digraphs):
                    
                    dfs_result = graph_funtions.dfs(G, node_option)
                    print('\n'+Fore.GREEN + 'Visitados: ' + Fore.RESET + str(dfs_result['visited']))
                    print(Fore.GREEN + 'Tempo de entrada: ' + Fore.RESET + str(dfs_result['entry_time']))
                    print(Fore.GREEN + 'Tempo de saída: ' + Fore.RESET + str(dfs_result['exit_time']))
                    print(Fore.GREEN + 'Arestas de árvore: ' + Fore.RESET + str(dfs_result['tree_edges']))
                    print(Fore.GREEN + 'Arestas de retorno: ' + Fore.RESET + str(dfs_result['back_edges']))
                    print(Fore.GREEN + 'Arestas de avanço: ' + Fore.RESET + str(dfs_result['forward_edges']))
                    print(Fore.GREEN + 'Arestas de cruzamento: ' + Fore.RESET + str(dfs_result['cross_edges'])+'\n')

                    graph_funtions.draw_generated_tree(G, dfs_result)

                elif digraphs_option == '0':
                    break
                else:
                    trow = Exception('Opção inválida.')

            except:
                print('\n'+Fore.RED + 'Opção inválida.\n')

            digraphs_option = (input(Fore.YELLOW + '0 para sair, Enter para coninuar: ' + Fore.CYAN))

            if digraphs_option == '0':
                break

    elif menu_option == '4':
        file_path = input(Fore.YELLOW + 'Digite o caminho do arquivo: ' + Fore.CYAN)
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            print(Fore.GREEN + 'Conteúdo do arquivo:\n\n' + Fore.RESET + content)
            
            save_path = base_funtions.get_resource_path(os.path.join('lib', 'imports', os.path.basename(file_path)))
            print(save_path)
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