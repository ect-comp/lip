#include <iostream>

using namespace std;

int main(){

    int dia;

    cout << "Insira um dia (1-30) de Abril/2022:\n";
    cin >> dia;

    switch((dia-1) % 7){
        case 0:
            cout << "Dia " << dia << " - sexta\n";
            break;
        case 1:
            cout << "Dia " << dia << " - sabado\n";
            break;
        case 2:
            cout << "Dia " << dia << " - domingo\n";
            break;
        case 3:
            cout << "Dia " << dia << " - segunda\n";
            break;
        case 4:
            cout << "Dia " << dia << " - terca\n";
            break;
        case 5:
            cout << "Dia " << dia << " - quarta\n";
            break;
        case 6:
            cout << "Dia " << dia << " - quinta\n";
            break;
    }

    return 0;
}