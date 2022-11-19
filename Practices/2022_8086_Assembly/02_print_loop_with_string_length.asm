mov AH, 00h
mov AL, 3
int 10h

mov BX, 000Fh
mov CX, 0001h
mov SI, 00h


testt:
    mov DI, SI
    sub DI, len
    je exitt
    jne printt


printt:
    mov AH, 09h
    mov AL, nameX[SI]
    int 10h
    add SI, 01h
    
    mov AH, 02h
    mov DX, SI
    int 10h
    
    jmp testt


exitt:
    hlt
      
 
;len DW 12h                                   
;nameX DB "G", "r", "e", "e", "t", "i", "n", "g", "s", " ", "X", "Z", "A", "N", "A", "T", "O", "L", "!"

len DW 0Eh
nameX DB "G", "r", "e", "e", "t", "i", "n", "g", "s", " ", "M", "O", "R", "A"

;len DW 0Fh
;nameX DB "G", "r", "e", "e", "t", "i", "n", "g", "s", " ", "S", "A", "L", "M", "A"

;len DW 12h
;nameX DB "G", "r", "e", "e", "t", "i", "n", "g", "s", " ", "K", "W", "A", "B", "O", "N", "G", "A"