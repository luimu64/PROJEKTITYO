#include <iostream>
#include <string>
#include <tchar.h>
#include <clocale>
#include <Windows.h>

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
	cout << "K�velet ulos huoneesta ja n�et kaksi reitti�. \nYksi oikealle ja yksi vasemmalle. \nKumpaan suuntaan menet?\n";
	cout << "vasemmalle [z] oikealle [x] katsele viel� ymp�rillesi [c]\n";
	cin >> pelaaja;
	clearcmd();
	switch (pelaaja) {
	case 'z':
		cout << "N�et syv�n kuilun edess�si, \njoka vaikuttaa mahdolliselta hyp�t� yli, \nmutta vaaralliselta.\n";
		valinta = 1;
		break;
	case 'x':
		cout << "N�et huoneen jonka keskell� on kaksi avainta, \nkyltti joka sanoo\"ota vain yksi\" ja ulosk�ynti.\n";
		valinta = 2;
		break;
	case 'c':
		cout << "Katselet ymp�rillesi ja huomaat \nvivun joka avaa salaisen huoneen. \nHuoneen keskell� on lauta.\n";
		valinta = 3;
	}
	if (valinta == 1 && secret == false) {
		cout << "hypp�� yli [z] mene takaisin [x]\n";
		cin >> pelaaja;
		clearcmd();
		if (pelaaja == 'z') {
			cout << "Hypp�sit kuilun yli onnistuneesti, mutta \nsatutit jalkasi koska aliarvioit \nhypyn korkeuden.\n";
		}
		else {
			valinta = 0;
			room1();
		}
	}
	if (valinta == 1 && secret == true) {
		cout << "hypp�� yli [z] mene takaisin [x] k�yt� lautaa ylitykseen [c]\n";
		cin >> pelaaja;
		clearcmd();
		if (pelaaja == 'z') {
			cout << "Hypp�sit kuilun yli onnistuneesti, mutta \nsatutit jalkasi koska aliarvioit \nhypyn korkeuden.";
		}
		else if (pelaaja == 'c') {
			cout << "K�ytit aikaisemmin l�yt�nytt� lankkua kuilun ylitykseen.\n";
			secret = false;
		}
		else {
			valinta = 0;
			room1();
		}
	}
	if (valinta == 2) {
		cout << "ota yksi ja avaa ovi [z] ota molemmat ja avaa ovi [x] mene takaisin [c]\n";
		cin >> pelaaja;
		clearcmd();
		if (pelaaja == 'z') {
			cout << "Otit yhden avaimen ja avasit oven.\n";
		}
		else if (pelaaja == 'x') {
			cout << "Otit molemmat avaimet ja avasit oven.\n";
		}
		else {
			valinta = 0;
			room1();
		}
	}
	if (valinta == 3) {
		cout << "ota lankku mukaan ja mene takaisin [z] mene takaisin ilman sit� [x]\n";
		cin >> pelaaja;
		clearcmd();
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
	cout << "Her��t tyhj�st� huoneesta jossa on yksi ulosk�ynti.\n";
	room1();
}
