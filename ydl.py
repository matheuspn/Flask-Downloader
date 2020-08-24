import subprocess
import requests
from fetcher import id_generator

"""
	Video Downloader used to download the best quality
	audio,
	video,
	Playlist of audio files,
	Playlist of video files
	from a URL supported for youtube-dl.

"""


def fetch_name(url):
    """ To get the title of the video """
    output = subprocess.getoutput(
        'youtube-dl --get-filename -o "%(title)s" "{url}" '.format(url= url),
        )
    return output



def get_media(url, choice):
    """
	Uses `choice`, to download the required content from `url`
	"""
    id_generated = id_generator()
    try:

        if url == "":

            pass

        else:

            if choice == 1:

                subprocess.call(
                    'youtube-dl -f mp3/bestaudio -o "media/Audio downloads/{id_generated}.%(ext)s" -q --no-playlist --extract-audio --audio-format mp3 --no-warnings "{url}"'.format(
                        id_generated=id_generated, url=url
                    ),
                    shell=True,
                )
                return id_generated

            elif choice == 2:

                subprocess.call(
                    'youtube-dl -o "media/Video downloads/{id_generated}.%(ext)s" -q --no-playlist --no-warnings -f mp4/bestvideo "{url}"'.format(
                        id_generated=id_generated, url=url
                    ),
                    shell=True,
                )
                return id_generated

            elif choice == 3:

                subprocess.call(
                    'youtube-dl -i -o "media/{id_generated}/%(playlist_index)s.%(title)s.%(ext)s" --yes-playlist --extract-audio --audio-format mp3 --no-warnings "{url}"'.format(
                        id_generated=id_generated, url=url
                    ),
                    shell=True,
                )
                return id_generated

            elif choice == 4:
                
                subprocess.call(
                    'youtube-dl -i -o "media/{id_generated}/%(playlist_index)s.%(title)s.%(ext)s" --yes-playlist --newline --no-warnings -f mp4 "{url}"'.format(
                        id_generated=id_generated, url=url
                    ),
                    shell=True,
                )
                return id_generated

    except Exception as e:  # for any other unknown errors,  used it to get the other exceptions mentioned above, while debugging used to print `e`

        return e


if __name__ == "___main__":

    print("This is a borrowed script")

else:
    url = ""
    choice = 1
    get_media(url, choice)

