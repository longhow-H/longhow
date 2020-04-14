'''
  Version = 1.0.0
  author = HMY
  这是一个赌博游戏：Craps,又称为花旗骰。
'''
from random import randint

#---掷色子
def throw_dice(*,num=2):
	total = 0
	for i in range(num):
		total += randint(1,6)
	return total
	
def main():
	money = int(input("请输入你的本金："))
	while money > 0:
		print("你的总资产为：",money)
		flag = False
		while True:
			debt = int(input("请进行下注："))
			if 0 < debt <= money:
				break
		print("The Game is beginning--------")
		first = throw_dice(num=2)
		print(f'玩家摇出的点数为：{first} 点')
		if first == 7 or first == 11:
			print("Wonderful,You Win ......")
			money += debt
		elif first == 2 or first == 3 or first == 12:
			print("Oh NO,You lose......")
			money -=debt
		else:
			flag = True
		#可以添加追加投注的功能，期待下一个版本	
		while flag:
			flag = False
			current = throw_dice(num=2)
                        #下次可以添加掷色子的次数
			print(f'玩家摇出的点数为：{current} 点')
			if current == 7:
				print("Oh NO,You lose......")
				money -= debt
			elif current == first:
				print("Wonderful,You Win ......")
				money += debt
			else:
				flag = True
				
	print("你已经输光了，游戏结束。再见！")
	
if __name__ == '__main__':
        main()
        
                
