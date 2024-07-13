from prometheus_client import Counter
from prometheus_client import Gauge


#initialise a prometheus counter
class Metrics:
    post_created = Counter('post_created', 'total number of post created')
    post_retrieved = Counter('post_retrieved', 'total number of post retrieved')
    post_listed = Counter('post_listed', 'total number of post listed')
    post_updated = Counter('post_updated', 'total number of post updated')

    score_created = Counter('score_created', 'total number of score created')
    score_retrieved = Counter('score_retrieved', 'total number of score retrieved')
    score_listed = Counter('score_listed', 'total number of score listed')
    score_updated = Counter('score_updated', 'total number of score updated')

    