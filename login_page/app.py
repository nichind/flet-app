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

def main(page: ft.Page):

    page.client_storage.clear()

    page.title = 'Flet login page'

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

            times = int(page.client_storage.get("try"))
            page.client_storage.set("try", str(int(times) + 1))


            if times + 1 >= 4:
                page.client_storage.set("try", '0')
                try_times = int(page.client_storage.get("try-time"))
                page.client_storage.set("try-time", str(int(try_times) + 1))
                button.disabled = True
                seconds = 15 * try_times
                while seconds > 0:
                    answer.value = f'Incorrect password. Wait {seconds} seconds to try again.'
                    time.sleep(1)
                    seconds -= 1
                    page.update()

                button.disabled = False
                answer.value = f''

        time.sleep(1.5)
        page.update()

    if page.client_storage.contains_key("try") is False:
        page.client_storage.set("try", "0")

    if page.client_storage.contains_key("try-time") is False:
        page.client_storage.set("try-time", "1")

    answer = ft.Text(value='', italic=True)
    password = ft.TextField(hint_text="password", width=250)
    button = ft.ElevatedButton("Login", on_click=login)
    page.add(password, button, answer)

ft.app(target=main)