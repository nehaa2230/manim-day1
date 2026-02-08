def generate_manim_code(topic):
    topic = topic.lower()

    if topic == "gradient descent":
        text = "Gradient Descent"
    elif topic == "neural network":
        text = "Neural Network"
    else:
        text = "Hello AI Animation"

    code = f'''
from manim import *

class AutoScene(Scene):
    def construct(self):
        title = Text("{text}", font_size=64)
        self.play(Write(title))
        self.wait(2)
'''
    return code
