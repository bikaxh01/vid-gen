
from manim import *

# Color definitions from the scheme
BG_COLOR = "#ADD8E6"  # light_blue
HIGHLIGHT_COLOR = "#FFFF00" # yellow
TEXT_COLOR = "#FFFFFF" # white
TEXT_BOX_FILL_COLOR = "#6A96B5" # A darker, desaturated blue for text box background

class S03_http_request_explained(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # 1. "Request" text appears, centered initially
        request_text = Text("Request", color=TEXT_COLOR, font_size=72)
        # Appears at ORIGIN by default
        
        self.play(Write(request_text))
        self.wait(1)

        # 2. Transform "Request" to "HTTP Request" with "HTTP" highlighted
        http_request_target = MarkupText(
            f'<span fgcolor="{HIGHLIGHT_COLOR}">HTTP</span><span fgcolor="{TEXT_COLOR}"> Request</span>',
            font_size=72
        )
        # Ensure target is at the same position as the original text for smooth transform
        http_request_target.move_to(request_text.get_center())

        # request_text will be transformed into http_request_target.
        # The variable request_text will then refer to the transformed mobject.
        self.play(Transform(request_text, http_request_target))
        http_request_transformed_text = request_text 
        self.wait(1)

        # Move the "HTTP Request" title to the top edge
        self.play(http_request_transformed_text.animate.to_edge(UP, buff=1.0))
        self.wait(0.5)

        # 3. Explanation text box appears
        explanation_content = (
            "HTTP (Hypertext Transfer Protocol) is the language web browsers "
            "and servers use to communicate."
        )
        
        explanation_text = Paragraph(
            explanation_content,
            width=self.camera.frame_width * 0.85, 
            color=TEXT_COLOR,
            font_size=30,
            alignment="center"
        )
        # Position it below the moved title
        explanation_text.next_to(http_request_transformed_text, DOWN, buff=0.75)

        # Define the text box (filled rectangle with border)
        # It's created based on the size of explanation_text
        static_text_box = RoundedRectangle(
            width=explanation_text.width + 0.8, # Padding for width
            height=explanation_text.height + 0.8, # Padding for height
            corner_radius=0.15,
            color=HIGHLIGHT_COLOR, # Border color (yellow)
            fill_color=TEXT_BOX_FILL_COLOR,
            fill_opacity=0.80 
        )
        static_text_box.move_to(explanation_text.get_center()) # Align with the text

        # Create a small starting object (dot) for the transform into the box.
        # This dot will appear and then transform into the box shape.
        origin_dot_for_box = Dot(static_text_box.get_center(), color=HIGHLIGHT_COLOR, radius=0.01)
        
        # Animate box transformation (from dot) and text writing simultaneously
        self.play(
            Transform(origin_dot_for_box, static_text_box), # Dot becomes the box
            Write(explanation_text) # Text appears
        )
        
        self.wait(3)