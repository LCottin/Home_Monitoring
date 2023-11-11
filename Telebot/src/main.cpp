#include "MyBot.hpp"

int main(int argc, char* argv[])
{
    if(argc != 2)
    {
        cout << "Usage: " << argv[0] << " <token>" << endl;
        return -1;
    }

    MyBot bot(argv[1]);
    bot.run();

    return 0;
}