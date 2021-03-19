/*
UNIVERSIDADE PRESBITERIANA MACKENZIE
FACULDADE DE COMPUTACAO E INFORMATICA
LINGUAGENS FORMAIS E AUTOMATOS - PROJETO 2

GRUPO:
- GABRIEL TARDOCHI SALLES - TIA: 
- RODRIGO PIGATTO PASQUALE - TIA: 41816080
 */

#include<stdio.h>
#include<stdlib.h>

/*
 * S -> aBc$
 * B -> bB 
 * B -> e         e: palavra vazia
 */
 
char lookahead;   /* Excepcionalmente variavel global */

int  match(char t, char palavra[], int *pos){
	if (lookahead == t){
		lookahead= palavra[++(*pos)];
		return(1);
	}
	return(0);  
}
/*X -> S$ */
int X(char palavra[], int *pos){
    if(S(palavra, pos) && match('$', palavra, pos)) return (1);
    else return (0);
}

/* S -> T K  */
int S(char palavra[], int *pos){
    if(T(palavra, pos) && K(palavra, pos)) return (1);
    else return(0);
}
/* K-> + T K | - T K | e */
int K(char palavra[], int *pos){
    if(lookahead == '+'){
        if(match('+', palavra, pos) && T(palavra, pos) && K(palavra, pos)) return (1);
        else return (0);
    }
    else if (lookahead == '-'){ 
        if(match('-', palavra, pos) && T(palavra, pos) && K(palavra, pos)) return (1);
        else return (0);
    }
    else return(1); /* caso com palavra vazia */

}

/* T -> F Z */
int T(char palavra[], int *pos){
    if(F(palavra, pos) && Z(palavra, pos)) return (1);
    else return(0);
}

/* Z -> * F Z | / F Z | e */
int Z(char palavra[], int *pos){
    if(lookahead == '*'){
        if(match('*') && F(palavra, pos) && Z(palavra, pos)) return (1);
        else return (0);
    }
    else if(lookahead == '/'){
        if(match('/') && F(palavra, pos) && Z(palavra, pos)) return (1);
        else return (0);
    }
    else return (1); /* caso com palavra vazia */
} 

/* F -> (S) | N */
int F(char palavra[], int*pos){
    if (lookahead == '('){
        if(match('(') && S(palavra, pos) && match(')')) return (1);
    }
    else if (N(palavra pos)) return (1);
    else return(0);
}

/* N -> 0D | 1D | 2D | 3D | 4D | 5D | 6D | 7D | 8D | 9D */

int N(char palavra[], int *pos){
    if (lookahead >= '0' && lookahead <= '9'){
        if(match(lookahead) && D(palavra, pos)) return (1);
        else return (0);
    }
    return (0);
}

/* D -> 0D | 1D | 2D | 3D | 4D | 5D | 6D | 7D | 8D | 9D | e */

int D(char palavra[], int *pos){
    if (lookahead >= '0' && lookahead <= '9'){
        if(match(lookahead) && D(palavra, pos)) return (1);
        else return (0);
    }
    else return (1); /* caso com palavra vazia */
}

void trataErro(){
	printf("\n\nERRO DE SINTAXE\n\n");
	/* Faca um tratamento melhor */
}

int main(){
	char palavra[]= "abbbc$";
	int  pos=0;
	
	lookahead= palavra[pos];
	if (S(palavra, &pos))
	    printf("\nPalavra %s reconhecida\n", palavra);
	else 
	    trataErro();
	system("PAUSE");
	return(0);
}