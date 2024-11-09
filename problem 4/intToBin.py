def int_to_reverse_binary(num1):
    if num1 == 0:
        return ("0")
    
    binary_val = ''
#write your while loop here
    
    while num1 > 0:
        binary_val += str(num1 % 2)
        #rem = num1 % 2
        num1 //= 2
        #write your code

    return binary_val


def string_reverse(inputString): 
    # reverse_input = ''
    # for i in input_string:
    #     reverse_input = reverse_input + i
    # return(reverse_input)
    return inputString[::-1]
    
   #write your for loop here
    
    #return reverse_input

if __name__ == '__main__':
    user_input = int(input())
    
    binary_string = str(int_to_reverse_binary(user_input))
    binary_string = str(string_reverse(binary_string))
    
    print(binary_string)
    