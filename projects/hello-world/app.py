import flet as ft

def main(page):
    def hello(e):
        string.value=f'Hello {name.value}!'
        name.value = ""
        name.focus()
        page.update()

    string = ft.Text(value='')
    name = ft.TextField(hint_text="Name", width=300)
    page.add(ft.Row([name, ft.ElevatedButton("Say hello!", on_click=hello)]))
    page.add(string)

ft.app(target=main)