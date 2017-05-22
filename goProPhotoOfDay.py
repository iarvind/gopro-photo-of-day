import requests;
import os;
import sys;

def set_gnome_wallpaper(file_path):
	command = "gsettings set org.gnome.desktop.background picture-uri \"file://" + file_path + "\""
	os.system(command);

image_index = 0;
if(len(sys.argv) == 2):
	image_index = int(sys.argv[1])
url = "https://api.gopro.com/v2/channels/feed/playlists/photo-of-the-day.json?platform=web&page=1&per_page=30";
obj = requests.get(url);
data = obj.json();
image_name = data['media'][image_index]['permalink']+'.jpg';
image_url = data['media'][image_index]['thumbnails']['full']['image'];
image_obj = requests.get(image_url);
image_path = '/opt/go_pro_images/'+image_name;
with open(image_path, 'wb') as f:
	f.write(image_obj.content);
set_gnome_wallpaper(image_path);