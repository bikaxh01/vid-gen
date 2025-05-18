
from manim import *

class Scene09_ScalabilityKafka(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = "#2C3E50" # dark_blue

        # Title: Scalability
        title_scalability = Text("Scalability", color="#FFFFFF", font_size=48)
        title_scalability.to_edge(UP, buff=0.7)

        # Kafka Section Title
        kafka_header = Text("Kafka", color="#FFFFFF", font_size=40)
        kafka_header.next_to(title_scalability, DOWN, buff=0.5)
        
        self.play(Write(title_scalability))
        self.play(Write(kafka_header))
        self.wait(0.5)

        # Explanation Text
        explanation = Text(
            "High scalability through partitioning",
            color="#FFFFFF",
            font_size=32
        )
        explanation.next_to(kafka_header, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait(0.5)

        # Partition Diagram
        # Topic label
        topic_label_text = Text("Topic T", color="#FFFFFF", font_size=28)
        topic_label_text.next_to(explanation, DOWN, buff=1.0) # Positioned above partitions

        # Partitions
        num_partitions = 3
        partition_width = 2.0
        partition_height = 1.0
        partition_buff = 0.25
        highlight_color = "#FFFF00" # yellow
        text_on_highlight_color = "#2C3E50" # dark_blue for text on yellow background

        partitions_vgroup = VGroup()
        for i in range(num_partitions):
            partition_rect = Rectangle(
                width=partition_width,
                height=partition_height,
                color=highlight_color,
                fill_color=highlight_color,
                fill_opacity=0.3,
                stroke_width=2
            )
            partition_text_label = Text(f"P{i}", color=text_on_highlight_color, font_size=24)
            partition_text_label.move_to(partition_rect.get_center())
            partition_element = VGroup(partition_rect, partition_text_label)
            partitions_vgroup.add(partition_element)
        
        partitions_vgroup.arrange(RIGHT, buff=partition_buff)
        partitions_vgroup.next_to(topic_label_text, DOWN, buff=0.3)
        
        # Animation for diagram parts
        self.play(Write(topic_label_text))
        self.play(
            AnimationGroup(
                *[Create(p[0]) for p in partitions_vgroup],  # Create rectangles
                *[Write(p[1]) for p in partitions_vgroup],   # Write labels
                lag_ratio=0.2
            )
        )
        self.wait(1)

        # Arrow from explanation to the diagram title (Topic T)
        arrow_to_diagram = Arrow(
            start=explanation.get_bottom(),
            end=topic_label_text.get_top(),
            color="#FFFFFF", # white
            buff=0.2 # Adjusted buff for visual separation
        )
        self.play(GrowArrow(arrow_to_diagram))
        self.wait(0.5) # Short pause after arrow appears

        # Indicate the partitions to emphasize scalability through partitioning
        self.play(Indicate(partitions_vgroup, color=highlight_color, scale_factor=1.1))
        self.wait(2) # Hold final scene for a bit longer