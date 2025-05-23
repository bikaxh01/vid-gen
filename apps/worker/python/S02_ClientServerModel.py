
from manim import *

class S02_ClientServerModel(Scene):
    def construct(self):
        # Config
        BG_COLOR = "#000033"  # dark_blue
        HIGHLIGHT_COLOR = "#FFFF00"  # yellow
        TEXT_COLOR = "#FFFFFF"  # white

        self.camera.background_color = BG_COLOR

        # Scene Title
        scene_title_text = Text("Client-Server Model", color=TEXT_COLOR, font_size=40).to_edge(UP)
        self.play(Write(scene_title_text))
        self.wait(0.5)

        # Client Computer
        client_box = Rectangle(width=3, height=2, color=HIGHLIGHT_COLOR)
        client_text = Text("Client", color=TEXT_COLOR, font_size=28).move_to(client_box.get_center())
        client_group = VGroup(client_box, client_text).shift(LEFT * 4)

        self.play(Create(client_box), Write(client_text))
        self.wait(0.5)

        # Server Computer
        server_box = Rectangle(width=3, height=2, color=HIGHLIGHT_COLOR)
        server_text = Text("Server", color=TEXT_COLOR, font_size=28).move_to(server_box.get_center())
        server_group = VGroup(server_box, server_text).shift(RIGHT * 4)

        self.play(Create(server_box), Write(server_text))
        self.wait(0.5)

        # Request Arrow
        request_arrow = Arrow(
            start=client_box.get_right(),
            end=server_box.get_left(),
            buff=0.2,
            color=HIGHLIGHT_COLOR,
            stroke_width=6,
            tip_length=0.25
        )
        request_label = Text("Request", color=TEXT_COLOR, font_size=24).next_to(request_arrow, UP, buff=0.1)

        self.play(Indicate(client_group, color=HIGHLIGHT_COLOR, scale_factor=1.1))
        self.play(Create(request_arrow), Write(request_label))
        self.play(Indicate(server_group, color=HIGHLIGHT_COLOR, scale_factor=1.1))
        self.wait(0.5)

        # Response Arrow
        response_arrow = Arrow(
            start=server_box.get_left(),
            end=client_box.get_right(),
            buff=0.2,
            color=HIGHLIGHT_COLOR,
            stroke_width=6,
            tip_length=0.25
        )
        response_label = Text("Response", color=TEXT_COLOR, font_size=24).next_to(response_arrow, DOWN, buff=0.1)

        self.play(Indicate(server_group, color=HIGHLIGHT_COLOR, scale_factor=1.1))
        self.play(Create(response_arrow), Write(response_label))
        self.play(Indicate(client_group, color=HIGHLIGHT_COLOR, scale_factor=1.1))
        self.wait(2)