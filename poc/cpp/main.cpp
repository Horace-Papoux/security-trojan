// #include "pch.h"
#include <Windows.h>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <dpapi.h>
 
int main(int argc, char *argv[])
{
    DATA_BLOB DataOut;
    DATA_BLOB DataVerify;
    LPWSTR pDescrOut =  NULL;
    //--------------------------------------------------------------------
    // The buffer DataOut would be created using the CryptProtectData
    // function. If may have been read in from a file.

    //--------------------------------------------------------------------
    //   Begin unprotect phase.

    if (CryptUnprotectData(
            &DataOut,
            &pDescrOut,
            NULL,                 // Optional entropy
            NULL,                 // Reserved
            NULL,                 // Here, the optional 
                                // prompt structure is not
                                // used.
            0,
            &DataVerify))
    {
        printf("The decrypted data is: %s\n", DataVerify.pbData);
        printf("The description of the data was: %s\n",pDescrOut);
        LocalFree(DataVerify.pbData);
        LocalFree(pDescrOut);
    }
    else
    {
        printf("Decryption error!");
    }
}