from flask import Flask, jsonify

app = Flask(__name__)

from corals import corals


@app.route ('/corals')   
def getcorals():
    return jsonify({'corals': corals, 'message': 'corals list'})

@app.route ('/corals/<string:Coral_name>')
def get_coral(Coral_name):
    coralsFound = [coral for coral in corals if coral ['name'] == Coral_name ]
    if (len(coralsFound) > 0):
       return jsonify ({'coral':coralsFound [0]})
    return jsonify({'message': 'coral not present'})


if __name__ == '__main__':
    app.run(debug=True, port=4000)