#include <iostream>
#include <limits>

double add(double a, double b) {
  // Adding two values, return the result
  return a + b;
}

double subtract(double a, double b) {
  // Subtracting two values, return the result
  // Got to be careful with order as subtraction and division is not commutative
  return a - b;
}

double multiplication(double a, double b){
  // Multiplying two values, returning result
  return a * b;
}

double division(double a, double b) {
  // Dividing two values, return result
  // Got to be careful with order as subtraction and division is not commutative
  if (b == 0) {
      std::cout << "Error: Cannot divide by zero!\n";
      return std::numeric_limits<double>::quiet_NaN();
  }
  return a / b;
}

char get_operation() {
  bool valid {false};
  char operation {};

  while(!valid) {
    if(!(std::cin >> operation)) {
      std::cout << "\nInvalid operation! Please try again";

      // Clear the stream for retry
      std::cin.clear();
      std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
      continue;
    }

    valid = true;
  }

  return operation;
}

char print_menu() {
  std::cout << "Please enter your desired operation (+, -, *, /) or q to quit: ";
  char operation {get_operation()};
  std::cout << "\n";

  return operation;
}

double get_number() {
  bool valid {false};
  double value {};

  while(!valid) {
    std::cout << "Please enter a value: ";

    if(!(std::cin >> value)) {
      std::cout << "\nInvalid value, please try again";

      // Clear the stream for retry
      std::cin.clear();
      std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
      continue;    
    }

    valid = true;
  }
  
  std::cout << "\n";

  return value;
}

int main() {
  while(true) {
    char operation {print_menu()};

    if(operation == 'q') {
      break;
    }

    double x {get_number()};
    double y {get_number()};

    switch(operation) {
      case '+':
        std::cout << "The result of your calculation is: " << add(x, y) << "\n";
        break;
      case '-':
        std::cout << "The result of your calculation is: " << subtract(x, y) << "\n";
        break;
      case '*':
        std::cout << "The result of your calculation is: " << multiplication(x, y) << "\n";
        break;
      case '/':
        std::cout << "The result of your calculation is: " << division(x, y) << "\n";
        break;
      default:
        std::cout << "Sorry, the operation entered isn't recognised, please try again!" << "\n";
        break;
    }
  }

  return 0;
}
