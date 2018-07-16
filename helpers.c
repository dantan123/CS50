// Helper functions for music

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>
#include "helpers.h"

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    float numerator = fraction[0] - 48;
    float denominator = fraction[2] - 48;
    float result = numerator / denominator / 0.125;
    return result;
}

//Calculates frequency (in Hz) of a note
int frequency(string note)
{
    double octdif; //index difference between octave 4 and the passing octave in the note
    double hrz;    //frequency value
    double letdif; //index difference between letter A and the passing letter in the note
    char letter = note[0]; //letter of the note
    float base = 440.0; //frequency value of base case A4
    double term;
    double onesemi;
    double twosemi;

    hrz = base;

    //when the length of note is two(without accidentals)
    if (strlen(note) == 2)
    {
        char octave = note[1];

        //adjust when octave is not equal to 4
        if (octave != '4')
        {
            octdif = octave - 52.0;
            term = pow(2.0, octdif);
            hrz = round(base * term);
        }
    }

    // when the length of the note is three(with accidentals)
    else if (strlen(note) == 3)
    {
        char accidental = note[1];
        char octave = note[2];

        //adjust when octave is not equal to 4
        if (octave != '4')
        {
            octdif = octave - 52.0;
            term = pow(2.0, octdif);
            hrz = round(base * term);
        }

        //adjust for accidentals given the octave
        // use 1.0 for floating purpose
        onesemi = pow(2.0, 1.0 / 12.0);

        if (accidental == '#')
        {
            hrz = round(hrz * onesemi);
        }

        else if (accidental == 'b')
        {
            hrz = round(hrz / onesemi);
        }

    }

    //Adjust for letters assuming A is the current position

    //if letter is B, move two semitones up from A
    if (letter == 'B')
    {
        // use 1.0 for floating point purpose
        twosemi = pow(2.0, 1.0 / 6.0);
        hrz = round(hrz * twosemi);
    }

    //if letter is between C and E, move down relative to A
    else if (letter >= 'C' && letter <= 'E')
    {
        letdif = letter - 65.0 - 7.0;
        term = pow(2.0, (letdif * 2.0 + 1.0) / 12.0);
        hrz = round(hrz * term);
    }

    //if letter is between F and G, move down relative to B
    else if (letter >= 'F' && letter <= 'G')
    {
        letdif = letter - 65.0 - 7.0;
        term = pow(2.0, (letdif * 2.0) / 12.0);
        hrz = round(hrz * term);
    }

    return hrz;
}

// Determines whether a string represents a rest
bool is_rest(string s)
{
    if (s[0] == '\0')
    {
        return true;
    }
    else
    {
        return false;
    }
}

// citations: https://cs50.stackexchange.com/questions/29161/how-to-debug-pset3-music
// https://cs50.stackexchange.com/questions/29554/is-rest-and-duration-bugs-in-helpers-c-of-pset3-music
