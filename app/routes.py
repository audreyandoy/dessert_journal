from flask import Blueprint, json, jsonify, request, abort, make_response
from app.models.dessert import Dessert
from app import db 

desserts_bp = Blueprint("desserts_bp", __name__, url_prefix="/desserts")

def validate_req_body(body):
    if "name" not in body or "description" not in body:
        return abort(make_response(jsonify("Invalid Request"), 400))

@desserts_bp.route("", methods=["POST"])
def create_dessert():
    req_body = request.get_json()
    validate_req_body(req_body)
    new_dessert = Dessert.from_dict(req_body)
    db.session.add(new_dessert)
    db.session.commit()
    
    return jsonify(f"{new_dessert.name} has been successfully created"), 201

@desserts_bp.route("", methods=["GET"])
def read_all_desserts():
    desserts = Dessert.query.all()
    desserts_response = [ dessert.to_dict() for dessert in desserts]
    return jsonify(desserts_response), 200

@desserts_bp.route("/<id>", methods=["GET"])
def read_one_dessert(id):
    try:
        id = int(id)
    except ValueError:
        abort(make_response({"message": f"dessert {id} is invalid"}, 400))
        
    dessert = Dessert.query.get(id)
    
    if not dessert:
        return abort(make_response({"message": f"dessert {id} not found"}, 404))

    return {
            "id": dessert.id,
            "name": dessert.name,
            "description": dessert.description
        }

@desserts_bp.route("/<id>", methods=["PUT"])
def update_one_dessert(id):
    try:
        id = int(id)
    except ValueError:
        abort(make_response({"message": f"dessert {id} is invalid"}, 400))

    dessert = Dessert.query.get(id)
    request_body = request.get_json()
    dessert.update(request_body)
    db.session.commit()
    return jsonify(f"Dessert {dessert.id} successfully updated"), 200

@desserts_bp.route("/<id>", methods=["DELETE"])
def delete_one_dessert(id):
    try:
        id = int(id)
    except ValueError:
        abort(make_response({"message": f"dessert {id} is invalid"}, 400))

    dessert = Dessert.query.get(id)
    
    if not dessert:
        return abort(make_response({"message": f"dessert {id} not found"}, 404))
    
    db.session.delete(dessert)
    db.session.commit()
    return jsonify(f"Dessert {dessert.id} successfully deleted"), 200

##################################################
#               Review Routes                    #
##################################################

reviews_bp = Blueprint("reviews_bp", __name__, url_prefix="/reviews")

@reviews_bp.route("", methods=["POST"])
def create_review():
    pass
