
from manim import *

class Scene08_HTTPRequests(Scene):
    def construct(self):
        self.setup_scene_presentation()
        self.introduce_http_protocol()
        self.display_http_request_structure()
        self.conclude_scene()

    def setup_scene_presentation(self):
        self.camera.background_color = "#263238"  # Dark Blue-Grey (background)
        self.main_scene_title = Text(
            "HTTP Requests", 
            font_size=48, 
            color="#FFFFFF" # White (text)
        )
        self.play(Write(self.main_scene_title))
        self.wait(0.5)
        self.play(self.main_scene_title.animate.to_edge(UP, buff=0.5))

    def introduce_http_protocol(self):
        http_protocol_title = Text(
            "HTTP: Hypertext Transfer Protocol", 
            font_size=32, 
            color="#FFD700" # Yellow (highlights)
        )
        http_protocol_title.next_to(self.main_scene_title, DOWN, buff=0.5)
        
        http_explanation_text = Text(
            "The fundamental protocol for data communication on the World Wide Web,\n"
            "enabling the fetching of resources, such as HTML documents.",
            font_size=22, 
            color="#FFFFFF", # White (text)
            line_spacing=0.9
        )
        http_explanation_text.next_to(http_protocol_title, DOWN, buff=0.3)

        self.play(Write(http_protocol_title))
        self.play(Write(http_explanation_text))
        self.wait(2.5)
        
        self.intro_elements_group = VGroup(http_protocol_title, http_explanation_text)

    def display_http_request_structure(self):
        if hasattr(self, 'intro_elements_group'):
            self.play(FadeOut(self.intro_elements_group))
            self.wait(0.5)

        request_structure_title = Text(
            "HTTP Request Structure", 
            font_size=32, 
            color="#FFD700" # Yellow (highlights)
        )
        request_structure_title.next_to(self.main_scene_title, DOWN, buff=0.5)
        self.play(Write(request_structure_title))
        self.wait(0.5)

        request_container_width = 7.5
        request_container_height = 5.2
        
        request_details_box = RoundedRectangle(
            width=request_container_width, 
            height=request_container_height, 
            corner_radius=0.2,
            color="#FFFFFF", # White (text, for border)
            fill_color="#455A64", # Mid Blue-Grey, derived for contrast
            fill_opacity=0.3
        )
        request_details_box.next_to(request_structure_title, DOWN, buff=0.3)
        self.play(Create(request_details_box))
        self.wait(0.2)

        http_request_line = Text(
            "POST /api/v1/data HTTP/1.1", 
            font_size=20, 
            font="Monospace", 
            color="#FFFFFF" # White (text)
        )
        http_request_line.align_to(request_details_box, UL).shift(RIGHT * 0.3 + DOWN * 0.3)
        self.play(Write(http_request_line))
        current_object_on_screen = http_request_line

        headers_section_label = Text(
            "Headers:", 
            font_size=20, 
            weight=BOLD, 
            color="#FFD700" # Yellow (highlights)
        )
        headers_section_label.next_to(current_object_on_screen, DOWN, buff=0.25, aligned_edge=LEFT)
        self.play(Write(headers_section_label))

        header_content_list = [
            "Host: api.example.com",
            "Content-Type: application/json",
            "Accept: application/json",
            "User-Agent: ManimClient/1.0"
        ]
        headers_vgroup_content = VGroup(*[
            Text(header_item, font_size=16, font="Monospace", color="#FFFFFF") # White (text)
            for header_item in header_content_list
        ]).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        
        headers_vgroup_content.next_to(headers_section_label, DOWN, buff=0.15, aligned_edge=LEFT).shift(RIGHT * 0.3)
        self.play(LaggedStartMap(Write, headers_vgroup_content, lag_ratio=0.25, run_time=2))
        current_object_on_screen = headers_vgroup_content

        content_separator_line = Line(
            request_details_box.get_left() + RIGHT * 0.2,
            request_details_box.get_right() + LEFT * 0.2,
            stroke_width=1.5, 
            color="#BBBBBB" # Light Grey, neutral
        )
        content_separator_line.next_to(current_object_on_screen, DOWN, buff=0.25)
        content_separator_line.set_x(request_details_box.get_center()[0])
        self.play(Create(content_separator_line))
        current_object_on_screen = content_separator_line

        body_section_label = Text(
            "Body:", 
            font_size=20, 
            weight=BOLD, 
            color="#FFD700" # Yellow (highlights)
        )
        body_section_label.next_to(current_object_on_screen, DOWN, buff=0.25, aligned_edge=LEFT)
        body_section_label.align_to(headers_section_label, LEFT)
        self.play(Write(body_section_label))

        body_content_list = [
            '{',
            '  "name": "Manim Example",',
            '  "project": "HTTP Visualization"',
            '}'
        ]
        body_vgroup_content = VGroup(*[
            Text(body_item, font_size=16, font="Monospace", color="#FFFFFF") # White (text)
            for body_item in body_content_list
        ]).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        
        body_vgroup_content.next_to(body_section_label, DOWN, buff=0.15, aligned_edge=LEFT).shift(RIGHT * 0.3)
        self.play(LaggedStartMap(Write, body_vgroup_content, lag_ratio=0.25, run_time=2))
        
    def conclude_scene(self):
        self.wait(3)
