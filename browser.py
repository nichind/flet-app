import os
import subprocess
import flet as ft
import glob
import signal


def main(page: ft.Page):

    class Button(object):
        def __init__(self):
            self.path = ''
            self.process = None
            self.row = None

        def setpath(self, path):
            self.path = path

        def run(self):
            def start(e):
                self.process = subprocess.Popen(f'python {self.path}app.py')

            def close(e):
                try:
                    os.kill(self.process.pid, signal.SIGTERM)
                except: pass

            def row():
                gen = ft.ElevatedButton(project.split('\\')[-2].upper().replace('-', ' '), on_click=start)
                cl = ft.ElevatedButton('Kill', on_click=close, opacity=5)

                self.row = [gen, cl]
                return self.row

            return row()

    page.theme = ft.Theme(color_scheme_seed='green')
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(ft.Text('nichind flet Projects Browser.'))

    for project in glob.glob(".\\projects\\*\\", recursive = True):
        prj = Button()

        prj.setpath(project)

        page.add(ft.Row(prj.run(), alignment=ft.MainAxisAlignment.CENTER))

    page.title = 'Browse current flet apps in this repo'


if __name__ == '__main__':
    ft.app(target=main)
