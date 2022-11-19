; Set video mode
mov AH, 00h  ; Function code
mov AL, 3    ; Video mode
int 10h      ; OBLIVION                            


;print " Greetings XZANATOL!"


greetX DB "H", "E", "L", "L", "O", " "
nameX DB "X", "Z", "A", "N", "A", "T", "O", "L"
mov DI, 00h ; array Index 
mov BX, 0Fh ; AH,09 param
mov CX, 01h ; AH,09 param
       
testa:
    mov DX, DI        ; Copy index to test arena
    sub DL, 06h       ; Test using subtraction to ZERO
    JZ c_testb           ; Jump if ZERO
    JNZ printG        ; Jump if not ZERO

printG: 
    mov AH, 09h       ; Function code
    mov AL, greetX[DI] ; Char to print
    int 10h           ; OBLIVION 
    
    add DI, 01h       ; Increment array index
    
    mov AH, 02h       ; Update cursor position
    mov DX, DI        ; Set column
    mov DH, 00h       ; Set row
    int 10h           ; OBLIVION    
    jmp testa
   

c_testb:
    mov DI, 00h       ; Reset Index
    jmp testb         ; To the next word
   
      
testb:    
    mov DX, DI        ; Copy index to test arena
    sub DL, 08h       ; Test using subtraction to ZERO
    JZ exit           ; Jump if ZERO
    JNZ printN        ; Jump if not ZERO

printN:
    mov AH, 09h       ; Function code
    mov AL, nameX[DI] ; Char to print
    int 10h           ; OBLIVION 
    
    add DI, 01h       ; Increment array index
    
    mov AH, 02h       ; Update cursor position
    mov DX, DI        ; Set column
    add DL, 6h        ; Set cursor column + previous word length
    mov DH, 00h       ; Set row
    int 10h           ; OBLIVION
    jmp testb 
    
exit:
    hlt