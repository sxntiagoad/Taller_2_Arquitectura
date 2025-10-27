

import random

from flask import Blueprint, render_template

from app.pokeneas import POKENEAS
from app.utils import get_container_id, get_s3_image_url


bp = Blueprint('pokenea_web', __name__)

@bp.route("/", methods=["GET"])
def index():
    random_pokenea = random.choice(POKENEAS)

    container_id = get_container_id()

    image_url = get_s3_image_url(random_pokenea['imagen'])

    pokenea_con_url = random_pokenea.copy()
    pokenea_con_url['imagen'] = image_url
    
    return render_template(
        "index.html",
        pokenea=pokenea_con_url,
        container_id=container_id
    )
    
