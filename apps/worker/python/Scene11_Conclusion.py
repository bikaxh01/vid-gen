
from manim import *

class Scene11_Conclusion(Scene):
    def construct(self):
        self.camera.background_color = "#00003A"

        conclusion_message = "Conclusion: Choose the right tool for the job!"
        conclusion_text = Text(
            conclusion_message,
            color="#FFFFFF",
            font_size=40
        )

        self.play(Write(conclusion_text), run_time=3)
        self.wait(2)
        self.play(FadeOut(conclusion_text), run_time=1.5)
        self.wait(1)