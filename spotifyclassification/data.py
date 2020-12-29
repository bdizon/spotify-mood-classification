'''
Visualize and organize Spotify seed attribute data
'''
import spotipy
from functions import *
import csv
from oauth import OAuth
import pandas as pd
import time


watson_sentiments = ['sadness_score','joy_score','fear_score','disgust_score','anger_score']
sentiments = ['sadness_score','joy_score','anger_score']
happy = "happy"
sad = "sad"
angry = "angry"

num_angry = 9
num_sad = 12
num_happy = 11

def track_info(sp, index, tracks):
        '''
        Get track details
        Parameter Spotipy client object, dictionary of track details and index of the track
        Returns track uri and name
        '''
        track_uri = tracks['items'][index]['track']['uri']
        track_name = tracks['items'][index]['track']['name']
        return track_uri, track_name

def artist_info(sp, index, tracks):
        '''
        Get artist details
        Parameter Spotipy client object, dictionary of track details and index of the track
        Returns artist_uri, artist_name, genre, popularity, followers
        '''
        artist_uri = tracks['items'][index]['track']['artists'][0]['uri']
        artist_name = tracks['items'][index]['track']['artists'][0]['name']
        artist_info = sp.artist(artist_uri)
        # print(len(artist_info['genres']))
        if len(artist_info['genres']) > 0:
                genre = artist_info['genres'][0] # grab the first genre from list of genres
        else:
                genre = "na" # genre not available
        popularity = artist_info['popularity']
        followers = artist_info['followers']['total']
        return artist_uri, artist_name, genre, popularity, followers

def attribute_info(sp, mood, track_uri, track_details):
        '''
        Get a track's Spotify seed attributes details
        Parameter Spotipy client object, mood of track, track uri, dictionary of track details, dictionary with all the track data
        '''
        audio_info = sp.audio_features(track_uri)
        danceability = audio_info[0]['danceability']
        track_details['danceability'] = danceability
        energy = audio_info[0]['energy']
        track_details['energy'] = energy
        key = audio_info[0]['key']
        track_details['key'] = key
        loudness = audio_info[0]['loudness']
        track_details['loudness'] = loudness
        mode = audio_info[0]['mode']
        track_details['mode'] = mode
        speechiness = audio_info[0]['speechiness']
        track_details['speechiness'] = speechiness
        acousticness = audio_info[0]['acousticness']
        track_details['acousticness'] = acousticness
        instrumentalness = audio_info[0]['instrumentalness']
        track_details['instrumentalness'] = instrumentalness
        liveness = audio_info[0]['liveness']
        track_details['liveness'] = liveness
        valence = audio_info[0]['valence']
        track_details['valence'] = valence
        tempo = audio_info[0]['tempo']
        track_details['tempo'] = tempo
        time_signature = audio_info[0]['time_signature']
        track_details['time_signature'] = time_signature
        track_details['mood'] = mood
        if not(track_uri in track_dict):
                track_dict[str(track_uri)] = track_details
                # print(track_details)
        
        return



def get_songs(sp, index, num_playlists, mood, track_dict):
        '''
        Aggregate songs from numerous playlists
        Parameters: Spotipy Spotify client, index of first playlist and maximum number of playlists in library
        Return dictionary of track uris with dictionary of each tracks info (e.g., URI's, titles, genres)
        '''
        # track_dict = {}
        playlists = sp.current_user_playlists(limit=num_playlists, offset=index) #get all the playlists
        # print(len(playlists['items']))
        # outer loops through all the playlists
        for i in range(len(playlists['items'])):
                play_id = playlists['items'][i]['uri']
                print(play_id)
                print(playlists['items'][i]['name'])
        # print("########")
                tracks = sp.playlist_tracks(playlist_id=play_id) # info for all tracks in a playlist 
                # inner loops through all the tracks per playlist
                for j in range(len(tracks['items'])):
                        track_details = {}
                        # get track details
                        track_uri, track_name = track_info(sp, j, tracks)
                        track_details['track_name'] = track_uri
                        track_details['track_name'] = track_name
                        # get artist info
                        artist_uri, artist_name, genre, popularity, followers = artist_info(sp, j, tracks)
                        track_details['artist_uri'] = artist_uri
                        track_details['artist_name'] = artist_name
                        track_details['genre'] = genre
                        track_details['popularity'] = popularity
                        track_details['followers'] = followers
                        # try except to catch Spotify max retries error
                        try:
                                # get audio features
                                attribute_info(sp, mood, track_uri, track_details)
                        except:
                                print("Connection refused by the server...")
                                print("sleeping for 5 seconds...")
                                time.sleep(5)
                                print("Slept for 5 seconds, time to continue...")
                                continue
                       
        return track_dict

sp = OAuth()
token = sp.get_token()

if token:        
        # get angry songs
        track_dict = {}
        sp = spotipy.Spotify(auth=token)
        print(type(sp))
        track_dict = get_songs(sp, 0, num_angry, angry, track_dict) # get info about angry songs
        print(len(track_dict))
        
        # turn dictionary of songs into a dataframe
        df = pd.DataFrame.from_dict(track_dict, orient='index')
        df.rename(columns={'Unnamed: 0':'track_uri'}, inplace=True)
        print(df)
        # df to csv file
        df.to_csv('angry_songs.csv')
      
        # get sad songs
        track_dict = {}
        sp = spotipy.Spotify(auth=token)
        track_dict = get_songs(sp, 9, num_sad, sad, track_dict) # get info about sad songs
        print(len(track_dict))
        
        # turn dictionary of songs into a dataframe
        df = pd.DataFrame.from_dict(track_dict, orient='index')
        df.rename(columns={'Unnamed: 0':'track_uri'}, inplace=True)
        print(df)
        df.to_csv('sad_songs.csv')

        # get happy songs
        track_dict = {}
        sp = spotipy.Spotify(auth=token)
        track_dict = get_songs(sp, 21, num_happy, happy, track_dict) # get info about happy songs
        print(len(track_dict))
        
        # turn dictionary of songs into a dataframe
        df = pd.DataFrame.from_dict(track_dict, orient='index')
        df.rename(columns={'Unnamed: 0':'track_uri'}, inplace=True)
        print(df)
        df.to_csv('happy_songs.csv')

else:
    print("Can't get token")

