import flet as ft

class CalcularBotao(ft.ElevatedButton):
    def __init__(self, text, resultado, expand=1):
        super().__init__(
            text=text,
            expand=expand,
            on_click=self.clique_botao,  
        )
        self.data = text
        self.resultado = resultado

    def clique_botao(self, e):
        if self.data == "AC":
            self.resultado.value = "0"
        elif self.data == "=":
            try:
                
                self.resultado.value = str(eval(self.resultado.value))
            except Exception:
                self.resultado.value = "Erro"
        else:
           
            if self.resultado.value == "0" or self.resultado.value == "Erro":
                self.resultado.value = self.data
            else:
                self.resultado.value += self.data
        self.resultado.update()


class DigitarBotao(CalcularBotao):
    def __init__(self, text, resultado, expand=1):
        super().__init__(text, resultado, expand)
        self.bgcolor = ft.Colors.WHITE24
        self.color = ft.Colors.WHITE

class AcaoBotao(CalcularBotao):
    def __init__(self, text, resultado):
        super().__init__(text, resultado)
        self.bgcolor = ft.Colors.ORANGE
        self.color = ft.Colors.WHITE

class BotaoExtra(CalcularBotao):
    def __init__(self, text, resultado):
        super().__init__(text, resultado)
        self.bgcolor = ft.Colors.BLUE_GREY_100
        self.color = ft.Colors.BLACK


def main(page: ft.Page):
    page.title = "Calculadora"
    resultado = ft.Text(value="0", color=ft.Colors.WHITE, size=20)

    content = ft.Column(
        controls=[
            ft.Row(controls=[resultado], alignment="end"),
            ft.Row(
                controls=[
                    BotaoExtra(text="AC", resultado=resultado),
                    BotaoExtra(text="+/-", resultado=resultado),
                    BotaoExtra(text="%", resultado=resultado),
                    BotaoExtra(text="/", resultado=resultado),
                ]
            ),
            ft.Row(
                controls=[
                    DigitarBotao(text="7", resultado=resultado),
                    DigitarBotao(text="8", resultado=resultado),
                    DigitarBotao(text="9", resultado=resultado),
                    AcaoBotao(text="x", resultado=resultado),
                ]
            ),
            ft.Row(
                controls=[
                    DigitarBotao(text="4", resultado=resultado),
                    DigitarBotao(text="5", resultado=resultado),
                    DigitarBotao(text="6", resultado=resultado),
                    DigitarBotao(text="-", resultado=resultado),
                ]
            ),
            ft.Row(
                controls=[
                    DigitarBotao(text="1", resultado=resultado),
                    DigitarBotao(text="2", resultado=resultado),
                    DigitarBotao(text="3", resultado=resultado),
                    AcaoBotao(text="+", resultado=resultado),
                ]
            ),
            ft.Row(
                controls=[
                    DigitarBotao(text="0", resultado=resultado, expand=2),
                    DigitarBotao(text=".", resultado=resultado),
                    AcaoBotao(text="=", resultado=resultado),
                ]
            ),
        ]
    )

    page.add(
        ft.Container(
            width=350,
            bgcolor=ft.Colors.BLACK,
            border_radius=ft.border_radius.all(20),
            padding=20,
            content=content,
        )
    )

# Executa o app
ft.app(target=main)