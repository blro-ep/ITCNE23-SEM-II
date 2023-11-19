# ITCNE23-SEM-II

## Einleitung
Der Focus der Semesterarbeit liegt beim Knowhowaufbau CI/CD Pipeline mit AWS.
Es soll eine CI/CD Pipeline Aufgebaut werden, welche mittels Git eine Lambda Function updaten kann. Mittels Git PUSH soll AWS CodeBuild angestossen werden, welches das Deployment der Lambda Function übernimmt. 
Die Function soll als REST API via Web erreichbar sein.

## Projektmanagement
Als Projektmanagementmethode wird Kanban eingesetzt. Ich habe mich für diese agile Methode entschieden, um die Arbeitsprozesse zu visualisieren und den Arbeitsfluss zu steuern. 
Die Semsterarbeit soll in mehreren Iteration (Sprints) aufgeteilt werden um den Vorschritt zu tracken.

Das gesamte Projektmangement wird in einem Github Project abgewickelt ([ITCNE23-SEM-II
](https://github.com/users/blro-ep/projects/6)).

### Kanbanboard
Die Visualisierung erfolgt in einem Kanbanboard. Daruch soll der Arbeitsfluss optimiert und die Effizeinz geteigert werden. Engpässe können damit identifiziert und entprechende Manssnahmen abgeleitet werden.

#### Status
Das Kanbanboard wir in 4 Spalten aufgeteilt.
- Todo
- In Progress
- Done
- Backlog

![Kanbanboard](picture/kanban_board.png)

#### Labels
Es werden folgende Labels verwendet um die Tasks nach Themen zu gruppieren
- Doku  --> Task für die Dokumentation
- IaC   --> Task für Infrastructure as Code
- FaaS  --> Task für Function as a Serivce


### Roadmap
Die Roadmap enthält Milestones, welche den Sprints entsprechen. Sämtliche Aufgaben werden einen Sprint zugeordnet.

![Roadmap](picture/roadmap.png)

| Datum | Sprint |
| --- | --- |
| 27.11.23 | Ergebnis 1. Sprint |
| 18.12.23 | Ergebnis 2. Sprint |
| 31.01.24 | Ergebnis 3. Sprint / Abgabe / Abnahem |

### Tasklist
Die Taskliste soll eine einfache möglichkeit bieten, um die Aufgaben nach Kategorien zu filtern.

Kategorien:
- Status
- Priority
- Milestones

![Taskliste](picture/tasklist.png)

### SEUSAG
#### Systemgrenze
![Roadmap](picture/systemgrenzen.png)

#### Einflussgrößen
![Einflussgrössen](picture/Einflussgroessen.png)

#### Unter- bzw. Teilsysteme 
![Unter-Teilsystem](picture/Unter-Teilsystem.png)

#### Schnittstellen
| Schnittstelle | <div style="width:175px">Element</div> | Beschreibung |
|---------------|---------|-------------|
| S1 | User / Git Repo | Der Code für die AWS Lambda Function wird in einem Git Repo verwaltet. |
| S2 | User / AWS Services | Das Deployment der AWS Ressourcen erfolgt via AWS CLI / AWS SDK. |
| S3 | Git / AWS | Das Deployment der Lambda Function erfolgt auf dem Git Repo. |

#### Analyse der Unter- bzw. Teilsysteme

##### AWS Provider
AWS wird verwendet, um eine FaaS zur Verfügung zu stellen, welche auf dem Service AWS Lambda aufgebaut wird.
Das Deploment soll von Github angestossen werden und mitteld CodeBuild automatisch erfolgen. 
Es ist zu prüfen, welche AWS Services für die Vorgehen zusätlich benötigt werden.

##### Github
Github wird für die Code Verwaltung der Lambda Function eingesetzt und soll dem automatischen Deplomymentprozess in AWS anstossen.
Der Code für die Function wird in einem Git Repo gehalten. 
Git Project wird eingesetzt um die Umsetzung in Tasks aufzuteilen und den Fortschritt zu tracken.

##### Local System
Der User erstellt und modifiziert den Code für die Lambda Function von seinem lokalen System in einem Github Repo.
Das Deployment der notwendigen AWS Komponenten soll soweit möglich via AWS CLI / SDK automatisiert werden. 

#### Gemeinsamkeiten
- Git
- Python
- AWS-Schnittstellen

### Ziele SMART
- Die nötigen AWS-Ressourcen für die Lambda Function sollen automatisiert erstellt werden können (z.B. AWS-CLI / AWS-SDK).
- Die Lambda Function soll mit einem Git PUSH Befehl aktualisiert werden können. Dies bedeutet, dass die Code Änderungen aus dem GitRepo auto. in die Lambda Function übernommen wird.
- Die Lambda Function soll mit der Programmiersprache Python umgesetzt werden.
- Mittels GET API Request soll die Function mindestens den Status Code 200 zurück geben.

### Testing

### Sprints
Das Ende von Sprint wird dokumentiert und der Stand des Kanbanboard grafisch festgehalten.

#### Sprint 1 - 27.11.23


#### Sprint 2 - 18.12.23


#### Sprint 3 - 31.01.24


## Local System
Als lokales System wir ein Ubuntu 22.04 verwendet. Von diesem System soll das Deployment der AWS Infrastruktur sowie die Verwatung des Function Code in Github erfolgen.

### Installation

- [Install the AWS SDK for Python](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)
- [Code examples for SDK for Python](https://docs.aws.amazon.com/code-library/latest/ug/python_3_code_examples.html)

```
pip install boto3[crt]

sudo apt install tox

sudo apt install npm (Node Package Manager)

https://deb.nodesource.com/
```

## IaC
### AWS Lambda Function erstellen
- [Lmabda AWS CLI](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-awscli.html)

### AWS Code Build Project erstellen

### AWS API Gateway erstellen

## CI / CD Pipeline

## FaaS

## Fazit
