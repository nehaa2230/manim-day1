from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello Manim!", font_size=72)
        self.play(Write(text))
        self.wait(2)


class Welcome(Scene):
    def construct(self):
        text = Text("Welcome to Day 3 🎉", font_size=60)
        self.play(Write(text))
        self.wait(2)

