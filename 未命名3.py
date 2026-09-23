# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 21:04:09 2026

@author: a3026
"""

# 提示：流程图中菱形判断框里的 "socre" 拼写有误，代码中已修正为 "score"

while True:
    try:
        # 1. 获取分数 (Get score)
        score = float(input("请输入分数 (0-100): "))
        
        # 2. 判断分数是否合法 (0 <= score <= 100)
        if 0 <= score <= 100:
            break  # 如果合法，跳出循环，继续往下执行
       
            # 不合法则循环回到 "Get score"
            
    except ValueError:
        print("输入错误：请输入有效的数字。")

# 3. 条件判断分支
if score >= 80:
    # 如果分数 >= 80，等级为 A
    grade = "A"
elif score >= 60:
    # 如果不满足上一条，且分数 >= 60，等级为 B
    grade = "B"
elif score >= 50:
    # 如果不满足上两条，且分数 >= 50，等级为 C
    grade = "C"
else:
    # 如果以上都不满足 (即小于 50)，等级为 Fail
    grade = "Fail"

# 4. 输出结果并结束 (End)
print(f"最终成绩等级: {grade}")