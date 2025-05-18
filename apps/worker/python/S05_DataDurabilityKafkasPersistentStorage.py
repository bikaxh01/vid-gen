
from manim import *

class S05_DataDurabilityKafkasPersistentStorage(Scene):
    def construct(self):
        # Scene Configuration
        BG_COLOR = "#0D1B2A"  # Dark Blue
        TEXT_COLOR = "#FFFFFF" # White
        HIGHLIGHT_COLOR = "#FFFF00" # Yellow

        self.camera.background_color = BG_COLOR

        # Scene Title (contextual)
        scene_context_title = Text(
            "Data Durability: Kafka's Persistent Storage",
            font_size=30,
            color=TEXT_COLOR
        ).to_edge(UP, buff=0.5)
        self.play(Write(scene_context_title), run_time=1.0)
        self.wait(0.3)

        # "Data Durability Text" - Visual Element
        data_durability_text = Text(
            "Data Durability",
            font_size=48,
            weight=BOLD,
            color=TEXT_COLOR
        ).next_to(scene_context_title, DOWN, buff=0.7)
        self.play(Write(data_durability_text), run_time=1.0)
        self.wait(0.5)

        # "Persistent Storage Text" - Visual Element
        persistent_storage_text = Text(
            "Persistent Storage",
            font_size=40,
            color=TEXT_COLOR
        ).next_to(data_durability_text, DOWN, buff=1.0).shift(LEFT*2.5)
        self.play(Write(persistent_storage_text), run_time=1.0)
        self.wait(0.5)

        # "Disk Icon" - Visual Element
        casing = RoundedRectangle(
            corner_radius=0.15, 
            width=1.5, 
            height=1.0, 
            color=HIGHLIGHT_COLOR, 
            fill_color=HIGHLIGHT_COLOR, 
            fill_opacity=0.2
        )
        platter_visual = Circle(
            radius=0.3, 
            color=HIGHLIGHT_COLOR, 
            fill_color=HIGHLIGHT_COLOR, 
            fill_opacity=0.4
        ).move_to(casing.get_center())
        
        platter_center_dot = Dot(
            point=platter_visual.get_center(), 
            radius=0.05, 
            color=HIGHLIGHT_COLOR,
            fill_opacity=0.7 
        )
        
        detail_element = Rectangle(
            width=0.1, 
            height=0.1, 
            color=HIGHLIGHT_COLOR, 
            fill_color=HIGHLIGHT_COLOR, 
            fill_opacity=0.6
        ).move_to(casing.get_corner(DR) + UL * 0.15)

        disk_icon = VGroup(casing, platter_visual, platter_center_dot, detail_element)
        disk_icon.scale(0.9)
        disk_icon.next_to(persistent_storage_text, RIGHT, buff=1.0)

        self.play(FadeIn(disk_icon), run_time=1.0)
        self.wait(0.5)

        # "Arrow" - Visual Element
        arrow_to_disk = Arrow(
            start=persistent_storage_text.get_right(),
            end=disk_icon.get_left(),
            color=TEXT_COLOR, 
            buff=0.2,
            stroke_width=6,
            tip_length=0.2
        )
        self.play(GrowArrow(arrow_to_disk), run_time=1.0)
        self.wait(0.5)

        # Indicate the disk icon
        self.play(Indicate(disk_icon, color=HIGHLIGHT_COLOR, scale_factor=1.25, repetitions=2), run_time=1.0)
        self.wait(1.5)