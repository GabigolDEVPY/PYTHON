from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class BinaryApp(App):
    def build(self):
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Título
        layout.add_widget(Label(text='Codificador/Decodificador Binário', font_size=24))

        # Entrada de dados
        self.input_text = TextInput(hint_text="Digite uma palavra ou código binário", multiline=False)
        layout.add_widget(self.input_text)

        # Botões
        btn_encode = Button(text='Codificar')
        btn_encode.bind(on_press=self.encode_text)
        layout.add_widget(btn_encode)

        btn_decode = Button(text='Decodificar')
        btn_decode.bind(on_press=self.decode_text)
        layout.add_widget(btn_decode)

        # Área de resultado
        self.output_label = Label(text="Resultado:")
        layout.add_widget(self.output_label)

        return layout

    def encode_text(self, instance):
        letras_valores = {
            'a': '01000001', 'b': '01000010', 'c': '01000011', 'd': '01000100', 'e': '01000101', 'f': '01000110', 'g': '01000111', 'h': '01001000',
            'i': '01001001', 'j': '01001010', 'k': '01001011', 'l': '01001100', 'm': '01001101', 'n': '01001110', 'o': '01001111', 'p': '01010000',
            'q': '01010001', 'r': '01010010', 's': '01010011', 't': '01010100', 'u': '01010101', 'v': '01010110', 'w': '01010111', 'x': '01011000',
            'y': '01011001', 'z': '01011010', ' ': '00100000',
        }
        palavra = self.input_text.text.lower()
        nova_palavra = ''
        for letra in palavra:
            if letra in letras_valores:
                nova_palavra += (f' {letras_valores[letra]}')
        self.output_label.text = f"Codificado: {nova_palavra}"

    def decode_text(self, instance):
        letras_valores = {
            '01000001': 'a', '01000010': 'b', '01000011': 'c', '01000100': 'd', '01000101': 'e', '01000110': 'f', '01000111': 'g', '01001000': 'h',
            '01001001': 'i', '01001010': 'j', '01001011': 'k', '01001100': 'l', '01001101': 'm', '01001110': 'n', '01001111': 'o', '01010000': 'p',
            '01010001': 'q', '01010010': 'r', '01010011': 's', '01010100': 't', '01010101': 'u', '01010110': 'v', '01010111': 'w', '01011000': 'x',
            '01011001': 'y', '01011010': 'z', '00100000': ' ',
        }
        palavra = self.input_text.text
        lista_palavra = palavra.split()
        nova_palavra = ''
        for letra in lista_palavra:
            if letra in letras_valores:
                nova_palavra += (f'{letras_valores[letra]}')
        self.output_label.text = f"Decodificado: {nova_palavra}"

# Rodar o app
if __name__ == '__main__':
    BinaryApp().run()
