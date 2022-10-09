from os import system


keywords = {
    '只因': 'while',
    '食不食': 'if',
    '油饼': 'not',
    '鸡叫': 'print',
    '真IKUN': 'True',
    '小黑子': 'False',
    '下蛋': 'def',
    '练习': 'for',
    '与': 'and',
    '或': 'or',
    '空': 'None',
    '荔枝': 'break',
    '跳过': 'continue',
    '鸡群': 'class',
    '否则食不食': 'elif',
    '否则': 'else',
    '鸡圈': 'import',
    '忽略': 'pass',
    '律师函警告': 'return',
    '在': 'in',
    '迭代鸡': 'range',
    '鸡始化': '__init__',
    '自鸡': 'self',
    '添加鸡素': 'append',
    '长度': 'len'
}
splitWordList = [' ', '(', ')', ':', '\n', '.', '=', ',', '<', '>', '[', ']']


def read(file):
    with open(file, 'r', encoding='utf-8') as f:
        return ''.join(f.readlines())


def compileCodes(code):
    print('编译结果：\n')

    ind = 0
    tmp = ''
    result = ''
    while ind < len(code):
        if code[ind] in splitWordList:
            if keywords.get(tmp):
                tmp = keywords.get(tmp)
            result += tmp + code[ind]
            tmp = ''
        else:
            tmp += code[ind]
        ind += 1
    if keywords.get(tmp):
        tmp = keywords.get(tmp)
    writeCodes(result + tmp)
    print(result + tmp)


def writeCodes(code):
    with open(pyname, 'w', encoding='utf-8') as fi:
        fi.write(code)


def run():
    print('运行结果：\n')
    system('python %s' % pyname)


filename = input('文件名(xxx.ikun)：')
pyname = filename[:-5] + '.py'

compileCodes(read(filename))
print('\n\n')
run()
