import boto3
import json

CODEBUILD_POLICY = "SemCodeBuildPolicy"
CODEBUILD_TRUST_POLICY = "CodeBuildTrustPolicy.json"

# Erstelle eine AWS Identity and Access Management (IAM)-Verbindung
iam = boto3.client('iam')

# Lese die JSON-Richtlinie aus einer Datei ein
with open(CODEBUILD_TRUST_POLICY, 'r') as json_file:
    codebuild_policy_document = json.load(json_file)

# Liste vorhandener Richtlinien
existing_policies = iam.list_policies(Scope='Local')

# Überprüfe, ob die gewünschte Richtlinie bereits existiert
policy_exists = any(policy['PolicyName'] == CODEBUILD_POLICY for policy in existing_policies['Policies'])

# Wenn die Richtlinie nicht existiert, erstelle sie
if not policy_exists:
    # Konvertiere die JSON-Richtlinie in einen String
    codebuild_policy_document_str = json.dumps(codebuild_policy_document)

    # Erstelle die IAM-Richtlinie für CodeBuild
    response = iam.create_policy(
        PolicyName=CODEBUILD_POLICY,
        PolicyDocument=codebuild_policy_document_str,
        Description='IAM Policy for AWS CodeBuild'
    )

    # Gib die ARN (Amazon Resource Name) der erstellten Richtlinie aus
    print('Die ARN der erstellten CodeBuild-Richtlinie ist:', response['Policy']['Arn'])
else:
    print(f'Die Richtlinie "{CODEBUILD_POLICY}" existiert bereits.')
