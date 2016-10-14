import random
import operator
import time
import sqlite3


con = sqlite3.connect('database.db')
sql = con.cursor()
#sql.execute('''create table RESULTS (name, score)''')
#con.commit()


def random_calc():
    ops = {'+': operator.add, '*': operator.mul, '-': operator.sub}
    num1 = random.randint(0, 12)
    num2 = random.randint(0, 12)
    op = random.choice(list(ops.keys()))
    answer = ops.get(op)(num1, num2)
    print('{} {} {} ='.format(num1, op, num2))
    return answer


def askQuestion():
    correct_answer = random_calc()
    while True:
        try:
            your_answer = int(input())
            if your_answer != correct_answer:
                print("wrong")
            else:
                print('Correct!\n')
                break
        except ValueError:
            print("only numbers man")


def quiz():
    begin_test = input('Enter yes if you are ready for the test! (yes/no) ')
    if begin_test.lower() == 'yes' or begin_test.lower() == 'y':
        your_name = input("Enter your name here -> ")
        print('Welcome. This is a 10 question math quiz\n')
        begin_time = time.time()
        score = 0
        for i in range(2):
            score += 1
            print("question %s/10" % (score))
            askQuestion()
            end_time = time.time()
            result = end_time - begin_time
            round_result = round(result, 5)
            print("Your time : %s sec" % (round_result))
    else:
        print("\n\n\n")
        start_results()
    sql.execute('INSERT INTO RESULTS (name, score) VALUES("%s", "%s")' % (your_name, round_result))
    con.commit()


def results():
    print("####### RESULTS #######")
    sql.execute('SELECT name, score FROM RESULTS ORDER BY score')
    while True:
        row = sql.fetchone()
        if row:
            print('Name : {} | Score : {}'.format(row[0], row[1]))


def start_results():
    print("1 - start new test")
    print("2 - show results")
    choise = input("Enter your choise here -> ")
    if choise == "1":
        quiz()
    elif choise == "2":
        results()
    else:
        print("Wrong choice\n\n\n\n")
        start_results()
start_results()





