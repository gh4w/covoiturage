#!/usr/bin/env python3
# coding:utf-8

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/demo/', methods=['GET'])
def reponse():
    nom = request.args.get("nom", None)
    print("reçu le nom: {}".format(nom))

    reponse = {}
    if not nom:
        reponse["ERROR"] = "pas de nom fourni, svp fournissez un nom."
    else:
        reponse["MESSAGE"] = "Salut {}. Pas grand chose ici pour l'instant.".format(nom)

    return jsonify(reponse)


@app.route('/')
def index():
    return "<h1>Y a quelqu'un ?</h1>"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)

