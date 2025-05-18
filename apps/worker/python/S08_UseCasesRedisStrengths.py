
from manim import *

class S08_UseCasesRedisStrengths(Scene):
    def construct(self):
        self.camera.background_color = "#1E1E2E"  # dark_blue
        text_color = "#FFFFFF"  # white
        highlight_color = "#FFFF00"  # yellow

        # Scene Title from input
        scene_title_text = Text(
            "Use Cases: Redis's Strengths",
            font_size=40,
            color=highlight_color
        ).to_edge(UP)
        self.play(Write(scene_title_text))
        self.wait(0.5)

        # "Redis" main text
        redis_main_text = Text(
            "Redis",
            font_size=60,
            color=text_color,
            weight=BOLD
        ).next_to(scene_title_text, DOWN, buff=0.6)
        self.play(Write(redis_main_text))
        self.wait(0.5)

        # "Use Cases Text": "Caching, Session Management"
        use_cases_label_text = Text(
            "Caching, Session Management",
            font_size=36,
            color=text_color
        ).next_to(redis_main_text, DOWN, buff=0.5)
        self.play(Write(use_cases_label_text))
        self.wait(0.5)

        # Caching Section
        caching_icon = self._create_caching_icon(color=highlight_color)
        caching_text = Text("Caching", font_size=32, color=text_color) # "Caching Text"
        caching_group = VGroup(caching_icon, caching_text).arrange(DOWN, buff=0.3)

        # Session Management Section
        session_icon = self._create_session_icon(color=highlight_color) # "Session Icon"
        session_text = Text("Session Management", font_size=32, color=text_color)
        session_group = VGroup(session_icon, session_text).arrange(DOWN, buff=0.3)

        # Arrange use case visual elements horizontally
        use_case_elements_group = Group(caching_group, session_group).arrange(RIGHT, buff=2.5)
        use_case_elements_group.next_to(use_cases_label_text, DOWN, buff=1.0)

        self.play(
            FadeIn(caching_icon, shift=UP*0.5),
            Write(caching_text),
            FadeIn(session_icon, shift=UP*0.5),
            Write(session_text),
            run_time=1.5
        )
        self.wait(0.5)

        # Arrows
        arrow_to_caching = Arrow(
            start=use_cases_label_text.get_bottom(),
            end=caching_icon.get_top(),
            buff=0.2,
            color=highlight_color,
            stroke_width=4,
            tip_length=0.25
        )
        arrow_to_session = Arrow(
            start=use_cases_label_text.get_bottom(),
            end=session_icon.get_top(),
            buff=0.2,
            color=highlight_color,
            stroke_width=4,
            tip_length=0.25
        )

        self.play(
            GrowArrow(arrow_to_caching),
            GrowArrow(arrow_to_session),
            run_time=1.5
        )
        self.wait(0.5)

        # Indicate visual elements
        self.play(
            Indicate(caching_group, color=highlight_color, scale_factor=1.1),
            Indicate(session_group, color=highlight_color, scale_factor=1.1),
            run_time=2
        )
        self.wait(1)

    def _create_caching_icon(self, color):
        bar_height = 0.25
        bar_width = 1.2
        bar1 = Rectangle(width=bar_width, height=bar_height, color=color, fill_opacity=0.7, stroke_width=2).round_corners(0.05)
        bar2 = bar1.copy().next_to(bar1, DOWN, buff=0.1)
        bar3 = bar1.copy().next_to(bar2, DOWN, buff=0.1)
        icon = VGroup(bar1, bar2, bar3).scale(0.7)
        return icon

    def _create_session_icon(self, color):
        head = Circle(radius=0.3, color=color, fill_opacity=0.7, stroke_width=2)
        shoulders_width_top = 0.5
        shoulders_width_bottom = 0.8
        body_height = 0.5
        body_points = [
            [-shoulders_width_top / 2, 0, 0],
            [shoulders_width_top / 2, 0, 0],
            [shoulders_width_bottom / 2, -body_height, 0],
            [-shoulders_width_bottom / 2, -body_height, 0]
        ]
        body = Polygon(*body_points, color=color, fill_opacity=0.7, stroke_width=2)
        head.move_to(ORIGIN + UP * (head.radius - body_height/2 + 0.25) ) # Manually adjust for better centering
        body.next_to(head, DOWN, buff=0.05)
        icon = VGroup(head, body).scale(0.8)
        icon.center()
        return icon