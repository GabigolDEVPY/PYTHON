from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard  # Import necessário para usar o clipboard

class BinaryApp(App):
    def build(self):
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Título
        layout.add_widget(Label(text='Codificador/Decodificador Binário', font_size=24))

        # Entrada de dados
        self.input_text = TextInput(hint_text="Digite uma palavra ou código binário", multiline=False)
        layout.add_widget(self.input_text)

        # Botões de codificação e decodificação
        btn_encode = Button(text='Codificar')
        btn_encode.bind(on_press=self.encode_text)
        layout.add_widget(btn_encode)

        btn_decode = Button(text='Decodificar')
        btn_decode.bind(on_press=self.decode_text)
        layout.add_widget(btn_decode)

        # Área de resultado
        self.output_label = Label(text="Resultado:")
        layout.add_widget(self.output_label)

        # Botão para copiar o resultado
        btn_copy = Button(text='Copiar Resultado')
        btn_copy.bind(on_press=self.copy_result)
        layout.add_widget(btn_copy)

        return layout

    def encode_text(self, instance):
        letras_valores = {
    ' ': '00100000', '!': '00100001', '"': '00100010', '#': '00100011', '$': '00100100', '%': '00100101', '&': '00100110', "'": '00100111',
    '(': '00101000', ')': '00101001', '*': '00101010', '+': '00101011', ',': '00101100', '-': '00101101', '.': '00101110', '/': '00101111',
    '0': '00110000', '1': '00110001', '2': '00110010', '3': '00110011', '4': '00110100', '5': '00110101', '6': '00110110', '7': '00110111',
    '8': '00111000', '9': '00111001', ':': '00111010', ';': '00111011', '<': '00111100', '=': '00111101', '>': '00111110', '?': '00111111',
    '@': '01000000', 'A': '01000001', 'B': '01000010', 'C': '01000011', 'D': '01000100', 'E': '01000101', 'F': '01000110', 'G': '01000111',
    'H': '01001000', 'I': '01001001', 'J': '01001010', 'K': '01001011', 'L': '01001100', 'M': '01001101', 'N': '01001110', 'O': '01001111',
    'P': '01010000', 'Q': '01010001', 'R': '01010010', 'S': '01010011', 'T': '01010100', 'U': '01010101', 'V': '01010110', 'W': '01010111',
    'X': '01011000', 'Y': '01011001', 'Z': '01011010', '[': '01011011', '\\': '01011100', ']': '01011101', '^': '01011110', '_': '01011111',
    '`': '01100000', 'a': '01100001', 'b': '01100010', 'c': '01100011', 'd': '01100100', 'e': '01100101', 'f': '01100110', 'g': '01100111',
    'h': '01101000', 'i': '01101001', 'j': '01101010', 'k': '01101011', 'l': '01101100', 'm': '01101101', 'n': '01101110', 'o': '01101111',
    'p': '01110000', 'q': '01110001', 'r': '01110010', 's': '01110011', 't': '01110100', 'u': '01110101', 'v': '01110110', 'w': '01110111',
    'x': '01111000', 'y': '01111001', 'z': '01111010', '{': '01111011', '|': '01111100', '}': '01111101', '~': '01111110'

        }
        palavra = self.input_text.text.lower()
        nova_palavra = ''
        for letra in palavra:
            if letra in letras_valores:
                nova_palavra += (f' {letras_valores[letra]}')
        self.output_label.text = nova_palavra

    def decode_text(self, instance):
        letras_valores = {
    '00100000': ' ', '00100001': '!', '00100010': '"', '00100011': '#', '00100100': '$', '00100101': '%', '00100110': '&', '00100111': "'",
    '00101000': '(', '00101001': ')', '00101010': '*', '00101011': '+', '00101100': ',', '00101101': '-', '00101110': '.', '00101111': '/',
    '00110000': '0', '00110001': '1', '00110010': '2', '00110011': '3', '00110100': '4', '00110101': '5', '00110110': '6', '00110111': '7',
    '00111000': '8', '00111001': '9', '00111010': ':', '00111011': ';', '00111100': '<', '00111101': '=', '00111110': '>', '00111111': '?',
    '01000000': '@', '01000001': 'A', '01000010': 'B', '01000011': 'C', '01000100': 'D', '01000101': 'E', '01000110': 'F', '01000111': 'G',
    '01001000': 'H', '01001001': 'I', '01001010': 'J', '01001011': 'K', '01001100': 'L', '01001101': 'M', '01001110': 'N', '01001111': 'O',
    '01010000': 'P', '01010001': 'Q', '01010010': 'R', '01010011': 'S', '01010100': 'T', '01010101': 'U', '01010110': 'V', '01010111': 'W',
    '01011000': 'X', '01011001': 'Y', '01011010': 'Z', '01011011': '[', '01011100': '\\', '01011101': ']', '01011110': '^', '01011111': '_',
    '01100000': '`', '01100001': 'a', '01100010': 'b', '01100011': 'c', '01100100': 'd', '01100101': 'e', '01100110': 'f', '01100111': 'g',
    '01101000': 'h', '01101001': 'i', '01101010': 'j', '01101011': 'k', '01101100': 'l', '01101101': 'm', '01101110': 'n', '01101111': 'o',
    '01110000': 'p', '01110001': 'q', '01110010': 'r', '01110011': 's', '01110100': 't', '01110101': 'u', '01110110': 'v', '01110111': 'w',
    '01111000': 'x', '01111001': 'y', '01111010': 'z', '01111011': '{', '01111100': '|', '01111101': '}', '01111110': '~'
        }
        palavra = self.input_text.text
        lista_palavra = palavra.split()
        nova_palavra = ''
        for letra in lista_palavra:
            if letra in letras_valores:
                nova_palavra += (f'{letras_valores[letra]}')
        self.output_label.text = nova_palavra

    def copy_result(self, instance):
        # Copiar o texto que está na Label de resultado
        Clipboard.copy(self.output_label.text)
        self.output_label.text += " (Texto copiado!)"

# Rodar o app
if __name__ == '__main__':
    BinaryApp().run()