// GAME.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <windows.h>
using namespace std;

char pelaaja;
int progress = 0;
int valinta;
bool secret = false;

void clearcmd() {
	for (int i = 1; i <= 100; i++) {
		cout << "\n";
	}
}

void room1() {
	cout << "You walk out of the room and see two different paths. \nOne to the right and one to the left. \nWhich one do you choose?\n";
	cout << "##########################################################################" << endl;
	cout << "left [z] right [x] search for something else [c]\n";
	cin >> pelaaja;
	clearcmd();
	cout << "##########################################################################" << endl;
	switch (pelaaja) {
	case 'z':
		cout << "You can see a deadly chasm in front \nof you which looks possible to \njump over but is risky.\n";
		valinta = 1;
		break;
	case 'x':
		cout << "You can see a room with 2 keys in the middle \nof it, sign that says \"take only one\" and a exit.\n";
		valinta = 2;
		break;
	case 'c':
		cout << "You search the area closely and find a secret \nlever which opens a secrect room. Inside \nthe secrect room is plank.\n";
		valinta = 3;
	}
	if (valinta == 1 && secret == false) {
		cout << "##########################################################################" << endl;
		cout << "jump over [z] go back [x]\n";
		cin >> pelaaja;
		clearcmd();
		cout << "##########################################################################" << endl;
		if (pelaaja == 'z') {
			cout << "You jumped over succesfully but hurt \nyour ankle because you underestimated \nthe height of the jump.\n";
			cout << "##########################################################################" << endl;
		}
		else {
			valinta = 0;
			room1();
		}
	}
	if (valinta == 1 && secret == true) {
		cout << "##########################################################################" << endl;
		cout << "jump over [z] go back [x] use plank [c]\n";
		cin >> pelaaja;
		clearcmd();
		cout << "##########################################################################" << endl;
		if (pelaaja == 'z') {
			cout << "You jumped over succesfully but hurt \nyour ankle because you underestimated \nthe height of the jump.";
			cout << "##########################################################################" << endl;
		}
		else if (pelaaja == 'c') {
			cout << "You used the earlier accuired plank to cross the chasm safely.\n";
			cout << "##########################################################################" << endl;
			secret = false;
		}
		else {
			valinta = 0;
			room1();
		}
	}
	if (valinta == 2) {
		cout << "##########################################################################" << endl;
		cout << "take one and open the door [z] take both and open the door [x] go back [c]\n";
		cin >> pelaaja;
		clearcmd();
		cout << "##########################################################################" << endl;
		if (pelaaja == 'z') {
			cout << "You took one key and opened the door succesfully\n";
			cout << "##########################################################################" << endl;
		}
		else if (pelaaja == 'x') {
			cout << "You took both of the keys and opened the door succesfully.\n";
			cout << "##########################################################################" << endl;
		}
		else {
			valinta = 0;
			room1();
		}
	}
	if (valinta == 3) {
		cout << "##########################################################################" << endl;
		cout << "take the plank with you and go back [z] go back without it [x]\n";
		cin >> pelaaja;
		clearcmd();
		cout << "##########################################################################" << endl;
		if (pelaaja == 'z') {
			cout << "You take the plank with you and\n";
			secret = true;
			valinta = 0;
			room1();
		}
		else {
			valinta = 0;
			room1();
		}
	}
}
int main()
{
	clearcmd();
	cout << "##########################################################################" << endl;
	cout << "You wake up in a empty room with one exit.\n";
	room1();
}
