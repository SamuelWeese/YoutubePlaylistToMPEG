# importing packages
import pytube
import os

playlistURL = 'enter playlist here, or feed in some matter'
playlistURL = input('Enter your playlist url:')
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
