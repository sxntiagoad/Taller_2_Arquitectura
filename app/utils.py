

import socket

from app.config import Config


def get_container_id():
    try: 
        container_id = socket.gethostname()
        return container_id
    except:
        return "LOCAL" 
    
def get_s3_image_url(image_name):
    bucket = Config.S3_BUCKET
    region = Config.AWS_REGION
    url = f"https://{bucket}.s3.{region}.amazonaws.com/{image_name}"
    return url
