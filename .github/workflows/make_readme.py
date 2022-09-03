from pathlib import Path
import re


def insert_text(main_readme: str, text: str) -> str:
    """Insert Readmes at comment tags

    Parameters
    ----------
    main_readme : str
        Text in main readme
    text : str
        text to insert

    Returns
    -------
    str
        merged readmes
    """
    open_tag = "<!-- TALKS -->"
    close_tag = "<!-- //TALKS -->"

    first = main_readme.split(open_tag)[0]
    second = main_readme.split(close_tag)[1]

    return "\n".join([first, open_tag] + text + [close_tag, second])


def get_readme_paths():
    return [readme for readme in Path(".").rglob("README.md") if readme != Path(".", "README.md")]


def read_readmes(paths: list) -> list:
    out_txt = []
    for path in paths:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read().replace("# ", "### ")

        m = re.findall(r"Video \|\n(.*)\n(.*)\n", text)[0]

        path_str = str(path.parents[0]).replace(" ", "%20")

        out_txt.append(
            text.replace(m[0], m[0] + " ------ |")
            .replace(m[1], m[1] + f" [Slides]({path_str}/) |")
            .replace(" Video |", " Video | Slides |")
        )
    return out_txt


with open("README.md", "r", encoding="utf-8") as f:
    main_readme = f.read()

readme_paths = get_readme_paths()
text = read_readmes(readme_paths)
mod_readme = insert_text(main_readme, text)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(mod_readme)
