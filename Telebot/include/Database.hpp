#ifndef __DATABASE_HPP__
#define __DATABASE_HPP__

#include <string>
#include <mysql_connection.h>
#include <mysql_driver.h>
#include <cppconn/driver.h>
#include <cppconn/exception.h>
#include <cppconn/prepared_statement.h>
#include <iostream>
#include <string>
#include <memory>

#include "Common.hpp"

using namespace std;
using namespace sql;

class Database
{
    private:
        string _Host;
        string _User;
        string _Password;
        string _DbName;
        Connection *_Conn;

    public:
        Database(const string& host, const string& user, const string& password, const string& dbName);

        void getData(const string& dataType, data_t *data, const int number = 1);
        void getLastData(const string& dataType, data_t *data);
        
        ~Database();
};

#endif
