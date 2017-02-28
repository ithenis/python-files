# Write a program that inputs a 4 digit year and then calculates whether or not it is a leap year.
def is_it_leap(x):
    aa = 365
    if x % 400 ==0:         
        aa =366
        
    else:
        if x % 100 == 0:
            aa = 365
            
        else:
            if x % 4 == 0:
                aa = 366
                
    return aa           
            
              
        
aa = is_it_leap(1996)
aa = is_it_leap(1000)
aa = is_it_leap(2000)
aa = is_it_leap(2017)

################################################################
# Using a variation of the above program, calculate the number of days in the inclusive date range  '1st January 2000' to '31st December 2999'.


year1 = 2000
year2 = 2999+1
days = 0

for kk in range(year1,year2):
    jj = is_it_leap(kk)
    days = days+jj
    

print days
