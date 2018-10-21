def main():
    name1=input("Enter the First Name : ")
    name2=input("Enter the Second Name : ")
    st=name1+"love"+name2
    print(str.upper(name1),"LOVE",str.upper(name2))
    su=part1(st)
    part2(su)
    
#Function to get characters Count
def part1(st):
    stg=""                                     #An Empty String 
    emp=""                                  #An Empty String
    #To count the no. of occurance of character in string st
    
    for i in st:                               
        if i not in stg:                     #count the no. of occurance of a character only ones
            emp+=str(st.count(i))       
            stg+=i
    return emp

#Function to calculate Percentage
def part2(su):
    A=list(su)
    count=3                                
    while(count>2):                              #no. of values in list >2
        first=0
        j=len(A)-1
        mid=(first+j)//2
        count=0
    
        for i in range(first,mid+1):

            if(i<j):                                      #specially becoz i==j value
                A[i]=str(int(A[i])+int(A[j]))
                
            j-=1
        A=A[:mid+1]                         #delete the unwanted part of list
        for i in A:                              #to check the no. of values in list
            count+=1
       
        
        delimiter=""
        res=delimiter.join(A)                #Conversion of list into string
    
    if(len(res)>2):                              #For the value Greater than 100
        part2(res)
    else:
        print("Congrats! Your love Percentage are", res,"%")
    ch=input("Do you want to continue with some other names(y/n) ")
    if(ch=="y" or ch=="Y"):
        main()

        
main()
