# ITCNE23-SEM-II

## Einleitung
Die zentrale Ausrichtung der Semesterarbeit konzentriert sich auf den Aufbau von Know-how im Bereich der Continuous Integration/Continuous Deployment (CI/CD) Pipeline unter Verwendung von AWS (Amazon Web Services). Das Ziel besteht darin, eine effiziente CI/CD-Pipeline zu erstellen, die in der Lage ist, eine Lambda-Funktion mithilfe von Git-Operationen zu aktualisieren. Der gesamte Prozess wird durch einen Git-PUSH ausgelöst, der wiederum AWS CodeBuild in Gang setzt. AWS CodeBuild übernimmt dabei das Deployment der aktualisierten Lambda-Funktion.

Die Lambda-Funktion, die Gegenstand dieser Pipeline ist, soll als REST API über das Web zugänglich sein. Dies bedeutet, dass die Funktionalität der Lambda-Funktion über HTTP-Anfragen erreichbar sein wird.

Der gesamte Ablauf beginnt mit Änderungen im Git-Repository, die durch einen Git-PUSH ausgelöst werden. Dieses Ereignis dient als Auslöser für AWS CodeBuild, das den Build-Prozess initiiert und sicherstellt, dass alle erforderlichen Abhängigkeiten und Ressourcen korrekt verarbeitet werden. Nach einem erfolgreichen Build übernimmt AWS CodeBuild das Deployment der Lambda-Funktion in der AWS-Infrastruktur.

Um sicherzustellen, dass die Lambda-Funktion als REST API über das Web zugänglich ist, wird das AWS API Gateway eingesetzt. Dies umfasst die Konfiguration von Endpunkten sowie die Implementierung von Sicherheitsmaßnahmen, um eine nahtlose und sichere Kommunikation mit der Lambda-Funktion zu gewährleisten. Das AWS API Gateway spielt dabei eine zentrale Rolle, indem es als Schnittstelle zwischen externen Anfragen und der Lambda-Funktion fungiert.

## Projektmanagement
Die gewählte Projektmanagementmethode für diese Semesterarbeit ist Kanban, eine agile Arbeitsmethode, die darauf abzielt, Arbeitsprozesse zu visualisieren und den Arbeitsfluss effektiv zu steuern. Die Entscheidung für Kanban basiert auf der Flexibilität und Anpassungsfähigkeit, die diese Methode bietet, insbesondere im Hinblick auf die Dynamik von Forschungsprojekten und Semesterarbeiten.

Um die Semesterarbeit effektiv zu verwalten, wird sie in mehrere Iterationen, auch als Sprints bekannt, unterteilt. Diese Sprints dienen dazu, den Fortschritt der Arbeit zu verfolgen, klare Ziele für bestimmte Zeiträume zu setzen und regelmäßige Überprüfungen durchzuführen. Die Aufgaben werden entsprechend priorisiert und in die Kanban-Board-Phasen wie "To-Do", "In Progress" und "Done" einsortiert, um einen klaren Überblick über den Projektstatus zu gewährleisten.

