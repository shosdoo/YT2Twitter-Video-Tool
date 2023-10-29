import os
import subprocess
from colorama import init, Fore
from tqdm import tqdm
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

init()
GREEN = "\033[92m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
RESET = "\033[0m"
ROSA = "\033[91m\033[97m"

start_time = 0
end_time = 125

url_video = input(f"{Fore.GREEN}Ingresa la url del video:{Fore.RESET} ")
if url_video.startswith("https://youtu.be"):
    mp3_video = input(f"{Fore.GREEN}Quieres convertirlo en formato mp3? Y/N:{Fore.RESET} ")
    if mp3_video == "N":    
        def_name = "video.webm"
        name_sinformat = input(f"{Fore.BLUE}Ingresa un nombre para el video:{Fore.RESET} ")
        name_format = f"{name_sinformat}.mp4"

        download_video = f"yt-dlp -o {def_name} {url_video}"
        result = subprocess.run(download_video, shell=True)#subprocess es para correr el comando shell true para que lo ejecute en una subterminal

        convert = f"ffmpeg -i {def_name} {name_format}"
        rere = subprocess.run(convert, shell=True)
        os.remove(def_name)#aqui eliminamos el archivo creado por defecto para dejar solo el que tiene el formato correcto        
        name_video_noformat = f"2{name_format}"
        
        
        ffmpeg_extract_subclip(name_format, start_time, end_time, targetname=name_video_noformat)        
        os.remove(name_format)
        name_video_recor = name_video_noformat.lstrip('0123456789')
        os.rename(name_video_noformat, name_video_recor)
        print(f"{Fore.BLUE}Se descargo el video:{Fore.RESET} {Fore.GREEN}{name_video_recor}{Fore.RESET}")
    
    
    elif mp3_video == "Y":
        unamemp3 = "music.webm"
        name_mp3_nof = input(f"{Fore.GREEN}Ingresa el nombre de la cancion:{Fore.RESET} ")
        name_mp3for = f"{name_mp3_nof}.mp3"
        
        downmp3 = f"yt-dlp -o {unamemp3} {url_video}"
        resmp3 = subprocess.run(downmp3, shell=True)
        
        conmp3 = f"ffmpeg -i {unamemp3} {name_mp3for}"
        remp3 = subprocess.run(conmp3, shell=True)
        os.remove(unamemp3)                    
        print(f"{Fore.GREEN}Se descargo el archivo {name_mp3for}{Fore.RESET}")                                
else:
    print(f"{Fore.BLUE}No es url valida{Fore.RESET}")


