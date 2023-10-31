import argparse
from itertools import cycle

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()



def visualize_color_mapping(color_mapping):
    """Generate an HTML legend for entity types and their corresponding colors."""
    html_legend = "<div><b>Legend:</b></div>"
    for entity, color in color_mapping.items():
        html_legend += f'<div style="margin: 5px; padding: 3px; background-color: {color}; display: inline-block;">{entity}</div>'
    return html_legend

def visualize_annotations(text, annotations, color_mapping):
    # Sort annotations by start offset
    annotations = sorted(annotations, key=lambda x: x["start"])
    
    highlighted_text = ""
    prev_end = 0
    for ann in annotations:
        # Extract non-annotated text segment
        highlighted_text += text[prev_end:ann["start"]]
        # Add annotated segment with background color
        color = color_mapping.get(ann["type"], "lightgrey")
        highlighted_text += f'<span style="background-color: {color}">{text[ann["start"]:ann["end"]]}</span>'
        prev_end = ann["end"]
    
    # Add remaining text
    highlighted_text += text[prev_end:]
    
    return highlighted_text


def main(txt_file, ann_file, output_file):
    # Read the contents of the input files
    sample_txt_content = read_file(txt_file)
    sample_ann_content = read_file(ann_file)
    
    # Colors to be used for annotations
    COLORS = cycle(["lightblue", "lightgreen", "lightpink", "lightsalmon", "lightyellow", "lightcyan"])
    
    # Parsing the .ann content
    annotations = []
    entity_types = set()  # To track unique entity types

    for line in sample_ann_content.split("\n"):
        parts = line.split("\t")
        _, offsets, text = parts
        start, end = map(int, offsets.split()[1:])
        entity_type = offsets.split()[0]
        annotations.append({
            "start": start,
            "end": end,
            "text": text,
            "type": entity_type
        })
        entity_types.add(entity_type)

    # Assigning a color to each entity type
    color_mapping = {entity: next(COLORS) for entity in entity_types}

    # Visualize the color mapping
    html_legend = visualize_color_mapping(color_mapping)

    # Visualize the annotations
    html_content = visualize_annotations(sample_txt_content, annotations, color_mapping)
    
    # Save the visualized content to the output file
    with open(output_file, 'w') as f:
        f.write(html_legend +"\n\n" + html_content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Visualize BRAT annotations.')
    parser.add_argument('txt_file', type=str, help='Path to the .txt file.')
    parser.add_argument('ann_file', type=str, help='Path to the .ann file.')
    parser.add_argument('output_file', type=str, help='Path to save the visualized content.')
    args = parser.parse_args()

    main(args.txt_file, args.ann_file, args.output_file)
