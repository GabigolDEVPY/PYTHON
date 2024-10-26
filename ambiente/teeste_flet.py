import tkinter as tk

def on_button_click():
    print("Botão clicado!")

def main():
    # Criar a janela principal
    root = tk.Tk()
    root.title("App Móvel com Tkinter")
    root.geometry("300x500")  # Dimensões da janela

    # Adicionar um frame para centralizar os componentes
    frame = tk.Frame(root, bg="#ADD8E6", bd=10)
    frame.pack(expand=True, fill=tk.BOTH)

    # Adicionar um título
    title_label = tk.Label(frame, text="Bem-vindo ao meu App Móvel!", font=("Arial", 24), bg="#ADD8E6")
    title_label.pack(pady=20)

    # Adicionar um botão
    button = tk.Button(frame, text="Clique Aqui", command=on_button_click, font=("Arial", 16), bg="#4CAF50", fg="white")
    button.pack(pady=10)

    # Adicionar mais componentes conforme necessário
    info_label = tk.Label(frame, text="Este é um exemplo de app.", font=("Arial", 14), bg="#ADD8E6")
    info_label.pack(pady=10)

    # Iniciar o loop principal
    root.mainloop()

if __name__ == "__main__":
    main()
