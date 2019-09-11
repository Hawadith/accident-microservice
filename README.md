# accident-microservice
1. table Accident
```SQL
CREATE TABLE Accident (AccidentID INT NOT NULL AUTO_INCREMENT, ReportType varchar (255) NOT NULL, Location vahrchar(255) NOT NULL,Dateandtime DATETIME NOT NULL, PRIMARY KEY (AccidentID))
```

2. table Accidentreport
```SQL
CREATE TABLE Accidentreport (AccidentID INT, FOREIGN KEY (AccidentID) REFERENCES Accident (AccidentID), PLate_num INT NOT NULL)
```

3. table Fineid
```SQL
CREATE TABLE Fineid (FineID INT NOT NULL AUTO_INCREMENT, Fee INT, AccidentID INT, FOREIGN KEY (AccidentID) REFERENCES Accident (AccidentID), PRIMARY KEY (FineID) )
```