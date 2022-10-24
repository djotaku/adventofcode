import cProfile
import solution
import solution_x_in_y

our_salt = "ihaygndm"
print("Regex for quintuple")
cProfile.run('solution.find_one_time_pad_keys(our_salt, 64)')
print("*************")
print("X in Y for quintuple")
cProfile.run('solution_x_in_y.find_one_time_pad_keys(our_salt, 64)')
