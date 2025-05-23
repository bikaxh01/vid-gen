
from manim import *

class S01_IntroductionToTheWeb(Scene):
    def construct(self):
        # Color Scheme based on prompt
        background_color_hex = "#ADD8E6"  # light_blue
        text_color_hex = "#FFFFFF"        # white
        # highlight_color_hex = "#FFFF00" # yellow, not used in this scene based on description

        # Background: "A subtle background fade-in introduces a calm blue theme."
        # Create a full-screen rectangle for the background to enable FadeIn animation.
        background_rect = Rectangle(
            width=self.camera.frame_width,
            height=self.camera.frame_height,
            stroke_width=0,  # No border for the background rectangle
            fill_color=background_color_hex,
            fill_opacity=1
        )
        # Ensure it's centered; for a full-screen rectangle, this confirms it covers the origin.
        background_rect.move_to(ORIGIN) 

        # Animate the background fade-in as per "Animation Types: ["FadeIn"]"
        self.play(FadeIn(background_rect, run_time=1.5)) # run_time for a "subtle" effect

        # Title Text: "'How the Web Works: A Beginner's Guide' appears at the center using a Write animation."
        # Visual Elements: ["Title text"]
        title_text_content = "How the Web Works: A Beginner's Guide"
        title = Text(
            title_text_content,
            color=text_color_hex
        )
        
        # Adjust title size to fit well within the screen.
        # Scale to fit 80% of the screen width to leave some margin.
        title.scale_to_fit_width(self.camera.frame_width * 0.8)
        
        # Max height check: if scaling by width makes the text too tall (e.g., long text over many lines),
        # cap its height. For a single-line title, this is a safety measure.
        if title.height > self.camera.frame_height * 0.25:
            title.scale_to_fit_height(self.camera.frame_height * 0.25)
            
        # Position the title at the center of the screen.
        title.move_to(ORIGIN)

        # Animate the title appearing with a Write animation as per "Animation Types: ["Write"]"
        self.play(Write(title, run_time=3)) # run_time for a readable writing speed

        # Hold the final scene for a moment to allow viewers to read.
        self.wait(2)