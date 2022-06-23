import glob

from PIL import Image

def makegif(folder):
    frames = [Image.open(image) for image in glob.glob(f"{folder}/*.jpg")]
    frame_one =frames[0]
    frame_one.save("my_awesome.gif", format="GIF", append_images=frames,
            save_all=True, duration=100, loop=0)

makegif("d:/SASS/colisions")