from flask import Flask, request, jsonify
from tinydb import TinyDB

from helpers import (fields_name_intersect, fields_types_match, \
                     get_fields_and_types, get_proper_form)


db = TinyDB('db.json')
app = Flask(__name__)


@app.route('/get_form', methods=['POST'])
def get_form():
    data = request.form
    forms = db.all()
    form_name = get_proper_form(forms, data)
    if form_name:
        return jsonify({"template name": form_name})
    fields_and_types = get_fields_and_types(data)
    return jsonify(fields_and_types)

app.run(debug=True)




