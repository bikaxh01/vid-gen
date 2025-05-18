
from manim import *

class Scene02_SettingTheStageTwoDistributedSystems(Scene):
    def construct(self):
        # Set background color as per scheme: dark_blue
        self.camera.background_color = "#232946"

        # Scene Title: "Setting the Stage: Two Distributed Systems"
        # Description: "The text 'Distributed Systems' appears at the top."
        title_text_mobject = Text("Distributed Systems", color="#FFFFFF", font_size=60)
        title_text_mobject.to_edge(UP, buff=0.75)
        self.play(FadeIn(title_text_mobject, shift=DOWN*0.3, duration=1.0))
        self.wait(0.5)

        # Description: "Two columns are introduced side by side. The left column is labeled 'Kafka' and the right column is labeled 'Redis'."
        # Visual Elements: "Kafka label", "Redis label"
        kafka_label_mobject = Text("Kafka", color="#FFFFFF", font_size=48)
        redis_label_mobject = Text("Redis", color="#FFFFFF", font_size=48)

        # Position labels side by side below the title
        column_labels_group = VGroup(kafka_label_mobject, redis_label_mobject).arrange(RIGHT, buff=4.0)
        column_labels_group.next_to(title_text_mobject, DOWN, buff=1.2)

        # Visual Elements: "Column headers" - interpreted as labels with underlines
        # Highlights color: yellow for underlines
        kafka_underline_mobject = Line(
            kafka_label_mobject.get_left() + DOWN*0.15, 
            kafka_label_mobject.get_right() + DOWN*0.15,
            color="#FFFF00", # yellow
            stroke_width=3
        )
        redis_underline_mobject = Line(
            redis_label_mobject.get_left() + DOWN*0.15, 
            redis_label_mobject.get_right() + DOWN*0.15,
            color="#FFFF00", # yellow
            stroke_width=3
        )

        # Animation Types: "FadeIn", "Transform"
        # Create source mobjects (invisible dots) for Transform animation of underlines
        kafka_dot_source = Dot(kafka_underline_mobject.get_center(), radius=0.001, fill_opacity=0, color="#FFFF00")
        redis_dot_source = Dot(redis_underline_mobject.get_center(), radius=0.001, fill_opacity=0, color="#FFFF00")
        
        # Add dots to scene; they will be replaced by underlines during Transform
        self.add(kafka_dot_source, redis_dot_source)

        # Animate labels (FadeIn) and underlines (Transform from dots) simultaneously
        self.play(
            FadeIn(kafka_label_mobject, shift=LEFT * 0.3),
            Transform(kafka_dot_source, kafka_underline_mobject),
            
            FadeIn(redis_label_mobject, shift=RIGHT * 0.3),
            Transform(redis_dot_source, redis_underline_mobject),
            
            run_time=1.5
        )

        self.wait(2)