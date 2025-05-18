
from manim import *

class S05_KafkaHighThroughput(Scene):
    def construct(self):
        self.camera.background_color = "#ADD8E6" 

        kafka_heading = Text("Kafka", font_size=72, color="#FFFFFF")
        kafka_heading.to_edge(UP, buff=1.0)

        characteristic_text = Text("High Throughput", font_size=48, color="#FFFFFF")
        characteristic_text.next_to(kafka_heading, DOWN, buff=0.7)

        self.add(kafka_heading)
        self.wait(0.5)

        self.play(Write(characteristic_text), run_time=2)
        self.wait(0.5)

        self.play(Indicate(characteristic_text, color="#FFFF00", scale_factor=1.1), run_time=1.5)
        self.wait(1)