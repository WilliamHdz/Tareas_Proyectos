flag = 1;

while flag == 1
    
    fprintf('\n');
	fprintf('##############################################################\n');
	fprintf('# 1. MOSTRAR TODOS LOS DIVISORES DE UN NÚMERO ---------- (d) #\n');
	fprintf('# 2. SALIR --------------------------------------------- (s) #\n');
	fprintf('##############################################################\n');
	fprintf('\n');

	opt = input('INGRESE LA OPCIÓN QUE DESEA EJECUTAR: ','s');
	fprintf('\n');	                
    
    switch opt
        
        case 'd'
            
            num = input('INGRESE UN NÚMERO ENTERO POSITIVO: ');
            fprintf('\n');
            
            fprintf('LOS DIVISORES DE %g SON LOS NÚMEROS: ',num);
            
            for i = 1:num
                if mod(num,i) == 0
                    fprintf('%g, ',i);
                else
                    i = i;
                end
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