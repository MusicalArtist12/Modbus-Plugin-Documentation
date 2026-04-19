import re

# replace <HEADER> with a table using the functions metadata
# replace <{key}> with an appropriate subheading
def on_page_markdown(markdown: str, page, config, files):
    functions: object = page.meta.get('functions')
    if functions is None:
        return markdown

    markdown_table = []

    markdown_table.append("| Return | Call |")
    markdown_table.append("| --- | --- |")

    for key in functions.keys():
        output = functions[key]["output"]
        inputs = [i.replace("<", "&lt;").replace(">", "&gt;") for i in functions[key].get("inputs", [])]
        annotations = functions[key].get("annotations", [])

        string = f"| {output} | [{key}](#{key})({', '.join(inputs)}) |"

        markdown_table.append(string)


        def handle_param(param: str):
            spl = param.split(' ')
            type = ' '.join(spl[0:-1])
            name = spl[-1]

            return f"<mark>{type}</mark> {name}"

        params = ', '.join([handle_param(i) for i in inputs])
        annotations = f"<i>{" ".join(annotations)}</i>" if len(annotations) > 0 else ""

        markdown = markdown.replace(f"<{key}>",
                                    f"<hr id=\"{key}\"></hr>\n" +
                                    f"<p class=\"mono-title\"><mark>{output}</mark> <strong>{key}</strong>({params}) {annotations} <a class=\"link\" href=\"#{key}\">link</a></p>")



    markdown = markdown.replace("<HEADER>", "\n".join(markdown_table))



    return markdown

def on_page_content(html: str, page, config, files):
    # negative lookahead, as long as its not immediately followed by a header tag, link to subheader, or part of another link
    # this probably doesn't work for everything lol
    html = re.sub(r"(UModbusTcpSocket|UModbusClient|ModbusError)(?![^<>]*(<\/h[1-6]>)|(<\/a>)|([#\"\.]))", r"<a href=../\1 class='re'>\1</a>", html)

    html = re.sub(r"(TArray)", r"<a href='https://dev.epicgames.com/documentation/unreal-engine/API/Runtime/Core/TArray?lang=en-US'>\1</a>", html)

    return html