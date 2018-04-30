# pip3 install requests spotipy
# python3 <this_file>
#
# remember to remove '.cache-username' file

import sys
import spotipy
import spotipy.util as util

artist = 'spotify:artist:3D6CKTHC9H0bCujZmG9llH'

if len(sys.argv) > 1:
    username = str(sys.argv[1])
    if len(sys.argv) > 2:
        artist = str(sys.argv[2])
else:
    print("Usage: %s username" % sys.argv[0])
    sys.exit()

token = util.prompt_for_user_token(username)

if token:
    spotify = spotipy.Spotify(auth=token)

    results = spotify.artist_albums(artist_uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    print('Artist Albuns :')
    for album in albums:
        print('[#] Album [#] ' + album['name'])
        print('[#] Link  [#] ' + album['external_urls']['spotify'])
        print('[#] URI   [#] ' + album['uri'])
        print('')

else:
    print("Can't get token for ", username)
