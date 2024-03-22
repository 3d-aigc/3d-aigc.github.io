from moviepy.editor import *
import sys
if __name__ == '__main__':
    input_path = sys.argv[1]
    clip = (VideoFileClip(input_path))
    clip.write_gif(os.path.join('./', os.path.basename(input_path.split('.')[0]+'.gif')))


