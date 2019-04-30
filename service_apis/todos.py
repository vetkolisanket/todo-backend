import json

from flask_restful import Resource
from flask import request, abort, jsonify

from models.restresponse import RestResponse
from models.todos import Todo


class Todos(Resource):
    def get(self, todo_id=None):
        if not todo_id:
            return jsonify(todos=Todo.todos)
        for todo in Todo.todos:
            if todo['id'] == todo_id:
                # return RestResponse(status=True, data=todo).to_json()
                # return jsonify(todo)
                return todo
        return RestResponse(status=False, message="Not Found").to_json()

    def post(self):
        if not request.json:
            abort(400)
        todo = request.json
        todo = Todo(description=todo['description'], status=todo['status'])
        return todo.get_dict()