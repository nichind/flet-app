import os
import flet as ft
from flet.security import encrypt, decrypt
from dotenv import load_dotenv
load_dotenv()

def checkPass(userInput: str):

    password = os.getenv('password')

    if userInput == password:
        return True
    else:
        return False

def main(page):

    page.theme = ft.Theme(color_scheme_seed='pink')

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def login(e):

        if checkPass(password.value):
            answer.value = 'Successfull login.'
        else:
            answer.value = 'Incorrect password. Please try again.'
            password.focus()
        page.update()

    answer = ft.Text(value='', italic=True)
    password = ft.TextField(hint_text="Name", width=250)
    page.add(password, ft.ElevatedButton("Login", on_click=login), answer)

ft.app(target=main)