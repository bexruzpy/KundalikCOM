# Update the geometry parsing to handle non-integer or improperly formatted values

def safe_int_conversion(text, default=0):
    """Convert text to integer safely; return a default value if conversion fails."""
    try:
        return int(text.strip())
    except (ValueError, AttributeError):
        return default  # Default value if conversion fails

def convert_to_kv_fixed(element, depth=0):
    """Convert each widget and its properties from Qt XML to Kivy format with error handling."""
    indentation = '    ' * depth  # Indentation level for Kivy
    widget_class = element.get('class', 'Widget')  # Default to generic 'Widget' if class not found
    widget_name = element.get('name', 'unknown')

    kv_structure = [f"{indentation}{widget_class}:" if widget_class else ""]  # Add widget class
    prop_indent = indentation + '    '  # Inner indentation for properties

    # Parsing common attributes to translate to Kivy
    for child in element:
        if child.tag == 'property':
            name = child.get('name')
            if name == 'text':
                # Translate the 'text' property
                kv_structure.append(f"{prop_indent}text: '{child.text or ''}'")
            elif name == 'geometry':
                # Translate 'geometry' attributes to Kivy 'pos' and 'size' with safe conversion
                geom_values = {c.tag: safe_int_conversion(c.text) for c in child}  # x, y, width, height
                pos = (geom_values.get('x', 0), geom_values.get('y', 0))
                size = (geom_values.get('width', 100), geom_values.get('height', 30))
                kv_structure.append(f"{prop_indent}pos: {pos}")
                kv_structure.append(f"{prop_indent}size: {size}")

    # Recursively convert child widgets
    for sub_element in element.findall(".//widget"):
        kv_structure.extend(convert_to_kv_fixed(sub_element, depth + 1))

    return kv_structure

# Parse the main root widget with updated parsing
kv_content_fixed = []
kv_content_fixed.extend(convert_to_kv_fixed("Home.ui"))

# Save the fixed .kv file
kv_file_path_fixed = 'Home.kv'
with open(kv_file_path_fixed, 'w') as kv_file:
    kv_file.write('\n'.join(kv_content_fixed))

