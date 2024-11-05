#include "iostream"  // Include input-output stream library
#include "string"    // Include string library
#include "fstream"   // Include file stream library

using namespace std;

// Function name hdou with three parameters: two integers (p, o) and one string (jo)
void hdou(int p, int o, string jo) {
    cout << "    ========= BURP FORCE ==========      ";
    cout << "\nFIRST NUMBER: ";
    cin >> p;  // Input the first integer
    cout << "SECOND NUMBER: ";
    cin >> o;  // Input the second integer
    printf("Do you want to create a file? (yes/no): ");
    cin >> jo;  // Input to decide if a file should be created

    if (jo == "yes" || jo == "y") {  // If the user wants to create a file
        string in;  // Variable to decide whether to delete the file
        if (p < o) {  // Check if the first number is less than the second
            ofstream iu("brupforce.txt");  // Create an output file stream
            cout << "File name: brupforce.txt";
            for (int i = p; i <= o; i++) {  // Loop from p to o
                iu << i << endl;  // Write each number to the file
            }
            cout << endl << "Thank you for creating the file." << endl;

            printf("\nDo you want to delete the file? (y/n): ");
            cin >> in;  // Input to decide whether to delete the file
        } else if (p > o) {  // If the first number is greater than the second
            cout << "\nbhima " << p << " > " << o;  // Display message
        } else if (p == o) {  // If both numbers are equal
            cout << "\nalhmar " << p << " = " << o;  // Display message
        } else {
            cout << "\nERROR ";  // In case of unexpected input
        }

        if (in == "y") {  // If user wants to delete the file
            remove("brupforce.txt");  // Remove the file
        } else if (in == "n" || in == "no") {  // If user does not want to delete the file
            printf("Ok, not deleting the file.");
        } else {
            cout << "\n<<error>> " << in;  // Handle unexpected input
        }
    } else if (jo == "no") {  // If the user does not want to create a file
        cout << "\nNo file created.";
    } else {
        cout << "\nError: " << jo;  // Handle unexpected input
    }
}

int main() {
    int p;  // First number
    int o;  // Second number
    string jo;  // User response for file creation
    hdou(p, o, jo);  // Call the hdou function with the variables
}
