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

Das Kanbanboard wir in 4 Spalten aufgeteilt
- Todo
- In Progress
- Done
- Backlog

![Kanbanboard](picture/kanban_board.png)

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

### Sprints
Das Ende von Sprint wird dokumentiert und der Stand des Kanbanboard grafisch festgehalten.

#### Sprint 1 - 27.11.23


#### Sprint 2 - 18.12.23


#### Sprint 3 - 31.01.24


## IaaC

### Installation
- [Install the AWS SDK for Python](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)
- [Code examples for SDK for Python](https://docs.aws.amazon.com/code-library/latest/ug/python_3_code_examples.html)

```
pip install boto3[crt]

sudo apt install tox

sudo apt install npm (Node Package Manager)

https://deb.nodesource.com/
```

### Credentials
~/.aws




## FaaS

## Fazit
