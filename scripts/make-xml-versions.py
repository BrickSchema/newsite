import glob
import rdflib

# for each file in static/schema/<version>/Brick.ttl, create an XML-encoded version
# in static/schema/<version>/Brick
for filename in glob.glob('static/schema/*/Brick.ttl'):
    version = filename.split('/')[2]
    g = rdflib.Graph()
    g.parse(filename, format='turtle')
    g.serialize(filename.rstrip('.ttl'), format='xml')
    print('Wrote XML version of', filename, 'to', filename.rstrip('.ttl'))
