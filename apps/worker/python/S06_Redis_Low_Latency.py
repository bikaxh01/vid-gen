
from manim import *

class S06_Redis_Low_Latency(Scene):
    def construct(self):
        # Color Scheme Configuration
        background_color = "#A5D8E0"  # Light Blue from config: light_blue
        text_color = "#FFFFFF"      # White from config: text
        highlight_color = "#FFFF00"  # Yellow from config: highlights

        self.camera.background_color = background_color

        # "Redis" text - This provides context as per description "Under 'Redis,'..."
        redis_context_text = Text("Redis", font_size=60, color=text_color)
        redis_context_text.move_to(UP * 2.0) # Positioned towards the top of the scene

        # "Low Latency" characteristic text - Main focus of this scene
        # Visual Elements: "Text: Low Latency"
        low_latency_text = Text("Low Latency", font_size=48, color=text_color)
        # Positioned directly under the "Redis" text
        low_latency_text.next_to(redis_context_text, DOWN, buff=0.75)

        # --- Animations Start Here ---

        # Animate the appearance of the context text "Redis"
        # Although not explicitly in "Animation Types" for this element, 
        # it's required for the scene to be self-contained and make sense.
        self.play(Write(redis_context_text))
        self.wait(0.5) # Brief pause for readability

        # Animate the writing of "Low Latency"
        # Animation Types: "Write"
        self.play(Write(low_latency_text))
        self.wait(0.5) # Brief pause for readability

        # Indicate the "Low Latency" text with an arrow for emphasis
        # Animation Types: "Indicate"
        # Visual Elements: "Arrow indicator"
        # Description: "A small arrow briefly indicates the text for emphasis."
        self.play(Indicate(low_latency_text, color=highlight_color, scale_factor=1.15))
        self.wait(1.5) # Hold the final state for a moment longer for the viewer

        # --- Animations End Here ---