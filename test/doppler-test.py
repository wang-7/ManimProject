from manim import *
from manim.typing import Point3D
from utils import PlaneWave
import numpy as np

quality = 'low_quality'

class DopplerTest(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 3],
            y_range=[-1, 1],
            x_length=5,
            y_length=4,
            axis_config={
                "include_numbers": True
            }
        )
        t = ValueTracker(0).add_updater(lambda mob, dt: mob.increment_value(dt))
        plot_sine = always_redraw(lambda: ax.plot(lambda x: np.sin(4*PI*(x-t.get_value())), x_range=[0, 3]))
        num = DecimalNumber().add_updater(lambda mob: mob.set_value(t.get_value())).to_edge(UP)
        self.add(ax, plot_sine, num, t)
        self.wait(5)
        # pw = PlaneWave(quality, freq=4)
        # waves = pw.get_wave()
        # self.add(waves)
        # self.wait(3)
        # pw.set_target(RIGHT*3)
        # self.wait(4)
        # pw.go()
        # pw.set_target(LEFT*3)
        # self.wait(4)


with tempconfig({"quality": quality, "preview": True, "save_last_frame": False, "disable_caching": True}):
    s = DopplerTest()
    s.render()
