"""


CLI-интерфейс для Менеджера задач.


"""

import argparse
import task_tracker as tt


def cli():
    parser = argparse.ArgumentParser()

    parser.add_argument("--add-task", help="Добавить новую задачу.")
    parser.add_argument(
        "--mark-task", help="Пометить задачу как `⏳ В процессе...` или `✅ Выполнено!`"
    )
    parser.add_argument("--task-list", help="Вывести список задач.")
    parser.add_argument(
        "--update-task", help="Обновить задачу."
    )
    parser.add_argument(
        "--remove-task", help="Удалить задачу из списка задач."
    )
    