#include "MyBot.hpp"

MyBot::MyBot() 
{
    _Token = TG_TOKEN;
    _Bot   = new Bot(_Token);
    _Db    = new Database(DB_HOST, DB_USER, DB_PWD, DB_NAME);

    init();
}

/**
 * @brief Initialize the bot with the commands
 */
void MyBot::init()
{
    _Bot->getEvents().onCommand("start", [this](Message::Ptr message) 
    {
        sendWelcome(message);
    });

    _Bot->getEvents().onCommand("help", [this](Message::Ptr message) 
    {
        sendWelcome(message);
    });

    _Bot->getEvents().onCommand("last", [this](Message::Ptr message) 
    {
        sendLastData(message);
    });

    _Bot->getEvents().onCommand("stop", [this](Message::Ptr message) 
    {
        sendStop(message);
    });
}


void MyBot::sendWelcome(Message::Ptr message) 
{
    _Bot->getApi().sendMessage(message->chat->id, "Welcome!");
}

void MyBot::sendLastData(Message::Ptr message) 
{
    _Bot->getApi().sendMessage(message->chat->id, "Last data: ...");
    _Db->getLastData("temperature");
}

void MyBot::sendStop(Message::Ptr message) 
{
    _Bot->getApi().sendMessage(message->chat->id, "Bot stopped");
    // Implement logic to stop the bot here.
}

void MyBot::run() 
{
    try {
        _Bot->getApi().deleteWebhook();
        TgLongPoll longPoll(*_Bot);
        while (true) {
            longPoll.start();
        }
    } catch (std::exception& e) {
        printf("error: %s\n", e.what());
    }
}

MyBot::~MyBot() 
{
    delete _Bot;
}