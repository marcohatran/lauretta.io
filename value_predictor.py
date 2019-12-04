def value_predictor(num_lst):
    
    if not type(num_lst)==list:    #input a list
        print("ERROR. Please enter a list of integers.")
    
    
    else:
        
        if not all((isinstance(x,int) for x in num_lst)):    # all integers
            print("ERROR. Please enter integers only.")

        else:   

            lst_length = len(num_lst)

            if lst_length < 6:    #6 ints

                print("ERROR. Please enter at least 6 integers.")

            else:

                if lst_length % 2 == 0:    

                    left_pos = int(lst_length/2) - 1    

                    right_pos = left_pos + 1    

                    left_val = num_lst[left_pos]    

                    right_val =num_lst[right_pos]

                    mid_val = (left_val+right_val)/2


                else:

                    mid_pos = int(lst_length/2)    

                    mid_val = num_lst[mid_pos]


                return mid_val
if __name__ == '__main__':
    print(value_predictor([1,2,3,4,5,6]))
    print(value_predictor([1,1,1,6,6,6]))