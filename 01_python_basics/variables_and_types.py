"""
Python基础教程 - 变量和数据类型

这个文件包含了Python中变量和数据类型的基础知识。
学习目标：
1. 理解变量的概念和命名规则
2. 掌握Python的基本数据类型
3. 学会类型转换和检查
"""

# ============================================================================
# 1. 变量基础
# ============================================================================

# 变量赋值 - Python不需要声明变量类型
name = "小明"           # 字符串
age = 25               # 整数
height = 175.5         # 浮点数
is_student = True      # 布尔值

print(f"姓名: {name}")
print(f"年龄: {age}")
print(f"身高: {height}cm")
print(f"是学生: {is_student}")

# ============================================================================
# 2. 基本数据类型详解
# ============================================================================

# 2.1 数字类型
integer_num = 42               # 整数
float_num = 3.14159           # 浮点数
complex_num = 3 + 4j          # 复数

print(f"\n=== 数字类型 ===")
print(f"整数: {integer_num}, 类型: {type(integer_num)}")
print(f"浮点数: {float_num}, 类型: {type(float_num)}")
print(f"复数: {complex_num}, 类型: {type(complex_num)}")

# 2.2 字符串类型
single_quote = '单引号字符串'
double_quote = "双引号字符串"
multiline_string = """
多行字符串
可以跨越多行
"""

print(f"\n=== 字符串类型 ===")
print(single_quote)
print(double_quote)
print("多行字符串:", multiline_string.strip())

# 字符串操作示例
greeting = "Hello"
target = "World"
message = greeting + " " + target + "!"  # 字符串连接
print(f"连接结果: {message}")
print(f"字符串长度: {len(message)}")
print(f"转为大写: {message.upper()}")
print(f"转为小写: {message.lower()}")

# 2.3 布尔类型
is_python_fun = True
is_difficult = False

print(f"\n=== 布尔类型 ===")
print(f"Python有趣吗? {is_python_fun}")
print(f"Python困难吗? {is_difficult}")

# 布尔运算
print(f"True and False = {True and False}")
print(f"True or False = {True or False}")
print(f"not True = {not True}")

# ============================================================================
# 3. 集合数据类型
# ============================================================================

# 3.1 列表 (List) - 有序、可变
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
numbers = [1, 2, 3, 4, 5]
mixed_list = ["文本", 123, True, 3.14]

print(f"\n=== 列表类型 ===")
print(f"水果列表: {fruits}")
print(f"第一个水果: {fruits[0]}")
print(f"最后一个水果: {fruits[-1]}")

# 列表操作
fruits.append("樱桃")        # 添加元素
print(f"添加樱桃后: {fruits}")
fruits.remove("香蕉")        # 删除元素
print(f"删除香蕉后: {fruits}")

# 3.2 元组 (Tuple) - 有序、不可变
coordinates = (10, 20)
rgb_color = (255, 128, 0)

print(f"\n=== 元组类型 ===")
print(f"坐标: {coordinates}")
print(f"RGB颜色: {rgb_color}")
print(f"坐标X: {coordinates[0]}, Y: {coordinates[1]}")

# 3.3 字典 (Dictionary) - 键值对，无序
student_info = {
    "name": "张三",
    "age": 20,
    "major": "计算机科学",
    "grades": [85, 92, 78, 96]
}

print(f"\n=== 字典类型 ===")
print(f"学生信息: {student_info}")
print(f"学生姓名: {student_info['name']}")
print(f"学生年龄: {student_info['age']}")

# 字典操作
student_info["email"] = "zhangsan@email.com"  # 添加新键值对
print(f"添加邮箱后: {student_info}")

# 3.4 集合 (Set) - 无序、不重复
unique_numbers = {1, 2, 3, 4, 5}
colors = {"红", "绿", "蓝", "红", "黄"}  # 重复的"红"会被自动去除

print(f"\n=== 集合类型 ===")
print(f"唯一数字: {unique_numbers}")
print(f"颜色集合: {colors}")

# 集合操作
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"交集: {set1 & set2}")
print(f"并集: {set1 | set2}")
print(f"差集: {set1 - set2}")

# ============================================================================
# 4. 类型检查和转换
# ============================================================================

print(f"\n=== 类型检查和转换 ===")

# 类型检查
var = 42
print(f"变量 {var} 的类型: {type(var)}")
print(f"是否为整数: {isinstance(var, int)}")
print(f"是否为字符串: {isinstance(var, str)}")

# 类型转换
num_str = "123"
num_int = int(num_str)          # 字符串转整数
num_float = float(num_str)      # 字符串转浮点数

print(f"字符串 '{num_str}' 转为整数: {num_int}")
print(f"字符串 '{num_str}' 转为浮点数: {num_float}")

# 数字转字符串
number = 456
str_number = str(number)
print(f"数字 {number} 转为字符串: '{str_number}'")

# 列表和字符串转换
char_list = ['H', 'e', 'l', 'l', 'o']
word = ''.join(char_list)       # 列表转字符串
print(f"字符列表 {char_list} 转为字符串: '{word}'")

word_chars = list(word)         # 字符串转列表
print(f"字符串 '{word}' 转为字符列表: {word_chars}")

# ============================================================================
# 5. 练习题
# ============================================================================

def practice_exercises():
    """
    练习题：测试你对变量和数据类型的理解
    """
    print(f"\n=== 练习题 ===")
    
    # 练习1: 创建个人信息
    print("练习1: 创建一个包含你个人信息的字典")
    my_info = {
        "name": "你的姓名",
        "age": 0,  # 请填写你的年龄
        "hobbies": ["编程", "阅读"],  # 添加你的爱好
        "is_learning_python": True
    }
    print(f"我的信息: {my_info}")
    
    # 练习2: 列表操作
    print("\n练习2: 列表操作")
    shopping_list = ["牛奶", "面包", "鸡蛋"]
    print(f"购物清单: {shopping_list}")
    
    # TODO: 在这里添加两个新商品到购物清单
    # TODO: 移除一个商品
    # TODO: 打印最终的购物清单
    
    # 练习3: 字符串格式化
    print("\n练习3: 字符串格式化")
    name = "Python学习者"
    days_learning = 30
    
    # TODO: 使用f-string格式化输出一个鼓励的句子
    message = f"加油，{name}！你已经学习Python {days_learning}天了！"
    print(message)
    
    # 练习4: 类型转换挑战
    print("\n练习4: 类型转换")
    user_input = "42"  # 模拟用户输入
    
    # TODO: 将字符串转换为数字，进行数学运算，再转回字符串
    # 提示: int() -> 数学运算 -> str()
    
    print("练习完成！继续加油学习！")

if __name__ == "__main__":
    practice_exercises()

# ============================================================================
# 学习总结
# ============================================================================
"""
🎓 学习总结：

1. 变量命名规则：
   - 只能包含字母、数字和下划线
   - 不能以数字开头
   - 大小写敏感
   - 不能使用Python关键字

2. 基本数据类型：
   - 数字: int, float, complex
   - 文本: str
   - 布尔: bool
   - 集合: list, tuple, dict, set

3. 重要概念：
   - 可变类型: list, dict, set
   - 不可变类型: int, float, str, tuple
   - 类型检查: type(), isinstance()
   - 类型转换: int(), float(), str(), list()

4. 下一步学习：
   - 控制结构 (if/else, 循环)
   - 函数定义和调用
   - 面向对象编程

继续前往 control_structures.py 学习控制结构！
"""
