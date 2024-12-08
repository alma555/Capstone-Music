# some work with the musicbrainz database
# possibly obsolated by the Spotipy stuff? 

import musicbrainzngs as mb
import random

def get_relations(artist_id):
    return mb.get_artist_by_id(artist_id, includes=['artist-rels'])['artist']['artist-relation-list']

def get_release_groups(artist_id):
    return mb.get_artist_by_id(artist_id, includes=['release-groups'], release_type=['album', 'ep'])['artist']['release-group-list']

def get_results(artist_id):
    project_members = get_relations(artist_id)
    results = []
    # it would be wise to rewrite this as a recursive function
    depth_one = [random.choice(project_members),random.choice(project_members),random.choice(project_members),
                random.choice(project_members),random.choice(project_members),random.choice(project_members),
                random.choice(project_members),random.choice(project_members),random.choice(project_members)]
    for i in depth_one:
        depth_two = get_relations(i['artist']['id']) #bands members are in
        depth_two = random.choice(depth_two)
        depth_three = random.choice(get_relations(depth_two['artist']['id'])) #members of bands members are in
        depth_four = random.choice(get_relations(depth_three['artist']['id'])) #bands of members of bands members are in
        results.append(depth_four)
    return results

def return_artist_list(db_list):
   names_list = []
   for i in db_list:
       names_list.append(i)
   return names_list

def produce_list(prompt):
    final_list = []
    search = mb.search_artists(artist=prompt)
    artist_id = search['artist-list'][0]['id']
    artist_list = return_artist_list(get_results(artist_id))
    for i in artist_list:
        if i['artist']['id'] != artist_id:
            releases = get_release_groups(i['artist']['id'])
            if releases != []:
                pick = random.choice(releases)
                final_list.append(pick['title'])
    return final_list

mb.set_useragent("capstone testing", 0.1, "almathompson@protonmail.com")
# testing prompt; will eventually be user input
prompt = "The Killers"

final_list = produce_list(prompt)
print(final_list)
