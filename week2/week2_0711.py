#第一題

def find_and_print(messages):
    keywords = ["18", "college", "legal age", "vote"]
    for name, message in messages.items():
        if any(keyword in message
               for keyword in keywords):
            print(name)

find_and_print({
    "Bob": "My name is Bob. I'm 18 years old.",
    "Mary": "Hello, glad to meet you.",
    "Copper": "I'm a college student. Nice to meet you.",
    "Leslie": "I am of legal age in Taiwan.",
    "Vivian": "I will vote for Donald Trump next week",
    "Jenny": "Good morning."
})

#第二題
def calculate_sum_of_bonus(data):
    # 複製一份資料當獎金
    # 薪水要把美金換算，扣掉逗號
    # 表現跟職位要換算成加成倍率
    # 算出原始獎金，依照總獎金限制等比例增減
    bonus = []
    bonus_limit = 10000
    final_bonus = 0

    for employee in data["employees"]:
        bonus.append(employee.copy())
        
    print(bonus)

    def salary_count(salary):
        if isinstance(salary, str):
            if "USD" in salary:
                salary = int(salary.replace("USD", "")) * 30
            else:
                salary = int(salary.replace(',', ''))
        return salary

    def performance_rate(performance):
        if "above" in performance:
            return 2
        elif "below" in performance:
            return 0.5
        else:
            return 1
        
    def role_rate(role):
        if "CEO" in role:
            return 2
        elif "Engineer" in role:
            return 1.2
        elif "Sales" in role:
            return 1.5
    
    total_bonus_beginning = 0

    for bonus_person in bonus:
        bonus_person['salary'] = salary_count(bonus_person['salary'])
        bonus_person['performance'] = performance_rate(bonus_person['performance'])
        bonus_person['role'] = role_rate(bonus_person['role'])
        total_bonus_beginning += bonus_person['salary'] * bonus_person['performance'] * bonus_person['role']

    magic_number = bonus_limit /total_bonus_beginning

    bonus_given = 0

    for bonus_person in bonus:
        final_bonus = int(bonus_person['salary'] * bonus_person['performance'] * bonus_person['role'] * magic_number )
        bonus_given  += final_bonus

        print(f"{bonus_person['name']}'s bonus: {final_bonus}")

    print("bonus all:", bonus_given)

calculate_sum_of_bonus ({
    "employees": [
        {
            "name": "John",
            "salary": "1000USD",
            "performance": "above average",
            "role": "Engineer"
        }, 
        {
            "name": "Bob",
            "salary": 60000,
            "performance": "average",
            "role": "CEO"
        }, 
        {
            "name": "Jenny",
            "salary": "50,000",
            "performance": "below average",
            "role": "Sales"
        }
    ]
})

# Task 3
# 以物件紀錄名字出現次數
# 抓出第二個字，沒存在就創一個，有存在就多推一個
# 把只有一個的名字，印出來

def func(*data):

    name_times = {}

    for data_name in data:

        second_name = data_name[1]

        if second_name in name_times:
            name_times[second_name].append(data_name)
        else:
            name_times[second_name] = [data_name]

    lonely_name = []

    for names in name_times.values():
        if len(names) == 1:
            lonely_name.append(names[0])
    # 印出來
    if lonely_name:
        print(lonely_name)
    else:
        print("沒有")

func("彭大牆", "王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花 
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有


#第四題
#0, 4, 3, 7, 6, 10, 9, 13, 12, 16, 15, ...
def get_number(index):
    if index % 2 == 0:
        return index + index // 2
    else:
        return index + (index // 2) + 3

print(get_number(1))   # 输出 4
print(get_number(5))   # 输出 10
print(get_number(10))  # 输出 15  
