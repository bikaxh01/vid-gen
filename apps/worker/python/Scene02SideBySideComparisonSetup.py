
from manim import *

class Scene02SideBySideComparisonSetup(Scene):
    def construct(self):
        # Set background color from scheme {"background":"light_blue"}
        self.camera.background_color = "#ADD8E6"

        # Define text color from scheme {"text":"white"}
        text_color = "#FFFFFF"
        
        # Column properties
        column_width = 5.0
        column_height = 6.0
        column_spacing = 1.0
        column_y_center = 0.0 # Vertically centered columns

        # Calculate horizontal positions for columns
        # Ensures columns are centered with spacing around the Y-axis
        left_column_x_center = -(column_width / 2 + column_spacing / 2)
        right_column_x_center = (column_width / 2 + column_spacing / 2)

        # Visual Element: "Column for Kafka"
        left_column_visual = Rectangle(
            width=column_width,
            height=column_height,
            stroke_color=text_color,
            stroke_width=2,
            fill_color=text_color, 
            fill_opacity=0.1 # Subtle fill to differentiate column area
        ).move_to(np.array([left_column_x_center, column_y_center, 0]))

        # Visual Element: "Column for Redis"
        right_column_visual = Rectangle(
            width=column_width,
            height=column_height,
            stroke_color=text_color,
            stroke_width=2,
            fill_color=text_color,
            fill_opacity=0.1
        ).move_to(np.array([right_column_x_center, column_y_center, 0]))

        # Group column visuals for simultaneous animation
        column_visuals = VGroup(left_column_visual, right_column_visual)

        # Visual Element: "Label: Kafka"
        kafka_text_label = Text("Kafka", color=text_color, font_size=60)
        # Position label near the top of the left column
        kafka_text_label.next_to(left_column_visual.get_top(), DOWN, buff=0.4)

        # Visual Element: "Label: Redis"
        redis_text_label = Text("Redis", color=text_color, font_size=60)
        # Position label near the top of the right column
        redis_text_label.next_to(right_column_visual.get_top(), DOWN, buff=0.4)

        # Animation: "Two columns are introduced side-by-side."
        # Using FadeIn as per Animation Types: ["FadeIn", "Transform"]
        self.play(FadeIn(column_visuals), run_time=1.0)
        
        # Short pause for visual pacing
        self.wait(0.2) 

        # Animation: "Each label fades in."
        # Using FadeIn with shift and scale for a more dynamic effect,
        # which implicitly uses transformation aspects.
        self.play(
            FadeIn(kafka_text_label, shift=DOWN * 0.3, scale=0.8),
            FadeIn(redis_text_label, shift=DOWN * 0.3, scale=0.8),
            run_time=1.0
        )
        
        # Hold the final scene setup
        self.wait(1.5)