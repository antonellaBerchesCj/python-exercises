'''
20 . [net] Download a video from a video sharing site (Dailymotion, Vimeo, YouTube etc.).
'''

import requests
import sys
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

def download_video(url):
	local_filename = 'downloaded.mp4'
	r = requests.get(url, stream=True)
	with open(local_filename, 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024): 
			if chunk: 
				f.write(chunk)
	return local_filename

def main():
	try:
		idd = sys.argv[1]
	except Exception as e:
		print ("[!] Usage: python3 filename.py youtube_video_id")
		print('e.g. python3 20_downloadVideo.py UZeInWIQZcI')
		exit()

	link = 'http://youtube.com/get_video_info?video_id='+ idd
	video = requests.get(link);
	parsed = urlparse.parse_qs(video.text)
	parsed = parsed['url_encoded_fmt_stream_map']
	a = str(parsed).split(',')
	ed = urlparse.parse_qs(a[0])

	for i in ed:
		if 'url' in i:
			download_video(ed[i][0])
			print('[*] File downloaded successfully!')

if __name__ == '__main__':
	main()
