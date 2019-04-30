import json

from flask_restful import Resource
from flask import request, abort, jsonify

from models.restresponse import RestResponse
from models.todos import Todo
from utils.utils import error_response


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
            error_response(400, 'Body required!')
        todo = request.json
        todo = Todo(description=todo['description'], status=todo['status'])
        return todo.get_dict()

    def put(self, todo_id):
        if not todo_id:
            error_response(400, 'id not found')
        if not request.json:
            error_response(400, 'Body required!')
        body = request.json        # validate json body
        for todo in Todo.todos:
            if todo['id'] == todo_id:
                todo['description'] = body['description']
                todo['status'] = body['status']
                return todo
        error_response(404, 'Not Found!')