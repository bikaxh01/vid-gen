
from manim import *

class S07_WebpageDisplayed(Scene):
    def construct(self):
        # Color Scheme
        background_color = "#ADD8E6"  # Light Blue
        highlight_color = "#FFFF00"   # Yellow
        text_color_white = "#FFFFFF"  # White for labels (Client/Server)
        
        # Specific colors for elements not in main scheme
        monitor_body_color = "#606060" # Dark gray for monitor
        monitor_stand_color = "#505050" # Slightly darker gray for stand
        screen_bg_color = "#F0F0F0"     # Off-white for the webpage background area
        webpage_text_color = "#333333"  # Dark gray for text on webpage

        self.camera.background_color = background_color

        # 1. Create Computer Monitor
        monitor_bezel = RoundedRectangle(
            width=7, height=4.5, corner_radius=0.2, 
            color=monitor_body_color, fill_opacity=1, 
            stroke_width=2, stroke_color="#000000"
        )
        screen_area = Rectangle(
            width=6.5, height=3.8, 
            color=screen_bg_color, fill_opacity=1
        ).move_to(monitor_bezel.get_center())
        
        monitor_stand_neck = Rectangle(
            width=0.8, height=0.5, 
            color=monitor_stand_color, fill_opacity=1, stroke_width=0
        ).next_to(monitor_bezel, DOWN, buff=0)
        
        monitor_stand_base = Ellipse(
            width=2, height=0.4, 
            color=monitor_stand_color, fill_opacity=1, stroke_width=0
        ).next_to(monitor_stand_neck, DOWN, buff=0)
        
        computer_group = VGroup(monitor_bezel, screen_area, monitor_stand_neck, monitor_stand_base)
        computer_group.scale(0.8).to_edge(UP, buff=0.5)

        # 2. Create Webpage Content
        webpage_title = Text(
            "Sample Webpage", 
            font_size=28, 
            color=webpage_text_color
        )
        
        webpage_paragraph_lines = [
            "This is a paragraph of text on the webpage.",
            "It demonstrates a basic content structure.",
            "The request-response cycle fetched this content."
        ]
        webpage_paragraph = Paragraph(
            *webpage_paragraph_lines, 
            font_size=16, 
            color=webpage_text_color, 
            alignment="left", 
            line_spacing=0.7
        )
        
        webpage_content_group = VGroup(webpage_title, webpage_paragraph).arrange(
            DOWN, buff=0.3, aligned_edge=LEFT
        )
        
        webpage_content_group.set_width(screen_area.width * 0.9)
        webpage_content_group.move_to(screen_area.get_center())

        # 3. Animate Webpage Appearance
        self.play(FadeIn(computer_group, shift=DOWN*0.5), run_time=1.5)
        self.wait(0.2)
        self.play(FadeIn(webpage_content_group, shift=UP*0.2), run_time=1.5)
        self.wait(1)

        # 4. Illustrate Request/Response Cycle
        # Client
        client_shape = Circle(radius=0.4, color=highlight_color, fill_opacity=1, stroke_width=0)
        client_shape.shift(LEFT*3.5 + DOWN*1.8) # Position shape first
        client_label = Text("Client", font_size=24, color=text_color_white).next_to(client_shape, DOWN, buff=0.2)
        client_group = VGroup(client_shape, client_label)

        # Server
        server_shape = RoundedRectangle(width=0.8, height=1.2, corner_radius=0.1, color=highlight_color, fill_opacity=1, stroke_width=0)
        server_shape.shift(RIGHT*3.5 + DOWN*1.8) # Position shape first
        server_label = Text("Server", font_size=24, color=text_color_white).next_to(server_shape, DOWN, buff=0.2)
        server_group = VGroup(server_shape, server_label)

        self.play(FadeIn(client_group), FadeIn(server_group), run_time=1)
        self.wait(0.5)

        # Request Arrow and Text
        request_arrow = Arrow(
            client_shape.get_right(), server_shape.get_left(), 
            buff=0.2, color=highlight_color, stroke_width=6, 
            max_tip_length_to_length_ratio=0.2
        )
        request_text = Text("Request", font_size=22, color=highlight_color).next_to(request_arrow, UP, buff=0.15)
        
        self.play(GrowArrow(request_arrow), FadeIn(request_text, shift=UP*0.2), run_time=1)
        self.play(Indicate(VGroup(request_arrow, request_text), color=highlight_color, scale_factor=1.1), run_time=1)
        self.wait(0.5)

        # Response Arrow and Text
        response_arrow = Arrow(
            server_shape.get_left(), client_shape.get_right(), 
            buff=0.2, color=highlight_color, stroke_width=6, 
            max_tip_length_to_length_ratio=0.2
        )
        response_text = Text("Response", font_size=22, color=highlight_color).next_to(response_arrow, DOWN, buff=0.15)
        
        self.play(GrowArrow(response_arrow), FadeIn(response_text, shift=DOWN*0.2), run_time=1)
        self.play(Indicate(VGroup(response_arrow, response_text), color=highlight_color, scale_factor=1.1), run_time=1)
        
        self.wait(2)