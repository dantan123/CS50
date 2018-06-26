#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

//Get key from command line argument

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Nothing");
        return 1;
    }

    //convert string to int
    int k = atoi(argv[1]);

    //ask the user for plaintext
    string p = get_string("Provide a sentence: ");

    //check whether k is postive
    if (k<0)
    {
        printf("Nothing");
        return 1;
    }

    else
    {

      //print string
      printf("ciphertext: ");

      for (int i = 0, n = strlen(p); i<n; i++)
      {

          //if the letter is capitalized
          if (isupper(p[i]))
          {
              //convert to alphabetical index
              int c = (p[i]-65+k)%26;

              //convert back to ASCII index
              int d = 65+c;
              printf("%c", d);
          }

          //if the letter is lowercased
          else if(islower(p[i]))
          {
              //convert from ASCII to alphabetical index
              int c = (p[i]-97+k)%26;

              //convert back to ASCII index
              int d = 97+c;
              printf("%c", d);
          }

          //otherwise
          else
          {
              printf("%c",p[i]);
          }

      }
    printf("\n");
    return 0;

    }

}