Für das Gesamtprojektmanagement wird ein Github Project verwendet ([ITCNE23-SEM-II](https://github.com/users/blro-ep/projects/6)). Github Project ermöglicht eine integrierte und kollaborative Verwaltung von Aufgaben, Issues und Milestones. Hier können nicht nur die Kanban-Boards erstellt werden, sondern auch die Fortschritte dokumentiert, Diskussionen geführt und notwendige Ressourcen bereitgestellt werden. Diese zentrale Plattform fördert die Zusammenarbeit und erleichtert die Nachverfolgung von Änderungen.

### Kanbanboard
Die Visualisierung der Arbeitsprozesse erfolgt auf einem Kanban-Board, das als zentrales Instrument für das Projektmanagement dient. Durch die Nutzung dieses Kanban-Boards wird nicht nur eine übersichtliche Darstellung sämtlicher Aufgaben ermöglicht, sondern auch das Ziel verfolgt, den Arbeitsfluss zu optimieren und die Gesamteffizienz des Projekts zu steigern.
Dies fördert nicht nur eine konsequente Arbeitsweise, sondern erleichtert auch die schnelle Identifikation von Engpässen und Bottlenecks im Arbeitsfluss.
Die effektive Nutzung dieses visuellen Instruments bildet somit einen wesentlichen Beitrag zur erfolgreichen Umsetzung der Semesterarbeit und ermöglicht eine flexible Anpassung an sich verändernde Anforderungen während des gesamten Projektablaufs.

### Roadmap
Die strategische Planung und Steuerung der Semesterarbeit erfolgt durch eine ausgearbeitete Roadmap, die wichtige Meilensteine enthält. Diese Meilensteine sind auf die einzelnen Sprints abgestimmt und dienen als Orientierungspunkte für die Fortschrittsverfolgung und den erfolgreichen Abschluss der einzelnen Etappen des Projekts.

![Roadmap](picture/roadmap.png)

| Datum | Sprint |
| --- | --- |
| 27.11.23 | Ergebnis 1. Sprint |
| 18.12.23 | Ergebnis 2. Sprint |
| 31.01.24 | Ergebnis 3. Sprint / Abgabe / Abnahem |

### Tasklist
Um die Verwaltung und Organisation der Aufgaben weiter zu optimieren, wird eine Taskliste erstellt. Die Taskliste dient dazu, die Aufgaben zu erfassen, Aufgaben nach verschiedenen Kategorien zu filtern und zu gruppieren. Ziel ist, eine höhere Übersichtlichkeit und Strukturierung innerhalb des Projektmanagements zu gewährleisten.

Die Taskliste wird so gestaltet, dass jeder Task mit spezifischen Metadaten versehen werden kann, die eine einfache Zuordnung zu bestimmten Kategorien ermöglichen. 

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
Das GitHub Repository fungiert als zentraler Speicherort für den gesamten Code der Semesterarbeit. Hier werden sämtliche Ressourcen, Skripte und Konfigurationen verwaltet. 
Zusätzlich dient das Repository als Schnittstelle für das Aktualisieren der Lambda-Funktion. Durch das Auslösen eines Git-Push-Vorgangs werden die Änderungen an der Lambda-Funktion automatisch übernommen.

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
Nach Abschluss eines Sprints wird eine Reflektion durchgeführt, die einen entscheidenden Bestandteil des agilen Projektmanagements darstellt. In diesem Prozess werden nicht nur die erreichten Fortschritte betrachtet, sondern auch Herausforderungen, Erfahrungen und mögliche Verbesserungspotenziale identifiziert. Ein zentrales Element dieser Reflexion ist die grafische Festhaltung des Status der Taskliste, was dazu dient, einen klaren Überblick über den Sprint-Verlauf zu erhalten.

#### Sprint 1 - 27.11.23
![Sprint 1](./picture/sprint-1.png)

##### Reflektion
Die von GitHub bereitgestellten Projektmanagement-Tools erweisen sich als äußerst wirkungsvoll. Die unkomplizierte Erstellung von Kanban-Boards, Roadmaps und Aufgabenlisten ermöglicht einen klaren und schnellen Überblick über den aktuellen Projektstatus.

Die Projektdokumentation wurde übersichtlich im Readme-Dateiformat festgehalten. Die bewusste Entscheidung, auf die manuelle Erstellung eines Inhaltsverzeichnisses zu verzichten, hat sich als effektiv erwiesen. Dies liegt daran, dass GitHub standardmäßig über diese Funktion verfügt und somit eine klare und strukturierte Navigation innerhalb der Dokumentation ermöglicht.

Die Erstellung von Rollen mithilfe der AWS CLI verläuft reibungslos und bildet die Grundlage für die automatisierte Erstellung der Lambda-Funktion. Die Unterscheidung, ob eine Rolle nicht existiert oder die Abfrage ein Problem aufweist, gestaltete sich aufwändiger als ursprünglich angenommen.

Die Automatisierung mittels AWS CLI wird weiterhin beibehalten.

#### Sprint 2 - 18.12.23
![Sprint 2](./picture/sprint-2.png)

**AWS Certified Cloud Practitioner**
Die Zertifizierung zum AWS Certified Cloud Practitioner hat mehr Zeit in Anspruch genommen als geplant.
Nachdem der erste Zertifizerungsversuche gescheiter war, habe ich mich mit folgenden Udemy Kursen auf die Prüfung vorbereitet [Ultimate AWS Certified Cloud Practitioner CLF-C02](https://www.udemy.com/share/103aFP3@TVzIE-KAghw3WT8BwYR3Eeg8C2WlORvf5_H3--T_a0D-fd6zdpe-7h2Lqm8TlU_vlw==/) / [6 Practice Exams | AWS Certified Cloud Practitioner CLF-C02](https://www.udemy.com/share/103e7s3@dO3_bmtPGRwYUTRlrmP7w7rLxmDDnp7NST5OVyaZiPfK12O_qLlovBH81VjxB8tEdQ==/).
Bei den Übungen hatte ich dann bemerkt, dass ich vielfach bei den selben Themen immer wieder Probleme hatte. Somit habe mir mittels [Anki](https://apps.ankiweb.net/) eine quelloffene Lernkartei-Software installerit und diese Punkte so zusätliche gelernt. 
Am 05.12.2023 konnte ich dann die Zertifizierung erfolgreich abschliessen.
[AWS Certified Cloud Practitioner certificate](./picture/AWS%20Certified%20Cloud%20Practitioner%20certificate.png)

**IaC**
Nachdem ich mich in das AWS SDK eingearbeitet hatte, entschied ich mich dazu, sämtliche Automatisierungen mit Hilfe von boto3 (Python) durchzuführen. Daher habe ich die bestehenden AWS CLI Bash-Scripts aus dem Sprint 1 direkt umgeschrieben.

Die Automatisierung mittels Boto3 gestaltete sich jedoch aufwändiger als erwartet, insbesondere aufgrund der komplexen Abhängigkeiten zwischen Lambda-Funktionen, Rollen, Richtlinien und CodeBuild. Besonders herausfordernd war die Implementierung der CodeBuild-Automatisierung. Die Dokumentation allein lieferte nicht ausreichend Klarheit darüber, welche Werte zwingend erforderlich sind und wie sie korrekt eingefügt werden müssen. In diesem Zusammenhang war es hilfreich, die Erstellung über die grafische Benutzeroberfläche durchzuführen und die Konfiguration anschließend in eine JSON-Datei zu exportieren.

Dieser Sprint war äusserst lehrreich im Kontext des Deployments mithilfe von CodeBuild und GitHub. In CodeBuild wird die Source (GitHub), das Container-Image für die Verarbeitung sowie die zu berücksichtigenden Ereignisse (Webhook) festgelegt. Eine interessante Option besteht darin, dass neben dem Ereignis (Push) auch Abhängigkeiten zur Commit-Nachricht definiert werden können. Auf diese Weise können für das Deployment spezifische Abhängigkeiten zwischen dem Ereignis und der Nachricht festgelegt werden.
Zusätzlich müssen die entsprechenden Berechtigungen (Policy/Role) vorhanden sein.

Aus den Erkenntnissen aus diesem Sprint, würde ich heute den IaC Teil direkt mit boto3 umsetzten.
Des Weiteren war die Zwei-Faktor-Authentifizierung über Microsoft Authenticator für AWS und GitHub eher lästig. Daher habe ich mich entschieden, zwei YubiKeys ([yubikey-5c-nano](https://www.yubico.com/ch/product/yubikey-5c-nano/) / [yubikey-5c-nfc](https://www.yubico.com/ch/product/yubikey-5c-nfc/)) anzuschaffen. Nach der Registrierung gestaltet sich die Anmeldung äußerst entspannt. Diese Schlüssel können zudem für verschiedene Online-Anwendungen genutzt werden.

**FaaC**
In diesem Sprint wurde mir klar, dass ich zusätzliche AWS-Komponenten benötige (API Gateway), damit die Function via Web erreichbar ist. Dies bedeutet, dass im Sprint 3 weiterhin Zeit für die Infrastruktur als Code (IaC)-Umsetzung investiert werden muss, und mir daher die Zeit für die Entwicklung von Functions as a Service (FaaS) fehlt. Es würde ein zusätlichner Issue für den Sprint 3 erfasst [AWS API Gateway](https://github.com/blro-ep/ITCNE23-SEM-II/issues/16).

Trotz dieser Herausforderung habe ich mich dazu entschieden, den Fokus auf die IaC zu legen und den FaaS-Teil so einfach wie möglich zu halten.

#### Sprint 3 - 31.01.24
** Zertifizierung AZ-900: Microsoft Azure Fundamentals **
Für die Prüfungsvorbereitung bin ich vor allem dem [Microsoft training course](https://learn.microsoft.com/en-us/training/courses/az-900t00) gefolgt und habe die offiziellen Probleprüfungen mehrmals durchgespielt [Exams AZ-900](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-900/).
![az-900-practice](./picture/az-900-practice.png)
Als züstzliche Unterstützung habe ich das Udemy Learining [az900-azure](https://www.udemy.com/course/az900-azure/) gekauft.
Die Prüfung wurde am 29.12.2023 erfolgreich absolviert [Microsoft Certified: Azure Fundamentals](https://learn.microsoft.com/api/credentials/share/en-us/RogerBlum-7482/25F3FCE9EAE61434?sharingId=965F21179058A5EF).



## Installation

### AWS CLI
Für das automatisierte Deployment wurde die AWS CLI gemäss folgender Anleitung installiert [Install or update the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#cliv2-linux-install).

### Boto3
Um das Deployment mittels Python zu automatisieren, habe ich Boto3 anhand von foldender AWS Dokumentation installiert [boto3.amazonaws.com - quickstart](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html).

## AWS Komponenten

### IAM
- [iam](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html)


### Lambda
- [lambda](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html)


### CodeBuild
- [codebuild](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html)


### API Gateway
- [apigateway](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html)

## Build Details
- Role muss vorhanden sein (Script noch nicht vorhanden)
- Lambda Role erstellen (CreateLambdaRole.py)
- Lambda Function erstellen (CreateLambdaFuction.py)
- CodeBuild Policy erstellen (CreateCodeBuildPolicy.py)
- CodeBuild Role erstellen (CreateCodeBuildRole.py)
- CodeBuild Project erstellen (CreateCodeBuildProject.py)
- CodeBuild Webhook erstellen (CreateCodeBuildWebhook.py)
- APIGateway erstellen (CreateAPIGateway.py)
- APIGateway Resource zufügen (CreateAPIGatewayResource.py)
- APIGateway Methode zufügen (PutAPIGatewayMethod.py)
- Lambda Permisson hinzufügen (AddLambdaPermission.py)

## Testing
Die Testaktivitäten umfassen die Verwendung der AWS-Konsole sowie das Testing über das Internet mithilfe von Postman.

### AWS-Konsole
#### Lambda
Nach dem Deployment kann die Funktionalität der Lambda-Funktion mithilfe der Standard-Testfunktion überprüft werden. Diese ist wie folgt zu finden.
[TestingLambdaFunction-1](./picture/TestingLambdaFunction-1.png)
[TestingLambdaFunction-2](./picture/TestingLambdaFunction-2.png)

#### CodeBuild
Nach dem Deployment kann CodeBuild durch einen GitHub-Commit getestet werden. Nach dem Commit wird der Build Run gestartet, und die einzelnen Schritte sind in den Phase Details ersichtlich.
[TestingCodeBuild-1](./picture/TestingCodeBuild-1.png)
[TestingCodeBuild-2](./picture/TestingCodeBuild-2.png)

#### API Gateway
Nach dem Deployment kann  API Gateway mithilfe der Standardfunktion überprüft werden.
[TestingAPIGateway-1](./picture/TestingAPIGateway-1.png)
[TestingAPIGateway-2](./picture/TestingAPIGateway-2.png)

### Postman
Die Lambda-Funktion kann extern über Postman getestet werden, wofür die Invoke-URL der AWS API Gateway Stages erforderlich ist.
[TestingPostmanInvokeURL](./picture/TestingPostmanInvokeURL.png)
[TestingPostmanCheck](./picture/TestingPostmanCheck.png)

## Fazit
