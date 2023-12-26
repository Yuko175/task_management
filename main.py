import flet
from flet import Page, app
from todoapp_add import TodoApp


def main(page: Page):
    app = TodoApp()
    page.add(app)


app(target=main)
