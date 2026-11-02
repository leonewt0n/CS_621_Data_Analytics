import json, os, sys
from bs4 import BeautifulSoup

def html_to_ipynb(html_path):
    soup = BeautifulSoup(open(html_path, encoding='utf-8'), 'html.parser')
    cells = [{"cell_type": "code", "metadata": {}, "outputs": [], "execution_count": None, "source": [d.get_text().strip()]} for d in soup.select('div.jp-InputArea-editor')]
    json.dump({"cells": cells, "metadata": {}, "nbformat": 4, "nbformat_minor": 5}, open(os.path.splitext(html_path)[0] + '.ipynb', 'w'))

if __name__ == '__main__':
    html_to_ipynb(sys.argv[1])
