// Copies a BMP file
// Received help from Stack Exchange and GitHub

#include <stdio.h>
#include <stdlib.h>

#include "bmp.h"

int main(int argc, char *argv[])
{

    // ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: copy infile outfile\n");
        return 1;
    }

    // Define how many times and remember filenames
    char *number = argv[1];
    char *infile = argv[2];
    char *outfile = argv[3];

    int n = atoi(number);

    // check to make sure that n is a positive integer less than or equal to 100
    if (n > 100 || n < 0)
    {
        fprintf(stderr, "n must be a positive integer less than or equal to 100\n");
        return 2;
    }

    // open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 3;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 4;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 5;
    }

    //Make outfile's BITMAPINFOHEADER and BITFILEHEADER
    BITMAPFILEHEADER outbf = bf;
    BITMAPINFOHEADER outbi = bi;

    // update width and height

        // resize width
        outbi.biWidth *= n;

        // resize height
        outbi.biHeight *= n;

    // determine padding for scanlines
    int originalpadding = (4 -(bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    int padding = (4-(outbi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    // resize image
    outbi.biSizeImage = abs(outbi.biHeight) * (outbi.biWidth * sizeof(RGBTRIPLE) + padding);

    // update file size
    outbf.bfSize = outbi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);

    // write outfile's BITMAPFILEHEADER
    fwrite(&outbf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&outbi, sizeof(BITMAPINFOHEADER), 1, outptr);


    // iterate over infile's scanlines
    for (int i = 0; i < abs(bi.biHeight); i++)
    {

        for (int j = 0; j < n; j++)
        {
            // set pointer to beginning of line
            fseek(inptr, 54 + (bi.biWidth * 3 + originalpadding) * i, SEEK_SET);

            // iterate over pixels in scanline
            for (int k = 0; k < bi.biWidth; k++)
            {
                // temporary storage
                RGBTRIPLE triple;

                // read RGB triple from infile
                fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

                // iterate each pixel n times
                for (int l = 0; l < n; l++)
                {
                    // write RGBTRIPLE to outfile
                    fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
                }

            }

            // then add it back to outfile
            for (int m = 0; m < padding; m++)
            {
                fputc(0x00, outptr);
            }
        }
    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}
