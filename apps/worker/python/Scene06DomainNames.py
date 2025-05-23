
from manim import *

class Scene06DomainNames(Scene):
    def construct(self):
        # Color Scheme
        background_color = "#142850"  # dark_blue
        highlight_color = "#FFFF00" # yellow
        text_color = "#FFFFFF"     # white

        self.camera.background_color = background_color

        # Scene Title
        scene_title_text = "Domain Names"
        scene_title = Text(scene_title_text, font_size=48, color=highlight_color)
        scene_title.to_edge(UP)
        self.play(Write(scene_title))
        self.wait(0.5)

        # Explanation 1: IP Addresses
        ip_intro_text_str = "Websites are hosted on servers, identified by IP Addresses."
        ip_intro_text = Text(ip_intro_text_str, font_size=30, color=text_color, t2c={"IP Addresses": highlight_color})
        ip_intro_text.next_to(scene_title, DOWN, buff=0.5)
        self.play(Write(ip_intro_text))
        self.wait(1)

        # Example IP Address
        ip_address_str = "172.217.160.142"
        ip_address_mobj = Text(ip_address_str, font_size=40, color=text_color)
        ip_address_mobj.next_to(ip_intro_text, DOWN, buff=0.5)
        self.play(Write(ip_address_mobj))
        self.wait(1)

        # Explanation 2: Difficulty of IP Addresses
        difficulty_text_str = "These numbers can be hard for humans to remember."
        difficulty_text = Text(difficulty_text_str, font_size=30, color=text_color)
        difficulty_text.next_to(ip_address_mobj, DOWN, buff=0.7)
        self.play(Write(difficulty_text))
        self.wait(1)
        
        # Introduce Domain Names
        domain_intro_text_str = "So, we use Domain Names as memorable aliases:"
        domain_intro_text = Text(domain_intro_text_str, font_size=30, color=text_color, t2c={"Domain Names": highlight_color})
        domain_intro_text.next_to(difficulty_text, DOWN, buff=0.7)
        self.play(Write(domain_intro_text))
        self.wait(1)

        # Target Domain Name for transformation
        domain_name_str = "google.com"
        domain_name_mobj_target = Text(domain_name_str, font_size=44, color=highlight_color)
        domain_name_mobj_target.move_to(ip_address_mobj.get_center())

        # Animation: Transform IP Address Text to Domain Name Text
        self.play(
            Transform(ip_address_mobj, domain_name_mobj_target)
        )
        # Now ip_address_mobj is visually the domain name.
        self.wait(1.5)

        # Explanation of association (after transformation)
        explanation_group = VGroup()

        line1_str = f"The domain '{domain_name_str}' is much easier to remember."
        line1_text = Text(line1_str, font_size=30, color=text_color)
        line1_text.next_to(ip_address_mobj, DOWN, buff=0.7) # Position relative to transformed object
        explanation_group.add(line1_text)

        line2_str = f"It acts as an alias for an IP address like {ip_address_str}."
        # Create line2_text with highlighting
        line2_text_highlighted = Text(line2_str, font_size=30, color=text_color, 
                                      t2c={domain_name_str: highlight_color, ip_address_str: text_color})
        line2_text_highlighted.next_to(line1_text, DOWN, buff=0.3)
        explanation_group.add(line2_text_highlighted)
        
        self.play(Write(explanation_group))
        self.wait(3) # Hold the final state