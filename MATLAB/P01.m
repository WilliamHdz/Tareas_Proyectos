flag = 1;

while flag == 1
    
    fprintf('\n');
	fprintf('########################################\n');
	fprintf('# 1. COMPARAR 3 NÚMEROS ---------- (i) #\n');
	fprintf('# 2. SALIR ----------------------- (s) #\n');
	fprintf('########################################\n');
	fprintf('\n');

	opt = input('INGRESE LA OPCIÓN QUE DESEA EJECUTAR: ','s');
	fprintf('\n');	                
    
    switch opt
        
        
       
        case 'i'
            
            num1 = input('INGRESE EL PRIMER NÚMERO: ');
            num2 = input('INGRESE EL SEGUNDO NÚMERO: ');
            num3 = input('INGRESE EL TERCER NÚMERO: ');
            fprintf('\n');
            
            if (num1 > num2 && num1 > num3) && (num1 ~= num2 && num1 ~= num3 && num2 ~= num3)

			fprintf('LA SUMA DE LOS NÚMEROS ES: %g', (num1+num2+num3));

            elseif (num2 > num1 && num2 > num3) && (num1 ~= num2 && num1 ~= num3 && num2 ~= num3)

			fprintf('LA MULTIPLICACIÓN DE LOS NÚMEROS ES: %g',(num1*num2*num3));

            elseif (num3 > num2 && num3 > num1) && (num1 ~= num2 && num1 ~= num3 && num2 ~= num3)

			fprintf('LA CONCATENACIÓN DE LOS TRES NÚMEROS ES: %g%g%g',num1,num2,num3);

            elseif (num1 == num2 && num3 ~= num1) || (num1 == num3 && num2 ~= num1) || (num2 == num3 && num1 ~= num3)

                if num1 == num2

				fprintf('EL NÚMERO DIFERENTE ES: %g', num3);
            
                elseif num1 == num3

				fprintf('EL NÚMERO DIFERENTE ES: %g', num2);
                
                else
                    
				fprintf('EL NÚMERO DIFERENTE ES: %g', num1);
                
                end
            
            else
			
			fprintf('LOS NÚMEROS SON IGUALES %g %g %g \n: ',num1,num2,num3);

            end
        case 's'
            
            flag = 0;
        
        otherwise
            
            fprintf('######################################\n');
            fprintf('# USTED NO INGRESO UNA OPCIÓN VALIDA #\n');
            fprintf('######################################\n');
    end
    
    fprintf('\n');
    
end

fprintf('####################################\n');
fprintf('# GRACIAS POR UTILIZAR EL PROGRAMA #\n');
fprintf('####################################\n');