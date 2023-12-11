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

#### Task Kategorien
- Status
- Priority
- Milestones

![Taskliste](picture/tasklist.png)

#### Task Status
Das Kanbanboard wir in 4 Spalten aufgeteilt.
- Todo
- In Progress
- Done
- Backlog

![Kanbanboard](picture/kanban_board.png)

#### Task Labels
Es werden folgende Labels verwendet um die Tasks nach Themen zu gruppieren
- Doku  --> Task für die Dokumentation
- IaC   --> Task für Infrastructure as Code
- FaaS  --> Task für Function as a Serivce
- Zert  --> Zertifizierung

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
Github wird für das Projektmanagent eingesetzt. Anhand von einem Github Project, wird die Semsterarbeit in Task aufgeteilt, welche innerhalb eines Sprint abgearbeitet werden.

Im Github Repository befindet sich der gesamte Code der Semserarbeit.
Diese Repository wird ebenfalls verwendet, um die Lambda Function mittels git Push zu aktualisieren.

[ITCNE23-SEM-II]{https://github.com/blro-ep/ITCNE23-SEM-II#project-management}

##### Entwicklungsumgebung
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.3 LTS
Release:	    22.04
Codename:	    jammy

#### Gemeinsamkeiten
- Git
- Python
- AWS-Schnittstellen

### Ziele SMART
- Die nötigen AWS-Ressourcen für die Lambda Function sollen automatisiert erstellt werden können (z.B. AWS-CLI / AWS-SDK).
- Die Lambda Function soll mit einem Git PUSH Befehl aktualisiert werden können. Dies bedeutet, dass die Code Änderungen aus dem GitRepo auto. in die Lambda Function übernommen wird.
- Die Lambda Function soll mit der Programmiersprache Python umgesetzt werden.
- Mittels GET API Request soll die Function mindestens den Status Code 200 zurück geben.

### Sprints
Am Ende eines Sprints erfolgt eine Reflektion, wobei der Status der Taskliste grafisch festgehalten wird.

#### Sprint 1 - 27.11.23
![Sprint 1](./picture/sprint-1.png)

##### Reflektion
Die von GitHub bereitgestellten Tools für das Projektmanagement erweisen sich als äußerst effektiv. Die einfache Erstellung von Kanban-Boards, Roadmaps und Aufgabenlisten ermöglicht einen klaren Überblick über den Projektstatus.

Die Projektdokumentation ist in einem Readme festgehalten. Die bewusste Entscheidung, auf die manuelle Erstellung eines Inhaltsverzeichnisses zu verzichten, beruht darauf, dass GitHub standardmäßig diese Funktion bereitstellt.

Die Erstellung von Rollen mithilfe der AWS CLI verläuft reibungslos und bildet die Grundlage für die automatisierte Erstellung der Lambda-Funktion. Die Unterscheidung, ob eine Rolle nicht existiert oder die Abfrage ein Problem aufweist, gestaltete sich aufwändiger als ursprünglich angenommen.

Die Automatisierung mittels AWS CLI wird weiterhin beibehalten.

#### Sprint 2 - 18.12.23

Die Zertifizierung zum AWS Certified Cloud Practitioner hat mehr Zeit in Anspruch genommen als geplant.
Nachdem der erste Zertifizerungsversuche gescheiter war, habe ich mich mit folgenden Udemy Kursen auf die Prüfung vorbereitet [Ultimate AWS Certified Cloud Practitioner CLF-C02](https://www.udemy.com/share/103aFP3@TVzIE-KAghw3WT8BwYR3Eeg8C2WlORvf5_H3--T_a0D-fd6zdpe-7h2Lqm8TlU_vlw==/) / [6 Practice Exams | AWS Certified Cloud Practitioner CLF-C02](https://www.udemy.com/share/103e7s3@dO3_bmtPGRwYUTRlrmP7w7rLxmDDnp7NST5OVyaZiPfK12O_qLlovBH81VjxB8tEdQ==/).
Bei den Übungen hatte ich dann bemerkt, dass ich vielfach bei den selben Themen immer wieder Probleme hatte. Somit habe mir mittels [Anki](https://apps.ankiweb.net/) eine quelloffene Lernkartei-Software installerit und diese Punkte so zusätliche gelernt. 
Am 05.12.2023 konnte ich dann die Zertifizierung erfolgreich abschliessen.
[AWS Certified Cloud Practitioner certificate](./picture/AWS%20Certified%20Cloud%20Practitioner%20certificate.png)

Nach der Einarbeitung in die AWS SDK habe ich mich entschieden, sämtliche automatisierungen mittels boto3 (Python) abzuwickeln. Somit habe ich die bestehenden AWS CLI Bash Scripts aus dem Sprint 1 auch gleich umgeschrieben. 
Die Automatisierung via Boto3 hat sich jedoch aufwändiger herausgestellt, als erwartet.
So waren die Abhängigkeiten zwischen LambdaFunction, Roles, Policy, CodeBuild nicht einfach zu verstehen.
Den grössten Aufwand hatte ich mit der automatisierung von CodeBuild. Anhand der Dokumentation war mir nicht klar, welche Werte zwingende notwending sind und wie diese abgefüllt werden. Was mir geholfen hat, war das erstellen via Gui und einen anschliessender Export in ein json File.
Dass der Webhook seperat erstellt werden muss, war mir ebenfalls nicht klar und hat mich viel Zeit gekostest.

Dieser Sprint war sehr lehrreich in Bezug auf das Deployment mittels CodeBuild und Github.





#### Sprint 3 - 31.01.24




## Installation

### AWS CLI
Für das automatisierte Deployment wurde die AWS CLI gemäss folgender Anleitung installiert [Install or update the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#cliv2-linux-install).

### Boto3
Um das Deployment mittels Python zu automatisieren, habe ich Boto3 anhand von foldender AWS Dokumentation installiert [boto3.amazonaws.com - quickstart](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html).

#### Dokumentation
Folgende AWS Dokumentationen liefert gute [Code examples for SDK for Python](https://docs.aws.amazon.com/code-library/latest/ug/python_3_code_examples.html). Des weitern sind auch interessante Informationen unter [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.36/reference/services/index.html) zu finden.


#### AWS Komponenten

##### Role


###### Policy


##### Function


##### CodeBuild


## Infrastructure as code
### AWS Lambda Function erstellen
- [Lmabda AWS CLI](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-awscli.html)
- [python_3_lambda_code_examples](https://docs.aws.amazon.com/code-library/latest/ug/python_3_lambda_code_examples.html)

### AWS Code Build Project erstellen
- [create-project-cli](https://docs.aws.amazon.com/codebuild/latest/userguide/create-project-cli.html)

### AWS API Gateway erstellen

## CI / CD Pipeline

## FaaS

## Testing

## Fazit
