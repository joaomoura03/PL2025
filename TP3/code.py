import re

def markdown_to_html(markdown):

    # Cabeçalhos
    markdown = re.sub(r'^### (.*)', r'<h3>\1</h3>', markdown)
    markdown = re.sub(r'^## (.*)', r'<h2>\1</h2>', markdown)
    markdown = re.sub(r'^# (.*)', r'<h1>\1</h1>', markdown)
    
    # Bold
    markdown = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown)
    
    # Itálico
    markdown = re.sub(r'\*(.*?)\*', r'<i>\1</i>', markdown)
    
    # Listas numeradas
    markdown = re.sub(r'(?m)^\d+\. (.*)', r'<li>\1</li>', markdown)
    markdown = re.sub(r'(<li>.*?</li>)', r'<ol>\1</ol>', markdown, flags=re.DOTALL)
    
    # Imagens
    markdown = re.sub(r'\!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', markdown)
    
    # Links
    markdown = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown)
    

    return markdown



# Teste
test_md = "Como se vê na imagem seguinte: [imagem dum coelho](http://www.coellho.com)"

test_md2 = """
1. Primeiro item
2. Segundo item
3. Terceiro item
"""

print(markdown_to_html(test_md))
