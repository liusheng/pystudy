import json
from collections import defaultdict

tree = lambda: defaultdict(tree)


# Usages:
users = tree()
users['harold']['username'] = 'hrldcpr'
users['handler']['username'] = 'matthandlersux'
json.dumps(users, sort_keys=True, indent=4, separators=(',', ': '))

# FYI: https://gist.github.com/hrldcpr/2012250
