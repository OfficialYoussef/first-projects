# first-project
my first projects created simple with cpp and python 
## bruceforce create number with <span style="color:blue;">c++</span>.
### C++ Code Description

This C++ code defines a function called `hdou` that takes three parameters: `p` (an integer), `o` (a character), and `jo` (a string). The function is used to perform a simple number range creation and file handling task.

The `hdou` function prompts the user to enter the first and second numbers, as well as whether they want to create a file. If the user chooses to create a file, the function will iterate through the range of numbers from the first to the second number and write each number to a file named "brupforce.txt". After writing the numbers to the file, the function will prompt the user to delete the file. If the user chooses to delete the file, it will be removed using the `remove` function. If the user chooses not to delete the file, a message will be displayed.

### `main` Function

```cpp
int main(){
    int p; char o;
    string jo;
    hdou(p,o,jo);
}
```
In the `main` function, the `hdou` function is called with placeholder values for `p`, `o`, and `jo`. You can replace these values with actual input if needed.
here use [file code](https://github.com/OfficialYoussef/first-projects/blob/main/NumBruce.cpp).
# second-project
## Python Interactive Program

This is my first project using Python, created in 2020. The program offers a simple text-based menu to interact with a calculator, calendar, question prompts, identity card generator, and a "hello" greeting section. This interactive program allows users to perform mathematical calculations, view a calendar, answer questions, and even simulate filling out a simple identity card.

### Features

- **Calculator**: Basic arithmetic operations (+, -, *, /).
- **Calc**: Advanced arithmetic options using multiple numbers and operators.
- **Calendar**: Displays the calendar for a specified year.
- **Questions**: Simple interactive questions to test your knowledge.
- **Identity Card Generator**: Asks users for personal information to generate an "identity card."
- **Help**: Provides brief help information.
- **Exit**: Exits the program.

## Sample Menu

```plaintext
                ©youssef
                   2020
00000000000000000000000000000000000000
           <===hello========>        0
           <===calendar=====>        0
           <===calculator===>        0
           <===calc=========>        0
           <===questions====>        0
           <===help=========>        0
           <===exit=========>        0
00000000000000000000000000000000000000
```
## Detailed Features

### Calculator
```
The `calculator` option allows basic operations between two numbers:
- **Addition (+)**, **Subtraction (-)**, **Multiplication (*)**, **Division (/)**.
  
After selecting `calculator`, enter the two numbers and choose the operation.

### Calc
This feature has additional mathematical options:
- **Calc [1]**: Uses four numbers and offers specific operations such as:
  - `o = x + y * z - a`
  - `h = x - y * z / a`
  - `k = x * y + z / a`
  - `l = x / y * z + a`
- **Calc [2]**: Uses three numbers and offers a different set of operations:
  - `x * y / a`
  - `x + y * a`
  - `x - y / a`
  - `x / y + a`
  - `x / y - a`

Each option requests numbers and the preferred operation, then displays the result.
```
### Calendar
Select `calendar` to view a yearly calendar. Currently, this is set to display the calendar for 2021.

### Questions
Choose `questions` to answer simple English language exercises. Options include:
1. Complete the sentence “He ___ the piano.”
2. Fill in the blank: “They ___ professors.”
3. Enter “I am” when prompted with “i.”
4. Convert 95% to decimal form.

Each prompt provides feedback based on the answer's correctness.

### Identity Card Generator
Choose `hello` to create a simulated identity card. The program will prompt for:
- Name, age, country, job, parents' names, residence, gender, and identity (e.g., man, woman).
- The current date and time are included on the "identity card" along with all provided information.

### Help
Typing `help` displays an introductory message about the program 
here use [file code](https://github.com/OfficialYoussef/first-projects/blob/main/Basic_py.py).
