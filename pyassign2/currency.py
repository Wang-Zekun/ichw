#
# 汇率转换器
# 实现165种货币之间的汇率计算
# Author: 王 泽锟
# Last Update: Nov.29 2018
# Copyright © 2018 Zekun Wang. All Rights Reserved.
#



#===================================================================
#货币交换测试模块
#作者：王泽锟 (No.1800011717)
#最后更新： Nov.29 2018
#===================================================================

"""
货币交换测试模块
当作为脚本运行时，该模块调用几个过程来测试模块a1中的各种函数。
该模块的主要功能是测试程序能否正常运行
"""

#测试货币交换功能是否有效（选用给定的数据以及随机抽取的数据），即能否正常返回货币转换后的数值。
def testA():
    import random
    
    test1 = exchange('USD','CNY','1')
    assert(test1 == '6.8521')
    
    test2 = exchange('HUF','MMK','1')
    assert(test2 == '5.4442872073208')
    
    test3 = exchange('XPT','XAU','1')
    assert(test3 == '0.6523164114501')
    
    test4 = exchange('USD','VND','1')
    assert(test4 == '23116.257672')
    
    testA_num1 = str(random.randrange(100000))
    testA_curr1 = abbrevlist[random.randrange(165)]
    testA_curr2 = abbrevlist[random.randrange(165)]
    test5 = float(exchange(testA_curr1,testA_curr2,testA_num1))
    assert(type(test5) == float)
    
    testA_num2 = str(random.randrange(100000))
    testA_curr3 = abbrevlist[random.randrange(165)]
    testA_curr4 = abbrevlist[random.randrange(165)]
    test6 = float(exchange(testA_curr3,testA_curr4,testA_num2))
    assert(type(test6) == float)
    

    
    
#测试执行货币交换函数是否有效，包括是否能够返回正常的结果字符串，能否在用户输入返回指令时返回，能否判定无效结果。
def testB():
    
    test1 = execution('USD','CNY','1')
    assert(test1 == '1 USD = 6.8521 CNY')
    test2 = execution('XPT','XAU','1')
    assert(test2 == '1 XPT = 0.6523164114501 XAU')
    test3 = execution('error','CNY','1')
    assert(test3 == 'Invalid Currency!')
    test4 = execution('','CNY','1')
    assert(test4 == 'Invalid Currency!')
    test5 = execution('CNY','error','1')
    assert(test5 == 'Invalid Currency!')
    test6 = execution('CNY','','1')
    assert(test6 == 'Invalid Currency!')
    test7 = execution('USD','CNY','error')
    assert(test7 == 'Invalid Value!')
    test8 = execution('USD','CNY','')
    assert(test8 == 'Invalid Value!')
    test9 = execution('x','CNY','1')
    assert(test9 == None)
    test10 = execution('CNY','x','1')
    assert(test10 == None)
    

    
    
#测试查找货币代码函数是否有效，包括能否根据正确输入正常返回货币代码，以及错误输入时能否提示。
def testC():
    
    test1 = search('Chinese Yuan')
    assert(test1 == '"Chinese Yuan" is "CNY"')
    test2 = search('Bitcoin')
    assert(test2 == '"Bitcoin" is "BTC"')
    test3 = search('Troy Ounce of Palladium')
    assert(test3 == '"Troy Ounce of Palladium" is "XPD"')
    test4 = search('')
    assert(test4 == 'Invalid Currency Name!')
    test5 = search('1')
    assert(test5 == 'Invalid Currency Name!')
    test6 = search('bitcoin')
    assert(test6 == 'Invalid Currency Name!')
    test7 = search('afeda1#$@$^#Y^UJ asDFW!$U')
    assert(test7 == 'Invalid Currency Name!')
    
    
#测试二级目录函数是否有效，即此函数能否正确通过对应的用户输入实现交互
def testD():
    selection1(1)
    test2 = selection1(2)
    assert(test2 == True)
    selection1(3)
    
    
    
