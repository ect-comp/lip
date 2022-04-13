#include <iostream>

using namespace std;

int main(){

    int num;

    cout << "Insira um num. inteiro:\n";
    cin >> num;

    //Duas soluções:
    
    //cout << ( (num == 11)*num + (num != 11)*(num+1) ) << endl;
    cout << ( (num != 11) + num ) << endl;

    return 0;
}