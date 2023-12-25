def convert_to_str(data):
    if isinstance(data, (int, float, bool, str, type(None))):
        # Keep primitive types as is
        return data
    elif isinstance(data, dict):
        # Convert dictionary values recursively
        return {key: convert_to_str(value) for key, value in data.items()}
    elif isinstance(data, (list, tuple)):
        # Convert list or tuple elements recursively
        return [convert_to_str(item) for item in data]
    elif isinstance(data, set):
        # Convert set elements recursively
        return {convert_to_str(item) for item in data}
    else:
        # Convert non-primitive types to string representation
        return str(data)


import re


def extract_hashtags(post_content):
    # Define a regular expression pattern for hashtags
    hashtag_pattern = r'#\w+'

    # Use re.findall to find all occurrences of the pattern in the post content
    hashtags = re.findall(hashtag_pattern, post_content)

    return hashtags