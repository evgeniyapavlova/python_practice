import json
import os


directory = "lp_revie"
output_directory = "output"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for filename in os.listdir(directory):
    if filename.endswith(".json"):
        # Construct input and output file paths
        input_file_path = os.path.join(directory, filename)
        output_file_path = os.path.join(output_directory, f"{filename[:-5]}.js")

        # Read the input JSON file
        with open(input_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Extract the required fields
        required_fields = {
            "reviews.matt_text": data.get("reviews.matt_text"),
            "reviews.ashish_text": data.get("reviews.ashish_text"),
            "reviews.ahmad_text": data.get("reviews.ahmad_text"),
            "reviews.brian_text": data.get("reviews.brian_text"),
            "reviews.amanda_text": data.get("reviews.amanda_text"),
            "reviews.jenn_text": data.get("reviews.jenn_text"),
        }

        js_content = f"export default {json.dumps(required_fields, indent=2, ensure_ascii=False)};"

        # Write the extracted fields to the output JSON file
        with open(output_file_path, "w", encoding="utf-8") as f:
            f.write(js_content)

        print(
            f"Required fields extracted from {filename} and saved to {output_file_path}"
        )
