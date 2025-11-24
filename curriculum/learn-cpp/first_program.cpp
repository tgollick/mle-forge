#include <iostream>

int main() 
{
  std::cout << "Welcome to my program, enter a single number you want to triple";

  int input {};
  std::cin >> input;

  std::cout << "Your value " << input << " has been tripled to " << input * 3 << "!" << std::endl;

  return 0;
}
