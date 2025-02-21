!apt-get install gcc g++

def run_c_code(c_code):                 
    with open("temp.c", "w") as f:
        f.write(c_code)
    
    !gcc temp.c -o temp_program
    !./temp_program

c_example_code = """
#include <stdio.h>
int main() {
    printf("Hello World!\\n");
    return 0;
}
"""

run_c_code(c_example_code)
