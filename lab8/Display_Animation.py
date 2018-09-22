import matplotlib.pyplot as plt
from tempfile import NamedTemporaryFile
import base64
from IPython.display import HTML
from matplotlib import animation

VIDEO_TAG = """<video controls>
 <source src="data:video/x-m4v;base64,{0}" type="video/mp4">
 Your browser does not support the video tag.
</video>"""

def anim_to_html(anim):
    if not hasattr(anim, '_encoded_video'):
        anim.save("test.mp4", fps=20, extra_args=['-vcodec', 'libx264'])

        video = open("test.mp4","rb").read()

    anim._encoded_video = base64.b64encode(video).decode('utf-8')
    # prevent figure displayed as a PNG below the animation
    plt.close()
    return VIDEO_TAG.format(anim._encoded_video)

#  this is an automatic hook which is nice if you want to display as soon as you call the animation but causes
#  problems if it's in an object
# animation.Animation._repr_html_ = anim_to_html

def display_animation(anim):
    plt.close(anim._fig)
    return HTML(anim_to_html(anim))