#ifndef __MYBOT_HPP__
#define __MYBOT_HPP__

#include <string>
#include <tgbot/tgbot.h>
#include <iostream>

#include "Database.hpp"
#include "CONFIGS.hpp"

using namespace std;
using namespace TgBot;

class MyBot 
{
    private:
        string    _Token;
        Bot      *_Bot;
        Database *_Db;

        void init();

    public:
        MyBot();
        
        void sendWelcome(Message::Ptr message);

        void sendLastData(Message::Ptr message);

        void sendStop(Message::Ptr message);

        void run();

        ~MyBot();
};

#endif