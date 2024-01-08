from manim import *


class Test(Scene):
    def construct(self):
        # euler_img = ImageMobject("Euler.png")
        txt = Tex(r'Stirling\\Bernoulli\\Goldbach')
        self.play(Write(txt))
        self.play(FadeOut(txt))
        txt.move_to(UP)
        self.play(Write(txt))



with tempconfig({"quality": "low_quality", "preview": True, "save_last_frame": False}):
    scene = Test()
    scene.render()
