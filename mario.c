//The following code was written entirely by Dan Tan with help from the CS50 course
//Methodology: this problem is broken down into three parts-left pyramid, gap in the middle, and right pyramid.


#include <stdio.h>
#include <cs50.h>


int main(void)
{
    int height;

    //Prompt user for a positive number
    do
    {
        height = get_int("Give a Positive Number less than 23: ");
    }
    while (height < 0 || height > 23);

//pyramid
    
  for (int i = 0; i < height; i++)
  {
      
    //print number of spaces on the left
    char nums = height - 1;
    for (int j = i; j < nums; j++)
    {
        printf(" ");
    }
      
    //print number of hashes on the left
    char numh1 = i + 1;
    for (int j = 0; j < numh1; j++)
    {
        printf("#");
    }

    //print the gap
    printf("  ");

    //print the right pyramid
    char numh2 = i + 1;
    for (int j = 0; j < numh2; j++)
    {
        printf("#");
    }

    //Print the next line
    printf("\n");

 }

}



