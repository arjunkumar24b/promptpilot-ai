from .templates import CATEGORY_TEMPLATES


def detect_category(query: str) -> str:

    q = query.lower()

    programming_words = [
        "code",
        "python",
        "java",
        "c++",
        "bug",
        "leetcode",
        "algorithm"
    ]

    health_words = [
        "diet",
        "weight",
        "fat",
        "exercise",
        "gym",
        "health"
    ]

    education_words = [
        "learn",
        "study",
        "understand",
        "explain"
    ]

    career_words = [
        "resume",
        "job",
        "interview",
        "career"
    ]

    if any(word in q for word in programming_words):
        return "programming"

    if any(word in q for word in health_words):
        return "health"

    if any(word in q for word in education_words):
        return "education"

    if any(word in q for word in career_words):
        return "career"

    return "general"


def generate_tips(category: str):

    tips = {

        "programming": [
            "Include your programming language.",
            "Share error messages.",
            "Mention expected output."
        ],

        "education": [
            "Mention your current knowledge level.",
            "Specify examples you prefer."
        ],

        "health": [
            "Mention age and goals.",
            "Include relevant details."
        ],

        "career": [
            "Mention your experience level.",
            "Specify job role."
        ],

        "general": [
            "Provide more context.",
            "Mention your goal clearly."
        ]
    }

    return tips.get(category, [])


def optimize_prompt(query: str):

    category = detect_category(query)

    template = CATEGORY_TEMPLATES[category]

    optimized = template.format(query=query)

    tips = generate_tips(category)

    return category, optimized, tips