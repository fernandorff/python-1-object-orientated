from js import console
from datetime import datetime
tasks = []


def update_list():
    created_tasks = Element('created_tasks')
    created_tasks.element.innerText = ""
    for i in tasks:
        created_tasks.element.innerText += f"{i['content']}\n"


def create_task(*ags, **kags):
    danger_message = Element('danger_message')
    danger_message.element.style.display = 'none'
    input_task = Element('input_task')
    task = input_task.element.value

    list_filter = list(filter(lambda x: x['content'] == task, tasks))
    if len(list_filter) > 0:
        danger_message.element.style.display = 'flex'
        return none

    dictionary_task = {'task-id': len(task),
                       'content': task,
                       'date': datetime.now(),
                       'status': 'A'}

    console.log(dictionary_task)

    tasks.append(dictionary_task)
    input_task.element.value = ""
    update_list()

    def add_task_event(e):
        if e.key == 'Enter':
            create_task()

    input_task = Element('input_task')
    input_task.element.onkeypress = add_task_event
