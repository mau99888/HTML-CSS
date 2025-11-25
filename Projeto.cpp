int main(){
    float calcular_salario_bruto();
    float calcular_desconto();
    float calcular_salario_liquido();
    int x, y;
    float j, z, a;
    x = 8;
    y = 8 * 21;
    j = 200 * 21;
    z = 4200 * 0.09;
    a = 4200 - 378;
printf("Horas de Trabalho: %d \n\n", x);
printf("Horas Trabalhadas no Mes: %d \n\n", y);
printf("Salario Bruto: %.2f \n\n", j);
printf("Desconto sobre salario: %.2f \n\n", z);
printf("Salario Liquido: %.2f \n\n", a);


return 0;
} 
