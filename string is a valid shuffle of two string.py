#This is a program where we are checking that whether the resultant string is a valid shuffle of the two given string
#Rule for valid string:
#1: The length of the resultant string should be same.
#2: The order of both the string in the resultant string should be same.
s1='ab'
s2='12'
s3='z12b'
i=j=k=0
if len(s1) + len(s2) != len(s3):
    print("NO")
else:
    while k < len(s3):
        if i<len(s1) and s1[i]==s3[k]:
            i+=1
        elif j<len(s2) and s2[j]==s3[k]:
            j+=1
        else:
            break
        k+=1

    if i<len(s1) or j<len(s2):
        print('NO')
    else:
        print('YES')
