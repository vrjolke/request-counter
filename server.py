from flask import Flask, render_template, request, redirect, url_for
import data_mgr

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/request-counter', methods=['GET', 'POST', 'PUT', 'DELETE'])
def count():
    data_mgr.method_to_file(request.method, 'request_counts.txt')
    return redirect('/')

@app.route('/statistics', methods=['POST'])
def stats():
    text_dictionary = data_mgr.text_to_dict('request_counts.txt')
    return render_template('stats.html', text = text_dictionary)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )