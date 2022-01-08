print('hello python')

# 输出内容到文件中
# fp = open('C:\Workspace\python_demo_pro\README.md', 'a+')
# print('python笔记', file=fp)
# fp.close()

print('hello', 'python', 'learning', 'hjh')

# 转义字符  \n[换行]  \t[水平制表符]  \r[回车]  \b[退格]
print('hello\ni am coming')
print('helloo\tworld')
print('helloooo\tworld')
print('hello\rworld')
print('hello\bworld')
print('C:\\\\Workspace\\\\python_demo_pro')
print('\'你好，python\'')

# 输出字符最后一个不能是反斜杠\

#原字符，不希望原字符中的转义字符起作用，就使用原字符，就是在字符串前加上r或者R
print(r'helloo\tworld')

# chr() 二进制转汉字    ord()汉字转十进制
print(chr(0b100111001011000))
print(ord('乘'))