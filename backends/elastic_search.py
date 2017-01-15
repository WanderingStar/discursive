from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
from backends import config


def esconn():
    '''
    Create elastic search connection
    '''
    host = config.es_host
    awsauth = AWS4Auth(config.access_id, config.access_secret, config.aws_region, 'es')

    es = Elasticsearch(
        hosts=[{'host': host, 'port': 443}],
        http_auth=awsauth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection
    )
    return es


def create_es_index(index):
    '''

    '''

    es = esconn()
    # use this to delete an index
    if es.indices.exists(index=index):
        es.indices.delete(index=index)

    # use this to create an index
    settings = {
        'settings': {
            'number_of_shards': 1,
            'number_of_replicas': 0
        },
        'mappings': {
            'tweets': {
                'properties': {
                    'name': {'type': 'string'},
                    'message': {'type': 'string'},
                    'description': {'type': 'string'},
                    'loc': {'type': 'string'},
                    'text': {'type': 'string', 'store': 'true'},
                    'user_created': {'type': 'date'},
                    'followers': {'type': 'long'},
                    'id_str': {'type': 'string'},
                    'created': {'type': 'date', 'store': 'true'},
                    'retweet_count': {'type': 'long'},
                    'friends_count': {'type': 'long'},

                    # These fields are synthesized from other metadata
                    'topics': {'type': 'string', 'store': 'true'},
                    'retweet': {'type': 'string'},
                    'hashtags': {'type': 'string', 'store': 'true'},
                    'original_id': {'type': 'string'},
                    'original_name': {'type': 'string'}
                }
            }
        }
    }
    es.indices.create(index=index, body=settings)

    # check if the index now exists
    if es.indices.exists(index=index):
        print('Created the index')
    else:
        print('Something went wrong. The index was not created.')


if __name__ == '__main__':
    create_es_index('twitter')
