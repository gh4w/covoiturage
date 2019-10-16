# coding:utf-8

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/demo/', methods=['GET'])
def reponse():
    nom = request.args.get("nom", None)
    reponse = {}
    if not nom:
        reponse["ERROR"] = "pas de nom fourni, svp fournissez un nom."
    else:
        reponse["MESSAGE"] = "Bonjour {}. Pas grand chose ici pour l'instant.".format(nom)

    return jsonify(reponse)


@app.route('/')
def index():
    return "<h1>Bienvenue dans Karpoule !</h1>"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)

