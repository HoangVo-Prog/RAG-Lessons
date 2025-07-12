import nbformat
import sys

path = sys.argv[1]
nb = nbformat.read(path, as_version=4)

# Remove problematic metadata
if 'widgets' in nb['metadata']:
    del nb['metadata']['widgets']

nbformat.write(nb, path)