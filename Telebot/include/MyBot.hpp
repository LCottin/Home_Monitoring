#ifndef __MYBOT_HPP__
#define __MYBOT_HPP__

#include <string>
#include <tgbot/tgbot.h>
#include <iostream>

#include "Database.hpp"
#include "CONFIGS.hpp"
#include "Common.hpp"

using namespace std;
using namespace TgBot;

class MyBot
{
    private:
        string    _Token;
        Bot      *_Bot;
        Database *_Db;
        int       _ChatID;

        void init();

    public:
        MyBot();

        void sendWelcome(Message::Ptr message) const;

        void sendMessage(string message) const;

        void sendLastData(Message::Ptr message) const;

        void sendStop(Message::Ptr message) const;

        void run();

        ~MyBot();
};

#endif