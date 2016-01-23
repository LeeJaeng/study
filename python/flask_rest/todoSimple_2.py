from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}


class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


class Todo1(Resource):
    def get(self):
        return {'task': 'Hello World'}

class Todo2(Resource):
    def get(self):
        return {'task': 'Hello World'}, 201

class Todo3(Resource):
    def get(self):
        return {'task': 'Hello World'}, 201, {'Etag': 'some-opaque-string'}


api.add_resource(TodoSimple, '/<string:todo_id>')
api.add_resource(Todo1, '/todo1')
api.add_resource(Todo2, '/todo2')
api.add_resource(Todo3, '/todo3')


if __name__ == '__main__':
    app.run(debug=True)