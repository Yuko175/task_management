import flet
from flet import (
    UserControl,
    Column,
    Row,
    TextField,
    FloatingActionButton,
    icons,
)
from task import Task


class TodoApp(UserControl):
    def build(self):
        self.new_task = TextField(hint_text="タスクを入力してください", expand=True)
        self.tasks = Column()
        self.task_view = Column(
            width=600,
            controls=[
                Row(
                    controls=[
                        self.new_task,
                        FloatingActionButton(icon=icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                self.tasks,
            ],
        )

        return self.task_view

    def add_clicked(self, e):
        task = Task(self.new_task.value, self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()
