
from manim import *

class S03_KafkaMessageBrokerDefinition(Scene):
    def construct(self):
        # Color Scheme from prompt
        BG_COLOR = "#1E1E2F"  # Dark Blue
        TEXT_COLOR = "#FFFFFF"  # White
        HIGHLIGHT_COLOR = "#39FF14"  # Neon Green / Bright Green

        self.camera.background_color = BG_COLOR

        # "Kafka Column" - represented by a title text
        # This text establishes the 'column' mentioned in the description.
        kafka_column_title = Text(
            "Kafka",
            font_size=60,
            color=TEXT_COLOR,
            weight=BOLD
        )
        kafka_column_title.to_edge(UP, buff=1.25)

        # "Message Broker" text to be written under the Kafka column title
        message_broker_text = Text(
            "Message Broker",
            font_size=48,
            color=TEXT_COLOR
        )
        message_broker_text.next_to(kafka_column_title, DOWN, buff=0.75)

        # Animations sequence as per description
        # 1. Establish the 'Kafka' column context (optional animation, can also appear instantly)
        self.play(Write(kafka_column_title))
        self.wait(0.5) # Brief pause after Kafka title appears

        # 2. Write 'Message Broker' text under 'Kafka'
        # Animation Type: Write
        self.play(Write(message_broker_text))
        self.wait(1)  # Pause before highlighting

        # 3. Highlight 'Message Broker' text in green
        # Animation Type: Highlight (achieved by changing color)
        self.play(message_broker_text.animate.set_color(HIGHLIGHT_COLOR))
        self.wait(2)  # Hold the highlighted state for a few seconds
