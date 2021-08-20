import os
import pandas as pd
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
#app.config["DEBUG"] = True


data = pd.read_excel('dogs.xlsx', usecols=['Breed', 'Eyes', 'Background', 'Drug', 'Clothing', 'Accessory', 'Rarity', 'Rank'])

dogs = []

for row in data.itertuples(index=True, name='Pandas'):
    meta = {
        'name': f'TrapDog #{row.Index}',
        'external_url': 'https://trapdogs.app/',
        'index': row.Index,
        'attributes': [
            {'trait_type':'Breed', 'value':row.Breed},
            {'trait_type':'Eyes', 'value':row.Eyes},
            {'trait_type':'Background', 'value':row.Background},
            {'trait_type':'Drug', 'value':row.Drug},
            {'trait_type':'Clothing', 'value':row.Clothing},
            {'trait_type':'Accessory', 'value':row.Accessory},
            {'trait_type':'Rarity', 'value':row.Rarity},
            {'trait_type':'Rank', 'value':row.Rank}
            ],
        'image': f'https://trapdogs.app/images/{row.Index}.gif'
        }        
    
    dogs.append(meta)

@app.route('/api/trapDogMeta', methods=['GET'])
def api_index():
    # Check if an index was provided as part of the URL.
    # If index is provided, assign it to a variable.
    # If no index is provided, display an error in the browser.
    if 'index' in request.args:
        index = int(request.args['index'])
    else:
        return "Error: Please provide a valid token ID"

    # Create an empty list for our results
    #results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    if 0<=index<10000:
        for dog in dogs:
            if dog['index'] == index:
                result = dog
    else:
        result = 'null'

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)