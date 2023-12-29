import re
from subprocess import Popen
from bs4 import BeautifulSoup
from pathlib import Path
import sys

from images import ImageHost

PATH_INPUT_MD = sys.argv[1]

PATH_INPUT_MD = Path(PATH_INPUT_MD)

ROOT_PATH = Path(__file__).parent
PATH_md_temp = ROOT_PATH / "temp/result.md"
PATH_html_temp = ROOT_PATH / "temp/result.html"
PATH_html_result = PATH_INPUT_MD.parent / f"{PATH_INPUT_MD.stem}.html"
PATH_pandoc = '/opt/homebrew/bin/pandoc'


def replace_link(m):
    text, url = m.groups()
    url_i = urls.index(url)
    return re.sub(r"\[(?P<text>.*?)\]\((?P<url>.*?)\)",
                  f"{text} <sup>[{url_i+1}]</sup>", m.group())


def replace_image(m):
    text, url = m.groups()
    image_url = image_host.upload(url)
    return re.sub(url, image_url, m.group())


with open(PATH_INPUT_MD, "r") as f:
    content = f.read()
image_host = ImageHost()

pattern_link = r"[^!]\[(?P<text>.*?)\]\((?P<url>.*?)\)"
pattern_image = r"!\[(?P<text>.*?)\]\((?P<url>.*?)\)"
links = re.findall(pattern_link, content)
urls = []
for t, l in links:  # keep the urls in order (so not using `set()`)
    if l not in urls:
        urls.append(l)

content = re.sub(pattern_link, replace_link, content)
content += "\n<p></p>\n---\n\n" + "\n".join(
    [f"\[{i+1}\]: {u}  " for i, u in enumerate(urls)])

for t, l in re.findall(pattern_image, content):
    content = re.sub(f"\n{t}\n", "\n", content)

content = re.sub(pattern_image, replace_image, content)

with open(PATH_md_temp, "w") as f:
    f.write(content)
Popen([PATH_pandoc, PATH_md_temp, '-o', PATH_html_temp])

with open(PATH_html_temp, "r") as f:
    soup = BeautifulSoup(f.read(), "lxml")

################################# HTML process #################################
style_list = [
    # ("h1", "font-size: 24px; font-weight: bold; margin-top: 20px; margin-bottom: 5px;"),
    (["p", "li", "ul"], "font-size:14;"),
    ("sup", "color: #1d222d;"),
    ("figure", "text-align: center;")
]

for node, style in style_list:
    elements = soup.find_all(node)
    for el in elements:
        if 'style' in el.attrs:
            el['style'] = el['style'].strip(' ;') + '; ' + style
        else:
            el['style'] = style

figcaptions = soup.find_all('figcaption')
for figcaption in figcaptions:
    text = figcaption.get_text().strip()  # 获取元素文本并去除空格

    # 如果文本以 'Screenshot' 或 'Untitled' 开头，则删除元素
    if text.startswith(('Screenshot', 'Untitled')):
        figcaption.decompose()  # 删除元素
    else:
        # 设置居中，大小为12px，颜色为灰色
        figcaption[
            'style'] = 'text-align: center; font-size: 12px; color: gray;'

for node in ['h1', 'h2']:
    elements = soup.find_all(node)
    with open(f"templates/{node}.html", "r") as f:
        node_template = f.read()
    for el in elements:
        el.replace_with(
            BeautifulSoup(node_template.format(text=el.text.strip()),
                          'html.parser'))

# 将修改后的 HTML 内容写回文件
with open(PATH_html_result, 'w', encoding='utf-8') as file:
    file.write(str(soup))
