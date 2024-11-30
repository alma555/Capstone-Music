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

def get_results(artist_id):
    project_members = get_relations(artist_id)
    results = []
    # it would be wise to rewrite this as a recursive function
    for i in project_members:
        depth_one = get_relations(i['artist']['id']) #bands members are in
        for j in depth_one:
            results.append(j)
            j['artist']['id']
            depth_two = get_relations(j['artist']['id']) #members of bands members are in
            for k in depth_two:
                results.append(k)
                depth_three = get_relations(k['artist']['id']) #bands of members of bands members are in
                for l in depth_three:
                    results.append(l)
    return results

def return_artist_list(db_list):
   names_list = []
   for i in db_list:
       names_list.append(i['artist']['name'])
   names_list = list(set(names_list)) #remove duplicates
   return names_list

# testing prompt; will eventually be user input
prompt = "Mountain Goats"
mb.set_useragent("capstone testing", 0.1, "almathompson@protonmail.com")

search = mb.search_artists(artist=prompt)
artist_id = search['artist-list'][0]['id']
print(return_artist_list(get_results(artist_id)))
