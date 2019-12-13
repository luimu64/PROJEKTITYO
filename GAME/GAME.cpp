#include <windows.h>
#include <iostream>
#include <string>
#include <tchar.h>
#include <clocale>


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
	cout << "Kävelet ulos huoneesta ja näet kaksi reittiä. \nYksi oikealle ja yksi vasemmalle. \nKumpaan suuntaan menet?\n";
	cout << "##########################################################################" << endl;
	cout << "vasemmalle [z] oikealle [x] katsele vielä ympärillesi [c]\n";
	cin >> pelaaja;
	clearcmd();
	cout << "##########################################################################" << endl;
	switch (pelaaja) {
	case 'z':
		cout << "Näet syvän kuilun edessäsi, \njoka vaikuttaa mahdolliselta hypätä yli, \nmutta vaaralliselta.\n";
		valinta = 1;
		break;
	case 'x':
		cout << "Näet huoneen jonka keskellä on kaksi avainta, \nkyltti joka sanoo\"ota vain yksi\" ja uloskäynti.\n";
		valinta = 2;
		break;
	case 'c':
		cout << "Katselet ympärillesi ja huomaat \nvivun joka avaa salaisen huoneen. \nHuoneen keskellä on lauta.\n";
		valinta = 3;
	}
	if (valinta == 1 && secret == false) {
		cout << "##########################################################################" << endl;
		cout << "hyppää yli [z] mene takaisin [x]\n";
		cin >> pelaaja;
		clearcmd();
		cout << "##########################################################################" << endl;
		if (pelaaja == 'z') {
			cout << "Hyppäsit kuilun yli onnistuneesti, mutta \nsatutit jalkasi koska aliarvioit \nhypyn korkeuden.\n";
			cout << "##########################################################################" << endl;
		}
		else {
			valinta = 0;
			room1();
		}
	}
	if (valinta == 1 && secret == true) {
		cout << "##########################################################################" << endl;
		cout << "hyppää yli [z] mene takaisin [x] käytä lautaa ylitykseen [c]\n";
		cin >> pelaaja;
		clearcmd();
		cout << "##########################################################################" << endl;
		if (pelaaja == 'z') {
			cout << "Hyppäsit kuilun yli onnistuneesti, mutta \nsatutit jalkasi koska aliarvioit \nhypyn korkeuden.";
			cout << "##########################################################################" << endl;
		}
		else if (pelaaja == 'c') {
			cout << "Käytit aikaisemmin löytänyttä lankkua kuilun ylitykseen.\n";
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
		cout << "ota yksi ja avaa ovi [z] ota molemmat ja avaa ovi [x] mene takaisin [c]\n";
		cin >> pelaaja;
		clearcmd();
		cout << "##########################################################################" << endl;
		if (pelaaja == 'z') {
			cout << "Otit yhden avaimen ja avasit oven.\n";
			cout << "##########################################################################" << endl;
		}
		else if (pelaaja == 'x') {
			cout << "Otit molemmat avaimet ja avasit oven.\n";
			cout << "##########################################################################" << endl;
		}
		else {
			valinta = 0;
			room1();
		}
	}
	if (valinta == 3) {
		cout << "##########################################################################" << endl;
		cout << "ota lankku mukaan ja mene takaisin [z] mene takaisin ilman sitä [x]\n";
		cin >> pelaaja;
		clearcmd();
		cout << "##########################################################################" << endl;
		if (pelaaja == 'z') {
			cout << "Otat lankun mukaasi ja\n";
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
	setlocale(LC_ALL, "fi-FI");
	SetConsoleTitle(_T("DEMO"));
	clearcmd();
	cout << "##########################################################################" << endl;
	cout << "Heräät tyhjästä huoneesta jossa on yksi uloskäynti.\n";
	room1();
}
