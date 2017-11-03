from flask import Flask, request

app = Flask(__name__)


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def home(path):
    print(request.method)
    # print(request.headers)
    # print(request.data)
    # print(request.form)
    # print(request.get_json())
    return 'Hello ' + path



app.run('localhost', 2345, debug=True)