#进行所有测试
def testAll():
    print('Running TestA ...')
    testA()
    print('TestA Complete!')
    print('Running TestB ...')
    testB()
    print('TestB Complete!')
    print('Running TestC ...')
    testC()
    print('TestC Complete!')
    print('Running TestD ...')
    testD()
    print('TestD Complete!')
    print('\n'+'All tests passed!'+'\n')






#===================================================================
#列表模块
#作者：王泽锟 (No.1800011717)
#最后更新： Nov.29 2018
#===================================================================

"""
列表模块
该模块提供了所有可转换货币的列表，用于更好地实现调用、交互和测试。
该模块的主要功能是提供货币的名称以及缩写列表。

注意！！由于URL不支持 BYR EEK LTL LVL MTL ZMK 六种货币的转换，该六种货币已经从列表中去除！！
"""

#所有货币缩写的列表
def curr_abbrev():
    Currency_list = ['AED','AFN','ALL','AMD','ANG','AOA','ARS','AUD','AWG','AZN','BAM',
                     'BBD','BDT','BGN','BHD','BIF','BMD','BND','BOB','BRL','BSD','BTC',
                     'BTN','BWP','BZD','CAD','CDF','CHF','CLF','CLP','CNY','COP','CRC',
                     'CUC','CUP','CVE','CZK','DJF','DKK','DOP','DZD','EGP','ERN','ETB',
                     'EUR','FJD','FKP','GBP','GEL','GGP','GHS','GIP','GMD','GNF','GTQ',
                     'GYD','HKD','HNL','HRK','HTG','HUF','IDR','ILS','IMP','INR','IQD',
                     'IRR','ISK','JEP','JMD','JOD','JPY','KES','KGS','KHR','KMF','KPW',
                     'KRW','KWD','KYD','KZT','LAK','LBP','LKR','LRD','LSL','LYD','MAD',
                     'MDL','MGA','MKD','MMK','MNT','MOP','MRO','MUR','MVR','MWK','MXN',
                     'MYR','MZN','NAD','NGN','NIO','NOK','NPR','NZD','OMR','PAB','PEN',
                     'PGK','PHP','PKR','PLN','PYG','QAR','RON','RSD','RUB','RWF','SAR',
                     'SBD','SCR','SDG','SEK','SGD','SHP','SLL','SOS','SRD','STD','SVC',
                     'SYP','SZL','THB','TJS','TMT','TND','TOP','TRY','TTD','TWD','TZS',
                     'UAH','UGX','USD','UYU','UZS','VEF','VND','VUV','WST','XAF','XAG',
                     'XAU','XCD','XDR','XOF','XPD','XPF','XPT','YER','ZAR','ZMW','ZWL']
    return Currency_list


