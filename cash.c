//The program adopts the greedy algorithm approach and always takes the largest coin values possible
//In this case, we are dealing with quaters(25c), dime(10c), nickel(5c), penny(1c) in descending order

#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int count = 0;
    float amount;

    //Prompt user for an amount
    do
    {
    amount = get_float("Provide an amount of dollar: ");
    }
    while (amount<=0);

    //first use quarters if possible
    while (amount>=0.25)
    {
        count = count + 1;
        amount = amount - 0.25;
        printf("amount left: %f\n", amount);
    }

    //second use dime if possible
    while (amount>=0.1 && amount<0.25)
    {
       count = count + 1;
       amount = amount - 0.1;
       printf("amount left: %f\n", amount);
    }

    //third use nickle if possible
    while (amount>=0.05 && amount<0.1)
    {
        count = count + 1;
        amount = amount - 0.05;
        printf("amount left: %f\n", amount);
    }

    //forth use penny if possible
    while (amount>0.009)
    {
        count = count + 1;
        amount = amount - 0.01;
        printf("amount left: %f\n", amount);
    }

    printf("Number of coins used: %i\n", count);
    printf("Amount: %f\n", amount);
}

