from pytube import YouTube
import datetime
import subprocess
import os
import fnmatch

def main():
    
    #youtube
    def convert(n):
        return str(datetime.timedelta(minutes = n))
        
    def yt_operation(link):
        yt = YouTube(line)   
        #title of video
        print("Title: ",yt.title)

        #Views
        print("Views: ",yt.views)

        #length
        print("length of video: ",str(datetime.timedelta(seconds = yt.length)))

        #resolution
        ys = yt.streams.get_highest_resolution()
    
                        
        #download
        ys.download()
        
       #audio only true/false, i dont know how to do this part yet
       
    
    with open('Links.txt', 'r') as link:  
        for line in link.readlines():
            yt_operation(line)    
    
    for files in fnmatch.filter(os.listdir(),"*.mp4"):
        subprocess.run(['ffmpeg.exe', '-i', files, files[0:files.find('.mp4')] + '.mp3'])

if __name__ == "__main__":
    main()
    
