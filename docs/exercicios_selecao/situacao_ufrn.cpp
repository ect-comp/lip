#include <iostream>

using namespace std;

int main(){

    float n1, n2, n3, media;

    cout << "Insira as 3 notas:\n";
    cin >> n1 >> n2 >> n3;

    media = (n1 + n2 + n3)/3;

    if(n1 >= 3 && n2 >= 3 && n3 >= 3 && media >= 5){
        cout << "Aprovado\n";
    }
    else if(media >= 3){
        cout << "Reposicao\n";
    }
    else{
        cout << "Reprovado\n";
    }

    return 0;
}