flag = 1;
num1 = 0;
num2 = 0;
z = 0;

while flag == 1
    
    disp('          CALCULADORA          ');
    disp(' ');
    disp('###############################');
    disp('# 1. SUMA ----------------(1) #');
    disp('# 2. RESTA ---------------(2) #');
    disp('# 3. MULTIPLICACI�N ------(3) #');
    disp('# 4. DIVISI�N ------------(4) #');
    disp('# 5. SALIR ---------------(5) #');
    disp('###############################');
    disp(' ');
    
    opt = input('ELIJA UNA OPCI�N: ');
    
    switch opt
        
        case 1
            
            disp(' ');
            disp('###################################');
            disp('# USTED SELECCIONO LA OPCI�N SUMA #');
            disp('###################################');
            disp(' ');
            num1 = input('INGRESE EL PRIMER N�MERO: ');
            num2 = input('INGRESE EL SEGUNDO N�MERO: ');
            disp('                                  ')
            z = num1 + num2;
            fprintf('EL RESULTADO DE LA SUMA ES: %d \n',z);
            disp('___________________________________');
            disp('                                   ');

        case 2
            
            disp(' ');
            disp('####################################');
            disp('# USTED SELECCIONO LA OPCI�N RESTA #');
            disp('####################################');
            disp(' ');
            num1 = input('INGRESE EL PRIMER N�MERO: ');
            num2 = input('INGRESE EL SEGUNDO N�MERO: ');
            disp('                                  ')
            z = num1 - num2;
            fprintf('EL RESULTADO DE LA RESTA ES: %d \n',z);
            disp('____________________________________');
            disp('                                   ');

        case 3
            
            disp(' ');
            disp('#############################################');
            disp('# USTED SELECCIONO LA OPCI�N MULTIPLICACI�N #');
            disp('#############################################');
            disp(' ');
            num1 = input('INGRESE EL PRIMER N�MERO: ');
            num2 = input('INGRESE EL SEGUNDO N�MERO: ');
            disp('                                  ')
            z = num1 * num2;
            fprintf('EL RESULTADO DE LA MULTIPLICACI�N ES: %d \n',z);
            disp('_____________________________________________');
            disp('                                   ');
            
        case 4
            
            disp(' ');
            disp('#######################################');
            disp('# USTED SELECCIONO LA OPCI�N DIVISI�N #');
            disp('#######################################');
            disp(' ');
            num1 = input('INGRESE EL PRIMER N�MERO: ');
            num2 = input('INGRESE EL SEGUNDO N�MERO: ');
            disp('                                  ');
            
            if num2 == 0
                
                disp('LA DIVISI�N ENTRE 0 NO ES POSIBLE');
                disp(' ');
                
            else 
                
                z = num1 / num2;
                fprintf('EL RESULTADO DE LA DIVISI�N ES: %d \n',z);
                disp('_______________________________________');
                disp('                                   ');
            
            end
 
        case 5
            
            flag = 0;
              
        otherwise
            
            disp(' ');
            disp('USTED NO INGRESO UNA OPCI�N VALIDA');
            disp(' ');
        
    end
end

disp(' ');
disp('####################################');
disp('# GRACIAS POR UTILIZAR EL PROGRAMA #');
disp('####################################');
