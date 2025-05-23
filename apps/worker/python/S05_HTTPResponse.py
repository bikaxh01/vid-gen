
from manim import *

class S05_HTTPResponse(Scene):
    def construct(self):
        self.camera.background_color = "#ADD8E6" # light_blue

        # Client and Server representations
        client_text_obj = Text("Client", color="#FFFFFF", font_size=36)
        client_box = SurroundingRectangle(client_text_obj, color="#FFFF00", buff=0.5, corner_radius=0.1)
        client_group = VGroup(client_box, client_text_obj).to_edge(LEFT, buff=1)

        server_text_obj = Text("Server", color="#FFFFFF", font_size=36)
        server_box = SurroundingRectangle(server_text_obj, color="#FFFF00", buff=0.5, corner_radius=0.1)
        server_group = VGroup(server_box, server_text_obj).to_edge(RIGHT, buff=1)

        self.add(client_group, server_group)
        self.wait(0.5)

        # HTTP Response Arrow
        response_arrow = Arrow(
            start=server_group.get_edge_center(LEFT),
            end=client_group.get_edge_center(RIGHT),
            buff=0.2,
            color="#FFFF00", # Yellow highlight
            stroke_width=8
        )
        response_label = Text("HTTP Response", color="#FFFFFF", font_size=28).next_to(response_arrow, UP, buff=0.2)

        # GrowArrow is a Transform, fulfilling one animation type requirement.
        self.play(
            GrowArrow(response_arrow),
            Write(response_label), # Fulfills Write animation type.
            run_time=2
        )
        self.wait(1)

        # Explanation Text Box
        explanation_content = (
            "The server sends back the requested information\n"
            "(HTML, CSS, JavaScript, images)\n"
            "as an HTTP Response."
        )
        explanation_text = Text(
            explanation_content,
            font_size=24,
            color="#FFFFFF" # White text
        )

        # Text box background uses highlight for border, and a contrasting fill for readability
        text_box_background = RoundedRectangle(
            width=explanation_text.width + 1.0,
            height=explanation_text.height + 0.8,
            corner_radius=0.2,
            color="#FFFF00", # Yellow highlight for border
            fill_color="#0000CD", # MediumBlue for fill (chosen for contrast)
            fill_opacity=0.85
        )
        explanation_text.move_to(text_box_background.get_center())

        explanation_group = VGroup(text_box_background, explanation_text)
        explanation_group.move_to(DOWN * 2.0)

        # Save the final state of the text_box_background for the Restore animation.
        text_box_background.save_state()
        # Set its initial state for the animation (scaled down and transparent).
        text_box_background.scale(0.01)
        text_box_background.set_opacity(0)
        
        # Add the group. The text_box_background is initially tiny and transparent.
        # The explanation_text is also in the group, ready for the Write animation.
        self.add(explanation_group)

        # Restore animation makes the box grow to its saved state (Transform)
        self.play(
            Restore(text_box_background),
            run_time=1.5
        )
        # Write animation for the text itself.
        self.play(
            Write(explanation_text),
            run_time=3
        )
        self.wait(3)