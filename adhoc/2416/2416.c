#include<stdio.h>

int main(){
    int treinamento_metros, comprimento_pista, ponto_termino;

    scanf("%d %d", &treinamento_metros, &comprimento_pista);

    ponto_termino = treinamento_metros % comprimento_pista;

    printf("%d\n", ponto_termino);

    return 0;
}