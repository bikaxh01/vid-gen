
from manim import *

class Scene05IPAddresses(Scene):
    def construct(self):
        self.camera.background_color = "#0D1B2A" # Dark Blue

        # Scene Title
        scene_title_text = Text("IP Addresses", color="#FFFFFF", font_size=48, weight=BOLD)
        scene_title_text.to_edge(UP, buff=0.7)
        self.play(Write(scene_title_text))
        self.wait(0.5)

        # Explanation of IP Address
        explanation_lines = [
            "An IP Address (Internet Protocol Address) is a unique number",
            "that identifies a device on a network.",
            "Think of it like a postal address for your computer,",
            "allowing it to send and receive data over the internet."
        ]

        explanation_vgroup = VGroup()
        for i, line_str in enumerate(explanation_lines):
            line_text = Text(line_str, color="#FFFFFF", font_size=28)
            explanation_vgroup.add(line_text)
        
        explanation_vgroup.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        explanation_vgroup.next_to(scene_title_text, DOWN, buff=0.5)
        explanation_vgroup.to_edge(LEFT, buff=1.0)

        self.play(Write(explanation_vgroup), run_time=4)
        self.wait(1)

        # Example IP Address Label
        example_label = Text("Example IP Address:", color="#FFFFFF", font_size=32)
        example_label.next_to(explanation_vgroup, DOWN, buff=1.0, aligned_edge=LEFT)
        
        self.play(Write(example_label))
        self.wait(0.5)

        # Example IP Address Parts
        ip_1 = Text("192", color="#FFFF00", font_size=72, weight=BOLD)
        dot_1 = Text(".", color="#FFFF00", font_size=72, weight=BOLD) # Highlight color for consistency
        ip_2 = Text("168", color="#FFFF00", font_size=72, weight=BOLD)
        dot_2 = Text(".", color="#FFFF00", font_size=72, weight=BOLD)
        ip_3 = Text("1", color="#FFFF00", font_size=72, weight=BOLD)
        dot_3 = Text(".", color="#FFFF00", font_size=72, weight=BOLD)
        ip_4 = Text("1", color="#FFFF00", font_size=72, weight=BOLD)

        ip_full_vgroup = VGroup(ip_1, dot_1, ip_2, dot_2, ip_3, dot_3, ip_4)
        ip_full_vgroup.arrange(RIGHT, buff=0.1)
        ip_full_vgroup.next_to(example_label, DOWN, buff=0.4, aligned_edge=LEFT)
        
        # Animate the creation of the IP Address
        self.play(
            LaggedStart(
                *[Write(part) for part in ip_full_vgroup],
                lag_ratio=0.5, 
                run_time=3 
            )
        )
        self.wait(2)

        # End Scene
        self.wait(3)