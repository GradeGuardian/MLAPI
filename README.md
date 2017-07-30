# MLAPI

Send HTTP POST Request to http://165.227.66.86/

Send JSON with the following params:

Possible Answers for each question found here
https://www.kaggle.com/uciml/student-alcohol-consumption

###Note: Instead of Yes or No, I used 1 for yes and 0 for no

###Note: all values are Strings that are case sensitive

	"sex":M or F,
	"age":Interger cast to string,
	"famsize": LE3 or GT3,
	"Pstatus": A or T,
	"Medu" : Interger cast to string,
	"Fedu" : Interger cast to string,
	"Mjob" : teacher, health, services, at_home or other,
	"Fjob" : teacher, health, services, at_home or other,
	"reason": home, reputation, course or other,
	"guardian": mother, father or other,
	"traveltime": Interger cast to string,
	"studytime": Interger cast to string,
	"failures": Interger cast to string,
	"schoolsup": Interger cast to string,
	"famsup": Interger cast to string,
	"paid": Interger cast to string,
	"activities":Interger cast to string,
	"nursery":Interger cast to string,
	"higher":Interger cast to string,
	"internet": Interger cast to string,
	"romantic":Interger cast to string,
	"famrel": Interger cast to string,
	"freetime": Interger cast to string,
	"goout": Interger cast to string,
	"Dalc": Interger cast to string,
	"Walc": Interger cast to string,
	"health": Interger cast to string,
	"absences": Interger cast to string,
	"G1": Interger cast to string,
	"G2": "Interger cast to string

Example request

```
{
	"sex":"F",
	"age":"15",
	"famsize":"GT3",
	"Pstatus": "T",
	"Medu" : "4",
	"Fedu" : "3",
	"Mjob" :"services",
	"Fjob" :"other",
	"reason": "reputation",
	"guardian": "mother",
	"traveltime": "1",
	"studytime": "1",
	"failures": "0",
	"schoolsup": "0",
	"famsup": "0",
	"paid": "1",
	"activities": "1",
	"nursery":"1",
	"higher":"1",
	"internet": "1",
	"romantic":"0",
	"famrel": "4",
	"freetime": "5",
	"goout": "5",
	"Dalc": "1",
	"Walc": "3",
	"health": "1",
	"absences": "4",
	"G1": "16",
	"G2": "17"
}
```
