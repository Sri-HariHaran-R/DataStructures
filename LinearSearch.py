pos=-1 #Global Variable

def search(nums,n):

    for i in range(len(nums)):
        if nums[i]==n:
            globals()['pos']=i
            return True

nums=[10,1,18,17,16,10,2,0,55]
n=int(input("Enter a Number : "))

if search(nums,n):
    print("Element Found at index : ",pos)
else:
    print("Element Not Found")
