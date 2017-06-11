#!/usr/bin/env python

"""
This Python script downloads YouTube Videos for Offline viewing,
This application has all the basic features such as set save location, select
resolution and encoding to download and etc.

Any Suggestions are welcome at https://github.com/dotSLASH21/PythonSamples

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. ;)

"""

__author__ = "Arunangshu Biswas"
__credits__ = ["Arunangshu Biswas", "nficano"]
__license__ = "GPL"
__version__ = "0.1a"
__maintainer__ = "Arunangshu Biswas"
__email__ = "arunangshubsws@gmail.com"
__status__ = "Development"
__date__ = "10-06-2017"

#use "pip install pytube" to install pytube module
from pytube import YouTube

getUrl = input("Enter the YouTube video URL (e.g. https://www.youtube.com/watch?v=jNQXAC9IVRw): ")
yt = YouTube(getUrl)

#prints the video name.
print("Video Name: "+yt.filename)
#prints the list of different video qualities.
videoList = yt.get_videos()
for i in range(len(videoList)):
    print("%02d) %s"%((i+1), videoList[i]))

#Select Video
listIn = list(input("Enter the encoding and resolution with <space> between them (e.g. mp4 720p): ").strip().split(' '))


#Set filename
customName = input("Enter the filename to store the video as (Leave blank to save it with default filename): ").strip()
if customName != "":
    yt.set_filename(customName)

#SetSave Location
loc = input("Enter the absolute path to save the video (e.g. C:\\Users\\User\\Downloads\\): ")

#Get Video
video = yt.get(listIn[0], listIn[1])

#Download Video
video.download(loc)
print("Downloading please wait...")
#Completed
print("/nYour Video has been Downloaded!! Get it at "+loc)
input("Press any key to exit...")