#所有货币名称的列表
def curr_name():
    namelist = [
'United Arab Emirates Dirham',
'Afghan Afghani',
'Albanian Lek',
'Armenian Dram',
'Netherlands Antillean Guilder',
'Angolan Kwanza',
'Argentine Peso',
'Australian Dollar',
'Aruban Florin',
'Azerbaijani Manat',
'Bosnia-Herzegovina Convertible Mark',
'Barbadian Dollar',
'Bangladeshi Taka',
'Bulgarian Lev',
'Bahraini Dinar',
'Burundian Franc',
'Bermudan Dollar',
'Brunei Dollar',
'Bolivian Boliviano',
'Brazilian Real',
'Bahamian Dollar',
'Bitcoin',
'Bhutanese Ngultrum',
'Botswanan Pula',
'Belize Dollar',
'Canadian Dollar',
'Congolese Franc',
'Swiss Franc',
'Chilean Unidad de Fomento',
'Chilean Peso',
'Chinese Yuan',
'Colombian Peso',
'Costa Rican Colón',
'Cuban Convertible Peso',
'Cuban Peso',
'Cape Verdean Escudo',
'Czech Republic Koruna',
'Djiboutian Franc',
'Danish Krone',
'Dominican Peso',
'Algerian Dinar',
'Egyptian Pound',
'Eritrean Nakfa',
'Ethiopian Birr',
'Euro',
'Fijian Dollar',
'Falkland Islands Pound',
'British Pound Sterling',
'Georgian Lari',
'Guernsey Pound',
'Ghanaian Cedi',
'Gibraltar Pound',
'Gambian Dalasi',
'Guinean Franc',
'Guatemalan Quetzal',
'Guyanaese Dollar',
'Hong Kong Dollar',
'Honduran Lempira',
'Croatian Kuna',
'Haitian Gourde',
'Hungarian Forint',
'Indonesian Rupiah',
'Israeli New Sheqel',
'Manx pound',
'Indian Rupee',
'Iraqi Dinar',
'Iranian Rial',
'Icelandic Króna',
'Jersey Pound',
'Jamaican Dollar',
'Jordanian Dinar',
'Japanese Yen',
'Kenyan Shilling',
'Kyrgystani Som',
'Cambodian Riel',
'Comorian Franc',
'North Korean Won',
'South Korean Won',
'Kuwaiti Dinar',
'Cayman Islands Dollar',
'Kazakhstani Tenge',
'Laotian Kip',
'Lebanese Pound',
'Sri Lankan Rupee',
'Liberian Dollar',
'Lesotho Loti',
'Libyan Dinar',
'Moroccan Dirham',
'Moldovan Leu',
'Malagasy Ariary',
'Macedonian Denar',
'Myanma Kyat',
'Mongolian Tugrik',
'Macanese Pataca',
'Mauritanian Ouguiya',
'Mauritian Rupee',
'Maldivian Rufiyaa',
'Malawian Kwacha',
'Mexican Peso',
'Malaysian Ringgit',
'Mozambican Metical',
'Namibian Dollar',
'Nigerian Naira',
'Nicaraguan Córdoba',
'Norwegian Krone',
'Nepalese Rupee',
'New Zealand Dollar',
'Omani Rial',
'Panamanian Balboa',
'Peruvian Nuevo Sol',
'Papua New Guinean Kina',
'Philippine Peso',
'Pakistani Rupee',
'Polish Złoty',
'Paraguayan Guarani',
'Qatari Rial',
'Romanian Leu',
'Serbian Dinar',
'Russian Ruble',
'Rwandan Franc',
'Saudi Riyal',
'Solomon Islands Dollar',
'Seychellois Rupee',
'Sudanese Pound',
'Swedish Krona',
'Singapore Dollar',
'Saint Helena Pound',
'Sierra Leonean Leone',
'Somali Shilling',
'Surinamese Dollar',
'São Tomé and Príncipe Dobra',
'Salvadoran Colón',
'Syrian Pound',
'Swazi Lilangeni',
'Thai Baht',
'Tajikistani Somoni',
'Turkmenistani Manat',
'Tunisian Dinar',
"Tongan Pa'anga",
'Turkish Lira',
'Trinidad and Tobago Dollar',
'New Taiwan Dollar',
'Tanzanian Shilling',
'Ukrainian Hryvnia',
'Ugandan Shilling',
'United States Dollar',
'Uruguayan Peso',
'Uzbekistan Som',
'Venezuelan Bolívar Fuerte',
'Vietnamese Dong',
'Vanuatu Vatu',
'Samoan Tala',
'CFA Franc (BEAC)',
'Troy Ounce of Silver',
'Troy Ounce of Gold',
'East Caribbean Dollar',
'Special Drawing Rights',
'CFA Franc (BCEAO)',
'Troy Ounce of Palladium',
'CFP Franc',
'Troy Ounce of Platinum',
'Yemeni Rial',
'South African Rand',
'Zambian Kwacha',
'Zimbabwean Dollar']

    return namelist




#===================================================================
#货币交换模块
#作者：王泽锟 (No.1800011717)
#最后更新： Nov.28 2018
#===================================================================

"""
货币交换模块
该模块提供了字符串解析函数，以使用在线货币服务实现一个简单的货币交换操作。
该模块的主要功能是进行货币交换。
"""

