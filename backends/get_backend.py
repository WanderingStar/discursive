import os
import dataset

import settings
from backends import elastic_search


class Backend():
    '''create backend'''

    def __init__(self):
        if settings.BACKEND in ['ES', 'SQLITE', 'FILE', 'S3']:
            self.backend = settings.BACKEND

    def setup(self):
        if self.backend == 'ES':
            datastore = elastic_search.esconn()
            return datastore

        elif self.backend == 'SQLITE':
            db_path = os.path.join(settings.DATA_DIR, settings.DATABASE_NAME)
            datastore = dataset.connect("sqlite:///{}.sqlite".format(db_path))
            return datastore
