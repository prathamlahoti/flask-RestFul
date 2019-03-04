import re
import os
from options import RESULT_STATUS, data_template
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask import Response


app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
mongo = PyMongo(app)


@app.route('/heroes', methods=['GET'])
def get_heroes():
    """ List of all heroes.

        :returns: a list of all heroes.
     """
    heroes_info = [data_template(hero) for hero in mongo.db.lost_hero.find()]
    return jsonify({'Heroes Info': heroes_info})


@app.route('/hero/<string:hero_name>', methods=['GET'])
def get_hero_by_hero_name(hero_name: str):
    """ Information about particular hero.

        :param hero_name: name of a hero to find.
    """
    hero = mongo.db.lost_hero.find_one_or_404({'hero_name': hero_name})
    return jsonify({'Hero Info': data_template(hero)})


@app.route('/hero/add', methods=['POST'])
def add_hero():
    """ Adds a new hero to the document.

        :returns: List of all heroes.
    """
    cursor = mongo.db.lost_hero
    # Inserting received json data, sent by user
    # force=True allows to ignore the mimetype and always try to parse JSON
    cursor.insert_one({
        'actor_name': request.get_json(force=True).get('actor_name'),
        'hero_name':  request.get_json(force=True).get('hero_name'),
        'hero_rate':  request.get_json(force=True).get('hero_rate')
    })
    heroes_info = [data_template(hero) for hero in cursor.find()]
    return jsonify({'Heroes_Info': heroes_info})


@app.route('/hero/update/<string:hero_name>', methods=['PUT'])
def update_hero(hero_name: str):
    """ Updates existing hero info by hero_name.

        :param hero_name: Name of a hero.
        :returns: List of all heroes.
    """
    hero = mongo.db.lost_hero.find_one_or_404({'hero_name': hero_name})

    # Receiving json data, sent by user
    # force=True allows to ignore the mimetype and always try to parse JSON
    hero['hero_name'] = request.get_json(force=True).get('actor_name')
    hero['actor_name'] = request.get_json(force=True).get('hero_name')
    hero['hero_rate'] = request.get_json(force=True).get('hero_rate')
    # Saving updated info
    mongo.db.lost_hero.save(hero)
    heroes_info = [data_template(hero) for hero in mongo.db.lost_hero.find()]
    return jsonify({'Heroes Info': heroes_info})


@app.route('/hero/delete/<string:hero_name>', methods=['DELETE'])
def delete_hero(hero_name: str):
    """ Deletes hero info by hero_name

        :param hero_name: Name of a hero.
        :returns: List of all heroes.
     """
    template = re.compile(f"^{hero_name}", re.IGNORECASE)
    mongo.db.lost_hero.delete_one({'hero_name': template})
    heroes_info = [data_template(hero) for hero in mongo.db.lost_hero.find()]
    return jsonify({'Heroes_Info': heroes_info})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)
