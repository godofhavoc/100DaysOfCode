#include <iostream>

using namespace std;

class Vector {
    private:
        double* elem;
        int sz;
    public:
        Vector(int s) :elem{new double[s]}, sz{s} {}
        double& operator[](int i) { return elem[i]; }
        int size() { return sz; }
};

// void vector_init(Vector& v, int s) {
//   v.elem = new double[s];
//   v.sz = s;
// }

double read_and_sum(int s) {
    Vector v(s);
    for(auto i = 0; i != s; ++i)
        cin >> v[i];

    double sum = 0;
    for (auto i = 0; i != s; ++i)
        sum += v[i];
    return sum;
}

bool accept() {
  int tries = 1;
  while(tries < 4) {
    cout<<"Do you want to proceed or not(y or n)?\n";
    char answer = 0;
    cin>>answer;
    switch(answer) {
      case 'y':
        return true;
      case 'n':
        return false;
      default:
        cout << "Sorry didn't understand that. Try again\n";
        ++tries;
    }
  }
  cout << "Fuck this\n";
  return false;
}

int main() {
  int v[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

  cout << read_and_sum(10) << '\n';
}
