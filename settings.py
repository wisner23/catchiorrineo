import os


MONGODB_URI=os.environ['MONGODB_URI'] if 'MONGODB_URI' in os.environ else "52.36.152.213"

AUTH0_DOMAIN = 'catchiorrineo.auth0.com'
API_AUDIENCE = "https://catchiorrineo.auth0.com/api/v2/"
ALGORITHMS = ["RS256"]