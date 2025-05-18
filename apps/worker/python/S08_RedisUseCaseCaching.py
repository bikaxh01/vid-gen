
from manim import *

class S08_RedisUseCaseCaching(Scene):
    def construct(self):
        self.camera.background_color = "#ADD8E6"  # light_blue

        # "Redis" text as a heading
        redis_text = Text("Redis", font_size=72, color="#FFFFFF")  # white text
        redis_text.to_edge(UP, buff=1.5)

        # Animate "Redis" text using FadeIn
        self.play(FadeIn(redis_text, shift=DOWN*0.2, run_time=1.0))
        self.wait(0.5)

        # "Caching" text, the use case
        # Using highlight color for this specific text element
        caching_text = Text("Caching", font_size=60, color="#FFFF00")  # yellow text
        caching_text.next_to(redis_text, DOWN, buff=0.75)

        # Animate "Caching" text using Write
        # The Write animation for text inherently involves characters appearing smoothly,
        # satisfying "written and fades in smoothly".
        self.play(Write(caching_text, run_time=2.0))

        self.wait(2)  # Hold the final scene for a few seconds