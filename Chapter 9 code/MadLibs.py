placeholders = ['NOUN','VERB_ING','ADJECTIVE','ANY_WORD']
def crazy_lib(filename):
    file = open(filename,'r')
    text = ''
    for line in file:
        text = text + process_line(line)
    file.close
    return text
def process_line(line):
    processed_line = ''
    words = line.split()
    for word in words:
        if word in placeholders:
            answer = input('Enter ' + word + ':')
            processed_line = processed_line + answer + ' ' 
        else:
            processed_line = processed_line + word + ' ' 
    return processed_line + '\n'
def main():
    lib = crazy_lib('TemplateLibs.txt')
    return lib
print(main())
    
