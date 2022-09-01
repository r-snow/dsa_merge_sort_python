# create a test array
test_array = [1,5,2,9,3,6,4,7,8,10]

# create merge_sort function
def merge_sort(arr):

  # test if array length is greater than one
  if len(arr) > 1:
    # split array into a left and right half
    left_arr = arr[ : len(arr)//2 ]
    right_arr = arr[ len(arr)//2 :]

    # call recursive call on both left and right
    merge_sort(left_arr)
    merge_sort(right_arr)

    #define index for left, right, and merged array
    i = 0
    j = 0
    k = 0

    #while through left index and right index
    while i < len(left_arr) and j < len(right_arr):

      # test if left is less than right
      if left_arr[i] < right_arr[j]:

        # set merged at index to left at index
        arr[k] = left_arr[i]

        #increment left index
        i += 1

      # else if right is less than left
      else:

        # set merged at index to right at index
        arr[k] = right_arr[j]

        #increment right index
        j += 1

      #increment merged index
      k += 1

    # test arrays of length 1
    while i < len(left_arr):
      arr[k] = left_arr[i]
      i += 1
      k += 1

    while j < len(right_arr):
      arr[k] = right_arr[j]
      j += 1
      k += 1

# call merge_sort function on test array
merge_sort(test_array)

#printtest array
print(test_array)
