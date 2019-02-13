#! usr/bin/python3

def find_maximum_subarray(arr=[1,-3,2,1,-1,-1,-1,16]):
    max_current = arr[0]
    max_global = arr[0]
    largest_subarray = [arr[0]]

    for i in range(1,len(arr)):
        max_current = max(arr[i], max_current+arr[i])

        if max_current > max_global:
            max_global = max_current
            #largest_subarray = 
            
    return max_global


if __name__ == "__main__":
    print(find_maximum_subarray())
    
