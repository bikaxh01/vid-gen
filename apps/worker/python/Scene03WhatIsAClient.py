
from manim import *

class Scene03WhatIsAClient(Scene):
    def construct(self):
        self.camera.background_color = "#1E2A3A"

        title_text = Text("What is a Client?", color="#FFFFFF", font_size=40)
        title_text.to_edge(UP, buff=0.8)
        self.play(Write(title_text))
        self.wait(0.5)

        definition_str = "A client is a piece of computer hardware or software\n" \
                         "that accesses a service made available by a server."
        client_definition = Text(
            definition_str,
            color="#FFFFFF",
            font_size=28,
            line_spacing=1,
            t2c={"client": "#FFD700", "server": "#FFD700"}
        )
        client_definition.next_to(title_text, DOWN, buff=0.5)
        self.play(Write(client_definition), run_time=3)
        self.wait(1)

        comp_screen = Rectangle(width=2.0, height=1.2, fill_color="#A9A9A9", fill_opacity=1, stroke_color="#FFFFFF", stroke_width=2)
        comp_display = Rectangle(width=1.8, height=1.0, fill_color="#87CEEB", fill_opacity=1, stroke_width=0).move_to(comp_screen.get_center())
        comp_stand = Rectangle(width=0.3, height=0.4, fill_color="#696969", fill_opacity=1, stroke_color="#FFFFFF", stroke_width=2).next_to(comp_screen, DOWN, buff=0)
        comp_base = Rectangle(width=1.0, height=0.2, fill_color="#696969", fill_opacity=1, stroke_color="#FFFFFF", stroke_width=2).next_to(comp_stand, DOWN, buff=0)
        
        client_computer_vg = VGroup(comp_screen, comp_display, comp_stand, comp_base)
        client_computer_vg.scale(1.1)
        client_computer_vg.next_to(client_definition, DOWN, buff=0.8)

        self.play(FadeIn(client_computer_vg, scale=0.7))
        self.wait(1)

        browser_frame = RoundedRectangle(width=2.2, height=1.65, corner_radius=0.1, fill_color="#D3D3D3", fill_opacity=1, stroke_color="#FFFFFF", stroke_width=4)
        browser_header = Rectangle(width=2.2, height=0.33, fill_color="#B0B0B0", fill_opacity=1, stroke_width=0).align_to(browser_frame, UP)
        button_red_dot = Dot(color="#FF605C", radius=0.055).move_to(browser_header.get_left() + RIGHT * 0.22)
        button_yellow_dot = Dot(color="#FFD700", radius=0.055).next_to(button_red_dot, RIGHT, buff=0.11)
        button_green_dot = Dot(color="#00CA4E", radius=0.055).next_to(button_yellow_dot, RIGHT, buff=0.11)
        browser_content_area = Rectangle(width=2.0, height=1.1, fill_color="#4A90E2", fill_opacity=1, stroke_width=0)
        browser_content_area.next_to(browser_header, DOWN, buff=0.1) # Fixed line

        browser_icon_vg = VGroup(browser_frame, browser_header, button_red_dot, button_yellow_dot, button_green_dot, browser_content_area)
        browser_icon_vg.scale(1.2)
        browser_icon_vg.move_to(client_computer_vg.get_center())
        
        self.play(
            Transform(client_computer_vg, browser_icon_vg),
            run_time=2
        )
        self.wait(3)