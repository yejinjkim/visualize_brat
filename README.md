

## README: BRAT Annotation Visualization Tool

### Description
This script provides a way to visualize annotations from the BRAT format. It takes in a `.txt` file containing the raw text and a corresponding `.ann` file containing the annotations. The output is an HTML file that visually highlights the annotations on the text.

### Requirements
- Python 3.x

### Usage

1. Save the provided Python code to a file named `visualize_brat.py`.
   
2. To run the script, use the following command:

   ```
   python visualize_brat.py [txt_file_path] [ann_file_path] [output_html_file_path]
   ```

   - `txt_file_path`: Path to the `.txt` file containing the raw text.
   - `ann_file_path`: Path to the `.ann` file containing the BRAT annotations.
   - `output_html_file_path`: Path where the visualized content will be saved as an HTML file.

### Example

Assuming you have `sample.txt` and `sample.ann` in the current directory, and you want to save the output as `output.html`:

```
python visualize_brat.py sample.txt sample.ann output.html
```

After executing the above command, open the `output.html` file in a web browser to see the visualized annotations.
