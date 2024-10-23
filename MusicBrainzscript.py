# some work with the musicbrainz database
# possibly obsolated by the Spotipy stuff Richang wrote? 

import musicbrainzngs as mb
import random

# testing prompt; will eventually be user input
prompt = "Mountain Goats"
mb.set_useragent("capstone testing", 0.1, "almathompson@protonmail.com")

result = mb.search_artists(artist=prompt)
artist_id = result['artist-list'][0]['id']
release_groups = mb.get_artist_by_id(artist_id, includes=['release-groups'], release_type=['album', 'ep'])['artist']['release-group-list']
relations = mb.get_artist_by_id(artist_id, includes=['artist-rels'])['artist']['artist-relation-list']
for i in relations:
    linked_artist_id = i['artist']['id'])
    mb.get_artist_by_id(linked_artist_id, includes= 
print(relations)

#overall system
#get other projects of band members
#get albums by * (3)
#get album by bands they played with 
#get albums by (2)


