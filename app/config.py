import os

class Config:
    """
    Configuración de la aplicación
    Lee las variables de entorno para AWS S3
    """
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_REGION = os.getenv('AWS_REGION', 'us-east-2')
    S3_BUCKET = os.getenv('S3_BUCKET')