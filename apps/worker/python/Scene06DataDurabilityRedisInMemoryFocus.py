
from manim import *

class Scene06DataDurabilityRedisInMemoryFocus(Scene):
    def construct(self):
        self.camera.background_color = "#00003B" # dark_blue (background)

        # Data Durability Text (Scene Title)
        scene_title_obj = Text(
            "Data Durability: Redis's In-Memory Focus",
            font_size=40,
            color="#FFFFFF", # text (white)
            weight=BOLD
        )
        scene_title_obj.to_edge(UP, buff=0.5)
        self.play(Write(scene_title_obj))
        self.wait(0.5)

        # Redis Label (part of the explanation, highlighted)
        redis_label_text = Text(
            "Redis",
            font_size=48,
            color="#FFFF00", # highlights (yellow)
            weight=BOLD
        )
        redis_label_text.next_to(scene_title_obj, DOWN, buff=0.7)
        self.play(Write(redis_label_text)) # Animation Type: Write
        self.wait(0.5)

        # In-Memory Text (explanation part)
        in_memory_text_obj = Text(
            "In-Memory (Optional Persistence)",
            font_size=32,
            color="#FFFFFF" # text (white)
        )
        in_memory_text_obj.next_to(redis_label_text, DOWN, buff=0.5)
        self.play(Write(in_memory_text_obj)) # Animation Type: Write
        self.wait(0.5)

        # RAM Icon Visual Element
        ram_stick_color = "#777777"
        chip_color = "#333333"
        ram_outline_color = "#CCCCCC"

        ram_stick = Rectangle(
            width=2.5,
            height=0.8,
            color=ram_stick_color,
            fill_color=ram_stick_color,
            fill_opacity=1.0
        )
        ram_stick.set_stroke(color=ram_outline_color, width=2)

        num_chips = 4
        chip_width = 0.3
        chip_height = ram_stick.height * 0.6
        total_chip_width = num_chips * chip_width
        total_spacing = ram_stick.width - total_chip_width
        chip_spacing_unit = total_spacing / (num_chips + 1)

        chips_group = VGroup()
        for i in range(num_chips):
            chip = Rectangle(
                width=chip_width,
                height=chip_height,
                color=chip_color,
                fill_color=chip_color,
                fill_opacity=1.0
            )
            chip.set_stroke(color="#555555", width=1)
            
            chip_x_position = ram_stick.get_left()[0] + \
                              (i + 1) * chip_spacing_unit + \
                              i * chip_width + \
                              chip_width / 2
            chip.move_to([chip_x_position, ram_stick.get_center()[1], 0])
            chips_group.add(chip)
        
        ram_icon_obj = VGroup(ram_stick, chips_group) # RAM Icon visual element
        ram_icon_obj.scale(1.2)
        ram_icon_obj.next_to(in_memory_text_obj, DOWN, buff=1.0)

        self.play(Create(ram_icon_obj)) # Create is a suitable animation for visual elements
        self.wait(0.5)

        # Arrow Visual Element
        arrow_obj = Arrow(
            start=in_memory_text_obj.get_bottom() + DOWN * 0.2,
            end=ram_icon_obj.get_top() + UP * 0.2,
            color="#FFFF00", # highlights (yellow)
            buff=0.1
        )
        self.play(GrowArrow(arrow_obj)) # GrowArrow is fine, implicitly part of "Indicate" idea of flow
        self.wait(0.5)

        # Indication Animation
        self.play(Indicate(ram_icon_obj, color="#FFFF00", scale_factor=1.2)) # Animation Type: Indicate
        self.wait(1)

        self.wait(2) # Hold final scene