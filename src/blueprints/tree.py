from flask import Blueprint, request, jsonify

from src.node import Node

tree_bp = Blueprint('tree', __name__, url_prefix='/tree')
nodes_tree = Node()


@tree_bp.route('/', methods=('POST',))
def create_tree():
    """
    Body example:
    {
        "values": [
                [70, 84, 85],
                [70, 84, 78, 80],
                [70, 84, 78, 76],
                [70, 49, 54, 51],
                [70, 49, 37, 40],
                [70, 49, 37, 22]
            ]
    }
    :return:
    """
    body = request.json.get('values')
    [nodes_tree.insert(x) for y in body for x in y]

    return jsonify({'message': 'tree created'})


@tree_bp.route('/', methods=('GET', ))
def get_nearest_ancestor():
    """
    Parameters required: successor_a and successor_b
    Ex.
    ?successor_a=40&successor_b=78

    :return:
    """
    successor_a = int(request.args.get('successor_a'))
    successor_b = int(request.args.get('successor_b'))
    ancestor = nodes_tree.is_parent(successor_a, successor_b)

    return jsonify({'ancestor': ancestor})


@tree_bp.route('/', methods=('DELETE',))
def clean_tree():
    nodes_tree.clean()
    return jsonify({'message': 'Tree deleted'})

