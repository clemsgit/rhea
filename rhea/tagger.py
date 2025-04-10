from typing import List, Tuple, Dict

CATEGORIES = {
    "Kubernetes": ["kubernetes", "k8s", "helm", "pod", "cluster"],
    "GitLab": ["gitlab", "ci/cd", "pipeline", "runner", "devops"],
    "Terraform": ["terraform", "hcl", "infrastructure as code"],
    "Docker": ["docker", "container", "image", "compose"],
    "Sécurité": ["vulnérabilité", "cve", "sécu", "faille", "exploit"],
    "Cloud": ["aws", "azure", "gcp", "cloud", "s3"],
}

def classify_title(title: str) -> str:
    title_lower = title.lower()
    for category, keywords in CATEGORIES.items():
        if any(kw in title_lower for kw in keywords):
            return category
    return "Autres"

def score_title(title: str) -> int:
    title_lower = title.lower()
    score = 0
    for keywords in CATEGORIES.values():
        score += sum(1 for kw in keywords if kw in title_lower)
    return score