from urllib.request import urlopen


#交换函数，通过输入货币和转换币值，得到转换结果币值。
def exchange(cur_from,cur_to,amt_from):
    convstr = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+cur_from+'&to='+cur_to+'&amt='+amt_from
    doc = urlopen(convstr)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    jstrsplit = jstr.split('"')
    infosplit = jstrsplit[7].split(' ')
    return(infosplit[0])




#===================================================================
#主程序模块
#作者：王泽锟 (No.1800011717)
#最后更新： Nov.29 2018
#===================================================================

'''
主程序模块
该模块包括汇率计算、货币名称列表查看、货币缩写查询、测试程序、返回上级菜单和退出的功能
该模块的主要功能是实现人机交互
'''

#执行函数，用于执行货币汇率计算功能。
def execution(test_cur_from,test_cur_to,test_amt_from):
    while True:
        if test_cur_from == None:
            cur_from = input('\n'+'Insert the starting currency '+"(To close, insert 'x') : ")
        else:
            cur_from = test_cur_from
        if cur_from == 'x':
            break
        elif cur_from not in abbrevlist:
            return('Invalid Currency!')
            break
        
        if test_cur_to == None:
            cur_to = input('\n'+'Insert the target currency '+"(To close, insert 'x') : ")
        else:
            cur_to = test_cur_to
        if cur_to == 'x':
            break
        elif cur_to not in abbrevlist:
            return('Invalid Currency!')
            break
        
        if test_amt_from == None:
            amt_from = input('\n'+'The amount of your currency: ')
        else:
            amt_from = test_amt_from
        num = exchange(cur_from,cur_to,amt_from)
        if num != '':
            num2 = float(num)
            num = str(num2)
            result = (amt_from + ' ' + cur_from + ' = ' + num + ' ' + cur_to)
            return result
            break
        else:
            return('Invalid Value!')
            break
            

#查找函数，用于查找某个货币名称对应的简称。
def search(name):
        boo = False
        for i in range(len(namelist)):
            if name == namelist[i]:
                ret = '"'+namelist[i]+'"'+' is '+'"'+abbrevlist[i]+'"'
                return ret
                boo = True
        if boo == False:
            ret = 'Invalid Currency Name!'
            return ret

            

#二级目录。用户在主函数输入1后执行的内容，包括货币计算、货币列表、货币查找。
def selection1(test_userinput):
    if test_userinput == None:
        print('\n'+'Insert "1" to calculate. Insert "2" to get currency name list. Insert "3" to search for abbreviation.')
        userinput = input()
        if userinput == '1':
            result1 = execution(None,None,None)
            if result1 != None:
                print(result1)
                selection1('1')
        elif userinput == '2':
            for i in namelist:
                print(i)
            selection1(None)
        elif userinput == '3':
            name = input('The currency name? ')
            result3 = search(name)
            print(result3)
            selection1(None)
    elif test_userinput == 1:
        testB()
    elif test_userinput == 2:
        judge = True
        test_namelist = curr_name()
        for r in range(165):
            if namelist[r] != test_namelist[r]:
                judge = False
        return judge
    elif test_userinput == 3:
        testC()


    
    
#主程序
def main():
    print('\n'+'Thanks for using Exchange Calculator!'+'\n')
    print('Reminder:'+'\n'+ 'The correct form of currency code is THREE CAPITAL LETTER.')
    print('If you are not sure about the currency code, please insert "1"-"3" to search.')
    print('To list all the currency avalible, please insert "1"-"2".')
    print('Every time you need to return to previous menu, please insert "x".'+'\n')
    while True:
        print('Insert "1" to start a new calculation. Insert "2" to test the program. Insert "x" to exit.')
        str0 = input()
        if str0 == '1':
            selection1(None)
        elif str0 == '2':
            testAll()
        elif str0 == 'x':
            break
        else:
            print('Invalid Input!')

            
#运行主程序
namelist = curr_name()
abbrevlist = curr_abbrev()
if __name__ == '__main__':
    main()
        
        
        





