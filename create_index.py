from backends import elastic_search

if __name__ == '__main__':
    elastic_search.create_es_index('twitter')
