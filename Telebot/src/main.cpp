#include <thread>
#include <mutex>
#include <signal.h>

#include "MyBot.hpp"

using namespace std;

static mutex mtx;
static bool global_running;

static void stop_thread()
{
    bool thread_running = true;

    signal(SIGINT, [](int s)
    {
        mtx.lock();
        global_running = false;
        mtx.unlock();
    });

    while (thread_running == true)
    {
        this_thread::sleep_for(chrono::milliseconds(10));
    }
}

static void bot_thread()
{
    bool thread_running = true;
    MyBot *bot          = new MyBot();

    bot->run();

    while (thread_running == true)
    {
        mtx.lock();
        if (global_running == false)
        {
            mtx.unlock();
            thread_running = false;
            break;
        }
        mtx.unlock();
    }

    bot->stop();
    delete bot;
}

int main(int argc, char* argv[])
{
    global_running = true;

    thread bot(bot_thread);
    thread stop(stop_thread);

    bot.join();
    stop.join();

    return 0;
}