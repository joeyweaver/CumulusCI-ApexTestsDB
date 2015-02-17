import os
import json
from testresults.importer import import_test_results

results_dir = 'results'

for fname in os.listdir(results_dir):
    full_path = '%s/%s' % (results_dir, fname)
    print full_path
    f = open(full_path, 'r')
    results = json.loads(f.read())
    import_test_results(results)
    f.close()
