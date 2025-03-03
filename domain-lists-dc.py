import math
import requests

MAX_CHARS = 6500

def custom_escape(s):
    placeholder = "__WILDCARD__"
    s = s.replace(".*", placeholder)

    # Define characters to escape: . ? + ( ) [ ] { } ^ $ \ | /
    specials = r'.?+()[]{}^$\|/'
    escaped = ""
    for char in s:
        if char in specials:
            escaped += "\\" + char
        else:
            escaped += char

    # Restore literal wildcard sequences
    escaped = escaped.replace(placeholder, ".*")
    # Replace any escaped caret "\^" with "[\^]" for Cloudflare RE2 compatibility.
    escaped = escaped.replace("\\^", "[\\^]")
    return escaped

def process_input(input_source):
    rules = []
    # Determine if input_source is a URL or a local file.
    if input_source.startswith("http://") or input_source.startswith("https://"):
        try:
            response = requests.get(input_source)
            response.raise_for_status()
            lines = response.text.splitlines()
        except Exception as e:
            raise Exception(f"Failed to fetch URL: {e}")
    else:
        try:
            with open(input_source, 'r', encoding='utf-8') as f:
                lines = f.read().splitlines()
        except Exception as e:
            raise Exception(f"Failed to read file: {e}")

    for line in lines:
        line = line.strip()
        if not line or line.startswith("!"):
            continue
        # Process the line with custom_escape.
        rules.append(custom_escape(line))
    return rules

def group_rules(rules, max_length):
    groups = []
    current_group = ""
    allowed_length = max_length - 2

    for rule in rules:
        if not current_group:
            candidate = rule
        else:
            candidate = current_group + "|" + rule

        if len(candidate) <= allowed_length:
            current_group = candidate
        else:
            # Finish the current group and start a new one.
            groups.append(current_group)
            current_group = rule
    if current_group:
        groups.append(current_group)
    return groups

input_source = input("Enter the input TXT file URL or local file name: ").strip()

try:
    rules = process_input(input_source)
    if not rules:
        raise Exception("No valid domain rules found in the input.")
except Exception as e:
    print("An error occurred while processing the input:", e)
    raise

groups = group_rules(rules, MAX_CHARS)

output_files = []
for idx, group in enumerate(groups):
    regex = "(" + group + ")"
    file_name = f"{idx+1}.txt"
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(regex)
    output_files.append(file_name)

print("Regex patterns successfully written to the following file(s):")
for f in output_files:
    print(f)
