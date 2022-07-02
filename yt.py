from pytube import YouTube
SAVE_PATH = "E:/"
yt = YouTube('https://youtube.com/shorts/rqUKZUdi9z0?feature=share')
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(SAVE_PATH)




'''
# importing the module
from pytube import YouTube

# where to save
SAVE_PATH = "E:/" #to_do

# link of the video to be downloaded
link="https://youtube.com/shorts/rqUKZUdi9z0?feature=share"

try:
	# object creation using YouTube
	# which was imported in the beginning
	yt = YouTube(link)
except:
	print("Connection Error") #to handle exception

# filters out all the files with "mp4" extension
mp4files = yt.filter('mp4')

#to set the name of the file
yt.set_filename('Download video yt python')

# get the video with the extension and
# resolution passed in the get() function
d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
try:
	# downloading the video
	d_video.download(SAVE_PATH)
except:
	print("Some Error!")
print('Task Completed!')
'''