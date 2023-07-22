// 第一題
function findAndPrint(messages) {
    const keywords = ["18", "college", "legal age", "vote"];
    
    for (let name in messages) {
            let message = messages[name]; 
            if (keywords.some(
                function(keyword){
                    return message.includes(keyword);
                }
            )){
                console.log(name);
            }
    }
}

findAndPrint({
    "Bob": "My name is Bob. I'm 18 years old.",
    "Mary": "Hello, glad to meet you.",
    "Copper": "I'm a college student. Nice to meet you.",
    "Leslie": "I am of legal age in Taiwan.",
    "Vivian": "I will vote for Donald Trump next week",
    "Jenny": "Good morning."
});
// 第二題
function calculate_sum_of_bonus(data) {
    // 複製一份資料當獎金
    // 薪水要把美金換算，扣掉逗號
    // 表現跟職位要換算成加成倍率
    // 算出原始獎金，依照總獎金限制等比例增減
  
    const bonus = data["employees"].map(employee => ({ ...employee }));
  
    // 轉換美元乘以30、去除逗號
    function salary_count(salary) {
      if (typeof salary === 'string') {
        if (salary.includes("USD")) {
          salary = parseInt(salary.replace("USD", "")) * 30;
        } else {
          salary = parseInt(salary.replace(',', ''));
        }
      }
      return salary;
    }
  
    // 表現加成
    function performance_rate(performance) {
      if (performance.includes("above")) {
        return 2;
      } else if (performance.includes("below")) {
        return 0.5;
      } else {
        return 1;
      }
    }
    
    //職位加成
    function role_rate(role) {
      if (role.includes("CEO")) {
        return 2;
      } else if (role.includes("Engineer")) {
        return 1.2;
      } else if (role.includes("Sales")) {
        return 1.5;
      }
    }
    
    //初始輸字
    let total_bonus_beginning = 0;
  
    //資料處理與獎金計算
    for (const bonus_person of bonus) {
      bonus_person['salary'] = salary_count(bonus_person['salary']);
      bonus_person['performance'] = performance_rate(bonus_person['performance']);
      bonus_person['role'] = role_rate(bonus_person['role']);
      total_bonus_beginning += bonus_person['salary'] * bonus_person['performance'] * bonus_person['role'];
    }
  
    //算出與獎金的差異
    const bonus_limit = 10000;
    const magic_number = bonus_limit / total_bonus_beginning;

    //每人獎金
    let final_bonus = 0;
    //給出的總獎金
    let bonus_given = 0;
  
    for (const bonus_person of bonus) {
      final_bonus = Math.floor(bonus_person['salary'] * bonus_person['performance'] * bonus_person['role'] * magic_number);
      bonus_given += final_bonus;
      console.log(`${bonus_person['name']}'s bonus: ${final_bonus}`);
    }
  
    console.log("bonus all:", bonus_given);
  }
  
  calculate_sum_of_bonus({
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
  });  

// 第三題
function func(...data) {
    // 以物件紀錄名字出現次數
    // 抓出第二個字，沒存在就創一個，有存在就多推一個
    // 把只有一個的名字，印出來

    const name_times = {};
  
    for (const data_name of data) {
      const second_name = data_name[1];
  
      if (name_times[second_name]) {
        name_times[second_name].push(data_name);
      } else {
        name_times[second_name] = [data_name];
      }
    }
  
    const lonely_name = [];
  
    for (let name in name_times) {
      if (name_times[name].length === 1) {
        lonely_name.push(name_times[name][0]);
      }
    }

    // 印出來
    if (lonely_name.length > 0) {
      console.log(lonely_name);
    } else {
      console.log("沒有");
    }
  }
  
  func("彭大牆", "王明雅", "吳明"); // print 彭大牆
  func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花"); // print 林花花 
  func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
  
// 第四題
function getNumber(index) {
    if (index % 2 === 0) {
      return index + Math.floor(index / 2);
    } else {
      return index + Math.floor(index / 2) + 3;
    }
  }
  
  console.log(getNumber(1));   // 输出 4
  console.log(getNumber(5));   // 输出 10
  console.log(getNumber(10));  // 输出 15