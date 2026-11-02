from bs4 import BeautifulSoup
import json
import sys

if __name__ == '__main__':
    argv = sys.argv
    if len(argv) != 3:
        raise ValueError("Usage: python script.py <input_path> <output_path>")
    else:
        input_path = argv[1]
        output_path = argv[2]

    with open(input_path) as f:
        text = f.read()
        
    soup = BeautifulSoup(text, 'lxml')
    dictionary = {'nbformat': 4, 'nbformat_minor': 1, 'cells': [], 'metadata': {}}
    
    for d in soup.find_all("div"):
        if 'class' in d.attrs.keys():
            for clas in d.attrs["class"]:
                if clas in ["text_cell_render", "input_area"]:
                    # code cell
                    if clas == "input_area":
                        cell = {}
                        cell['metadata'] = {}
                        cell['outputs'] = []
                        # Strip newlines from the start and end of the text
                        cell['source'] = [d.get_text().strip('\n')]
                        cell['execution_count'] = None
                        cell['cell_type'] = 'code'
                        dictionary['cells'].append(cell)
                    else:
                        cell = {}
                        cell['metadata'] = {}
                        # Strip newlines from the start and end of the markdown content
                        cell['source'] = [d.decode_contents().strip('\n')]
                        cell['cell_type'] = 'markdown'
                        dictionary['cells'].append(cell)
                        
    with open(output_path, 'w') as f:
        f.write(json.dumps(dictionary))
