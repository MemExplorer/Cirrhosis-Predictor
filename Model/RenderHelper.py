class RenderHelper:
    def render_page(file_path):
        print("Content-Type: text/html\n")
        with open(file_path, "r") as f:
            contents = f.read()
            print(contents)
    