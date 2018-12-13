def save_file(file_name, card_name, content):
    with open(f"../../jace/page_files/{file_name}/{card_name}.html", "wb") as f:
        f.write(content)

