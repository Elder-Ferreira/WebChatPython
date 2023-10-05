import flet as ft

def main(pagina):
    texto = ft.Text("Hashzap")

    def entrar_chat(evento):
        texto_entrou = ft.Text("Entrou no chat")
        pagina.add(texto_entrou)

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_chat)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER)