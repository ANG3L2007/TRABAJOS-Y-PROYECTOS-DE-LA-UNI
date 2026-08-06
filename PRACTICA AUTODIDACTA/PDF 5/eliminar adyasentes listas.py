def remove_adyacent(nums):
    cont = 0
    new_list = []
    value = 0
    while cont != len(nums):
        value = nums[cont]
        if nums[cont] != nums[cont-1]:
            new_list.append(nums[cont])
        cont += 1
    return new_list
nums = [2,2,3,5,7,2,3]
print(remove_adyacent(nums))