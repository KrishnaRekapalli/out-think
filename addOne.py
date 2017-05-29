
    
def plusOne(digits):
        
    def sumCarry(digit):
        carry = digit//10
        remainder = digit % 10
            
        return (carry,remainder)
        
            
    digits2 = digits
    digits2.reverse() 
    result = []
        
    for i in range(len(digits2)):
            
        if i==0:

            digRes = digits2[i]+1
            digits2[i] = sumCarry(digRes)[1]
            carryOver = sumCarry(digRes)[0]
        else:
            #print digits2[i]
            print carryOver
            digRes2 = carryOver+digits2[i]
            digits2[i] = sumCarry(digRes2)[1]
            carryOver = sumCarry(digRes2)[0]

    #print carryOver
    if carryOver != 0:

        print carryOver

        digits2.append(carryOver)

    digits2.reverse()
        
    return digits2



class Solution1(object):

    def repeatedSubstringPattern(self, s):
        
        
        #def substr
        
        
        #rep = 0
        for i in range(1,(len(s)//2)+1):
            rep = 0
            for j in range(1,(len(s)//i)):
                print 'substring length  '+str(i)
                print '    '+s[:i]+ ':' +s[(i)*j:((i)*j)+i]

                if s[:i] == s[(i)*j:((i)*j)+i]:

                    rep = rep+1
                    
                else:
                    print 'not '+str(i)+'  checking length'+ str(i+1)
                    break
            print 'reps found are: '+str(rep)
            print 'reps needed are: '+ str((len(s)//i)-1)
            if (rep == (len(s)//i)-1 ) & ((rep+1)*i == len(s)):
                
                return True
            
            else:
                pass
                
                
            if i == (len(s)//2):
                return False


k = Solution1()

print k.repeatedSubstringPattern("ajdnamndncsghghghgdjsdkfsdbcsjhcshdajdnamndncsdjsdkfsdbchjsjhcshdajdnamndncsdjsdkfsdbcsjhcshdajdnamndncsdjsdkfsdkbcsjhcshdajdnamndncsdjsdkfsdbcsjhcshdajdnamndncsdjsdkfsdbcsjhcshdajdnamndncsdjsdkfsdbcsjhcshdajdnamndncsdjsdkfsdbcsjhcshdajdnamndncsdjsdkfsdbcsjhcshdajdnamndncsdjsdkfsdbcsjhcshdajdnamndncsdjsdkfsdbcsjhcshdajdnamndncsdjsdkfsdbcsjhcshd")

