#include <iostream>

using namespace std;

int main(){

    char letra;

    cout << "Insira uma letra:\n";
    cin >> letra;

    if(letra >= 'a' && letra <= 'z'){
        if(letra == 'a' || letra == 'e' || letra == 'i' ||
           letra == 'o' || letra == 'u'){
            cout << "Vogal minuscula\n";
        }
        else{
            cout << "Consoante minuscula\n";   
        }
    }
    else{
        if(letra == 'A' || letra == 'E' || letra == 'I' ||
           letra == 'O' || letra == 'U'){
            cout << "Vogal maiuscula\n";
        }
        else{
            cout << "Consoante maiuscula\n";
        }
    }

    return 0;
}