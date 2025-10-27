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
    
    # Formato correcto de URL de S3
    # Opción 1: Virtual-hosted-style URL (recomendado)
    url = f"https://{bucket}.s3.{region}.amazonaws.com/{image_name}"
    
    # Si no funciona, prueba:
    # Opción 2: Path-style URL
    # url = f"https://s3.{region}.amazonaws.com/{bucket}/{image_name}"
    
    # Debug
    print(f"DEBUG - S3 URL generada: {url}")
    print(f"DEBUG - Bucket: {bucket}, Region: {region}, Image: {image_name}")
    
    return url
