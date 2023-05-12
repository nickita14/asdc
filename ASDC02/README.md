# Sorting Algorithms in Python

This Python script implements three popular sorting algorithms - Bubble Sort, Quick Sort and Merge Sort - and applies them to a column of numeric data in a CSV file. The program measures and reports the execution time, number of comparisons, and number of permutations for each algorithm.

## Description of the Sorting Algorithms

1. **Bubble Sort**: Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

2. **Quick Sort**: QuickSort is a divide and conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. It works by dividing the input into two smaller lists and recursively sorting each of those lists.

3. **Merge Sort**: Merge Sort is also a divide and conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge() function is used to merge two halves. 

## How to Run the Program

The program is run from the command line as follows:

python lab2.py

You will be prompted to enter the column name to sort. The column name must exist in the CSV file and it should contain numeric data. The CSV file ('students.csv') should be in the 'src' directory relative to the script.

## Results

The program will output the execution time, number of comparisons, and number of permutations for each of the sorting algorithms. It will also display the theoretical time complexity of each algorithm. 
