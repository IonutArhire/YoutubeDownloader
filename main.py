import os
import sys
import moviepy.editor as mp
from pytube import YouTube, Playlist


def remove_extensions(collection):
    return [os.path.splitext(fn)[0] for fn in collection]


def is_video_in_collection(collection, song_title):
    print("Checking if song is already in collection: " + song_title)

    is_in_collection = song_title in collection
    print("YES" if is_in_collection else "NO")

    return is_in_collection


def convert_to_audio(vid_filename, song_title, collection_dir, quality):
    clip = mp.VideoFileClip(vid_filename)
    audioclip_full_filename = os.path.join(collection_dir, song_title + '.mp3')

    if (quality == 'SD'):
        chosen_bitrate = '128k'
    elif (quality == 'HD'):
        chosen_bitrate = '320k'

    clip.audio.write_audiofile(audioclip_full_filename, bitrate=chosen_bitrate)

    del clip.reader
    del clip


def main(args):
    collection_dir = args[1]
    playlist_link = args[2]
    quality = args[3]

    collection_files = os.listdir(collection_dir)
    collection = remove_extensions(collection_files)

    playlist = Playlist(playlist_link)
    playlist.populate_video_urls()

    for link in playlist.video_urls:
        try:
            video = YouTube(link)

            '''remove characters from video title that are not allowed in windows filenames.'''
            video_title = video.title.translate(
                {ord(c): None for c in video.title if c in '\\\"/<>?:*|'})

            if not is_video_in_collection(collection, video_title):
                video_stream = video.streams.filter(progressive=True).first()
                video_stream.download()

                convert_to_audio(video_stream.default_filename,
                                 video_title, collection_dir, quality)

                os.remove(video_stream.default_filename)

        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    main(sys.argv)
