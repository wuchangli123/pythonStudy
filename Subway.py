'''业务：
#以一个月为期限，一张一卡通乘坐北京轨道交通累计消费满100元后，下一次开始乘车时有8折优惠；满150元后，从下一次乘车时有5折优惠；支出累计达到300元后，就将不再享受打折优惠。一卡通卡轨道交通支出累计记录	每自然月底清零,下自然月重新累计
#我的需求：我每天通勤的无折扣票价是12元，一个月上班22天要花多钱？'''


#编写伪代码
    #新建一个变量，用来存储每日的票价
    #新建一个变量，来储存一个月坐车多少天  input()
    #新建一个变量，用户储存计算结果
    #每日消费进行累加，一共累加“22”次
    #以上都是顺序控制
          #如果当前累计消费金额>=100，则今日票价* 0.8
          #如果当前累计消费金额>=150，则今日票价*0.5
          # 如果我的金额>=300 或者金额<100.今日票价不打折
          #for  后面i是临时变量


price = 12  #每日票价
days = 20  #月度乘车日
MountCost = 0   #累计消费金额
for  i  in range(1,days+1):
    print(f'第{i}天')
    if MountCost < 100:
        MountCost = price + MountCost
    elif MountCost  <150:
        MountCost = price*0.8 + MountCost
    elif MountCost < 300:
        MountCost = price * 0.5 +MountCost
    else:
        MountCost = MountCost + price
    print(f'当前累计消费{MountCost}')
print('%.2f' %MountCost)




