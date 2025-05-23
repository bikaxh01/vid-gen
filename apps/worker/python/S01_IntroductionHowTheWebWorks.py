
from manim import *

class S01_IntroductionHowTheWebWorks(Scene):
    def construct(self):
        # Scene Configuration Details:
        # Title: Introduction: How the Web Works
        # Sequence: 1
        # Description: The title 'How the Web Works' appears at the center of the screen using a Write animation. A dark blue background fades in.
        # Color Scheme: {"background":"dark_blue", "highlights":"yellow", "text":"white"}
        # Animation Types: ["Write","FadeIn"]
        # Visual Elements: ["Title Text"]

        # Define colors from the scheme using hex codes
        background_color_hex = "#0A2342"  # A deep dark blue, respecting "dark_blue"
        text_color_hex = "#FFFFFF"        # White, respecting "white"

        # 1. A dark blue background fades in.
        # Create a full-screen rectangle for the background.
        background_rect = Rectangle(
            width=self.camera.frame_width,
            height=self.camera.frame_height,
            stroke_width=0,  # No border for the background
            fill_color=background_color_hex,
            fill_opacity=1
        )
        # Ensure it's in the very back, behind all other elements.
        background_rect.set_z_index(-100) 

        # Animate the background fade-in, fulfilling "A dark blue background fades in."
        self.play(FadeIn(background_rect, duration=1.5))

        # 2. The title 'Introduction: How the Web Works' appears at the center of the screen
        #    using a Write animation.
        # The text content is taken from the scene's specific "Title" field.
        title_mobject = Text(
            "Introduction: How the Web Works",
            font_size=48, # A suitable font size for a main title
            color=text_color_hex
        )
        # Position the title in the center of the screen.
        title_mobject.move_to(ORIGIN)

        # Animate the title appearance using Write animation.
        self.play(Write(title_mobject, run_time=3))

        # Hold the final scene for a brief period.
        self.wait(2)
