

import random
from flask import Blueprint, jsonify
from app.pokeneas import POKENEAS
from app.utils import get_container_id

bp = Blueprint('pokenea_api', __name__)

@bp.route("/random_pokenea", methods=["GET"])
def random_pokenea():
    container_id = get_container_id()
    p = random.choice(POKENEAS)
    return jsonify(
        {
            "id": p['id'],
            "nombre": p['nombre'],
            "altura": p['altura'],
            "habilidad": p['habilidad'],
            "container_id": container_id
        }
    )

