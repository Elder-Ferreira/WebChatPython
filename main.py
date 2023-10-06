import flet as ft

def main(pagina):
    texto = ft.Text("Hashzap")

    chat = ft.Column()

    nome_usuario = ft.TextField(label="Escreva seu nome")

    campo_mensagem = ft.TextField(label="Digite uma mensagem")
    botao_enviar_mensagem = ft.ElevatedButton("Enviar")

    def entrar_popup(evento):
        pagina.add(chat)
        popup.open = False
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        pagina.add(ft.Row(
            [campo_mensagem, botao_enviar_mensagem]
        ))
        pagina.add(botao_enviar_mensagem)

        pagina.update()

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao Hashzap"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)]
    )

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_chat)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER)

