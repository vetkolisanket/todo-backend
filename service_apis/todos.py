import json

from flask_restful import Resource
from flask import request, abort, jsonify

from models.restresponse import RestResponse
from models.todos import Todo
from utils.utils import error_response, ok_response, StatusCodes


class Todos(Resource):
    def get(self, todo_id=None):
        if not todo_id:
            return ok_response({"todos": Todo.todos.values()})
        try:
            return ok_response(Todo.todos[todo_id])
        except KeyError as e:
            return error_response(404, 'Todo with id {} not found'.format(e.message))

    def post(self):
        if not request.json:
            return error_response(400, 'Body required!')
        todo = request.json  # add validation for json body
        todo = Todo(description=todo['description'], status=todo['status'])
        return ok_response(todo.get_dict(), code=StatusCodes.CREATED)

    def put(self, todo_id=None):
        if not todo_id:
            return error_response(405, 'id not found')
        if not request.json:
            return error_response(400, 'Body required!')
        body = request.json        # validate json body
        try:
            todo = Todo.todos[todo_id]
            todo['description'] = body['description']
            todo['status'] = body['status']
            return ok_response(todo)
        except KeyError as e:
            return error_response(404, 'Todo with id {} not found'.format(e.message))

    def patch(self, todo_id=None):
        if not todo_id:
            return error_response(400, 'id not found')
        if not request.json:
            return error_response(400, 'Body required!')
        body = request.json
        try:
            todo = Todo.todos[todo_id]
            todo['status'] = body['status']
            return ok_response(todo)
        except KeyError as e:
            return error_response(404, 'Todo with id {} not found'.format(e.message))

    def delete(self, todo_id=None):
        if not todo_id:
            return error_response(404, 'Todo with id {} not found'.format(todo_id))
        try:
            Todo.todos.pop(todo_id)
            return ok_response("Success")
        except KeyError as e:
            return error_response(404, 'Todo with id {} not found'.format(e.message))
