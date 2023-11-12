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

void Database::getLastData(const string &dataType, data_t *data) 
{
    getData(dataType, data, 1);
}

void Database::getData(const string &dataType, data_t *data, const int number)
{
    string query;
    Statement* stmt;
    ResultSet* res;

    stmt = _Conn->createStatement();

    if ((dataType == "all") || (dataType == "ALL"))
    {
        query = "SELECT * FROM LivingRoom ORDER BY id DESC LIMIT " + to_string(number);
    }
    else
    {
        query = "SELECT time, " + dataType + " FROM LivingRoom ORDER BY id DESC LIMIT " + to_string(number);
    }

    res = stmt->executeQuery(query);

    while (res->next()) 
    {
        data->time           = stoi(res->getString("time"));
        data->temperature    = ((dataType == "temperature")    || (dataType == "all")) ? stof(res->getString("temperature")) : 0.0f;
        data->humidity       = ((dataType == "humidity")       || (dataType == "all")) ? stof(res->getString("humidity"))    : 0.0f;
        data->pressure       = ((dataType == "pressure")       || (dataType == "all")) ? stof(res->getString("pressure"))    : 0.0f;
        data->altitude       = ((dataType == "altitude")       || (dataType == "all")) ? stof(res->getString("altitude"))    : 0.0f;
        data->gas_resistance = ((dataType == "gas_resistance") || (dataType == "all")) ? stof(res->getString("gas_resistance")) : 0.0f;
    }

    delete res;
    delete stmt;
}

Database::~Database()
{
    _Conn->close();
    delete _Conn;
}