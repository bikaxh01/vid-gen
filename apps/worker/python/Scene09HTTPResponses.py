
from manim import *

class Scene09HTTPResponses(Scene):
    def construct(self):
        # Scene configuration
        BG_COLOR = "#0A192F"  # Dark Blue
        HIGHLIGHT_COLOR = "#FFD700"  # Yellow (Gold)
        TEXT_COLOR = "#F0F0F0"  # Off-White

        self.camera.background_color = BG_COLOR

        # Title
        scene_title_text = "HTTP Responses"
        scene_title = Text(scene_title_text, font_size=48, color=TEXT_COLOR)
        scene_title.to_edge(UP, buff=0.5)
        self.play(Write(scene_title))
        self.wait(0.5)

        # Explanation text
        explanation_text_1 = Text(
            "An HTTP response is what a server sends back to a client after receiving a request.",
            font_size=24, color=TEXT_COLOR, line_spacing=0.9
        )
        explanation_text_1.next_to(scene_title, DOWN, buff=0.4)
        explanation_text_1.set_width(self.camera.frame_width - 1.5)

        explanation_text_2 = Text(
            "It typically includes a status line, headers, and an optional message body.",
            font_size=24, color=TEXT_COLOR, line_spacing=0.9
        )
        explanation_text_2.next_to(explanation_text_1, DOWN, buff=0.2)
        explanation_text_2.set_width(self.camera.frame_width - 1.5)

        self.play(Write(explanation_text_1))
        self.play(Write(explanation_text_2))
        self.wait(2)
        
        self.play(
            FadeOut(explanation_text_1),
            FadeOut(explanation_text_2),
            scene_title.animate.scale(0.75).to_edge(UP, buff=0.3)
        )
        self.wait(0.5)

        # Response Box visual
        response_box_width = 12.5
        response_box_height = 6.0
        response_box = Rectangle(
            width=response_box_width,
            height=response_box_height,
            color=TEXT_COLOR,
            stroke_width=2
        )
        response_box.next_to(scene_title, DOWN, buff=0.4)

        structure_title = Text("HTTP Response Structure", font_size=30, color=TEXT_COLOR)
        structure_title.next_to(response_box, UP, buff=0.25)

        self.play(Write(structure_title))
        self.play(Create(response_box))
        self.wait(0.5)

        # Define section heights
        status_line_ratio = 0.18
        headers_ratio = 0.42

        status_line_h = response_box_height * status_line_ratio
        headers_h = response_box_height * headers_ratio

        line1_y = response_box.get_top()[1] - status_line_h
        line1 = Line(
            [response_box.get_left()[0], line1_y, 0],
            [response_box.get_right()[0], line1_y, 0],
            color=TEXT_COLOR, stroke_width=1.5
        )

        line2_y = line1_y - headers_h
        line2 = Line(
            [response_box.get_left()[0], line2_y, 0],
            [response_box.get_right()[0], line2_y, 0],
            color=TEXT_COLOR, stroke_width=1.5
        )
        self.play(Create(line1), Create(line2))
        self.wait(0.3)

        label_x_pos = response_box.get_left()[0] + 0.4

        # --- Status Line Section ---
        status_label_text = "Status Line:"
        status_label = Text(status_label_text, font_size=22, color=HIGHLIGHT_COLOR, weight=BOLD)
        status_label.move_to([label_x_pos, (response_box.get_top()[1] + line1_y) / 2, 0], aligned_edge=LEFT)

        status_protocol = Text("HTTP/1.1", font_size=20, color=TEXT_COLOR, font="Monospace")
        status_code_msg = Text("200 OK", font_size=20, color=HIGHLIGHT_COLOR, font="Monospace", weight=BOLD)
        
        status_content_group = VGroup(status_protocol, status_code_msg).arrange(RIGHT, buff=0.2)
        status_content_group.next_to(status_label, RIGHT, buff=0.3)
        status_content_group.set_y(status_label.get_y())

        self.play(Write(status_label))
        self.play(Write(status_protocol))
        self.play(Write(status_code_msg))
        self.wait(0.5)

        # --- Headers Section ---
        headers_label_text = "Headers:"
        headers_label = Text(headers_label_text, font_size=22, color=HIGHLIGHT_COLOR, weight=BOLD)
        headers_label.move_to([label_x_pos, (line1_y + line2_y) / 2, 0], aligned_edge=LEFT)
        headers_label.align_to(status_label, LEFT)

        header_texts = [
            "Content-Type: application/json",
            "Content-Length: 128",
            "Server: MyNginx/1.20",
            "Date: Tue, 30 Jul 2024 14:30:00 GMT"
        ]
        header_mobjects = VGroup()
        for h_text in header_texts:
            header_line = Text(h_text, font_size=16, color=TEXT_COLOR, font="Monospace")
            header_mobjects.add(header_line)
        
        header_mobjects.arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        header_mobjects.next_to(headers_label, RIGHT, buff=0.3)
        header_mobjects.set_y((line1_y + line2_y) / 2)
        header_mobjects.align_to(status_content_group, LEFT)

        self.play(Write(headers_label))
        for i, h_mob in enumerate(header_mobjects):
            self.play(Write(h_mob), run_time=0.35)
            if i < len(header_mobjects) -1 : self.wait(0.05)
        self.wait(0.5)

        # --- Body Section ---
        body_label_text = "Body:"
        body_label = Text(body_label_text, font_size=22, color=HIGHLIGHT_COLOR, weight=BOLD)
        body_label.move_to([label_x_pos, (line2_y + response_box.get_bottom()[1]) / 2, 0], aligned_edge=LEFT)
        body_label.align_to(status_label, LEFT)

        body_content_raw = """{ 
  \"message\": \"Data retrieved successfully\",
  \"data\": {
    \"itemId\": \"X1723\",
    \"value\": 42
  }
}"""
        body_content = Text(body_content_raw, font_size=15, color=TEXT_COLOR, font="Monospace", line_spacing=0.75)
        
        body_content.next_to(body_label, RIGHT, buff=0.3)
        body_content.set_y((line2_y + response_box.get_bottom()[1]) / 2)
        body_content.align_to(header_mobjects, LEFT)

        body_content_allowed_width = response_box.get_right()[0] - body_content.get_left()[0] - 0.2 
        if body_content.width > body_content_allowed_width:
            body_content.scale_to_fit_width(body_content_allowed_width)
        
        body_content_allowed_height = abs(line2_y - response_box.get_bottom()[1]) - 0.3 
        if body_content.height > body_content_allowed_height:
            body_content.scale_to_fit_height(body_content_allowed_height)

        self.play(Write(body_label))
        self.play(Write(body_content), run_time=1.2)
        self.wait(3)