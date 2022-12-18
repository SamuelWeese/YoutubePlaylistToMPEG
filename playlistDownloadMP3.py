# importing packages
import pytube
import os

playlistURL = 'https://www.youtube.com/watch?v=TPmNm7i5q70&list=PL4Xt6BiyJc-53UGHO7aXKzhu7hdSJ3PI3&index=1&ab_channel=PUNCAKELyrics'
aPlaylist = pytube.contrib.playlist.Playlist(playlistURL)

destination = './Music'

for video in aPlaylist.videos:
    videoAudio = video.streams.filter(only_audio=True).first()
    out_file = videoAudio.download(output_path=destination)
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    # result of success
    print(video.title + " has been successfully downloaded.")
