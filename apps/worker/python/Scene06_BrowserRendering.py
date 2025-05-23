
from manim import *

class Scene06_BrowserRendering(Scene):
    def construct(self):
        self.camera.background_color = "#ADD8E6" # light_blue

        # Create computer icon
        computer = self._create_computer_icon().scale(1.3)
        computer.to_edge(DOWN, buff=0.8)
        
        # Screen area of the computer to place the browser icon on
        # computer[0] is monitor VGroup, computer[0][1] is the display_area inside monitor
        screen_display_area = computer[0][1] 
        
        # Create browser icon
        browser = self._create_browser_icon()
        browser.scale_to_fit_width(screen_display_area.width * 0.85) # Scale to fit screen
        browser.move_to(screen_display_area.get_center())
        
        # Explanation text and box
        text_str = "Your browser interprets the code (HTML, CSS, JS)\nand displays the web page."
        explanation_text = Text(
            text_str,
            font_size=26,
            color="#FFFFFF", # white text
            line_spacing=1.0 # Standard line spacing
        ).set_z_index(1) # Ensure text is on top of the box if needed

        text_box = SurroundingRectangle(
            explanation_text,
            buff=0.25,
            color="#FFFF00", # yellow highlight border
            fill_color="#1A2E3C", # Dark background for text box
            fill_opacity=0.9,
            corner_radius=0.1
        )
        
        explanation_group = VGroup(text_box, explanation_text)
        explanation_group.next_to(computer, UP, buff=0.35)
        
        # Adjust overall size of explanation group if too wide for the scene
        if explanation_group.width > self.camera.frame_width - 1.2:
            explanation_group.scale_to_fit_width(self.camera.frame_width - 1.2)

        # Animations
        self.play(FadeIn(computer, shift=DOWN*0.3), run_time=1.2)
        self.wait(0.3)
        
        # Browser icon appears over the computer
        self.play(FadeIn(browser, scale=0.6), run_time=1.0) # Browser appears and scales up
        self.wait(0.3)

        # Text box appears with explanation
        self.play(FadeIn(text_box, shift=UP*0.15), Write(explanation_text), run_time=1.8)
        self.wait(2.5) # Hold final scene for a few seconds

    def _create_computer_icon(self):
        screen_rect = Rectangle(width=2.8, height=2.0, fill_color="#3C3C3C", fill_opacity=1, stroke_color="#7F7F7F", stroke_width=2)
        display_area = Rectangle(width=2.6, height=1.8, fill_color="#001F3F", fill_opacity=1).move_to(screen_rect.get_center()) # Dark blue screen area
        monitor = VGroup(screen_rect, display_area)
        
        stand_neck = Rectangle(width=0.4, height=0.5, fill_color="#5A5A5A", fill_opacity=1, stroke_color="#7F7F7F", stroke_width=1)
        stand_neck.next_to(monitor, DOWN, buff=0)
        
        stand_base = Rectangle(width=1.2, height=0.2, fill_color="#5A5A5A", fill_opacity=1, stroke_color="#7F7F7F", stroke_width=1)
        stand_base.next_to(stand_neck, DOWN, buff=0)
        
        computer = VGroup(monitor, stand_neck, stand_base)
        return computer

    def _create_browser_icon(self):
        frame = RoundedRectangle(width=2.0, height=1.5, corner_radius=0.1,
                                 fill_color="#E0E0E0", fill_opacity=1,
                                 stroke_color="#A0A0A0", stroke_width=2)
        
        header_height = 0.25
        header = Rectangle(width=frame.width, height=header_height,
                           fill_color="#C0C0C0", fill_opacity=1,
                           stroke_width=0).align_to(frame, UP)
        
        dot_radius = 0.045 # Slightly larger dots for visibility
        spacing = 0.07
        red_dot = Dot(color="#FF605C", radius=dot_radius)
        yellow_dot = Dot(color="#FFBD44", radius=dot_radius)
        green_dot = Dot(color="#00CA4E", radius=dot_radius)
        
        controls = VGroup(red_dot, yellow_dot, green_dot).arrange(RIGHT, buff=spacing)
        # Position controls on the left side of the header, vertically centered
        controls.move_to(header.get_left() + RIGHT * (controls.width / 2 + spacing * 2.5))
        controls.align_to(header, UP).shift(DOWN * header_height / 2)
        
        content_area_width = frame.width * 0.95 
        content_area_height = frame.height - header_height - 0.1 # Margin at bottom
        content_area = Rectangle(width=content_area_width, height=content_area_height,
                                 fill_color="#FFFFFF", fill_opacity=1,
                                 stroke_width=0)
        content_area.next_to(header, DOWN, buff=0.05)

        # Placeholder for "web page" content (lines of text)
        line_color = "#888888"
        line_stroke_width = 1.5 # Thinner lines for mock content
        mock_line1 = Line(LEFT, RIGHT, stroke_color=line_color, stroke_width=line_stroke_width).set_width(content_area.width * 0.8)
        mock_line2 = mock_line1.copy().set_width(content_area.width * 0.7)
        mock_line3 = mock_line1.copy().set_width(content_area.width * 0.85)
        mock_line4 = mock_line1.copy().set_width(content_area.width * 0.6)
        
        page_content_mock = VGroup(mock_line1, mock_line2, mock_line3, mock_line4).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        page_content_mock.scale_to_fit_height(content_area.height * 0.6)
        page_content_mock.move_to(content_area.get_center())
                                 
        browser_icon = VGroup(frame, header, controls, content_area, page_content_mock)
        return browser_icon