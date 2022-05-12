from flask import Blueprint, json, jsonify, request, abort, make_response

def validate_record(cls, id):
    try:
        id = int(id)
    except ValueError:
        abort(make_response({"message": f"{cls} {id} is invalid"}, 400))
        
    obj = cls.query.get(id)
    
    if not obj:
        return abort(make_response({"message": f"{cls} {id} not found"}, 404))

    return obj