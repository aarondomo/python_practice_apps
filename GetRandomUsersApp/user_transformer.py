import json
from types import SimpleNamespace

def parse_user(data):
	# Parse JSON into an object with attributes corresponding to dict keys.
	return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))

