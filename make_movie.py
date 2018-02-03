# ffmpeg -i movie.mov -r 1 fooframes/frames%05d.jpg
# extract 1 frame for every second of the movie...
import os, sys

def combine():
	base = os.getcwd()
	files = os.listdir(base)
	files.sort()
	#-s 3840x2160 
	cmd = 'ffmpeg -framerate 4 -i birdseye_%04d.png -c:v libx264 -r 60 -pix_fmt yuv420p out.mp4 -y'
	print cmd
	os.system(cmd)
	return(0)

if __name__ == "__main__":
  combine()

