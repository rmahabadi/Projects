// This program is a guessing game where the user enters in a number
// if the user enters a wrong number more than 5 times, the program gives hints
// When the user exits, it tells them how many games they played, won and their winning percentage

#include <iostream>
#include <stdlib.h>
#include <time.h>

const int MIN_NUMBER = 1;
const int MAX_NUMBER = 100;
const int EXIT_VALUE = -1;
const int MAX_GAMES = 256;
 
using namespace std;

int main(int, char**) {
    srand(time(NULL));
    int guess,prev_guess,current_guess,gamesplayed,gameswon;
    int losing=0;
    char play_again;
    int counter=1;
          for (gamesplayed=1;play_again!='n';++gamesplayed){
            int random_number = rand() % MAX_NUMBER + 1;
            int duplicate_numbers[99] = {};
            for (int x=0;random_number!=guess||x<99;++x){
                cout << "Enter a number between 1 and 100 (-1 to give up): ";
                cin >> guess;
                for(int j=0; j<99; j++) {
                    //cout << "duplicate_number[j] = " << duplicate_numbers[j] << endl;
                    if (duplicate_numbers[j] == guess){
                        cout << "This is a duplicate number, guess again." << endl;
                        counter--;
                    } 
                }
                duplicate_numbers[x] = guess;
                //cout << "duplicate_number[x] = " << duplicate_numbers[x] << endl;
                counter++;
   
            if (random_number!=guess&& guess!=EXIT_VALUE){
                cout << "wrong..." << endl;
            }
            if (guess>MAX_NUMBER){
              cout << guess << " is too big..." << endl;
            }
            if (guess==EXIT_VALUE){
              cout << "*** QUITTER ***" << endl;
              losing++;
              break;
            }
            if (guess <MIN_NUMBER){
                cout << guess << " is too small..." << endl;
            }
            if (x>=5){
                if (guess<random_number){
                  cout << "higher..." << endl;
                }
                if (guess>random_number){
                    cout << "lower..." << endl;
                    }
            }
            if (guess==random_number){
              cout << " *** GOT IT *** " << endl;
              break;
            }
            }
            cout << " Do you want to play again? (y/n)";
            cin >> play_again;
            cout << endl;
            if (gamesplayed==MAX_GAMES){
                break;
            }
        }
        gameswon=gamesplayed-losing;
        cout << "Thanks for playing the CSC100 guessing game." << endl;
        cout << "You played " << gamesplayed << " games and won " <<
        gameswon << " of them" << endl;
        cout << "Your winning percentage is " << ((float)(gameswon) / (float)(gamesplayed)) *100 << "%" << endl;
}
