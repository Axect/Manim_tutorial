from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        
        self.play(ShowCreation(circle))
        #self.play(Rotate(square, PI/4))
        self.play(Transform(circle, square))
        self.play(FadeOut(circle))
