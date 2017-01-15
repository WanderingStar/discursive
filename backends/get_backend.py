import settings
from backends import elastic_search


class Backend():
    '''create backend'''

    def __init__(self):
        if settings.backend in ['ES', 'SQLITE', 'FILE', 'S3']:
            self.backend = settings.backend

    def setup(self):
        if self.backend == 'ES':
            datastore = elastic_search.esconn()
            return datastore

        # Return SQL Lite DB
        # Return file path
        # Return S3 connection
