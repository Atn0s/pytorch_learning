"""
Python基础教程 - 控制结构

学习目标：
1. 掌握条件判断 (if/elif/else)
2. 学会各种循环结构 (for, while)
3. 理解控制流语句 (break, continue)
4. 掌握列表推导式
"""

import random

# ============================================================================
# 1. 条件判断 (if/elif/else)
# ============================================================================

print("=== 条件判断 ===")

# 基本if语句
age = 18
if age >= 18:
    print("你已经成年了！")

# if-else语句
score = 85
if score >= 60:
    print(f"恭喜！你的分数是{score}，考试通过了！")
else:
    print(f"很遗憾，你的分数是{score}，需要重考。")

# if-elif-else语句
grade = 92
if grade >= 90:
    level = "优秀"
elif grade >= 80:
    level = "良好"
elif grade >= 70:
    level = "中等"
elif grade >= 60:
    level = "及格"
else:
    level = "不及格"

print(f"分数: {grade}, 等级: {level}")

# 复杂条件判断
username = "admin"
password = "123456"
is_vip = True

if username == "admin" and password == "123456":
    if is_vip:
        print("管理员VIP用户登录成功！")
    else:
        print("管理员普通用户登录成功！")
elif username == "guest":
    print("游客登录成功！")
else:
    print("用户名或密码错误！")

# ============================================================================
# 2. For循环
# ============================================================================

print(f"\n=== For循环 ===")

# 遍历列表
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print("我喜欢的水果:")
for fruit in fruits:
    print(f"- {fruit}")

# 遍历字典
student_scores = {
    "张三": 85,
    "李四": 92,
    "王五": 78,
    "赵六": 96
}

print("\n学生成绩单:")
for name, score in student_scores.items():
    if score >= 90:
        grade = "优秀"
    elif score >= 80:
        grade = "良好"
    else:
        grade = "需要努力"
    print(f"{name}: {score}分 ({grade})")

# 使用range()函数
print("\n使用range()生成数字序列:")
for i in range(5):  # 0到4
    print(f"数字: {i}")

print("\n计算1到10的和:")
total = 0
for i in range(1, 11):  # 1到10
    total += i
print(f"1到10的和是: {total}")

# 使用enumerate()获取索引
print("\n使用enumerate()获取索引:")
colors = ["红色", "绿色", "蓝色", "黄色"]
for index, color in enumerate(colors):
    print(f"第{index + 1}种颜色是: {color}")

# ============================================================================
# 3. While循环
# ============================================================================

print(f"\n=== While循环 ===")

# 基本while循环
count = 1
print("倒计时:")
while count <= 5:
    print(f"{count}...")
    count += 1
print("发射！🚀")

# 用户输入验证示例
print("\n密码验证示例:")
attempts = 0
max_attempts = 3
correct_password = "python123"

# 模拟用户输入（实际应用中使用input()）
user_inputs = ["wrong1", "wrong2", "python123"]  # 模拟输入序列
input_index = 0

while attempts < max_attempts:
    # 在实际应用中，这里应该是: password = input("请输入密码: ")
    password = user_inputs[input_index] if input_index < len(user_inputs) else "wrong"
    input_index += 1
    
    if password == correct_password:
        print("密码正确！登录成功！")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"密码错误！还有{remaining}次机会。")
        else:
            print("密码错误次数过多，账户已锁定！")

# ============================================================================
# 4. 控制流语句 (break, continue, pass)
# ============================================================================

print(f"\n=== 控制流语句 ===")

# break语句 - 跳出整个循环
print("寻找第一个偶数:")
numbers = [1, 3, 5, 8, 7, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"找到第一个偶数: {num}")
        break
    print(f"{num} 是奇数，继续寻找...")

# continue语句 - 跳过当前迭代
print("\n打印1到10的奇数:")
for i in range(1, 11):
    if i % 2 == 0:  # 如果是偶数，跳过
        continue
    print(f"奇数: {i}")

# pass语句 - 占位符
print("\n使用pass作为占位符:")
for i in range(3):
    if i == 1:
        pass  # TODO: 以后在这里添加代码
    else:
        print(f"处理数字: {i}")

# ============================================================================
# 5. 嵌套循环
# ============================================================================

print(f"\n=== 嵌套循环 ===")

# 打印乘法表
print("乘法表:")
for i in range(1, 4):  # 外层循环
    for j in range(1, 4):  # 内层循环
        result = i * j
        print(f"{i} × {j} = {result}", end="  ")
    print()  # 换行

# 二维列表遍历
print("\n遍历二维列表:")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row_index, row in enumerate(matrix):
    for col_index, value in enumerate(row):
        print(f"位置({row_index},{col_index}): {value}")

# ============================================================================
# 6. 列表推导式 (List Comprehension)
# ============================================================================

print(f"\n=== 列表推导式 ===")

# 基本列表推导式
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"原列表: {numbers}")
print(f"平方列表: {squares}")

# 带条件的列表推导式
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"偶数的平方: {even_squares}")

# 字符串处理
words = ["hello", "world", "python", "programming"]
capitalized = [word.upper() for word in words]
long_words = [word for word in words if len(word) > 5]

