# -*- coding: utf-8 -*-
# 1. 除零异常处理
try:
    num = int (input("请输入一个数字: "))
    result = 10 / num
    print(f"结果是: {result}")
except ZeroDivisionError:
    print('错误: 不能除以0! ')
except ValueError:
    print('错误: 请输入一个有效的整数！ ')
else:
    print('除法运算成功！ ')
finally:
    print("(无论是否出错，这里都会执行） \n")

# 2. 文件读取异常处理
file_path = input('请输入要读取的文件名: ')
try:
    with open(file_path,'r', encoding='utf-8') as f:
        content= f.read()
        print('文件内容如下: ')
        print(content)
except FileNotFoundError:
    print(f'错误: 文件: "{file_path}" 不存在! ')
except PermissionError:
    print(f'错误: 没有权限读取文件: "{file_path}"! ')
except Exception as e:
    print(f'发生未知错误: {e}')
else:
    print('文件读取成功! ')
finally:
    print("文件读取操作结束\n" )

# 3. 自定义函数中使用异常处理
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return '除数不能为0! '
    except Exception as e:
        return f'发生未知错误: {e}'
print('自定义函数测试结果: ')
print(safe_div(10, 2))
print(safe_div(10,0))
print(safe_div('a',1))





