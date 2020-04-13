from datetime import datetime

with open('words.txt','r') as fh1:
    lines = fh1.read().split('\n')

with open('template.html', 'r') as fh2:
    template = fh2.read()

lines.reverse()

def format_word(line):

    if "corona" not in line.lower() or line.strip() == "":
        return ""

    parts = line.lower().split('corona')
    
    suffix = parts[1]
    dash = ""
    
    if suffix[0] == "-":
        dash = "-"
        suffix = suffix[1:]
    
    return "<li><span>Corona{dash}</span>{suffix}</li>".format(dash=dash, suffix=suffix)

num_items = len(lines)
content = '\n'.join([format_word(line) for line in lines])
today = datetime.today().strftime("%d-%m-%Y")

with open('index.html','w') as fh3:
    formatted = template.replace('{updated_at}',today).replace('{num_items}', str(num_items+1)).replace('{content}', content)
    fh3.write(formatted)
    print('Wrote {} items.'.format(num_items))