#include "Database.hpp"

Database::Database(const string& host, const string& user, const string& password, const string& dbName)
{
    _Host     = host;
    _User     = user;
    _Password = password;
    _DbName   = dbName;

    mysql::MySQL_Driver *driver = mysql::get_mysql_driver_instance();
    _Conn = driver->connect(_Host, _User, _Password);
    _Conn->setSchema(_DbName);
}

void Database::getLastData(const string& dataType) 
{
    getData(dataType, 1);
}

void Database::getData(const string& dataType, const int number)
{
    string query;
    if ((dataType == "all") || (dataType == "ALL"))
    {
        query = "SELECT * FROM LivingRoom ORDER BY id DESC LIMIT " + to_string(number);
    }
    else
    {
        query = "SELECT time, " + dataType + " FROM LivingRoom ORDER BY id DESC LIMIT " + to_string(number);
    }

    Statement* stmt = _Conn->createStatement();
    ResultSet* res = stmt->executeQuery(query);
    while (res->next()) 
    {
        cout << "time: " << res->getString("time") << endl;
        cout << dataType << ": " << res->getString(dataType) << endl;
    }
    delete res;
    delete stmt;
}

Database::~Database()
{
    _Conn->close();
    delete _Conn;
}