import random
def main():
    print_info()
    a,b,n = get_info()    
    awins,bwins = simN(a,b,n)
    print_result(n,awins,bwins)

def print_info():
    print('这是一个模拟体育比赛成绩的程序：')
    print('输入两个运动员的成绩，模拟出N场比赛结果')

def get_info():
    a = eval(input('请输入运动员A的能力值（0-1之间两位小数）：'))
    b = eval(input('请输入运动员B的能力值（0-1之间两位小数）：'))
    c = eval(input('请输入需要模拟的场次数（整数）：'))
    return a,b,c

def print_result(n,a,b):
    '''输出N场比赛，a和b两个胜率百分数'''
    
    print('经过{}场比赛，A的胜率为：{:.2f}，B的胜率为：{:.2f}'.format(n,a/n,b/n))

def simN(a,b,n):
    awins,bwins = 0,0
    for i in range(n):
        if simone(a,b) == 1:
            awins += 1
        else:
            bwins += 1
            
    return awins,bwins

def simone(a,b):
    ascore,bscore = 0,0
    while ascore<15 and bscore <15:
        faqiu = 'a'
        while faqiu == 'a':
            randnum = random.random()
            if randnum < b:               
                faqiu = 'b'
            else:
                ascore += 1
                
        while faqiu == 'b':
            randnum = random.random()
            if randnum < a :
                faqiu = 'a'
            else:
                bscore += 1


    return 1 if ascore > bscore else 0
        
main()        
        
    
