import os
import time
import flet as ft
import glob

def button(project):

    def runProject(e):
        while True:
            try:
                os.system(f'python {project}app.py')
                break
            except ModuleNotFoundError:
                os.system(f'pip install flet')

    return(ft.ElevatedButton(project.split('\\')[-2].upper().replace('-', ' '), on_click=runProject))

def main(page: ft.Page):

    page.theme = ft.Theme(color_scheme_seed='green')
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    page.add(ft.Text('nichind flet Projects Browser.'))

    for project in glob.glob(".\\projects\\*\\", recursive = True):
        page.add(button(project))

    page.title = 'Browse current flet apps in this repo'


ft.app(target=main)
