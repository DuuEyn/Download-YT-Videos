import logging
import os

from pytube import YouTube


#Converts the video length from seconds to HH:MM:SS
def convert(seconds):
  seconds = seconds % (24 * 3600)
  hour = seconds // 3600
  seconds %= 3600
  minutes = seconds // 60
  seconds %= 60

  return "%d:%02d:%02d" % (hour, minutes, seconds)

def get_yt_vid(yt):
  print(f'\nTitle: {yt.title}')
  print(f'Views: {yt.views}')
  print(f'Length: {convert(yt.length)}')
  print('\nGetting available resolutions...')
  
  availReso = []

  try:
    #progressive flag is enabled to ensure that the downloaded file contains both the audio and video
    for stream in yt.streams.filter(progressive=True):
    
      #Retrieves the video's stream tags and resolution
      res = stream.resolution
      itag = stream.itag

      #Retrieved data is stored in a list if a resolution is found
      if res is not None and res not in availReso:
        availReso.append([itag, res])

    #Sorts the list based on the resolution and prints the sorted list
    sorted_reso = sorted(availReso, key=lambda x: (len(x[1]), x[1][:2]))  
    print(*(f'\nStream tag: {r[0]} Resolution:{r[1]}'for r in sorted_reso))
    return availReso
  except Exception as e:
   logging.error(e)

def download_vid(res, yt):
  res.append([0])
  tag = input("Enter the stream tag to download(Enter 0 to exit): ")

  #While loop will continue to run until the user enters a valid stream tag or enters '0'
  while int(tag) not in [r[0] for r in res]:
    print("Invalid input!. Select from one of the stream tags displayed above. To exit the program, enter 0")
    tag = input("Enter the stream tag to download: ")
  if tag == '0':
    print('Program terminated')
    exit()  

  try:
    #Retrieves the video stream with the matching stream tag
    dw_vid = yt.streams.get_by_itag(int(tag))
    print('Downloading...')
  
    #Creates the folder 'YT_downloads' in the working directory if it does not exist
    #Then downloads the video in the created folder
    if not os.path.exists('YT_Downloads'):
      os.mkdir('YT_Downloads')
    dw_vid.download(output_path='./YT_Downloads')
    print('Download complete!')
  except Exception as e:
    logging.error(e)


link = input("Enter the link of the video to check:  ")

#Calls the YouTube method to get the video's metadata
#use_oauth=True authorizes the program to access age-restricted videos.
#allow_oauth_caches=True allows Pytube to cache the credentials.
#If caching is set to False, the user will be prompted to authenticate everytime YouTube() is called.  
yt = YouTube(link, 
            use_oauth=True,
            allow_oauth_cache=True)
  
res = get_yt_vid(yt)
if res is not None: 
  dw = input('\nDownload? (y/n): ').lower()
  while dw != 'y' and dw != 'n':
    print("Error, invalid input!!")
    dw = input('Download? (y/n): ').lower()
  if dw == 'y':
    download_vid(res, yt)
  else:
    print('Program terminated')
