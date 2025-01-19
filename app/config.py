import os


class Config:
    default_key = '5c48e1550e2a493c3c8f4ae487f0e4b1a84353709ddaeb8d5368ddcd0f795b3d'
    COINGECKO_API_KEY = os.environ.get('COINGECKO_API_KEY',
                                       'CG-XoAjK3A3LnDVfVB5T8JrjTbv')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', default_key)
    PAGINATION_DEFAULT = 10
    PAGINATION_MAX = 50
