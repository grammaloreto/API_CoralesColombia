from flask import Flask, jsonify, request

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

@app.route('/corals', methods=['POST'])
def addCoral():
    new_coral = {
       'name': request.json['name'],
       'common name': request.json['common name'],
       'notes': request.json['notes']
    }
    corals.append(new_coral)
    return jsonify({'message': 'Coral added succesfully', 'corals': corals})

@app.route('/corals/<string:Coral_name>', methods = ['PUT'])
def editCoral(Coral_name):
    coralFound = [coral for coral in corals if coral['name'] == Coral_name]
    if (len(coralFound) > 0):
        coralFound[0]['name'] = request.json['name'],
        coralFound[0]['common name'] = request.json ['common name'],
        coralFound[0]['notes'] = request.json['notes']
        return jsonify({
            'message': 'Coral Update',
            'coral': coralFound[0]
        })   
    return jsonify({'message': 'Coral Not Found'})

@app.route('/corals/<string:Coral_name>', methods=['DELETE'])
def deleteCoral(Coral_name):
    coralsFound = [coral for coral in corals if coral['name'] == Coral_name]
    if len(coralsFound) > 0:
        corals.remove(coralsFound)
        return jsonify({
            'message': 'Coral deleted',
            'corals': corals
        })
    return jsonify({'message': 'Coral not found'})    

if __name__ == '__main__':
    app.run(debug=True, port=4000)