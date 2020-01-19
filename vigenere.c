#include <stdio.h>
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

    // Define string k (a character array)
    string k = argv[1];

    // Check if string contains non-alphabetical character
    for (int i = 0; i < strlen(k); i++)
    {
        if (k[i] < 65 || (k[i] > 90 && k[i] < 97) || k[i] > 122)
        {
            fprintf(stderr, "The key contains non-alphabetical characters\n");
            return 1;
        }
    }

    //ask the user for plaintext
    string p = get_string("Provide a sentence: ");

    //print string
    printf("ciphertext: ");

    // parallel loops;  increment at the same time
    int j = 0;

    for (int i = 0; i < strlen(p); i++)
    {
        // if p[i] is an alphabet
        if ( (p[i] >= 65 && p[i] <= 90) || (k[i] >= 97 && k[i] <= 122) )
        {
            // ith key
            char ikey = k[j];

            // two cases if the ith key is capitalized, then convert it to lowercase equivalent
            // if uppercase
            int knum;

            if (ikey >= 65 && ikey <= 90)
            {
                // convert to alphabeical indices
                knum = ikey - 65;
            }

            else
            {
                // convert to alphabetical indices
                knum = ikey - 97;
            }

            //now the plaintext
            //if the letter is capitalized
            if (isupper(p[i]))
            {
                //convert plaintext from hexadeciaml indices to alphabetical indices
                int c = (p[i]  - 65 + knum) % 26;

                //convert back to ASCII indices
                int d = 65 + c;
                printf("%c", d);
            }

            //if the letter is lowercased
            else if(islower(p[i]))
            {
                //convert from ASCII to alphabetical index
                int c = (p[i] - 97 + knum) % 26;

                //convert back to ASCII index
                int d = 97 + c;
                printf("%c", d);
            }

            j = j + 1;

            if (j == strlen(k))
            {
                j = 0;
            }

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
