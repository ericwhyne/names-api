#!/usr/bin/python
from flask import Flask
from flask import request
import random
app = Flask(__name__)
port = 8080

with open('female-names.txt') as f:
    female_names = f.read().splitlines()

@app.route('/')
def hello_root():
    return 'Names API, does stuff with names'

@app.route('/randfemale')
def rand_female():
    num = int(request.args.get('num'))
    random_names = list(map(lambda _: random.choice(female_names), range(num)))
    names = '<br>'.join(random_names)
    return 'Random Female Name API ' + str(num) + "<br><br>" + names

if __name__ == '__main__':
    #app.run(host='0.0.0.0',port=port,debug=True)
    app.run(host='0.0.0.0',port=port,threaded=True)
    print "App running..."
