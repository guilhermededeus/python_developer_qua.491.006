import flet as ft


class Task(ft.Column):
    def __init__(self, task_name, task_status_change, task_delete):
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete

 
        self.display_task = ft.Checkbox(
            value=False,
            label=self.task_name,
            on_change=self.status_changed
        )

     
        self.controls = [
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    self.display_task,
                    ft.IconButton(
                        icon=ft.Icons.DELETE_OUTLINE,
                        tooltip="Excluir tarefa",
                        on_click=self.delete_clicked,
                    ),
                ],
            )
        ]

    def status_changed(self, e):
        self.completed = self.display_task.value
        self.task_status_change()


    def delete_clicked(self, e):
        self.task_delete(self)

class TodoApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(hint_text="O que você quer fazer?", expand=True)
        self.tasks = ft.Column()
        self.items_left = ft.Text("0 tarefas ativas")

        self.filter = ft.Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[
                ft.Tab(text="Todos"),
                ft.Tab(text="Ativos"),
                ft.Tab(text="Finalizados"),
            ],
        )

        self.width = 600
        self.controls = [
            ft.Row(
                [ft.Text(value="To-do APP", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(
                        icon=ft.Icons.ADD,
                        on_click=self.add_clicked
                    ),
                ],
            ),
            ft.Column(
                spacing=25,
                controls=[
                    self.filter,
                    self.tasks,
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            self.items_left,
                            ft.OutlinedButton(
                                text="Limpar finalizados", on_click=self.clear_clicked
                            ),
                        ],
                    ),
                ],
            ),
        ]

  
    def add_clicked(self, e):
        if self.new_task.value and self.new_task.value.strip():
            task = Task(self.new_task.value.strip(), self.task_status_change, self.task_delete)
            self.tasks.controls.append(task)
            self.new_task.value = ""
            self.update()

    # Excluir tarefa
    def task_delete(self, task):
        try:
            self.tasks.controls.remove(task)
            self.update()
        except ValueError:
            pass

    def before_update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0
        for task in self.tasks.controls:
            task.visible = (
                status == "Todos"
                or (status == "Ativos" and not task.completed)
                or (status == "Finalizados" and task.completed)
            )
            if not task.completed:
                count += 1
        self.items_left.value = f"{count} tarefa(s) ativa(s)"

    def tabs_changed(self, e):
        self.update()

    def task_status_change(self, e=None):
        self.update()

    def clear_clicked(self, e):
        for task in self.tasks.controls[:]:
            if task.completed:
                self.task_delete(task)


def main(page: ft.Page):
    page.title = "Tarefas"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    todo = TodoApp()
    page.add(todo)
    page.update()


if __name__ == "__main__":
    ft.app(target=main)