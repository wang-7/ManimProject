from manim import *


class PlaneWave:
    def __init__(self, quality, start=ORIGIN, speed_dot=1, speed_wave=1, freq=2, max_radius=3, dot_color=YELLOW,
                 wave_color=WHITE, move_to=None, run=True):
        self.start = start
        self.speed_dot = speed_dot
        self.speed_wave = speed_wave
        self.freq = freq
        self.quality = quality
        self.wave_length = self.speed_wave / self.freq
        self.max_radius = max_radius + max_radius % self.wave_length
        self.dot_color = dot_color
        self.wave_color = wave_color
        self.run = run
        self.move_to = move_to

        self.frame_per_sec = 15 if quality == 'low_quality' else 60
        self.frame_count = 0

        # self.distance = np.linalg.norm(self.end - self.start)
        self.num_circle = round(self.max_radius / self.wave_length)
        if move_to is not None:
            self.distance = np.linalg.norm(self.move_to - self.start)
            self.direction = (self.move_to - self.start) / self.distance

        self.dot = Dot(color=self.dot_color).move_to(self.start).add_updater(
            lambda mob, dt: self.dot_updater(mob, dt))
        self.waves = VGroup(
            *[Circle(radius=1e-9, stroke_width=4, stroke_opacity=0, stroke_color=self.wave_color)
                  .add_updater(lambda mob, dt, i=i: self.wave_updater(mob, dt, index=i)) for i in
              range(self.num_circle)]
        )

    def wave_updater(self, mob, dt, index):
        if self.run:
            delay = index * 1 / self.freq
            if self.frame_count > self.frame_per_sec * delay:
                current_width = mob.get_width()
                next_width = current_width + dt * self.speed_wave * 2
                mob.set(width=next_width)
                radius = mob.get_width() / 2
                mob.set_stroke(opacity=1 - radius / self.max_radius)
            if mob.get_stroke_opacity() <= 0:
                mob.set(width=1e-9)
                mob.move_to(self.dot)

    def dot_updater(self, mob, dt):
        if self.run:
            if self.move_to is not None:
                mob.shift(self.direction * dt * self.speed_dot)
                self.frame_count += 1
                if np.linalg.norm(self.move_to - mob.get_center()) < dt * self.speed_dot:
                    self.pause()
            else:
                self.frame_count += 1

    def get_wave(self):
        return VGroup(self.dot, self.waves)

    def pause(self):
        self.run = False

    def go(self):
        self.run = True

    def set_target(self, target):
        self.move_to = target
        self.distance = np.linalg.norm(self.move_to - self.dot.get_center())
        self.direction = (self.move_to - self.dot.get_center()) / self.distance
