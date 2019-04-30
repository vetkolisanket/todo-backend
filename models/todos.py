class Todo:
    id = 1
    todos = []

    def __init__(self, description, status):
        self.id = Todo.id
        Todo.id += 1
        self.description = description
        self.status = status
        Todo.todos.append(self.get_dict())

    def get_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'status': self.status
        }