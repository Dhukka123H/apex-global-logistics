
# Install the library if needed:
# python -m pip install pillow

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path


def create_chart():
    # Save image in the same folder as this Python file
    output_path = Path(__file__).parent / "corporate_chart.png"

    # High-resolution canvas for a professional appearance
    SCALE = 2
    W, H = 1000, 650

    img = Image.new("RGB", (W, H), "#F3F6FA")
    draw = ImageDraw.Draw(img)

    # Corporate color palette
    NAVY = "#142D4E"
    BLUE = "#2878C8"
    GREEN = "#168568"
    ORANGE = "#D97732"
    DARK = "#25364A"
    MUTED = "#718096"
    WHITE = "#FFFFFF"
    BORDER = "#DCE4EE"
    LIGHT_BLUE = "#EAF3FC"
    LIGHT_GREEN = "#E9F6F1"
    LIGHT_ORANGE = "#FFF2E8"

    # Fonts with Windows and cross-platform fallback
    def get_font(size, bold=False):
        candidates = (
            [
                "C:/Windows/Fonts/arialbd.ttf",
                "C:/Windows/Fonts/segoeuib.ttf",
            ]
            if bold else [
                "C:/Windows/Fonts/arial.ttf",
                "C:/Windows/Fonts/segoeui.ttf",
            ]
        )

        for font_path in candidates:
            try:
                return ImageFont.truetype(font_path, size)
            except OSError:
                continue

        return ImageFont.load_default()

    title_font = get_font(30, True)
    subtitle_font = get_font(15)
    name_font = get_font(23, True)
    role_font = get_font(16)
    label_font = get_font(13, True)
    small_font = get_font(12)

    # Header banner
    draw.rounded_rectangle(
        (35, 30, W - 35, 135),
        radius=20,
        fill=NAVY
    )

    draw.text(
        (65, 51),
        "CORPORATE ORGANIZATION",
        font=title_font,
        fill=WHITE
    )

    draw.text(
        (67, 96),
        "APEX GLOBAL LOGISTICS  |  MANAGEMENT STRUCTURE",
        font=subtitle_font,
        fill="#C6D8EC"
    )

    # Decorative header accent
    draw.rounded_rectangle(
        (W - 95, 55, W - 65, 110),
        radius=10,
        fill=BLUE
    )

    # Chart title
    draw.text(
        (55, 165),
        "Leadership Hierarchy",
        font=get_font(21, True),
        fill=DARK
    )

    draw.text(
        (55, 198),
        "Executive leadership and departmental functions",
        font=subtitle_font,
        fill=MUTED
    )

    # Card positions
    ceo_box = (320, 245, 680, 355)
    cfo_box = (80, 455, 430, 565)
    admin_box = (570, 455, 920, 565)

    # Connection lines, drawn behind the cards
    line_color = "#9AAEC3"
    line_width = 5

    ceo_center_x = (ceo_box[0] + ceo_box[2]) // 2
    cfo_center_x = (cfo_box[0] + cfo_box[2]) // 2
    admin_center_x = (admin_box[0] + admin_box[2]) // 2

    junction_y = 405

    draw.line(
        [(ceo_center_x, ceo_box[3]),
         (ceo_center_x, junction_y)],
        fill=line_color,
        width=line_width
    )

    draw.line(
        [(cfo_center_x, junction_y),
         (admin_center_x, junction_y)],
        fill=line_color,
        width=line_width
    )

    draw.line(
        [(cfo_center_x, junction_y),
         (cfo_center_x, cfo_box[1])],
        fill=GREEN,
        width=line_width
    )

    draw.line(
        [(admin_center_x, junction_y),
         (admin_center_x, admin_box[1])],
        fill=ORANGE,
        width=line_width
    )

    # Draw junction dot
    draw.ellipse(
        (
            ceo_center_x - 7,
            junction_y - 7,
            ceo_center_x + 7,
            junction_y + 7
        ),
        fill=BLUE
    )

    # Helper to draw polished organizational cards
    def draw_card(box, name, role, department, accent,
                  light_color, executive=False):

        x1, y1, x2, y2 = box

        # Card shadow
        draw.rounded_rectangle(
            (x1 + 4, y1 + 6, x2 + 4, y2 + 6),
            radius=18,
            fill="#E1E7EF"
        )

        # Main card
        draw.rounded_rectangle(
            box,
            radius=18,
            fill=WHITE,
            outline=BORDER,
            width=2
        )

        # Colored accent bar
        draw.rounded_rectangle(
            (x1, y1, x1 + 10, y2),
            radius=5,
            fill=accent
        )

        # Role badge
        badge_text = "EXECUTIVE" if executive else "DEPARTMENT"

        badge_box = (x1 + 25, y1 + 15, x2 - 20, y1 + 39)

        draw.rounded_rectangle(
            badge_box,
            radius=8,
            fill=light_color
        )

        draw.text(
            (x1 + 36, y1 + 20),
            badge_text,
            font=label_font,
            fill=accent
        )

        # Name and role
        draw.text(
            (x1 + 25, y1 + 49),
            name,
            font=name_font,
            fill=NAVY
        )

        draw.text(
            (x1 + 25, y1 + 80),
            role,
            font=role_font,
            fill=MUTED
        )

        # Department label
        draw.text(
            (x2 - 22, y2 - 24),
            department,
            font=small_font,
            fill=accent,
            anchor="ra"
        )

    # CEO card
    draw_card(
        ceo_box,
        "Jane Smith",
        "Chief Executive Officer",
        "CEO",
        BLUE,
        LIGHT_BLUE,
        executive=True
    )

    # CFO card
    draw_card(
        cfo_box,
        "Finance Office",
        "Chief Financial Officer",
        "CFO",
        GREEN,
        LIGHT_GREEN
    )

    # Administration card
    draw_card(
        admin_box,
        "Administration",
        "Administrative Department",
        "ADMIN",
        ORANGE,
        LIGHT_ORANGE
    )

    # Footer
    draw.line(
        [(45, 605), (W - 45, 605)],
        fill=BORDER,
        width=2
    )

    draw.text(
        (50, 620),
        "APEX GLOBAL LOGISTICS",
        font=label_font,
        fill=NAVY
    )

    draw.text(
        (W - 50, 620),
        "CORPORATE STRUCTURE",
        font=small_font,
        fill=MUTED,
        anchor="ra"
    )

    # Export a crisp high-resolution PNG
    img.save(output_path, quality=95, dpi=(180, 180))

    print("Corporate chart generated successfully!")
    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    create_chart()
