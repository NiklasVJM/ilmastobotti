#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random
from twython import Twython


CONSUMER_KEY='XXXX'
CONSUMER_SECRET='XXXXXXXX'
ACCESS_TOKEN='XXXXXXXXXXXXXX'
ACCESS_SECRET='XXXXXXXXXX'

def varoitukset():
	varoitus = open('varoitukset_2.txt','r')
	varoitus_data = varoitus.read().splitlines()
	varoitus_str = random.choice(varoitus_data)
	varoitus.close()
	return varoitus_str

def alueet():
	alue = open('alueet_2.txt','r')
	alue_data = alue.read().splitlines()
	alue_str = random.choice(alue_data)
	alue.close()
	return alue_str

def paikat_genetiivi():
	paikat = open('paikat_n_2.txt','r')
	paikat_data = paikat.read().splitlines()
	paikat_str = random.choice(paikat_data)
	paikat.close()
	return paikat_str

def paikat_elatiivi():
	paikat = open('paikat_lla_2.txt','r')
	paikat_data = paikat.read().splitlines()
	paikat_str = random.choice(paikat_data)
	paikat.close()
	return paikat_str

def aineet():
	aineet = open('aineet_2.txt','r')
	aineet_data = aineet.read().splitlines()
	aineet_str = random.choice(aineet_data)
	aineet.close()
	return aineet_str

def sataa():
	sataa = open('sataa_2.txt','r')
	sataa_data = sataa.read().splitlines()
	sataa_str = random.choice(sataa_data)
	sataa.close()
	return sataa_str

def skenaario_1():
	twiitti= (varoitukset() + '\n' +  alueet() + " " + paikat_elatiivi() + " " + sataa() + " " + aineet() + " ja lämpötila pysyttelee " + str(random.randint(-40,50)) + " asteen tuntumassa.")
	api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_SECRET)
	api.update_status(status=twiitti)
	print (twiitti)

def skenaario_2():
	twiitti = (alueet() + " " + paikat_elatiivi() + " lämpötila vaihtelee " + str(random.randint(-40,50)) + " ja " + str(random.randint(-40,50)) + " asteen välillä. " + "Alueella on " + str(random.randint(0,100)) + "% mahdollisuus, että taivaalta voi sataa " + aineet() + ".")
	api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_SECRET)
	api.update_status(status=twiitti)
	print (twiitti)

def skenaario_3():
	twiitti= (varoitukset() + '\n' + aineet() + ", " + aineet() + " ja " + aineet() + " on odotettavissa " + paikat_genetiivi() + " " + paikat_elatiivi() + ".")
	api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_SECRET)
	api.update_status(status=twiitti)
	print (twiitti)

def skenaario_4():
	twiitti= ("Koko Suomessa on odotettavissa seuraavien " + str(random.randint(2,12)) + " tunnin sisällä mm. " + aineet() + " " + paikat_elatiivi() + ", " + aineet() + " " + paikat_elatiivi() + " sekä " + aineet() + " " + paikat_elatiivi() + ".")
	api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_SECRET)
	api.update_status(status=twiitti)
	print (twiitti)

#Valitaan satunnainen luku 1-4, jonka perusteella twiitataan skenaario.
number = random.randint(1,4)

if number == 1:
	skenaario_1()
elif number == 2:
	skenaario_2()
elif number == 3:
	skenaario_3()
elif number == 4:
	skenaario_4()







