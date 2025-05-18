
from manim import *

class Scene04RedisInMemoryDataStoreDefinition(Scene):
    def construct(self):
        # Scene Configuration:
        # Title: Redis: In-Memory Data Store Definition
        # Sequence: 4
        # Description: Under the 'Redis' column, the text 'In-Memory Data Store' is written.
        #              It's highlighted in green to emphasize its primary role.
        # Color Scheme: {"background":"dark_blue","highlights":"green","text":"white"}
        # Animation Types: ["Write","Highlight"]
        # Visual Elements: ["In-Memory Data Store text","Redis Column"]

        # Set background color
        self.camera.background_color = "#1E2D3E" # Dark Blue for background

        # Color definitions from scheme
        text_color = "#FFFFFF"       # White for text
        highlight_color = "#4CAF50"  # Green for highlights

        # "Redis Column" - represented by a header text
        # This acts as the title for the column under which information will be placed.
        redis_column_label = Text(
            "Redis",
            font_size=48,
            weight=BOLD,
            color=text_color
        )
        redis_column_label.to_edge(UP, buff=1.0) # Positioned at the top center

        # Animation: Write the Redis column label
        self.play(Write(redis_column_label), run_time=1.0)
        self.wait(0.5)

        # "In-Memory Data Store" text
        # This text is the core information for this scene.
        definition_text = Text(
            "In-Memory Data Store",
            font_size=40,
            color=text_color # Initially white, as per text color in scheme
        )
        # Position it under the "Redis" column label
        definition_text.next_to(redis_column_label, DOWN, buff=0.5)

        # Animation: Write the definition text
        self.play(Write(definition_text), run_time=1.5)
        self.wait(1)

        # Animation: Highlight the definition text in green
        # This emphasizes its primary role as stated in the scene description.
        self.play(definition_text.animate.set_color(highlight_color), run_time=1.0)
        self.wait(2) # Hold the highlighted state for visibility
