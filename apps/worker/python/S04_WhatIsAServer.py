
from manim import *

class S04_WhatIsAServer(Scene):
    def construct(self):
        self.camera.background_color = "#232937"

        definition_lines = [
            "A server is a powerful computer or a system of computers",
            "that provides services, resources, or data to other",
            "computers, known as clients, over a network.",
            "It often hosts websites, applications, or stores large amounts of data."
        ]
        definition_vgroup = VGroup()
        for i, line_text in enumerate(definition_lines):
            text_mobj = Text(line_text, font_size=32, color="#FFFFFF")
            if i > 0:
                text_mobj.next_to(definition_vgroup[-1], DOWN, buff=0.25)
            definition_vgroup.add(text_mobj)
        
        definition_vgroup.center().to_edge(UP, buff=0.8)

        comp_tower = Rectangle(width=1.5, height=2.5, fill_color="#C0C0C0", fill_opacity=1.0, stroke_color="#A9A9A9", stroke_width=3)
        comp_button = Circle(radius=0.1, fill_color="#FF0000", fill_opacity=1.0, stroke_width=0)
        comp_button.move_to(comp_tower.get_center() + UP * 0.8)
        comp_usb_port1 = Rectangle(width=0.4, height=0.15, fill_color="#333333", fill_opacity=1.0, stroke_width=0)
        comp_usb_port1.move_to(comp_tower.get_center() + UP * 0.4)
        comp_usb_port2 = comp_usb_port1.copy().next_to(comp_usb_port1, DOWN, buff=0.1)
        computer_visual = VGroup(comp_tower, comp_button, comp_usb_port1, comp_usb_port2)
        computer_visual.next_to(definition_vgroup, DOWN, buff=1.0)

        self.play(Write(definition_vgroup), run_time=4)
        self.wait(0.5)
        self.play(FadeIn(computer_visual), run_time=1.5)
        self.wait(1.5)

        rack_frame = Rectangle(width=1.2, height=3.5, fill_color="#282828", fill_opacity=1.0, stroke_color="#1E1E1E", stroke_width=3)
        
        server_units_stack = VGroup()
        num_servers = 5
        total_server_height_space = rack_frame.height * 0.9 
        individual_server_height = (total_server_height_space / num_servers) * 0.8 
        buff_between_servers = (total_server_height_space / num_servers) * 0.2
        server_unit_width = rack_frame.width * 0.8

        for _ in range(num_servers):
            unit_case = Rectangle(
                width=server_unit_width, 
                height=individual_server_height, 
                fill_color="#4A4A4A", 
                fill_opacity=1.0,
                stroke_color="#383838",
                stroke_width=2
            )
            
            led_colors_hex = ["#FFFF00", "#00FF00", "#FFFF00"]
            led_group = VGroup()
            led_radius = individual_server_height * 0.1 
            for k_color_hex in led_colors_hex:
                 led = Circle(radius=led_radius, fill_color=k_color_hex, fill_opacity=1.0, stroke_width=0)
                 led_group.add(led)
            led_group.arrange(RIGHT, buff=led_radius * 0.8)
            led_group.move_to(unit_case.get_left() + RIGHT * (led_group.width / 2 + server_unit_width * 0.1))
            
            server_unit_with_leds = VGroup(unit_case, led_group)
            server_units_stack.add(server_unit_with_leds)

        server_units_stack.arrange(DOWN, buff=buff_between_servers)
        server_units_stack.move_to(rack_frame.get_center())
        
        server_rack_visual = VGroup(rack_frame, server_units_stack)
        
        original_computer_center = computer_visual.get_center()
        original_computer_height = computer_visual.height
        
        server_rack_visual.scale_to_fit_height(original_computer_height * 1.2)
        server_rack_visual.move_to(original_computer_center)

        self.play(Transform(computer_visual, server_rack_visual), run_time=3)
        self.wait(3)