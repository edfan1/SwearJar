import os

# Database configuration
POSTGRES_USER = os.environ.get('POSTGRES_USER', 'flaskuser')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'flaskpassword')
POSTGRES_DB = os.environ.get('POSTGRES_DB', 'flaskapp')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'postgres')

SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Secret key for session management
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')