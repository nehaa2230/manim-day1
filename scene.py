
from manim import *

class AutoScene(Scene):
    def construct(self):
        title = Text("Neural Network", font_size=64)
        self.play(Write(title))
        self.wait(2)
