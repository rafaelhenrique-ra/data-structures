#include <stdio.h>

int main(){
    int myInteger;
    int *pointerToInteger; // Defines pointerToInteger as a pointer capable to point to a int type variable

    pointerToInteger = &myInteger; // pointerToInteger is a pointer to the int type initialized with the myInteger adress variable

    float myFloat = 3.14;
    float *pointerToFloat = &myFloat;

    *pointerToFloat = 1.6; // Atributes 1.6 to the content in the memory position pointed by pointerToFloat
    // Equals to "myFloat = 1.6;"

}