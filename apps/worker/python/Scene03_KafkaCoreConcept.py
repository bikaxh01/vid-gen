
from manim import *

class Scene03_KafkaCoreConcept(Scene):
    def construct(self):
        self.camera.background_color = "#ADD8E6"  # light_blue

        # Title "Kafka"
        kafka_title = Text("Kafka", font_size=48, color="#FFFFFF") # white
        kafka_title.to_edge(UP)

        # Text "Distributed Streaming Platform"
        text_content = "Distributed Streaming Platform"
        text_dsp = Text(text_content, font_size=36, color="#FFFFFF") # white
        text_dsp.next_to(kafka_title, DOWN, buff=0.5)

        # Animations
        self.play(Write(kafka_title))
        self.play(Write(text_dsp))

        # Highlight "Streaming"
        # Find the substring "Streaming"
        streaming_word = text_dsp.get_part_by_text("Streaming")
        if streaming_word:
            self.play(streaming_word.animate.set_color("#FFFF00")) # yellow
        else:
            # Fallback if get_part_by_text doesn't find it (e.g. for complex Text objects)
            # This part might need adjustment based on how Text splits the string
            # For simple Text, get_part_by_text is usually reliable.
            # As a robust alternative, one could create the text in parts.
            print("Warning: Could not find 'Streaming' to highlight.")

        self.wait(2)