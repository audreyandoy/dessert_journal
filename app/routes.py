from flask import Blueprint, json, jsonify, request, abort, make_response
from app.models.dessert import Dessert
from app.models.review import Review
from app import db 
from .helper_routes import validate_record
from datetime import datetime

desserts_bp = Blueprint("desserts_bp", __name__, url_prefix="/desserts")

@desserts_bp.route("", methods=["POST"])
def create_dessert():
    request_body = request.get_json()

    # guard clause
    if "name" not in request_body or "description" not in request_body:
        return jsonify("Invalid Request"), 400

    new_dessert = Dessert.create(request_body)

    db.session.add(new_dessert)
    db.session.commit()
    
    return jsonify(f"{new_dessert.name} has been successfully created"), 201

@desserts_bp.route("", methods=["GET"])
def read_all_desserts():
    desserts = Dessert.query.all()
    desserts_response = [ dessert.to_dict() for dessert in desserts]
    print(desserts)
    return jsonify(desserts_response), 200

@desserts_bp.route("/<id>", methods=["GET"])
def read_one_dessert(id):
    dessert = validate_record(Dessert, id)
    return dessert.to_dict()

@desserts_bp.route("/<id>", methods=["PUT"])
def update_one_dessert(id):
    dessert = validate_record(Dessert, id)
    request_body = request.get_json()
    dessert.update(request_body)
    db.session.commit()
    return jsonify(f"Dessert {dessert.id} successfully updated"), 200

@desserts_bp.route("/<id>", methods=["DELETE"])
def delete_one_dessert(id):
    dessert = validate_record(Dessert, id)
    db.session.delete(dessert)
    db.session.commit()
    return jsonify(f"Dessert {dessert.id} successfully deleted"), 200

@desserts_bp.route("/<id>/reviews", methods=["GET"])
def read_all_reviews_for_dessert(id):
    dessert = validate_record(Dessert, id)
    dessert_reviews = [review.to_dict() for review in dessert.reviews]
    return jsonify(dessert_reviews)

##################################################
#               Review Routes                    #
##################################################

reviews_bp = Blueprint("reviews_bp", __name__, url_prefix="/reviews")
@reviews_bp.route("", methods=["POST"])
def create_dessert_review():
    request_body = request.get_json()
    new_review = Review(
        description = request_body["description"],
        rating = request_body["rating"],
        dessert_id = request_body["dessert_id"],
        dateTime = datetime.utcnow()
    )
    db.session.add(new_review)
    db.session.commit()
    return jsonify(f"{new_review.description} for Dessert {request_body['dessert_id']} has been successfully created"), 201


@reviews_bp.route("", methods=["GET"])
def read_all_reviews():
    reviews = Review.query.all()
    reviews_response = [review.to_dict() for review in reviews]
    print(reviews)
    return jsonify(reviews_response), 200

