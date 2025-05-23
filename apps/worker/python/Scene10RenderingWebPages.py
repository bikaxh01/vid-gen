
from manimlib import *

class Scene10RenderingWebPages(Scene):
    def construct(self):
        self.camera.background_color = "#236B8E" # Dark Blue
        # Define colors
        highlight_color = "#FFFF00" # Yellow
        text_color = "#FFFFFF" # White
        code_block_bg_color = "#1E1E1E" # Dark grey for code background
        code_block_stroke_color = highlight_color
        rendered_page_h1_color = "#2c3e50" # Dark Blue-Gray from CSS
        rendered_page_p_color = "#7f8c8d"   # Grayish Blue from CSS

        # Scene Title
        scene_title_text = Text("How a Browser Renders a Web Page", font_size=36, color=text_color)
        scene_title_text.to_edge(UP, buff=0.4)
        self.play(Write(scene_title_text))
        self.wait(0.5)

        # Code snippets setup
        # Parameters for Code constructor itself
        code_init_params = {
            "tab_width": 2,
            "code_style": "monokai", # Corrected: was "style", changed to "code_style"
            "font_size": 14,
            "line_spacing": 0.4,
            "background": "rectangle",
            "background_stroke_color": code_block_stroke_color,
            "background_stroke_width": 1,
            "corner_radius": 0.05,
        }
        # Parameters to be applied manually to the background_mobject of Code
        manual_bg_style_params = {
            "fill_color": code_block_bg_color,
            "fill_opacity": 0.85,
        }
        
        total_code_width = self.camera.frame_width * 0.95 
        code_block_width = total_code_width / 3 - 0.3 

        # 1. HTML Code
        html_code_str = """<!DOCTYPE html>
<html>
<head>
  <title>My Page</title>
  <link rel=\"stylesheet\" href=\"style.css\">
</head>
<body>
  <h1>Hello!</h1>
  <p id=\"myPara\">A paragraph.</p>
  <script src=\"script.js\"></script>
</body>
</html>"""
        html_label = Text("HTML", font_size=22, color=highlight_color, weight=BOLD)
        html_code = Code(html_code_str, language="html", **code_init_params)
        if hasattr(html_code, 'background_mobject') and html_code.background_mobject is not None:
            html_code.background_mobject.set_style(**manual_bg_style_params)
        html_code.set_width(code_block_width)
        html_group = VGroup(html_label, html_code).arrange(DOWN, buff=0.1)

        # 2. CSS Code
        css_code_str = """body {
  font-family: Sans-Serif;
  background: #f0f0f0;
}
h1 {
  color: #2c3e50; 
  text-align: center;
}
p {
  color: #7f8c8d;
}"""
        css_label = Text("CSS", font_size=22, color=highlight_color, weight=BOLD)
        css_code = Code(css_code_str, language="css", **code_init_params)
        if hasattr(css_code, 'background_mobject') and css_code.background_mobject is not None:
            css_code.background_mobject.set_style(**manual_bg_style_params)
        css_code.set_width(code_block_width)
        css_group = VGroup(css_label, css_code).arrange(DOWN, buff=0.1)

        # 3. JavaScript Code
        js_code_str = """document.addEventListener(
  'DOMContentLoaded', () => {
  const p = document.getElementById('myPara');
  p.textContent = \"JS Updated!\";
});"""
        js_label = Text("JavaScript", font_size=22, color=highlight_color, weight=BOLD)
        js_code = Code(js_code_str, language="javascript", **code_init_params)
        if hasattr(js_code, 'background_mobject') and js_code.background_mobject is not None:
            js_code.background_mobject.set_style(**manual_bg_style_params)
        js_code.set_width(code_block_width)
        js_group = VGroup(js_label, js_code).arrange(DOWN, buff=0.1)
        
        all_code_groups = VGroup(html_group, css_group, js_group).arrange(RIGHT, buff=0.25)
        all_code_groups.next_to(scene_title_text, DOWN, buff=0.25)

        self.play(
            LaggedStart(
                Write(html_label), Create(html_code),
                Write(css_label), Create(css_code),
                Write(js_label), Create(js_code),
                lag_ratio=0.3, run_time=2.5
            )
        )
        self.wait(0.8)

        # "Browser" area
        browser_rect_outer = Rectangle(width=self.camera.frame_width * 0.7, height=3.0, color=text_color, stroke_width=1.5)
        browser_rect_outer.next_to(all_code_groups, DOWN, buff=0.4)
        browser_label = Text("Browser View", font_size=18, color=text_color)
        browser_label.next_to(browser_rect_outer, UP, buff=0.1)

        rendered_page_bg = Rectangle(
            width=browser_rect_outer.width - 0.1, 
            height=browser_rect_outer.height - 0.1,
            fill_color="#f0f0f0", # Light gray from CSS
            fill_opacity=1,
            stroke_width=0
        ).move_to(browser_rect_outer.get_center())

        self.play(Create(browser_rect_outer), Write(browser_label))
        self.play(Create(rendered_page_bg))
        self.wait(0.3)
        
        # Status text for processing steps
        status_text_obj = Text("", font_size=18, color=highlight_color).next_to(browser_label, LEFT, buff=0.3, aligned_edge=DOWN)

        # Initial state for web content
        h1_content_str = "Hello!"
        p_content_str_initial = "A paragraph."
        h1_obj = Text(h1_content_str, font_size=28, color="#000000")
        p_obj = Text(p_content_str_initial, font_size=20, color="#000000")
        rendered_content_group = VGroup(h1_obj, p_obj).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        rendered_content_group.move_to(rendered_page_bg.get_center())

        h1_obj.align_to(rendered_page_bg, LEFT).shift(RIGHT*0.2)
        p_obj.next_to(h1_obj, DOWN, buff=0.2, aligned_edge=LEFT)
        rendered_content_group = VGroup(h1_obj,p_obj) # Re-group after individual alignment
        rendered_content_group.move_to(rendered_page_bg.get_center()) # Center the re-aligned group


        # Step 1: HTML
        status_text_obj.become(Text("1. HTML: Content & Structure", font_size=18, color=highlight_color).move_to(status_text_obj.get_center()))
        arrow_html = Arrow(html_code.get_bottom(), rendered_page_bg.get_top(), buff=0.1, color=highlight_color, tip_length=0.15, stroke_width=2.5)
        self.play(Write(status_text_obj))
        self.play(Create(arrow_html), Indicate(html_group, color=highlight_color, scale_factor=1.03))
        self.play(Write(rendered_content_group))
        self.play(FadeOut(arrow_html))
        self.wait(0.3)

        # Step 2: CSS
        status_text_obj.become(Text("2. CSS: Styling", font_size=18, color=highlight_color).move_to(status_text_obj.get_center()))
        arrow_css = Arrow(css_code.get_bottom(), rendered_page_bg.get_top(), buff=0.1, color=highlight_color, tip_length=0.15, stroke_width=2.5)
        self.play(Indicate(status_text_obj, scale_factor=1.05))
        self.play(Create(arrow_css), Indicate(css_group, color=highlight_color, scale_factor=1.03))
        
        h1_target_center_x = rendered_page_bg.get_center()[0]
        
        self.play(
            h1_obj.animate.set_color(rendered_page_h1_color).move_to(np.array([h1_target_center_x, h1_obj.get_center()[1], 0])),
            p_obj.animate.set_color(rendered_page_p_color)
        )
        
        p_obj_styled_target = p_obj.copy().set_color(rendered_page_p_color) 
        p_obj_styled_target.next_to(h1_obj, DOWN, buff=0.2, aligned_edge=LEFT) 

        # Create a temporary group for Transform that accurately reflects the final state after styling
        styled_h1_temp = h1_obj.copy().set_color(rendered_page_h1_color).move_to(np.array([h1_target_center_x, h1_obj.get_center()[1], 0]))
        styled_p_temp = p_obj.copy().set_color(rendered_page_p_color)
        styled_p_temp.next_to(styled_h1_temp, DOWN, buff=0.2, aligned_edge=LEFT) # align p relative to styled h1
        
        styled_content_group_final_target = VGroup(styled_h1_temp, styled_p_temp)
        # Need to ensure this new group is centered correctly based on its new content
        styled_content_group_final_target.move_to(rendered_page_bg.get_center())        

        self.play(Transform(rendered_content_group, styled_content_group_final_target))

        self.play(FadeOut(arrow_css))
        self.wait(0.3)

        # Step 3: JavaScript
        status_text_obj.become(Text("3. JS: Dynamic Updates", font_size=18, color=highlight_color).move_to(status_text_obj.get_center()))
        p_content_js_updated_str = "JS Updated!"
        # Use the current p_obj from rendered_content_group for transformation target properties
        current_p_obj_in_group = rendered_content_group.submobjects[1] # p_obj is the second element
        p_js_updated_target = Text(p_content_js_updated_str, font_size=current_p_obj_in_group.font_size, color=current_p_obj_in_group.get_color())
        p_js_updated_target.align_to(current_p_obj_in_group, UL) 

        arrow_js = Arrow(js_code.get_bottom(), rendered_page_bg.get_top(), buff=0.1, color=highlight_color, tip_length=0.15, stroke_width=2.5)

        self.play(Indicate(status_text_obj, scale_factor=1.05))
        self.play(Create(arrow_js), Indicate(js_group, color=highlight_color, scale_factor=1.03))
        self.play(Transform(current_p_obj_in_group, p_js_updated_target)) 
        self.play(FadeOut(arrow_js))
        self.wait(0.8)
        self.play(FadeOut(status_text_obj))

        # Final message
        final_summary = Text(
            "Browser combines HTML, CSS, and JavaScript to render the web page.",
            font_size=20, color=text_color, line_spacing=0.7
        )
        final_summary.next_to(browser_rect_outer, DOWN, buff=0.3)

        self.play(Write(final_summary))
        self.wait(2.5)
        
        # Ensure all parts of transformed rendered_content_group are faded out
        current_h1_obj_in_group = rendered_content_group.submobjects[0]
        current_p_obj_in_group = rendered_content_group.submobjects[1] # This is now p_js_updated_target effectively

        self.play(
            FadeOut(scene_title_text), FadeOut(all_code_groups),
            FadeOut(browser_label), FadeOut(browser_rect_outer), FadeOut(rendered_page_bg),
            FadeOut(current_h1_obj_in_group), FadeOut(current_p_obj_in_group), 
            FadeOut(final_summary),
            run_time=1.5
        )
        self.wait(0.5)