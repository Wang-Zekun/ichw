## 概论作业2  
  
### Q1：用你的语言描述图灵为什么要证明停机问题, 其证明方法和数学原理是什么 
  
- 图灵证明停机问题的根本目的是为了证明Hilbert's tenth problem，即  

> 能否找到一种普遍的算法，可用来判定一个任意形式的丢番图方程是否有整数解 

他据此设计了图灵机，由于图灵机的纸带无限长，理论上它能够实现任何可能的运算。既然图灵机覆盖了任何可能的数学运算过程，那么如果存在图灵机无法判断的过程，那这个问题答案自然是没有普遍的算法。据此，图灵设计了停机问题，简单的说法即“是否有程序能够判断任何其他程序能否在有限的时间内中止运行”。他通过证明停机问题中的假想程序不存在，从而给出了Hilbert's tenth problem的答案。  

- 停机问题的证明方法和数学原理：  
**使用反证法来证明停机问题：假设一个程序f能够判断其他程序能否停机，则构造一个悖论的程序g，在g里调用程序f，但执行和f的输出相反的操作，这样f就无法判断g能否停机。**   
  
*这是一个用来判断一个程序是否能够停机的程序f：*

```
boolean f(program, input)  
  if (program halt on input) return true  
  else return false  
```

*这是一个主程序g：*
```
boolean g(program)
    if f(program, program) == true
        loop forever
        return false
    else 
        return true
```

在主程序g里用程序f判断g是否能停机。调用程序g(g)，如果f输出的结果是判断g能停机，就让g永久运行；如果f判断g不能停机，程序g返回true之后结束，无论如何都与f的判断结果相悖。因此，f在对g能否停机的问题上判断失败，即不存在一个万能程序能够判断其他任何程序能否停机，从而证否了Hilbert的命题。  

<br/><br/>
### Q2：你在向中学生做科普，请向他们解释二进制补码的原理.

（此处默认中学生已经知道十进制和二进制，不作详细解释）

- 计算机存储数据采用二进制的方式（因为有十种状态的存储单位技术难度远比仅有“真”“假”两种状态的存储单位要高），将我们习惯使用的十进制整数转化为二进制。
- 最简单的表示方法，就是将一个十进制数直接转化为二进制，存储在固定位数的单位里，多余的位数用“0”补足。然而，在实际使用的时候，需要考虑数字的正负，因此我们在存储单位中将第一位单独拿出，用来定义正负号，“0”为正，“1”为负，后面的(n-1)位用来存储数字。这样的存储方式称为二进制**原码**。
- 但是，原码的问题在于它不便进行运算。因为运算的时候要考虑正负，还要考虑加减法，这大大增加了设计难度和计算难度。  
因此，如果将a-b转化成a+(-b)，那么计算机就只用加法一种运算功能而不需要减法功能，据此，科学家发明了二进制**反码**。反码是对负的原码每位取反之后的表示法（除了第一位恒为“1”），即如果原码是负数，那么反码就将第二位至最后一位的所有数字“1”替换成“0”，“0”替换成“1”，这样在进行运算时，所有减法都可以表达为加上减数的相反数形式。这样就方便进行运算。例如:  
```
2+(-2)==0010+1010==1100          //原码运算显然有问题
2+(-2)==0010+1101==1111==(-0)    //反码运算数值正确
```

- 那么新的问题来了，这个反码和原码都有+0和-0，并且因为有-0，计算这个范围以外的值就有问题，例如
```
5+(-3) == 2 != 0101+1100 == 0001 == 1          //错误
3+(-5) == (-2) == 0011+1010 == 1101 == (-2)       //正确
3+(-2) == 1 != 0011+1101 == 0000 == 0          //错误
2+(-3) == (-1) == 0010+1100 == 1110 == (-1)       //正确
```
所以用反码运算的结果，因为有两个0，所以只要得到正数，都会比实际结果小1，这样就造成很大的麻烦，如果结果是正数就必须+1。  
- 因此，有大佬机智地解决了这个问题，他把所有的负数反码加上1，这样得到的二进制数集合叫做**补码**，补码完美地解决了上述问题。  
补码实际上利用了钟表盘的原理，一个X格的表盘，和N相反的数是(X-N)，这样N+(X-N)又转回到初始值0，并且有且仅有一个0。为什么这么说呢？上面反码的2+(-2)一例，0000相当于钟表的0点，1111相当于12点，但是现在的钟表既有12又有0，就成了一个13格的问题钟表。如果我们把负数的反码+1，变成补码  
```
2+(-2)==0010+1110==0000==0
```
那么所有的-0就消失了！  
对于其他的运算，补码也能消除问题结果
```
5+(-3) == 2 == 0101+1101 == 0010 == 2          //正确
3+(-5) == (-2) == 0011+1011 == 1110 == (-2)       //正确
3+(-2) == 1 == 0011+1110 == 0001 == 1          //正确
2+(-3) == (-1) == 0010+1101 == 1111 == (-1)       //正确
```
所有的负数结果因为是+1之后的补码，所以它们仍然正确，并且所有正数结果因为负数+1而正数补码不变，所以结果+1，变为正确！最终结果相当于把-0挤出去了，从而完美解决了二进制加减运算的问题。
最后复习一下二进制补码的转换：  
> 正数的补码和原码相同，把整数转换成二进制数，再在前面其他位数上补0即可  
负数的补码是先把整数转换成二进制数，在前面其他位数上补0，继而把所有数字取反（第一位变成1），再+1得到补码


