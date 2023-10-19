import flet as ft


def main(pagina):
    texto = ft.Text("Hashzap")

    chat = ft.Column()

    nome_usuario = ft.TextField(label="Escreva seu nome")

    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))        
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all(campo_mensagem.value)
        campo_mensagem.value = ""
        pagina.update()


    campo_mensagem = ft.TextField(label="Digite uma mensagem")
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_popup(evento):
        pagina.add(chat)
        popup.open = False
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        pagina.add(ft.Row([campo_mensagem, botao_enviar_mensagem]))
        pagina.add(botao_enviar_mensagem)

        pagina.update()

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao Hashzap"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)],
    )

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_chat)

    pagina.add(texto)
    pagina.add(botao_iniciar)


ft.app(target=main, view=ft.WEB_BROWSER)
