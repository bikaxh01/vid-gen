
from manim import *

class S01_IntroductionKafkaVsRedis(Scene):
    def construct(self):
        # Scene settings from color scheme
        background_hex_color = "#ADD8E6" # light_blue
        text_hex_color = "#FFFFFF" # white

        # 1. A subtle background fade-in introduces a calm blue theme.
        # Create a full-screen rectangle for the background.
        # The scene's default background is black, so fading in a blue rectangle achieves the effect.
        background_rect = FullScreenRectangle(
            fill_color=background_hex_color,
            fill_opacity=1,
            stroke_width=0
        )
        background_rect.set_z_index(-100) # Ensure it's behind all other mobjects

        # Animate the fade-in of this background rectangle.
        # This uses the "FadeIn" animation type.
        self.play(FadeIn(background_rect, run_time=1.5)

        # Set the camera's background color as well for robustness.
        # This ensures the background color persists if the rectangle were ever removed or made transparent.
        self.camera.background_color = background_hex_color

        # 2. The title "Kafka vs. Redis" appears at the center using a Write animation.
        # Create the title Text mobject.
        title_text = Text(
            "Kafka vs. Redis",
            font_size=72, # A prominent size for a title
            color=text_hex_color
        )
        title_text.move_to(ORIGIN) # Position it at the center of the screen

        # Animate the title appearing using the Write animation.
        self.play(Write(title_text, run_time=2))

        # Hold the final scene for a few seconds for viewing.
        self.wait(2)