from conf import *
from PlexMovieLib import PlexMovieLib
from argparse import ArgumentParser

function_map = {
    1: PlexMovieLib.reorganize_folders,
    2: PlexMovieLib.rename_movie_files,
    3: PlexMovieLib.download_trailers
}

argParser = ArgumentParser(
    prog = 'python main.py',
    description='Uses plex media library to organise folders and files and download trailers',
    epilog='for queries contact Kiritee Mishra (konark@gmail.com)'
)

argParser.add_argument("function", type=int, help="Mandatory field. Specifies funtion to be executed:\n1 - reorganize folders\n2 -rename movie files \n3 - download trailers")
argParser.add_argument("-q", "--quiet", action='store_true',help="Quiet Mode: no logging of intermediate steps")
argParser.add_argument("-l", "--log", action='store_true', help="Writes logs on to a log file. default is to show on console")
argParser.add_argument("-t", "--token", type=str, help="Plex API token. If not specified, value taken from conf file")
argParser.add_argument("-u", "--url", type=str, help="Plex URL. If not specified, value taken from conf file")
argParser.add_argument("-m", "--movielib", type=str, help="Name of the Films library in PLex. If not specified, value taken from conf file")

args = argParser.parse_args()

if args.function in function_map:
    method=function_map[args.function]

    quiet= args.quiet or QUIET
    log = args.log or LOG
    token = args.token if not None else PLEX_API_TOKEN
    url = args.url if not None else PLEX_URL
    library = args.library if not None else MOVIES_LIBRARY

    p=PlexMovieLib(plex_token=token,plex_url=url,movies_library =library,log=log, quiet=quiet)
    method(p)
else:
    print("Invalid value of 'function'. No corresponding method found.")


