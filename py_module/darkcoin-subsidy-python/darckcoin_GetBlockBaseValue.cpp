#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <stdio.h>
#include <math.h> 

static const int64_t COIN = 100000000;

int64_t static GetBlockBaseValue(int nBits, int nHeight)
{
    int nShift = (nBits >> 24) & 0xff;

    double dDiff =
        (double)0x0000ffff / (double)(nBits & 0x00ffffff);

    /* fixed bug caused diff to not be correctly calculated */
    if(nHeight > 4500) {
        while (nShift < 29)
        {
            dDiff *= 256.0;
            nShift++;
        }
        while (nShift > 29)
        {
            dDiff /= 256.0;
            nShift--;
        }
    }

    int64_t nSubsidy = 0;
    if(nHeight >= 5465) {
        if((nHeight >= 17000 && dDiff > 75) || nHeight >= 24000) { // GPU/ASIC difficulty calc
            // 2222222/(((x+2600)/9)^2)
            nSubsidy = (2222222.0 / (pow((dDiff+2600.0)/9.0,2.0)));
            if (nSubsidy > 25) nSubsidy = 25;
            if (nSubsidy < 5) nSubsidy = 5;
        } else { // CPU mining calc
            nSubsidy = (11111.0 / (pow((dDiff+51.0)/6.0,2.0)));
            if (nSubsidy > 500) nSubsidy = 500;
            if (nSubsidy < 25) nSubsidy = 25;
        }
    } else {
        nSubsidy = (1111.0 / (pow((dDiff+1.0),2.0)));
        if (nSubsidy > 500) nSubsidy = 500;
        if (nSubsidy < 1) nSubsidy = 1;
    }

    //printf("nBits %u height %u diff %4.2f reward %i \n", nBits, nHeight, dDiff, nSubsidy);

    nSubsidy *= COIN;

    return nSubsidy ;
}

#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
using namespace boost::python;
 
BOOST_PYTHON_MODULE(darkcoin_subsidy)
{
    def("GetBlockBaseValue", GetBlockBaseValue);
}

