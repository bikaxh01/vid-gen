
from manim import *

class Scene07KafkaUseCaseEventLogging(Scene):
    def construct(self):
        self.camera.background_color = "#ADD8E6"  # Light Blue

        # Main heading "Kafka"
        kafka_heading = Text("Kafka", color="#FFFFFF", font_size=72, weight=BOLD)
        # Sub-text "Event Logging"
        event_logging_text = Text("Event Logging", color="#FFFFFF", font_size=48)

        # Positioning
        # Position "Kafka" towards the top
        kafka_heading.to_edge(UP, buff=1.5)
        # Position "Event Logging" directly below "Kafka"
        event_logging_text.next_to(kafka_heading, DOWN, buff=0.75)

        # Animations
        # "Kafka" text fades in, shifting down slightly
        self.play(FadeIn(kafka_heading, shift=DOWN*0.5, run_time=1.0))
        self.wait(0.5)  # Brief pause for readability

        # "Event Logging" text is written out, fulfilling "written and fades in smoothly"
        self.play(Write(event_logging_text, run_time=2.0))

        self.wait(2)  # Hold the final scene for 2 seconds