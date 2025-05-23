
from manim import *

class Scene04ServerProcessing(Scene):
    def construct(self):
        background_color = "#ADD8E6"
        highlight_color = "#FFFF00"
        text_color = "#FFFFFF"
        object_color = "#444444"

        self.camera.background_color = background_color

        client = Square(side_length=1.5, color=object_color, fill_opacity=0.5).to_edge(LEFT, buff=1.5)
        client_label = Text("Client", font_size=24, color=text_color).next_to(client, DOWN, buff=0.3)

        server = Square(side_length=1.5, color=object_color, fill_opacity=0.5).to_edge(RIGHT, buff=1.5)
        server_label = Text("Server", font_size=24, color=text_color).next_to(server, DOWN, buff=0.3)

        self.play(
            Create(client), Write(client_label),
            Create(server), Write(server_label),
            run_time=1
        )
        self.wait(0.5)

        request_arrow = Arrow(
            client.get_right(), server.get_left(),
            buff=0.2,
            stroke_width=7,
            color=text_color 
        )
        request_text = Text("HTTP Request", font_size=24, color=text_color)
        request_text.next_to(request_arrow, UP, buff=0.2)

        self.play(Create(request_arrow), Write(request_text), run_time=1.5)
        self.wait(0.5)

        lens_radius = 0.35
        magnifying_glass_lens = Circle(radius=lens_radius, color=highlight_color, stroke_width=5)
        
        handle_angle = -PI / 4 
        handle_attach_point = magnifying_glass_lens.get_center() + \
                              RIGHT * lens_radius * np.cos(handle_angle) + \
                              UP * lens_radius * np.sin(handle_angle)
        
        handle_length = 0.5
        # Corrected line: Use manim.utils.space_ops.normalize (available via 'from manim import *')
        raw_handle_direction = handle_attach_point - magnifying_glass_lens.get_center()
        if np.linalg.norm(raw_handle_direction) == 0: # Avoid division by zero if points are coincident
            normalized_handle_direction = RIGHT # Default direction
        else:
            normalized_handle_direction = normalize(raw_handle_direction)
        handle_direction_vector = normalized_handle_direction * handle_length
        
        magnifying_glass_handle = Line(
            handle_attach_point,
            handle_attach_point + handle_direction_vector,
            color=highlight_color,
            stroke_width=5
        )
        
        magnifying_glass = VGroup(magnifying_glass_lens, magnifying_glass_handle)
        magnifying_glass.scale(1.3) 
        magnifying_glass.move_to(server.get_center() + UP * 0.15 + LEFT * 0.15)

        self.play(FadeIn(magnifying_glass, scale=0.6), run_time=0.75)
        
        self.play(
            Indicate(server, color=highlight_color, scale_factor=1.25), 
            magnifying_glass.animate(run_time=1.5, rate_func=there_and_back).shift(RIGHT * 0.1 + DOWN * 0.05).scale(1.1),
            run_time=1.5 
        )
        
        self.play(FadeOut(magnifying_glass), run_time=0.75)

        self.wait(1)