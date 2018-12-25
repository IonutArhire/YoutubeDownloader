# YoutubeDownloader
YoutubeDownloader is a python script used for downloading and converting to audio-only a youtube playlist to a specified folder.

The script checks each youtube video of the playlist you provided to see whether the video is already in the collection (if the collection has a file with the same name as the video title then the video is in the collection) or not. If it is, the script ignores the video; otherwise, the script will download the video in the highest possible quality in the script folder, convert it to audio of the desired quality and place the resulting audio file in the collection folder, after which the downloaded video (the one from the script folder) gets erased.

### Script Arguments

- **collection_dir** : the folder in which you want the resulting audio files to be saved.
- **playlist_link** &nbsp; &nbsp;: link to the public/unlisted youtube playlist that you want downloaded and converted to audio.
- **quality** &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;: quality of the resulting audio: *SD* for 128k bitrate and *HD* for 320k bitrate.

### Dependencies

- **pytube**
- **moviepy**
