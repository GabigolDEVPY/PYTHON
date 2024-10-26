import tkinter as tk
import pyperclip  # Biblioteca para copiar texto para a área de transferência

# Função para criar a interface
def criar_interface():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Atalhos e Comandos do Ubuntu")
    janela.geometry("500x800")  # Define o tamanho da janela
    janela.configure(bg="#808080")  # Cor de fundo cinza

        # Função para copiar texto para a área de transferência
    def copiar_texto(comando):
        pyperclip.copy(comando)  # Copia o comando# Função para copiar texto para a área de transferência
    def copiar_texto(comando):
        pyperclip.copy(comando)  # Copia o comando

    # Texto com atalhos do Ubuntu
    atalhos = (
        "Atalhos Essenciais do Ubuntu\n\n"
        "1. Alt + Tab         - Alternar entre janelas abertas\n"
        "2. Ctrl + Alt + T    - Abrir o terminal\n"
        "3. Super + D         - Minimizar todas as janelas\n"
        "4. Super + M         - Maximizar a janela atual\n"
        "5. Super + Arrow keys - Mover janelas\n"
        "6. Alt + F4          - Fechar a janela atual\n"
        "7. Ctrl + C          - Copiar\n"
        "8. Ctrl + V          - Colar\n"
        "9. Ctrl + X          - Recortar\n"
        "10. Ctrl + Z         - Desfazer\n"
        "11. Ctrl + A         - Selecionar tudo\n"
        "12. F2               - Renomear\n"
        "13. F5               - Atualizar\n"
        "14. F10              - Ativar menu da janela\n"
        "15. Super + L        - Bloquear a tela\n"
        "16. Ctrl + Esc       - Abrir menu do sistema\n"
        "17. Ctrl + Alt + Del - Acessar gerenciador de tarefas\n"
        "18. Ctrl + Shift + N - Criar nova pasta\n"
        "19. Alt + F2         - Executar comando\n"
        "20. Alt + Enter      - Propriedades do arquivo\n"
        "21. Ctrl + Shift + T - Abrir nova aba no terminal\n"
        "22. Ctrl + Shift + W - Fechar aba no terminal\n"
        "23. Ctrl + Shift + C - Copiar texto do terminal\n"
        "24. Ctrl + Shift + V - Colar texto no terminal\n"
        "25. Ctrl + Alt + F1  - Acessar tty1\n"
        "26. Ctrl + Alt + F7  - Voltar ao ambiente gráfico\n"
        "27. Super + R        - Abrir o executável\n"
        "28. Super + F        - Pesquisar arquivos\n"
        "29. Alt + Space      - Abrir menu de contexto\n"
        "30. Ctrl + P         - Abrir painel de impressão\n"
        "31. Ctrl + N         - Novo documento\n"
        "32. Ctrl + S         - Salvar documento\n"
        "33. Ctrl + Q         - Sair da aplicação\n"
        "34. Ctrl + F         - Encontrar texto\n"
        "35. Ctrl + H         - Mostrar arquivos ocultos\n"
        "36. Ctrl + Shift + E - Explorar arquivos\n"
        "37. Ctrl + Tab       - Mover para a aba seguinte\n"
        "38. Ctrl + Shift + Tab - Mover para a aba anterior\n"
        "39. Super + T        - Abrir terminal em nova aba\n"
        "40. Super + E        - Abrir gerenciador de arquivos\n"
        "41. Ctrl + Shift + F - Pesquisar em arquivos\n"
        "42. F11              - Alternar modo de tela cheia\n"
        "43. Ctrl + Shift + L - Adicionar marcador\n"
        "44. Ctrl + D         - Adicionar a favoritos\n"
        "45. Ctrl + 1         - Mudar para a aba 1\n"
        "46. Ctrl + 2         - Mudar para a aba 2\n"
        "47. Ctrl + Shift + L - Mostrar lista de marcadores\n"
        "48. Alt + Shift + Up - Mover a janela para cima\n"
        "49. Alt + Shift + Down - Mover a janela para baixo\n"
        "50. Ctrl + Alt + Up  - Aumentar o tamanho da fonte\n"
    )

    # Comandos do Terminal como lista de tuplas (comando, descrição)
    comandos = [
        ("ls", "Listar arquivos e diretórios"),
        ("cd <diretorio>", "Mudar para o diretório especificado"),
        ("mkdir <pasta>", "Criar um novo diretório"),
        ("rm <arquivo>", "Remover um arquivo"),
        ("cp <origem> <destino>", "Copiar um arquivo ou diretório"),
        ("mv <origem> <destino>", "Mover ou renomear um arquivo ou diretório"),
        ("cat <arquivo>", "Exibir o conteúdo de um arquivo"),
        ("nano <arquivo>", "Editar um arquivo com o nano"),
        ("touch <arquivo>", "Criar um novo arquivo vazio"),
        ("chmod <permissões> <arquivo>", "Alterar permissões de um arquivo"),
        ("chown <usuário>:<grupo> <arquivo>", "Alterar o proprietário de um arquivo"),
        ("ps aux", "Listar processos em execução"),
        ("kill <PID>", "Finalizar um processo pelo ID"),
        ("top", "Monitorar processos em tempo real"),
        ("df -h", "Exibir informações sobre espaço em disco"),
        ("du -sh <diretorio>", "Exibir o tamanho de um diretório"),
        ("grep <padrão> <arquivo>", "Pesquisar texto em um arquivo"),
        ("find <diretório> -name <nome>", "Encontrar arquivos por nome"),
        ("wget <url>", "Baixar um arquivo da web"),
        ("curl <url>", "Transferir dados de ou para um servidor"),
        ("sudo <comando>", "Executar um comando com privilégios de superusuário"),
        ("apt update", "Atualizar a lista de pacotes"),
        ("apt upgrade", "Atualizar os pacotes instalados"),
        ("apt install <pacote>", "Instalar um novo pacote"),
        ("apt remove <pacote>", "Remover um pacote"),
        ("nano ~/.bashrc", "Editar o arquivo de configuração do bash"),
        ("history", "Mostrar o histórico de comandos"),
        ("clear", "Limpar a tela do terminal"),
        ("alias <nome>='<comando>'", "Criar um atalho para um comando"),
        ("echo <mensagem>", "Exibir uma mensagem no terminal"),
        ("pwd", "Exibir o diretório atual"),
        ("scp <origem> <destino>", "Copiar arquivos entre sistemas"),
        ("rsync -av <origem> <destino>", "Sincronizar arquivos e diretórios"),
        ("tar -czvf <arquivo.tar.gz> <diretório>", "Compactar um diretório"),
        ("tar -xzvf <arquivo.tar.gz>", "Descompactar um arquivo"),
        ("mount <dispositivo> <ponto_de_montagem>", "Montar um sistema de arquivos"),
        ("umount <ponto_de_montagem>", "Desmontar um sistema de arquivos"),
        ("ssh <usuário>@<host>", "Conectar-se a um servidor remoto via SSH"),
        ("df -i", "Exibir informações sobre inodes"),
        ("free -h", "Exibir informações sobre uso de memória"),
        ("man <comando>", "Exibir o manual de um comando"),
        ("chmod +x <script>", "Tornar um script executável"),
        ("nano <script.sh>", "Criar um script bash"),
        ("./<script.sh>", "Executar um script bash"),
        ("python <script.py>", "Executar um script Python"),
        ("pip install <pacote>", "Instalar um pacote Python"),
        ("python3 -m http.server", "Iniciar um servidor HTTP simples"),
        ("killall <processo>", "Finalizar todos os processos com o nome especificado"),
        ("passwd <usuário>", "Alterar a senha de um usuário"),
        ("df -hT", "Exibir informações sobre sistemas de arquivos"),
        ("uname -a", "Exibir informações do sistema"),
        ("lscpu", "Exibir informações sobre a CPU"),
        ("lsusb", "Listar dispositivos USB"),
        ("lspci", "Listar dispositivos PCI"),
        ("dmesg", "Exibir mensagens do kernel"),
    ]

    # Cria um frame para atalhos
    frame_atalhos = tk.Frame(janela, bg="#808080")
    frame_atalhos.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    
    # Cria um widget de texto para atalhos
    text_widget_atalhos = tk.Text(frame_atalhos, wrap=tk.WORD, bg="#ffffff", fg="#000000", font=("Arial", 10))
    text_widget_atalhos.insert(tk.END, atalhos)
    text_widget_atalhos.config(state=tk.DISABLED)  # Desabilita edição
    text_widget_atalhos.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Cria um frame para comandos
    frame_comandos = tk.Frame(janela, bg="#808080")
    frame_comandos.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Cria um canvas para comandos
    canvas_comandos = tk.Canvas(frame_comandos, bg="#808080")
    canvas_comandos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Cria uma barra de rolagem para comandos
    scrollbar = tk.Scrollbar(frame_comandos, orient=tk.VERTICAL, command=canvas_comandos.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configura a barra de rolagem para o canvas
    canvas_comandos.config(yscrollcommand=scrollbar.set)

    # Cria um frame interno que será usado no canvas
    frame_interno = tk.Frame(canvas_comandos, bg="#808080")
    canvas_comandos.create_window((0, 0), window=frame_interno, anchor='nw')

    # Adiciona comandos ao frame interno
    for comando, descricao in comandos:
        # Adiciona o texto do comando
        label_comando = tk.Label(frame_interno, text=f"{comando} - {descricao}", bg="#808080", fg="#ffffff", font=("Arial", 10))
        label_comando.pack(anchor='w', padx=10, pady=5)

        # Cria um botão para copiar o comando
        btn_copiar_comando = tk.Button(frame_interno, text="Copiar", command=lambda c=comando: copiar_texto(c), bg="#ffffff")
        btn_copiar_comando.pack(anchor='w', padx=(20, 10), pady=5)

    # Atualiza a rolagem do canvas
    frame_interno.update_idletasks()
    canvas_comandos.config(scrollregion=canvas_comandos.bbox("all"))

    # Inicia a aplicação
    janela.mainloop()

# Chama a função para criar a interface
criar_interface()