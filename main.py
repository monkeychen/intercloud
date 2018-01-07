from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
todoMap = {}


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'python world!'}


class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todoMap[todo_id]}

    def put(self, todo_id):
        todoMap[todo_id] = request.form['data']
        return {todo_id: todoMap[todo_id]}


class Echo(Resource):
    def get(self, msg):
        return {'reply': msg}

api.add_resource(HelloWorld, '/')
api.add_resource(TodoSimple, '/<string:todo_id>')
api.add_resource(Echo, '/echo/<string:msg>')

if __name__ == '__main__':
    app.run(debug=True)
