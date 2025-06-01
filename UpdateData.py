import requests
import json
import os


API_URL = "http://localhost:3000"


def generate_api_url(keyword):
  # Simple normalization: lowercase and replace spaces with '+'
  normalize_keyword = keyword.lower().replace(' ', '+')
  return f"{API_URL}/api/search?keyword={normalize_keyword}&allowSites=jobvision,karlancer,punisha,jobinja"

def fetch_and_save_data(keyword):
  """Fetches data from API for a keyword and saves it as a JSON file."""
  api_url = generate_api_url(keyword)
  print(f"Fetching data for keyword: '{keyword}' from {api_url}")
  try:
    response = requests.get(api_url)
    response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)

    data = response.json()

    # Create filename from keyword (lowercase, replace spaces with underscore)
    filename = keyword.lower().replace(' ', '_') + '.json'
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    os.makedirs(data_dir, exist_ok=True) # Create data directory if it doesn't exist
    file_path = os.path.join(data_dir, filename)

    with open(file_path, 'w', encoding='utf-8') as f:
      json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Successfully saved data for '{keyword}' to {file_path}")

  except requests.exceptions.RequestException as e:
    print(f"Error fetching data for '{keyword}': {e}")
  except json.JSONDecodeError:
    print(f"Error decoding JSON response for '{keyword}'.")
  except IOError as e:
    print(f"Error writing file for '{keyword}': {e}")
  except Exception as e:
    print(f"An unexpected error occurred for '{keyword}': {e}")

def process_keywords_file(file_path):
  """Reads keywords from a file and fetches/saves data for each."""
  print(f"Processing keywords from file: {file_path}")
  try:
    with open(file_path, 'r', encoding='utf-8') as f:
      for line in f:
        keyword = line.strip() # Remove leading/trailing whitespace and newline characters
        if keyword: # Process non-empty lines
          fetch_and_save_data(keyword) # Call the new function
  except FileNotFoundError:
    print(f"Error: The file {file_path} was not found.")
  except Exception as e:
    print(f"An error occurred while processing the file: {e}")

# Example usage:
if __name__ == "__main__":
  keywords_file_path = os.path.join(os.path.dirname(__file__), "keywords.txt")
  process_keywords_file(keywords_file_path)
