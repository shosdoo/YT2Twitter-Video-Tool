import subprocess
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from colorama import init, Fore

init()

def recortar(archivo):
    start_time = 0
    end_time = 120
    sub_clip = f"2{archivo}"
    ffmpeg_extract_subclip(archivo, start_time, end_time, targetname=sub_clip)
    return sub_clip

def descarga(url, name):
    def_name = 'video.webm'
    comando = f'yt-dlp -o {def_name} {url}'
    result = subprocess.run(comando, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    salida = result.stdout
    
    comando2 = f'ffmpeg -i {def_name} {name}.mp4'
    result2 = subprocess.run(comando2, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    salida2 = result2.stdout
    os.remove(def_name)
    if result.returncode == 0 and result2.returncode == 0:        
        rec_video = input(f"{Fore.WHITE}Deseas recortar el video?(S/N):{Fore.RESET}")
        if rec_video.upper() == "S":
            recortar(f"{name}.mp4")
            sub_clip = recortar(f"{name}.mp4")
            name_rec = f"{name}.mp4"
            os.rename(sub_clip, name_rec)
            print(f"{Fore.GREEN}Se descargo {name_rec}{Fore.RESET}")
        elif rec_video.upper() == "N":
            sub_clip = recortar(f"{name}.mp4")
            name_rec = f"{name}.mp4"
            os.rename(sub_clip, name_rec)
            print(f"{Fore.GREEN}Se descargo {name_rec}{Fore.RESET}")
        
    return

def descarga_mp3(url_mp3,name_mp3):
    def_mp3name = 'music.webm'
    comando = f"yt-dlp -o {def_mp3name} {url_mp3}"
    result = subprocess.run(comando, shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    salida = result.stdout
    
    comando2 = f'ffmpeg -i {def_mp3name} {name_mp3}.mp3'
    result2 = subprocess.run(comando2, shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    salida2 = result2.stdout
    os.remove(def_mp3name)
    if result.returncode == 0 and result2.returncode == 0:        
        print(f"{Fore.GREEN}Se descargo correctamente {name_mp3}{Fore.RESET}")
    
    else:
        print(f"{Fore.RED}Hubo un error en la descarga{Fore.RESET}")
    return        



opcion = input(f"{Fore.WHITE}Ingresa la opcion que quieres:\n{Fore.WHITE}[1]{Fore.RESET} {Fore.RED}Formato mp4{Fore.RESET}\n{Fore.WHITE}[2]{Fore.RESET} {Fore.RED}Formato mp3\n:{Fore.RESET}")
if opcion == "1":
    url = input(f"{Fore.WHITE}Ingresa la url:{Fore.RESET} ")
    if url.startswith("https://youtu.be"):
        name = input(f"{Fore.WHITE}Ingresa el nombre:{Fore.RESET} ")
        down = descarga(url, name)
        
    else:
        print(f"{Fore.RED}Url no valida{Fore.RESET}")
        
elif opcion == "2":
    url_mp3 = input(f"{Fore.WHITE}Ingresa la url:{Fore.RESET} ")
    if url_mp3.startswith("https://youtu.be"):        
        name_mp3 = input(f"{Fore.WHITE}Ingresa el nombre:{Fore.RESET} ")
        down2 = descarga_mp3(url_mp3, name_mp3)
    else:
        print(f"{Fore.RED}La Url no es valida{Fore.RESET}")
else:
    print(f"{Fore.RED}La opcion no es valida{Fore.RESET}")
