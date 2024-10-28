# first-projects
my first projects created simple with cpp and python 
## bruceforce create number with <span style="color:blue;">*c++*</span>.
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
