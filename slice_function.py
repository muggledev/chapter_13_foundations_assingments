
# Step 1: convert any negative starts or stops to their positive equivalent
# Step 2: iterate over it_obj -- do some logic to correctly pull out the right values, based on between the start and the stop and then the step
# (do some logic to pull those out and add them to our sliced list so that we can return that)
# Step 3: check if start is less than or greater than the stop, and how that applies to the step
# ******
# def sliced(it_obj, start=0, stop=None, step=1):
#     sliced_stuff = slice(start, stop, step)
#     sliced_list = it_obj[sliced_stuff]
    
    
    
#     # print( slice(abs(it_obj, start=0)))

#     # print( slice(abs)(it_obj, stop = None))

#     # print( slice(abs)(it_obj, step=1))
    
    

#     # print(nums[0:7:3])
    
    
#     return sliced_list

# print(sliced([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, None, 2))
# ******



nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]

def sliced(iter_obj, start=3, stop=None, step=3):

    if start < 0:
        start += len(iter_obj)
    if stop is None:
        stop = len(iter_obj)
    if stop < 0:
        stop += len(iter_obj)

    sliced_list = []

    if step > 0:
        i = start 
        while i < stop:
            sliced_list.append(iter_obj[i])
            i += step
    # else:
    #     i = start
    #     while i > stop:
        
    #         sliced_list.append(iter_obj[i])
    #         i += step

    return sliced_list

print(sliced(nums))










































# **********CHAT GPT*************************
# def sliced(iter_obj, start=0, stop=None, step=1):

#     if stop is None:
#         stop = len(iter_obj)

#     sliced_list = []

#     for i in range(start, stop, step):
#         sliced_list.append(iter_obj[i])

#     return sliced_list

# print(sliced([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# ********OR********************
    
    
    
# def sliced(iter_obj, start=0, stop=None, step=1):

#     sliced_list = []
    
#     start = abs(start)  
#     stop = abs(stop) if stop is not None else float('inf')

#     idx = 0
    
#     for item in iter_obj:
        
#         if idx < start:
#             idx += 1
#             continue
        
#         if idx >= stop:
#             break
        
#         if (idx - start) % step == 0:
#             sliced_list.append(item)
        
#         idx += 1
       
#     return sliced_list
    

# print(sliced([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(sliced([1, 2, 3, 4, 5, 6, 7, 8, 9], -2, None, 2))  

        
