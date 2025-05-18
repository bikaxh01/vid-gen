
from manim import *

class S04_RedisCoreConcept(Scene):
    def construct(self):
        self.camera.background_color = "#58C4DD"  # light_blue

        # "Redis" text, interpreted as a header
        redis_header = Text("Redis", color="#FFFFFF", font_size=48)
        redis_header.to_edge(UP, buff=1.0)

        # "In-Memory Data Structure Store" text
        main_text_str = "In-Memory Data Structure Store"
        main_text = Text(main_text_str, color="#FFFFFF", font_size=36)
        main_text.next_to(redis_header, DOWN, buff=0.5)

        # Animation for writing Redis header
        self.play(Write(redis_header))
        self.wait(0.5)

        # Animation for writing the main text
        self.play(Write(main_text))
        self.wait(0.5)

        # Identify the "In-Memory" part of the main text
        # "In-Memory" consists of the first 9 characters (indices 0-8)
        in_memory_part = main_text[0:9]

        # Animation to highlight "In-Memory" by changing its color to yellow
        self.play(in_memory_part.animate.set_color("#FFFF00"))  # yellow

        self.wait(2)