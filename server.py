from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

counts = {'GET': 0, 'POST': 0, 'PUT': 0, 'DELETE': 0}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/request-counter', methods=['GET', 'POST', 'PUT', 'DELETE'])
def count():
    global counts

    counts[request.method] += 1
    print(counts)

    return redirect('/')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )