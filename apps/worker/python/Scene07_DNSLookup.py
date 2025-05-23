
from manim import *

class Scene07_DNSLookup(Scene):
    def construct(self):
        # Scene Colors based on scheme: {"background":"dark_blue","highlights":"yellow","text":"white"}
        BG_COLOR = "#000033" # Dark Blue (representative hex for "dark_blue")
        TEXT_COLOR = "#FFFFFF" # White
        HIGHLIGHT_COLOR = "#FFFF00" # Yellow
        
        # Visual Element specific colors (not part of scheme, for clarity)
        CLIENT_BOX_FILL = "#3B82F6" # Medium Blue for Client box
        DNS_SERVER_BOX_FILL = "#F97316" # Orange for DNS Server box
        BOX_STROKE_COLOR = "#FFFFFF" # White stroke for boxes

        self.camera.background_color = BG_COLOR

        # Title of the scene
        scene_title_text = "DNS Lookup Process"
        title = Text(scene_title_text, font_size=48, color=TEXT_COLOR)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP, buff=0.5))
        self.wait(0.5)

        # Visual Element: Client
        client_label_text = "Client"
        client_label = Text(client_label_text, font_size=28, color=TEXT_COLOR)
        client_box = Rectangle(width=2.5, height=1.5, color=BOX_STROKE_COLOR, fill_color=CLIENT_BOX_FILL, fill_opacity=0.9)
        client = VGroup(client_box, client_label).move_to(LEFT * 4.5 + UP * 0.5)

        # Visual Element: DNS Server
        dns_server_label_text = "DNS Server"
        dns_server_label = Text(dns_server_label_text, font_size=28, color=TEXT_COLOR)
        dns_server_box = Rectangle(width=3, height=2, color=BOX_STROKE_COLOR, fill_color=DNS_SERVER_BOX_FILL, fill_opacity=0.9)
        dns_server = VGroup(dns_server_box, dns_server_label).move_to(RIGHT * 4.5 + UP * 0.5)

        self.play(Write(client_box), Write(client_label), Write(dns_server_box), Write(dns_server_label))
        self.wait(1)

        # Visual Elements: Domain Name and IP Address values
        domain_name_val = "example.com" 
        ip_address_val = "93.184.216.34" # Actual IP for example.com

        # --- DNS Request Process ---
        # 1. Client prepares to request Domain Name lookup
        request_info_text = Text(f"Request: IP for\n'{domain_name_val}'?", font_size=20, color=TEXT_COLOR, line_spacing=0.7)
        request_info_text.next_to(client, DOWN, buff=0.3)
        self.play(Write(request_info_text))
        self.wait(0.3)

        # 2. Data (Domain Name) flows from Client to DNS Server
        data_packet_domain = Text(domain_name_val, font_size=22, color=HIGHLIGHT_COLOR, weight=BOLD)
        data_packet_domain.move_to(client.get_right() + RIGHT*0.1) # Position packet to start from client edge

        request_arrow = Arrow(
            start=client.get_right(), end=dns_server.get_left(), buff=0.1, color=HIGHLIGHT_COLOR,
            stroke_width=5, max_tip_length_to_length_ratio=0.2, max_stroke_width_to_length_ratio=4
        )
        
        self.play(
            GrowArrow(request_arrow), # Animation Type: Indicate (flow)
            data_packet_domain.animate.move_to(dns_server.get_left() + LEFT*0.8 + UP*0.1) # Packet arrives near DNS server
        )
        self.play(Indicate(dns_server, color=HIGHLIGHT_COLOR, scale_factor=1.15)) # Animation Type: Indicate (reception)
        self.wait(0.1)
        self.play(FadeOut(request_info_text)) # Clean up client-side request text

        # 3. DNS Server "processes" the request
        processing_text = Text("Looking up IP...", font_size=18, color=TEXT_COLOR)
        processing_text.next_to(dns_server, DOWN, buff=0.3)
        self.play(FadeIn(processing_text), FadeOut(data_packet_domain)) # Domain Name packet is "consumed"
        self.wait(1.5) # Simulate lookup time
        self.play(FadeOut(processing_text))
        self.wait(0.2)

        # --- DNS Response Process ---
        # 1. DNS Server prepares response with IP Address
        response_info_text = Text(f"Found: '{domain_name_val}' is\n'{ip_address_val}'", font_size=20, color=TEXT_COLOR, line_spacing=0.7)
        response_info_text.next_to(dns_server, DOWN, buff=0.3)
        self.play(Write(response_info_text))
        self.wait(0.3)

        # 2. Data (IP Address) flows from DNS Server to Client
        data_packet_ip = Text(ip_address_val, font_size=22, color=HIGHLIGHT_COLOR, weight=BOLD)
        data_packet_ip.move_to(dns_server.get_left() + LEFT*0.1) # Position packet to start from server edge

        response_arrow = Arrow(
            start=dns_server.get_left(), end=client.get_right(), buff=0.1, color=HIGHLIGHT_COLOR,
            stroke_width=5, max_tip_length_to_length_ratio=0.2, max_stroke_width_to_length_ratio=4
        )

        self.play(
            GrowArrow(response_arrow), # Animation Type: Indicate (flow)
            data_packet_ip.animate.move_to(client.get_right() + RIGHT*0.8 + UP*0.1) # Packet arrives near client
        )
        self.play(Indicate(client, color=HIGHLIGHT_COLOR, scale_factor=1.15)) # Animation Type: Indicate (reception)
        self.wait(0.1)
        self.play(FadeOut(response_info_text)) # Clean up server-side response text

        # 3. Client receives the IP Address
        ip_received_display = Text(f"IP for {domain_name_val}:\n{ip_address_val}", font_size=20, color=HIGHLIGHT_COLOR, line_spacing=0.7)
        ip_received_display.next_to(client, DOWN, buff=0.3)
        self.play(FadeOut(data_packet_ip), FadeIn(ip_received_display)) # IP Address packet "consumed", info displayed at client
        self.wait(1)

        # Clean up arrows from the scene
        self.play(FadeOut(request_arrow), FadeOut(response_arrow))
        self.wait(0.5)

        # Final summary message
        summary_text = Text("DNS Resolution Complete", font_size=32, color=TEXT_COLOR)
        summary_text.next_to(title, DOWN, buff=0.8) # Positioned below the main title
        
        # Adjust layout slightly for final summary message if needed
        current_elements_on_screen = VGroup(client, dns_server, ip_received_display)
        self.play(
            Write(summary_text),
            current_elements_on_screen.animate.shift(DOWN*0.3), # Slightly shift elements to make space
            title.animate.shift(DOWN*0.1) # Adjust title slightly
        )
        self.wait(3) # Hold the final scene for a few seconds
