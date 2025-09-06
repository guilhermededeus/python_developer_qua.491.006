import flet as ft


def main(page: ft.Page):
    # Função de evento
    def calcular_melhor_preco(e):
        if not etanol.value:
            etanol.error_text = "Insira o etanol"
        else:
            etanol.error_text = None

        if not gasolina.value:
            gasolina.error_text = "Insira a gasolina"
        else:
            gasolina.error_text = None

        # Só calcula se ambos estiverem preenchidos
        if etanol.value and gasolina.value:
            try:
                # Converte valores para float (aceita vírgula)
                etanol_num = float(etanol.value.replace(",", "."))
                gasolina_num = float(gasolina.value.replace(",", "."))

                # Calcula o indice
                indice = etanol_num / gasolina_num

                # Prepara a mensagem
                if indice < 0.7:
                    mensagem = f"Compensa abastecer com Etanol."
                else:
                    mensagem = f"Compensa abastecer com Gasolina."

                # Mostra no modal
                dlg_modal.title.value = "Resultado:"
                dlg_modal.content.value = mensagem
                page.open(dlg_modal)

                # Limpa os campos
                etanol.value = ""
                gasolina.value = ""

            except ValueError:
                etanol.error_text = "Valor inválido"
                gasolina.error_text = "Valor inválido"

        page.update()

    # Função que limpa o erro quando o usuário digita
    def limpar_erro_etanol(e):
        etanol.error_text = None
        page.update()

    def limpar_erro_gasolina(e):
        gasolina.error_text = None
        page.update()

    # Variáveis
    etanol = ft.TextField(
        label="Etanol",
        prefix_text="R$",
        border_color="white",
        on_change=limpar_erro_etanol
    )
    gasolina = ft.TextField(
        label="Gasolina",
        prefix_text="R$",
        border_color="white",
        on_change=limpar_erro_gasolina,
        on_submit=calcular_melhor_preco
    )

    # Caixa de diálogo
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text(),
        content=ft.Text(size=20, weight="bold"),
        actions=[ft.TextButton("OK", on_click=lambda e: page.close(dlg_modal))],
        actions_alignment=ft.MainAxisAlignment.END
    )

    # Propriedades da janela
    page.title = "Cálculo de Combustível"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.DARK

    # Barra superior
    page.appbar = ft.AppBar(title=ft.Text("Índice Álcool x Gasolina", size=16))

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Qual compensa mais?", size=30, weight="bold"),
                alignment=ft.alignment.center
            ),
            expand=True,
        ),
        ft.ResponsiveRow(
            [
                ft.Container(etanol, col={"sm": 6, "md": 4, "xl": 2}),
                ft.Container(gasolina, col={"sm": 6, "md": 4, "xl": 2})
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.Container(
                    ft.ElevatedButton(
                        "Calcular",
                        on_click=calcular_melhor_preco,
                        bgcolor="white",
                        color="black"
                    ),
                    padding=30,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(main)
