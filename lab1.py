import csv
import time


class FindField:
    def __init__(self, field_value_to_find: str, column: int, list_of_elements: list):
        self.field_value_to_find = field_value_to_find
        self.column = column
        self.list_of_elements = list_of_elements

    def sequential_search_method(self):
        start_time = time.perf_counter()
        for el in self.list_of_elements:
            if el == self.field_value_to_find:
                print(f"Sequential: found in row №{self.list_of_elements.index(el) + 1}.")
                print(f"    {time.perf_counter() - start_time} seconds.")
                return
        print("Sequential: Not found.")
    
    def binary_search_method(self):
        start_time = time.perf_counter()
        self.field_value_to_find = int(self.field_value_to_find)
        left = 0
        right = len(self.list_of_elements) - 1 

        while left <= right:
            mid_index = int((left + right) / 2)
            if int(self.list_of_elements[mid_index]) == self.field_value_to_find:
                print(f"Binary: found in row №{mid_index + 1}.")
                print(f"    {time.perf_counter() - start_time} seconds.")
                return
            elif int(self.list_of_elements[mid_index]) < self.field_value_to_find:
                left = mid_index + 1
            else:
                right = mid_index - 1
        print("Binary: Not found.")

    def fibonacci_search_method(self):
        start_time = time.perf_counter()
        size = len(self.list_of_elements)
        self.field_value_to_find = int(self.field_value_to_find) 

        # Marks the eliminated range from front
        offset = -1
     
        # Initialize fibonacci numbers
        fib1 = 0 # (m-2)'th Fibonacci No.
        fib2 = 1 # (m-1)'th Fibonacci No.
        next_fib = fib1 + fib2 # m'th Fibonacci

        # fibM is going to store the smallest
        # Fibonacci Number greater than or equal to n
        while next_fib < size:
            fib1 = fib2
            fib2 = next_fib
            next_fib = fib1 + fib2
        
        while next_fib > 1:
            index = min(offset + fib1, size - 1)
            if int(self.list_of_elements[index]) < self.field_value_to_find:
                next_fib = fib2
                fib2 = fib1
                fib1 = next_fib - fib2
                offset = index
            elif int(self.list_of_elements[index]) > self.field_value_to_find:
                next_fib = fib1
                fib2 = fib2 - fib1
                fib1 = next_fib - fib2
            else:
                print(f"Fibonacci: found in row №{index + 1}.")
                print(f"    {time.perf_counter() - start_time} seconds.")
                return
        if fib2 and int(self.list_of_elements[index-1]) == self.field_value_to_find:
            print(f"Fibonacci: found in row №{index}.")
            print(f"    {time.perf_counter() - start_time} seconds.")
            return
        print("Fibonacci: Not found.")

    def tree_search_method(self):
        start_time = time.perf_counter()
        self.field_value_to_find = int(self.field_value_to_find)
        left = None
        right = None
        
        for el in self.list_of_elements:
            
        stack = [0]  # Initialize stasck with root index
        while stack:
            index = stack.pop()  # Pop last element from stack
            if self.list_of_elements[index] == self.field_value_to_find:  # If element is found, return index
                print(f"Tree Search: found in row №{index}.")
                print(f"    {time.perf_counter() - start_time} seconds.")
                return
            # Otherwise, add all child indices to stack
            for child in range(2*index+1, min(2*index+3, len(self.list_of_elements))):
                stack.append(child)
        # If element is not found, return -1
        print("Tree Search: Not found.")


if __name__ == "__main__":
    table_source = list(csv.reader(open('src/bank.csv', "r"), delimiter=","))
    column_name = input(f"Enter the column where we shall to search ({', '.join(table_source[0])}): ")
    if type(column_name) != str or column_name not in table_source[0] or column_name.isdigit():
        print("Invalid column.")
        exit()
    column_index = table_source[0].index(column_name)
    column_to_list = [ row[column_index] for row in table_source[1:] ]
    field_value_to_find = input("Enter the field to find: ")

    find_field = FindField(field_value_to_find, column_index, column_to_list)

    method = input(
        "Choose the search method: 1. Sequential search\n \
                         2. Binary search\n \
                         3. Fibonacci search\n \
                         4. Tree search\n \
                         5. All methods\n"
    )
    match method:
        case "1":
            find_field.sequential_search_method()
        case "2":
            if not table_source[1][column_index].isdigit():
                print("This column is not a number. Cannot use Binary search method.")
                exit()
            find_field.binary_search_method()
        case "3":
            if not table_source[1][column_index].isdigit():
                print("This column is not a number. Cannot use Fibonacci search method.")
                exit()
            find_field.fibonacci_search_method()
        case "4":
            if not table_source[1][column_index].isdigit():
                print("This column is not a number. Cannot use Tree search method.")
                exit()
            find_field.tree_search_method()
        case "5":
            if not table_source[1][column_index].isdigit():
                print("This column is not a number. Cannot use the Tree, Binary, Fibonacci search methods.")
                exit()
            find_field.sequential_search_method()
            find_field.binary_search_method()
            find_field.fibonacci_search_method()
            find_field.tree_search_method()
        case _:
            print("Invalid method.")
            exit()
