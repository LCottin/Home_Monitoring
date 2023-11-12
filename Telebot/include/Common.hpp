#ifndef __COMMON_HPP__
#define __COMMON_HPP__

typedef struct 
{
    unsigned id;
    unsigned time;
    float temperature;
    float humidity;
    float pressure;
    float altitude;
    float gas_resistance;
} data_t;

#endif