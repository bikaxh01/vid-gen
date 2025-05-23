
from manim import *

class Scene02ClientServerModel(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = "#ADD8E6"  # light_blue

        # Colors
        element_color = "#FFFFFF"  # white for icons, arrow, text
        highlight_color = "#FFFF00" # yellow for highlight

        # 1. Create Client Icon
        monitor = RoundedRectangle(corner_radius=0.05, width=1.2, height=0.9, color=element_color, stroke_width=3)
        stand_neck = Rectangle(width=0.2, height=0.25, color=element_color, stroke_width=3)
        stand_base = Rectangle(width=0.7, height=0.1, color=element_color, stroke_width=3)
        
        stand_neck.next_to(monitor, DOWN, buff=0)
        stand_base.next_to(stand_neck, DOWN, buff=0)
        
        client_icon = VGroup(monitor, stand_neck, stand_base)
        client_icon.move_to(LEFT * 3.5)

        # 2. Client Label
        client_label = Text("You (Client)", color=element_color, font_size=28)
        client_label.next_to(client_icon, DOWN, buff=0.4)

        # 3. Create Server Icon
        server_box = Rectangle(width=0.7, height=1.8, color=element_color, stroke_width=3)
        
        num_lines = 3
        lines_vg = VGroup()
        # Define line horizontal extent based on server_box properties for robustness
        line_start_x = server_box.get_left()[0] + 0.1 # Small margin from edge
        line_end_x = server_box.get_right()[0] - 0.1  # Small margin from edge
        
        for i in range(num_lines):
            # Distribute lines vertically within the box
            y_pos = server_box.get_bottom()[1] + (server_box.height / (num_lines + 1)) * (i + 1)
            line = Line(
                [line_start_x, y_pos, 0],
                [line_end_x, y_pos, 0],
                color=element_color, stroke_width=1.5
            )
            lines_vg.add(line)
        
        server_icon = VGroup(server_box, lines_vg)
        server_icon.move_to(RIGHT * 3.5)

        # 4. Server Label
        server_label = Text("Web Server", color=element_color, font_size=28)
        server_label.next_to(server_icon, DOWN, buff=0.4)

        # Animation: Show client elements
        self.play(
            Create(client_icon),
            Write(client_label),
            run_time=1.5
        )
        self.wait(0.2)

        # Animation: Show server elements
        self.play(
            Create(server_icon),
            Write(server_label),
            run_time=1.5
        )
        self.wait(0.5)

        # 5. Arrow connecting client to server
        arrow = Arrow(
            start=client_icon.get_right(), 
            end=server_icon.get_left(), 
            buff=0.2, 
            color=element_color, 
            stroke_width=5,
            max_tip_length_to_length_ratio=0.25,
            max_stroke_width_to_length_ratio=5 # Default is 5, explicitly stated
        )

        # 6. "Request" Text near the arrow
        request_text = Text("Request", color=element_color, font_size=24)
        request_text.next_to(arrow, UP, buff=0.2)

        # Animation: Show arrow and request text
        self.play(
            Create(arrow),
            Write(request_text),
            run_time=1.5
        )
        self.wait(0.5)

        # 7. Highlight the arrow to emphasize request flow
        self.play(
            Indicate(arrow, color=highlight_color, scale_factor=1.1),
            run_time=1.5
        )
        
        self.wait(2) # Hold the final scene for a bit