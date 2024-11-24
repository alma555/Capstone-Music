# some work with the musicbrainz database
# possibly obsolated by the Spotipy stuff? 

import musicbrainzngs as mb
import random

def get_relations(artist_id):
    return mb.get_artist_by_id(artist_id, includes=['artist-rels'])['artist']['artist-relation-list']

def get_release_groups(artist_id):
    return mb.get_artist_by_id(artist_id, includes=['release-groups'], release_type=['album', 'ep'])['artist']['release-group-list']

def get_member_projects(artist_id):
    get_relations(artist_id)
    return 0

#overall system
#get other projects of band members
#get albums by * (3)
#get album by bands they played with 
#get albums by (2)

# testing prompt; will eventually be user input
prompt = "Mountain Goats"
mb.set_useragent("capstone testing", 0.1, "almathompson@protonmail.com")

known = []
search = mb.search_artists(artist=prompt)
artist_id = search['artist-list'][0]['id']
members = get_relations(artist_id)
for i in members:
    depth_one = get_relations(i['artist']['id'])
    known.append(i['artist']['id'])
    for j in depth_one:
        if j['artist']['id'] in known:
            print('found')
        depth_two = get_relations(j['artist']['id'])
