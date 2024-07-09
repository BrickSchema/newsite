import glob
import rdflib

# for each file in static/schema/<version>/Brick.ttl, create an XML-encoded version
# in static/schema/<version>/Brick
for filename in glob.glob('static/schema/*/Brick.ttl'):
    version = filename.split('/')[2]
    g = rdflib.Graph()
    g.parse(filename, format='turtle')
    g.serialize(filename.rstrip('.ttl'), format='xml')

    # save a jsonld version too
    g.serialize(filename.replace('ttl', 'jsonld'), format='json-ld')
    print(f'Wrote {filename} to {filename.rstrip(".ttl")}')
