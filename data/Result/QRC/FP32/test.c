#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>  // Added to use isspace()

#define TOLERANCE 0.000001

void S_Gate(int n) {
    printf("S_Gate(%d)\n", n);
}

void H_Gate(int n) {
    printf("H_Gate(%d)\n", n);
}

void CNOT_Gate(int n, int m) {
    printf("CNOT_Gate(%d, %d)\n", n, m);
}

void RX_Gate(int n, double m) {
    printf("RX_Gate(%d, %lf)\n", n, m);
}

void RY_Gate(int n, double m) {
    printf("RY_Gate(%d, %lf)\n", n, m);
}

void RZ_Gate(int n, double m) {
    printf("RZ_Gate(%d, %lf)\n", n, m);
}

void trim(char *str) {
    char *end;

    // Trim leading space
    while(isspace((unsigned char)*str)) str++;

    // Trim trailing space
    if(*str == 0)  // All spaces?
        return;

    end = str + strlen(str) - 1;
    while(end > str && isspace((unsigned char)*end)) end--;

    // Write new null terminator character
    end[1] = '\0';
}

void QRC() {
    FILE *file = fopen("input.txt", "r");
    if (file == NULL) {
        printf("Error: Could not open input.txt\n");
        return;
    }

    char line[100];
    char gateType[10];
    int params[2];
    double angle;

    while (fgets(line, sizeof(line), file)) {
        trim(line);  // Trim leading and trailing spaces

        // Skip lines with just [ or ]
        if (line[0] == '[' || line[0] == ']') {
            continue;
        }

        // Parse for S and H gates
        if (sscanf(line, "('%[^']', [%d], -999)", gateType, &params[0]) == 2) {
            if (strcmp(gateType, "S") == 0) {
                S_Gate(params[0]);
            } else if (strcmp(gateType, "H") == 0) {
                H_Gate(params[0]);
            }
        }
        // Parse for CNOT gate
        if (sscanf(line, "('%[^']', [%d , %d], %lf)", gateType, &params[0], &params[1], &angle) == 4) {
            if (strcmp(gateType, "CNOT") == 0) {
                CNOT_Gate(params[0], params[1]);
            }
        }
        // Parse for RX, RY, RZ gates
        else if (sscanf(line, "('%[^']', [%d], %lf)", gateType, &params[0], &angle) == 3) {
            if (strcmp(gateType, "RX") == 0) {
                RX_Gate(params[0], angle);
            } else if (strcmp(gateType, "RY") == 0) {
                RY_Gate(params[0], angle);
            } else if (strcmp(gateType, "RZ") == 0) {
                RZ_Gate(params[0], angle);
            }
        }
    }

    fclose(file);
}

int main() {
    QRC();
    return 0;
}
