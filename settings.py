import os


MONGODB_URI=os.environ['MONGODB_URI'] if 'MONGODB_URI' in os.environ else "mongodb://52.36.152.213/catchiorrineo"
