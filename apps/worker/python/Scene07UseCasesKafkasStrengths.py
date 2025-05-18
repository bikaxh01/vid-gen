
from manim import *

class Scene07UseCasesKafkasStrengths(Scene):
    def construct(self):
        # Scene setup: colors and camera
        self.camera.background_color = "#232A37"  # dark_blue
        text_color = "#FFFFFF"                   # white
        highlight_color = "#FFFF00"             # yellow

        # 1. "Use Cases" main title
        use_cases_main_title = Text(
            "Use Cases",
            color=text_color,
            font_size=48
        )
        use_cases_main_title.to_edge(UP, buff=0.7)
        self.play(Write(use_cases_main_title))
        self.wait(0.3)

        # 2. "Kafka" heading
        kafka_heading = Text(
            "Kafka",
            color=text_color,
            font_size=40
        )
        kafka_heading.next_to(use_cases_main_title, DOWN, buff=0.8)
        self.play(Write(kafka_heading))
        self.wait(0.3)

        # 3. Arrow connecting Kafka to its use cases
        arrow_start_point = kafka_heading.get_bottom() + DOWN * 0.15
        arrow_end_point = arrow_start_point + DOWN * 0.6
        connecting_arrow = Arrow(
            start=arrow_start_point,
            end=arrow_end_point,
            stroke_width=7,
            color=highlight_color,
            max_tip_length_to_length_ratio=0.25,
            tip_shape=ArrowTriangleFilledTip
        )
        self.play(Create(connecting_arrow))
        self.wait(0.3)

        # 4. "Event Streaming, Logs" text (Kafka's use cases)
        use_cases_details_text = Text(
            "Event Streaming, Logs",
            color=text_color,
            font_size=32
        )
        use_cases_details_text.next_to(connecting_arrow, DOWN, buff=0.3)
        self.play(Write(use_cases_details_text))
        self.wait(0.3)

        # 5. Icons for "Event Streaming" and "Logs"
        # Event Streaming Icon: three circles connected by lines
        es_c1 = Circle(radius=0.12, color=text_color, fill_opacity=0.6, stroke_color=text_color, stroke_width=2.5)
        es_c2 = Circle(radius=0.12, color=text_color, fill_opacity=0.6, stroke_color=text_color, stroke_width=2.5).next_to(es_c1, RIGHT, buff=0.1)
        es_c3 = Circle(radius=0.12, color=text_color, fill_opacity=0.6, stroke_color=text_color, stroke_width=2.5).next_to(es_c2, RIGHT, buff=0.1)
        es_l1 = Line(es_c1.get_right(), es_c2.get_left(), color=text_color, stroke_width=2.5)
        es_l2 = Line(es_c2.get_right(), es_c3.get_left(), color=text_color, stroke_width=2.5)
        event_stream_icon = VGroup(es_c1, es_c2, es_c3, es_l1, es_l2).scale(0.9)

        # Log Icon: a rectangle with lines, like a document
        log_icon_rect = Rectangle(width=0.45, height=0.65, color=text_color, stroke_width=2.5)
        log_line_h_buff = 0.05  # Horizontal buffer for lines within the log icon
        log_line_v_start = 0.12 # Vertical start position for the first line
        log_line_v_spacing = 0.12 # Vertical spacing between lines
        
        log_lines = VGroup() # Group for lines within the log icon
        current_start_point = log_icon_rect.get_corner(UL) + RIGHT*log_line_h_buff + DOWN*log_line_v_start
        current_end_point = log_icon_rect.get_corner(UR) + LEFT*log_line_h_buff + DOWN*log_line_v_start
        for _ in range(3): # Create 3 lines
            line = Line(current_start_point, current_end_point, color=text_color, stroke_width=1.8)
            log_lines.add(line)
            current_start_point += DOWN * log_line_v_spacing
            current_end_point += DOWN * log_line_v_spacing
        
        log_icon_final = VGroup(log_icon_rect, log_lines).scale(0.9)

        # Position icons side-by-side below the details text
        icons_group = VGroup(event_stream_icon, log_icon_final).arrange(RIGHT, buff=1.2)
        icons_group.next_to(use_cases_details_text, DOWN, buff=0.7)
        
        # Animate icons appearing (Write them concurrently)
        self.play(Write(event_stream_icon), Write(log_icon_final))
        self.wait(0.5)

        # 6. Indicate animations to highlight key elements
        self.play(Indicate(use_cases_details_text, color=highlight_color, scale_factor=1.15))
        self.wait(0.2)
        self.play(Indicate(event_stream_icon, color=highlight_color, scale_factor=1.25))
        self.wait(0.1)
        self.play(Indicate(log_icon_final, color=highlight_color, scale_factor=1.25))
        
        self.wait(1.5) # Hold final scene