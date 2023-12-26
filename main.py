import flet
from flet import Page, View, app
from todoapp_add import TodoApp


def main(page: Page):
    def route_change(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [TodoApp(), flet.ElevatedButton("テストページへ移動", on_click=open_test)],
            )
        )
        # テストページ（テストページのときだけviewに追加する）
        if page.route == "/test":
            page.views.append(
                View(
                    "/test",
                    [
                        flet.AppBar(title=flet.Text("テストページ")),
                        flet.Text("これはテストページです"),
                    ],
                )
            )

    # 現在のページを削除して、前のページに戻る
    def view_pop(e):
        print("View pop:", e.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    def open_test(e):
        page.go("/test")

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # page.add(TodoApp())
    page.go(page.route)


app(target=main)
