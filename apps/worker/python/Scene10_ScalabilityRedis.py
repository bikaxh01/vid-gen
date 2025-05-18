
from manim import *

class Scene10_ScalabilityRedis(Scene):
    def construct(self):
        # Color Scheme
        background_color = "#1E2D3F" # Dark Blue
        text_color = "#FFFFFF"       # White
        highlight_color = "#FFFF00"  # Yellow

        self.camera.background_color = background_color

        # Title: "Scalability: Redis"
        title = Text(
            "Scalability: Redis",
            color=text_color,
            font_size=48
        )
        title.to_edge(UP, buff=0.8)
        self.play(Write(title))
        self.wait(0.5)

        # Description Text: "Scalable, but often requires clustering for high availability"
        description_text_markup = MarkupText(
            f"Scalable, but often requires <span fgcolor='{highlight_color}'>clustering</span> for high availability",
            font_size=28,
            color=text_color
        )
        description_text_markup.next_to(title, DOWN, buff=0.5)
        self.play(Write(description_text_markup))
        self.wait(0.5)

        # Clustering Diagram
        node_radius = 0.6
        node_fill_color = highlight_color
        node_stroke_color = text_color
        node_label_color = "#000000" # Black text on yellow nodes for contrast

        desc_bottom_y = description_text_markup.get_bottom()[1]
        cluster_center_y = desc_bottom_y - 2.5 

        node1_pos = array([-2.5, cluster_center_y - 0.5, 0])
        node2_pos = array([2.5, cluster_center_y - 0.5, 0])
        node3_pos = array([0, cluster_center_y + 1.2, 0])

        node1 = Circle(radius=node_radius, color=node_fill_color, fill_opacity=0.9, stroke_color=node_stroke_color, stroke_width=2).move_to(node1_pos)
        node2 = Circle(radius=node_radius, color=node_fill_color, fill_opacity=0.9, stroke_color=node_stroke_color, stroke_width=2).move_to(node2_pos)
        node3 = Circle(radius=node_radius, color=node_fill_color, fill_opacity=0.9, stroke_color=node_stroke_color, stroke_width=2).move_to(node3_pos)
        
        cluster_nodes = VGroup(node1, node2, node3)

        label1 = Text("M1", font_size=24, color=node_label_color).move_to(node1.get_center())
        label2 = Text("M2", font_size=24, color=node_label_color).move_to(node2.get_center())
        label3 = Text("M3", font_size=24, color=node_label_color).move_to(node3.get_center())
        cluster_labels = VGroup(label1, label2, label3)

        conn_stroke_width = 3
        conn12 = Line(node1.get_center(), node2.get_center(), color=text_color, stroke_width=conn_stroke_width)
        conn23 = Line(node2.get_center(), node3.get_center(), color=text_color, stroke_width=conn_stroke_width)
        conn31 = Line(node3.get_center(), node1.get_center(), color=text_color, stroke_width=conn_stroke_width)
        cluster_connections = VGroup(conn12, conn23, conn31)
        
        clustering_diagram = VGroup(cluster_nodes, cluster_labels, cluster_connections)
        
        self.play(
            LaggedStart(
                Create(cluster_nodes),
                Write(cluster_labels),
                Create(cluster_connections),
                lag_ratio=0.7,
                run_time=3 
            )
        )
        self.wait(0.5)

        clustering_span = description_text_markup.select_part("clustering")
        arrow_start_point = description_text_markup.get_center() + LEFT * 0.5 + DOWN * 0.2 # Fallback
        if clustering_span.submobjects: # Check if the VGroup returned by select_part is not empty
            arrow_start_point = clustering_span.get_bottom() + DOWN * 0.1

        arrow_end_point = node3.get_top() + UP * 0.1 # Changed from get_bottom to get_top for better arrow pointing

        arrow = Arrow(
            start=arrow_start_point,
            end=arrow_end_point,
            color=highlight_color,
            buff=0.2,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.2, 
            max_stroke_width_to_length_ratio=5 
        )
        
        self.play(GrowArrow(arrow))
        self.wait(0.5)

        self.play(Indicate(clustering_diagram, color=highlight_color, scale_factor=1.15, run_time=1.5))
        self.wait(2)