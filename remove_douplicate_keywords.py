# script.py

import sys

def remove_duplicate_lines(input_filename, output_filename):
    """
    Reads a file, removes duplicate lines, and writes unique lines to a new file.

    Args:
        input_filename (str): The path to the input file.
        output_filename (str): The path to the output file.
    """
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()

        # Use a set to store unique lines while maintaining order
        # This approach preserves order for Python 3.7+
        unique_lines = []
        seen_lines = set()
        for line in lines:
            # Remove leading/trailing whitespace (including newline characters)
            stripped_line = line.strip()
            if stripped_line and stripped_line not in seen_lines:
                unique_lines.append(line) # Keep original line with newline
                seen_lines.add(stripped_line)
            elif not stripped_line and line not in seen_lines:
                # Handle empty lines specifically
                unique_lines.append(line)
                seen_lines.add(line)


        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.writelines(unique_lines)

        print(f"Duplicate lines removed successfully. Unique lines saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def convert_to_lowercase(input_filename, output_filename):
    """
    Reads a file, converts all characters to lowercase, and writes to a new file.

    Args:
        input_filename (str): The path to the input file.
        output_filename (str): The path to the output file.
    """
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()

        # Convert all lines to lowercase while preserving original line endings
        lowercased_lines = [line.lower() for line in lines]

        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.writelines(lowercased_lines)

        print(f"All characters converted to lowercase successfully. Saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":

    input_file = "./keywords.txt"
    output_file = "./unique_keywords.txt"
    convert_to_lowercase(input_file, output_file)
    remove_duplicate_lines(output_file, output_file)