from datetime import datetime

with open('words.txt','r') as fh1:
    lines = fh1.read().split('\n')

with open('template.html', 'r') as fh2:
    template = fh2.read()

lines.reverse()

def format_word(line):

    if "corona" not in line.lower() or line.strip() == "":
        return None

    parts = line.lower().split('corona')
    
    suffix = parts[1]
    dash = ""
    
    if suffix[0] == "-":
        dash = "-"
        suffix = suffix[1:]
    
    return "<li><span>Corona{dash}</span>{suffix}</li>".format(dash=dash, suffix=suffix)

parsed = [format_word(line) for line in lines]
parsed = list(filter(None, parsed)) # remove None lines

content = '\n'.join(parsed)
num_css_items = len(parsed)+1

today = datetime.today().strftime("%d-%m-%Y")

with open('index.html','w') as fh3:
    formatted = template.replace('{updated_at}',today).replace('{num_css_items}', str(num_css_items)).replace('{content}', content)
    fh3.write(formatted)
    print('Wrote {} items.'.format(len(parsed)))