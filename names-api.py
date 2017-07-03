#!/usr/bin/python
from flask import Flask
from flask import request
import random
app = Flask(__name__)
port = 8080

with open('data/female-names.txt') as f:
    female_names = f.read().splitlines()
with open('data/male-names.txt') as f:
    male_names = f.read().splitlines()


def rand_names(names_list):
    random_names = []
    if request.args.get('num'):
        num = int(request.args.get('num'))
        if 1 <= num <= len(names_list):
            random_names = list(map(lambda _: random.choice(names_list), range(num)))
        else:
            return "Error: num must be within range 1 to " + str(len(names_list))
    else:
        return "Error: please specify a value for num"
    names = '<br>'.join(random_names)
    return names

@app.route('/')
def hello_root():
    return 'Names API, does stuff with names'

@app.route('/randfemale')
def rand_female():
    return rand_names(female_names)

@app.route('/randmale')
def rand_male():
    return rand_names(male_names)

if __name__ == '__main__':
    #app.run(host='0.0.0.0',port=port,debug=True)
    app.run(host='0.0.0.0',port=port,threaded=True)
    print "App running..."

