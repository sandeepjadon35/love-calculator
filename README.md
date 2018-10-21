# Love-Calculator
Its a simple love percentage calculator

First of all it accept 2 names and print the string name1 + love + name2

    name1=input("Enter the First Name : ")
    name2=input("Enter the Second Name : ")
    st=name1+"love"+name2
    print(str.upper(name1),"LOVE",str.upper(name2))
    
    
Then it gonna count the no. of occurance of every character in "name1 love name2" and once the no. of occrance of a particular character is done then do not count its occurance again
  
    for i in st:                               
        if i not in stg:                     
            emp+=str(st.count(i))       
            stg+=i
       
Now you have a string containg the no. of occurance of character in phrase name1 love name2
Then Add the First and Last number from the string and Store them in the same variable
Do this untill your string have a value less than or equal to 100
   
    while(count>2):                              
        first=0
        j=len(A)-1
        mid=(first+j)//2
        count=0
        for i in range(first,mid+1):

            if(i<j):                                    
                A[i]=str(int(A[i])+int(A[j]))
                
            j-=1
        A=A[:mid+1]                     
        for i in A:                            
            count+=1
 If the string have a value greater than 100 then do it again or print the outcome

    if(len(res)>2):                              
        part2(res)
    else:
        print("Congrats! Your love Percentage are", res,"%")

Now you have your Love Percentages with your Loving one
       
        

 

