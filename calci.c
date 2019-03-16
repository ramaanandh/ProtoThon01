

#include <stdio.h>
 
int main()
{
	char Operator;
	float a,b, result = 0;
	
	printf("\n Enter an Operator   ");
  	scanf("%c", &Operator);
  	
	printf("\nEnter the Values");
  	scanf("%f%f", &a, &b);
  	
  	switch(Operator)
  	{
  		case '+':
  			result =a+b;
  			break;
  		case '-':
  			result =a-b;
  			break;  			
  		case '*':
  			result =a*b;
  			break;
  		case '/':
  		    if(b==0)
  		    {
  		        printf(" \n invalid input");
  		    }
  		    else
  		    {
  			    result =a/b;
  		    }
  			break;
		default:
			printf("\nInvalid Operator was entered");				    			
	}
  
	printf("\n The result is %f", result);
	
  	return 0;
}

