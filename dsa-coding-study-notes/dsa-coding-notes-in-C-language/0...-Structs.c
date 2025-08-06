#include <stdio.h>

typedef struct {
    char name[30];
    short day, month, year;
} tregister;  // No pointer alias here

int main() {
    tregister personRegistration = {"Rafael Henrique", 22, 1, 2005};
    
    // Using "." (direct access)
    printf("Name: %s\n", personRegistration.name);
    
    // Using "->" via a manually declared pointer
    tregister *ptrToRegister = &personRegistration;
    printf("Name (via pointer): %s\n", ptrToRegister->name);
    
    return 0;
}