
from manim import *

class S01_Introduction_Kafka_vs_Redis(Scene):
    def construct(self):
        # Color Scheme details: background is dark_blue, text is white.
        # Using hex codes as per instructions.
        # 'dark_blue' interpreted as a subtle dark blue for background.
        background_color_hex = '#10102E'
        # 'text' color is white.
        text_color_hex = '#FFFFFF'

        # Visual Elements: Title Text.
        # Animation Types: Write, FadeIn.

        # Scene step 1: A subtle dark blue background fades in.
        # Using FullScreenRectangle for the background.
        background_rect = FullScreenRectangle(
            fill_color=background_color_hex,
            fill_opacity=1.0, # FadeIn will animate opacity from 0 to this value.
            stroke_width=0 # No border for the background.
        )
        # Play FadeIn animation for background.
        self.play(FadeIn(background_rect, duration=1.5))

        # Scene step 2: The title 'Kafka vs. Redis' appears in the center 
        # of the screen using a Write animation.
        title_text_mobject = Text(
            'Kafka vs. Redis', # Text content
            color=text_color_hex,
            font_size=60 # A prominent size for the title.
        )
        title_text_mobject.move_to(ORIGIN) # Centering the title.

        # Play Write animation for title.
        self.play(Write(title_text_mobject, run_time=2.5))

        # Hold the scene for a few seconds to allow viewing.
        self.wait(2)
