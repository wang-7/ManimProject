from manim import *


class MyLogo(Scene):
    def construct(self):
        text1 = Text("Q", color=RED).scale(3.5).move_to(LEFT + DOWN * 0.3)
        text2 = Text("ax").scale(3).move_to(LEFT * 0.3 + DOWN * 0.5)
        text3 = Tex(r"$\Gamma$", color=BLUE, fill_opacity=1).move_to(LEFT * 1.5).scale(7.5)

        size = 0.9
        center = RIGHT * 2 + DOWN * 0.5
        circle = Circle(color=RED, fill_opacity=1).shift(center + UP).scale(size)
        square = Square(color=BLUE, fill_opacity=1).shift(center + LEFT).scale(size)
        # tri = Triangle(color=GREEN, fill_opacity=1).shift(center+RIGHT*0.7).scale(size)
        shapes = VGroup(square, circle)
        # self.play(FadeOut(text2, shift=DOWN))
        self.play(Write(text1), Write(text3), SpiralIn(shapes), run_time=1.5)
        self.play(
            text1.animate.shift(LEFT * 1.3),
            text3.animate.shift(RIGHT * 3),
            shapes.animate.shift(RIGHT * 2),
            FadeIn(text2)
        )


with tempconfig({"quality": "high_quality", "preview": True, "save_last_frame": False}):
    scene = MyLogo()
    scene.render()
