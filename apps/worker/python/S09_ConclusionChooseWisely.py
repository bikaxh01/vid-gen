
from manim import *

class S09_ConclusionChooseWisely(Scene):
    def construct(self):
        self.camera.background_color = "#ADD8E6" # Light Blue

        # Concluding statement text elements
        conclusion_line1 = Tex("Choose Wisely:", color="#FFFFFF").scale(0.8)
        
        # Using double backslash for ampersand in Tex strings within Python strings
        conclusion_line2_cpp_text = "Performance \\& Power"
        conclusion_line2_cpp = Tex(conclusion_line2_cpp_text, color="#FFFFFF").scale(0.7)
        conclusion_cpp_tag = Tex("(C++)", color="#FFD700").scale(0.7) # Gold for C++ tag
        
        conclusion_line2_py_text = "Simplicity \\& Dev Speed"
        conclusion_line2_py = Tex(conclusion_line2_py_text, color="#FFFFFF").scale(0.7)
        conclusion_py_tag = Tex("(Python)", color="#4169E1").scale(0.7) # Royal Blue for Python tag
        
        vs_text = Tex("vs.", color="#FFFFFF").scale(0.7)

        # Arrange text elements
        # Group C++ related texts
        cpp_group = VGroup(conclusion_line2_cpp, conclusion_cpp_tag).arrange(RIGHT, buff=0.1)
        # Group Python related texts
        py_group = VGroup(conclusion_line2_py, conclusion_py_tag).arrange(RIGHT, buff=0.1)
        
        # Group comparison elements (C++ vs Python parts)
        comparison_group = VGroup(cpp_group, vs_text, py_group).arrange(RIGHT, buff=0.3)
        
        # Group the main line with the comparison line, align left, then center horizontally and position at bottom
        full_statement = VGroup(conclusion_line1, comparison_group).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        full_statement.center().to_edge(DOWN, buff=1.0)

        # Animations for text appearance
        self.play(Write(conclusion_line1))
        self.wait(0.2)
        self.play(
            Write(conclusion_line2_cpp),
            Write(conclusion_cpp_tag),
            run_time=1.0
        )
        self.wait(0.2)
        self.play(Write(vs_text), run_time=0.5)
        self.wait(0.2)
        self.play(
            Write(conclusion_line2_py),
            Write(conclusion_py_tag),
            run_time=1.0
        )
        self.wait(0.5)

        # Emphasizing arrow
        arrow = Arrow(
            start=full_statement.get_bottom() + DOWN * 0.5, # Start below the statement block
            end=full_statement.get_center_of_mass(), # Point towards the center of the statement block
            color="#FFFF00", # Yellow for highlight
            buff=0.2,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.25
        )

        self.play(GrowArrow(arrow))
        self.wait(0.5)

        # Indicate animation on "Choose Wisely:"
        self.play(Indicate(conclusion_line1, color="#FFFF00", scale_factor=1.1)) # Highlight color Yellow
        self.wait(0.5)

        # Transform animation: Highlight key phrases by changing their color
        target_cpp_line_highlight = conclusion_line2_cpp.copy().set_color("#FFFF00") # Target color Yellow
        target_py_line_highlight = conclusion_line2_py.copy().set_color("#FFFF00")   # Target color Yellow

        self.play(
            Transform(conclusion_line2_cpp, target_cpp_line_highlight),
            Transform(conclusion_line2_py, target_py_line_highlight),
            run_time=1.5
        )
        self.wait(2.5) # Hold the final message