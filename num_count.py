def total(num):
        nums = str(num)+'X'
        cur = ''
        count = 1
        ans = ''
        for i in nums:
                if  cur == '':
                        cur = i
                elif cur[-1:] == i:
                        cur += i
                else:
                        ans += cur[-1:]+str(len(cur))
                        cur = i

        print ans
total("122111")
