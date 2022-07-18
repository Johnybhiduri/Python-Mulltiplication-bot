# User will input any number and will get the multiplication table of that no.

Num = int(input('Enter The Number : '))

for i in range(1,11):
    print(f"{Num} X {i} = {Num*i}")
    # DONE