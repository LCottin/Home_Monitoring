#ifndef __MYBOT_HPP__
#define __MYBOT_HPP__

#include <string>
#include <tgbot/tgbot.h>

using namespace std;
using namespace TgBot;

class MyBot 
{
    private:
        string _Token;
        Bot *_Bot;

        void init();

    public:
        MyBot(const string& token);
        
        void sendWelcome(Message::Ptr message);

        void sendLastData(Message::Ptr message);

        void sendStop(Message::Ptr message);

        void run();

        ~MyBot();
};

#endif