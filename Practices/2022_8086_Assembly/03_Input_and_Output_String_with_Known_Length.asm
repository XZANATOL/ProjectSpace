include 'emu8086.inc'
; Set video mode
mov AH, 00h
mov AL, 3
int 10h

mov DI, 0Ah ; acumulated 10^x number for converting array of numbers to int
  
; **************** INT input *****************  
; Get length
input:
    mov AH, 01h      ; Take input
    int 21h          ; OBLIVION

    cmp AL, 0Dh      ; Check if input is enter button
    je ProcessInput_0; If yes, process the length variable
    
    mov DL, AL       ; Move hex char to DL
    sub DL, 30h      ; Subtract asccii coofficient to convert char to int
    mov DH, 00h      ; Making sure it's empty
    push DX          ; Push digit to stack
    add CX, 0001h    ; Loop iteration increment for processing
    jmp input        ; Repeat

; Convert array of numbers to int
ProcessInput_0:
    pop DX           ; Processing Units
    mov len, DX      ; Update variable
    mov SI, 000Ah    ; Add 10 to SI for tenths
    sub CX, 0001h    ; Loop iteration decrement for processing
    je  Update_Crsr_P; If only units entered
    jne ProcessInput_1; Continue to process tenths, hundreds, ..etc
    
ProcessInput_1:
    pop AX           ; Pop to AX for mul command
    mul SI           ; Multiplty coofficient
    add len, AX      ; Add result to variable
    mov AX, SI       ; Move coofficient to AX for accumulation 
    mul DI           ; Accumulate
    mov SI, AX       ; Update coofficient
    sub CX, 0001h    ; Loop iteration decrement for processing
    je Update_Crsr_P ; If final iteration
    jmp ProcessInput_1; Repeat

; Update cursor position for new line (since we pressed enter)
Update_Crsr_P:
    mov AH, 03h      ; Get cursor: DH = Row, DL = Col
    int 10h          ; OBLIVION
    add DH, 01h      ; Update for the next row 
    mov DL, 00h      ; Update for the 0th col
    mov AH, 02h      ; Set cursor function
    int 10h          ; OBLIVION
    jmp str_input_set; Setting params for string input
; **************** INT input *****************    

; **************** STR input *****************    
; Handle the word to print
str_input_set:
    mov DI, 0000h    ; len tracker
    jmp str_input    ; Begin input phase
    
str_input:
    mov AH, 01h      ; Take input
    int 21h          ; OBLIVION
    
    cmp AL, 0Dh      ; Check if input is enter button
    je Update_Crsr_P1
    
    mov nameX[DI], AL; Save char in nameX array
    add DI, 0001h    ; Increament index tracer
    jmp str_input    ; Repeat
    
; Update cursor position for new line (since we pressed enter)
Update_Crsr_P1:
    mov AH, 03h      ; Get cursor: DH = Row, DL = Col
    int 10h          ; OBLIVION
    add DH, 01h      ; Update for the next row
    mov DL, 00h      ; Update for the 0th col
    mov AH, 02h      ; Set cursor function
    int 10h          ; OBLIVION
    jmp print_set    ; Setting params for string input
; **************** STR input *****************

; **************** STR print *****************
print_set:
    mov DI, 0000h    ; Reset index tracker
    print "Greetings " ; Another practice 
    jmp printer      ; Let's begin

printer:

    mov BX, 000Fh    ; Set color (F= White) 
    mov CX, 0001h    ; Set number of print times
    
    cmp len, DI      ; Check if reached final index
    je exitt
    
    mov AL, nameX[DI]; Move char to the print stage
    mov AH, 09h      ; Print function
    int 10h          ; OBLIVION
    
    add DI, 0001h    ; Increament index tracker
    
    mov AH, 03h      ; Get cursor: DH = Row, DL = Col
    int 10h          ; OBLIVION
    
    mov CX, DI       ; Intermmedite area to get 8-bit block
    add CL, 0Ah      ; Add 'greetings ' length shift
    mov DL, CL       ; Update cursor col +=1
    mov AH, 02h      ; Set cursor position function
    int 10h          ; OBLIVION
    
    jmp printer      ; Repeat
; **************** STR print *****************           

exitt:
    mov AL, "!"
    mov AH, 09h
    int 10h
    hlt

len DW 0
nameX DB ""