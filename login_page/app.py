import os
import time

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

    page.theme = ft.Theme(color_scheme_seed='blue')

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def login(e):

        button.disabled = True
        answer.value = ''
        page.update()

        if checkPass(password.value):
            answer.value = 'Successfull login.'
            # page.go = '/login?access=' + encrypt('test', password.value)
        else:
            answer.value = 'Incorrect password. Please try again.'
            button.disabled = False
            password.focus()
        time.sleep(1.5)
        page.update()

    answer = ft.Text(value='', italic=True)
    password = ft.TextField(hint_text="password", width=250)
    button = ft.ElevatedButton("Login", on_click=login)
    page.add(password, button, answer)

ft.app(target=main)