print(f"原单词: {words}")
print(f"大写单词: {capitalized}")
print(f"长单词(>5字符): {long_words}")

# 字典推导式
word_lengths = {word: len(word) for word in words}
print(f"单词长度字典: {word_lengths}")

# ============================================================================
# 7. 实际应用示例
# ============================================================================

def number_guessing_game():
    """数字猜测游戏"""
    print(f"\n=== 数字猜测游戏 ===")
    
    target = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print("我想了一个1到100之间的数字，你能猜到吗？")
    print(f"你有{max_attempts}次机会！")
    
    # 模拟用户猜测（实际应用中使用input()）
    guesses = [50, 75, 88, 94, 97, 96]  # 模拟猜测序列
    guess_index = 0
    
    while attempts < max_attempts:
        attempts += 1
        
        # 在实际应用中: guess = int(input(f"第{attempts}次猜测: "))
        if guess_index < len(guesses):
            guess = guesses[guess_index]
            guess_index += 1
        else:
            guess = target  # 确保最终能猜中
            
        print(f"第{attempts}次猜测: {guess}")
        
        if guess == target:
            print(f"🎉 恭喜！你猜对了！数字是{target}")
            print(f"你用了{attempts}次就猜中了！")
            break
        elif guess < target:
            print("太小了！再试试更大的数字。")
        else:
            print("太大了！再试试更小的数字。")
        
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"还有{remaining}次机会。")
    else:
        print(f"😔 游戏结束！正确答案是{target}")

def analyze_student_data():
    """学生数据分析示例"""
    print(f"\n=== 学生数据分析 ===")
    
    students = [
        {"name": "张三", "math": 85, "english": 92, "science": 78},
        {"name": "李四", "math": 92, "english": 88, "science": 95},
        {"name": "王五", "math": 78, "english": 85, "science": 82},
        {"name": "赵六", "math": 96, "english": 90, "science": 93},
        {"name": "钱七", "math": 82, "english": 78, "science": 88}
    ]
    
    print("学生成绩统计:")
    print("-" * 50)
    
    total_students = len(students)
    math_total = 0
    english_total = 0
    science_total = 0
    
    for student in students:
        name = student["name"]
        math = student["math"]
        english = student["english"]
        science = student["science"]
        average = (math + english + science) / 3
        
        print(f"{name}: 数学{math}, 英语{english}, 科学{science}, 平均{average:.1f}")
        
        math_total += math
        english_total += english
        science_total += science
    
    print("-" * 50)
    print(f"班级平均分:")
    print(f"数学: {math_total / total_students:.1f}")
    print(f"英语: {english_total / total_students:.1f}")
    print(f"科学: {science_total / total_students:.1f}")
    
    # 找出最高分学生
    best_student = students[0]
    best_average = sum(best_student.values() if isinstance(v, int) else 0 for v in best_student.values()) / 3
    
    for student in students:
        current_average = (student["math"] + student["english"] + student["science"]) / 3
        if current_average > best_average:
            best_student = student
            best_average = current_average
    
    print(f"\n优秀学生: {best_student['name']} (平均分: {best_average:.1f})")

# ============================================================================
# 8. 练习题
# ============================================================================

def practice_exercises():
    """练习题"""
    print(f"\n=== 练习题 ===")
    
    # 练习1: 判断年份是否为闰年
    print("练习1: 闰年判断")
    years = [2020, 2021, 2022, 2024]
    
    for year in years:
        # 闰年规则：能被4整除但不能被100整除，或者能被400整除
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year}年是闰年")
        else:
            print(f"{year}年不是闰年")
    
    # 练习2: 计算阶乘
    print("\n练习2: 计算阶乘")
    def factorial(n):
        if n <= 1:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
    for num in [5, 6, 7]:
        print(f"{num}! = {factorial(num)}")
    
    # 练习3: 斐波那契数列
    print("\n练习3: 斐波那契数列")
    def fibonacci(n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        
        fib_list = [0, 1]
        for i in range(2, n):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list
    
    fib_10 = fibonacci(10)
    print(f"前10个斐波那契数: {fib_10}")
    
    # 练习4: 寻找质数
    print("\n练习4: 寻找质数")
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    primes = [num for num in range(2, 30) if is_prime(num)]
    print(f"2到30之间的质数: {primes}")

if __name__ == "__main__":
    number_guessing_game()
    analyze_student_data()
    practice_exercises()

# ============================================================================
# 学习总结
# ============================================================================
"""
🎓 学习总结：

1. 条件判断:
   - if/elif/else 语句
   - 逻辑运算符: and, or, not
   - 比较运算符: ==, !=, <, >, <=, >=

2. 循环结构:
   - for循环: 遍历序列
   - while循环: 条件循环
   - range()函数: 生成数字序列
   - enumerate(): 获取索引和值

3. 控制流:
   - break: 跳出循环
   - continue: 跳过当前迭代
   - pass: 占位符

4. 高级特性:
   - 嵌套循环
   - 列表推导式
   - 字典推导式

5. 编程技巧:
   - 合理使用条件判断
   - 选择合适的循环类型
   - 避免无限循环
   - 使用推导式简化代码

下一步学习: functions.py - 函数的定义和使用
"""
