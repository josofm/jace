def save_file(file_name, card_name, content):
    with open(f"../../jace/page_files/spider_pages/{file_name}/{card_name}.html", "wb") as f:
        f.write(content)

