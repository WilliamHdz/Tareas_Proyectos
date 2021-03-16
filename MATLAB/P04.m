flag = 1;

while flag == 1
    
    fprintf('\n');
	fprintf('####################################################################\n');
	fprintf('# 1. MOSTRAR LA SUMATORIA DESDE 0 HASTA UN NÚMERO n ---------- (c) #\n');
	fprintf('# 2. SALIR --------------------------------------------------- (s) #\n');
	fprintf('####################################################################\n');
	fprintf('\n');

	opt = input('INGRESE LA OPCIÓN QUE DESEA EJECUTAR: ','s');
	fprintf('\n');	                
    
    switch opt
        
        case 'c'
            
            num = input('INGRESE UN NÚMERO n: ');
            suma = 0;
            for i = 0:num
                
                suma = suma + i;
            
            end
        
        fprintf('LA SUMATORIA DEL NÚMERO %g ES: %g',num,suma);    
            
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