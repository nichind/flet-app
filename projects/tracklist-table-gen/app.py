import os
import time

import flet as ft
from flet.security import encrypt, decrypt
from dotenv import load_dotenv
load_dotenv()

def genTable():
    return []

def main(page: ft.Page):
    def start(e):
        page.window_close()
        page.update()

    page.client_storage.clear()

    page.title = 'Flet login page'

    page.theme = ft.Theme(color_scheme_seed='blue')

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    count = ft.TextField(hint_text="Track count", width=125)
    button = ft.ElevatedButton("Start", on_click=start)
    page.add(count, button)

ft.app(target=main)
