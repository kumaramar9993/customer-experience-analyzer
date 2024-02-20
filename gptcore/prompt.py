PROMPT = '''
You are tasked with developing a data analysis API capable of analyzing customer feedback. The API should be able to process feedback and extract relevant information based on predefined categories, subcategories, emotions, and sentiments.

Here is the provided lookup for predefined categories, subcategories, emotions, and sentiments
Also, issue_in_one_word,suggested_improvement_in_one_word,positive_feedback_in_one_word,negative_feedback_in_one_word - specific items are not outlined for these cases - granting you flexibility:

{  "sentiment_list": ["positive", "neutral", "negative"],
  "sentiment_score": "number between [0,1]",
  "issue_in_one_word": "unsupervised list for robustness",
  "suggested_improvement_in_one_word": "unsupervised list for robustness",
  "positive_feedback_in_one_word":  "unsupervised list for robustness",
  "negative_feedback_in_one_word": "unsupervised list for robustness",
  "emotion_list": ["happy", "satisfied", "anxious", "disappointed", "angry"],
  "emotion_score": "number between [0,1]",
  "category_subcateory_map":{"category_list": [
    "Ease of Use",
    "Payment Features",
    "Rewards and Offers",
    "Security Measures",
    "Customer Support",
    "Innovative Use Cases",
    "User Engagement",
    "Accessibility and Inclusivity",
    "Comparative Insights",
    "Future Expectations",
    "Emotional Responses",
    "Common Failures",
    "Frequent Issues"
  ],
  "categories": {
    "Ease of Use": {
      "subcategories": [
        "App Interface Design",
        "Navigation and Usability",
        "User Experience"
      ]
    },
    "Payment Features": {
      "subcategories": [
        "Money Transfers",
        "Contactless Payments",
        "Group Transactions"
      ]
    },
    "Rewards and Offers": {
      "subcategories": [
        "Reward System",
        "Cashbacks",
        "Personalization"
      ]
    },
    "Security Measures": {
      "subcategories": [
        "Transaction Security",
        "Data Privacy",
        "Authentication Processes"
      ]
    },
    "Customer Support": {
      "subcategories": [
        "Responsiveness",
        "Resolution Effectiveness",
        "Support Channels"
      ]
    },
    "Innovative Use Cases": {
      "subcategories": [
        "Unique Features",
        "App Integrations",
        "Utility Beyond Payments"
      ]
    },
    "User Engagement": {
      "subcategories": [
        "Social Features",
        "Community Engagement",
        "Gamification"
      ]
    },
    "Accessibility and Inclusivity": {
      "subcategories": [
        "Disability Access",
        "Language and Regional Adaptation",
        "Demographic Inclusivity"
      ]
    },
    "Comparative Insights": {
      "subcategories": [
        "Unique Strengths",
        "Areas for Improvement",
        "User Preference Trends"
      ]
    },
    "Future Expectations": {
      "subcategories": [
        "Desired Features",
        "Innovative Concepts",
        "Feedback on Roadmap"
      ]
    },
    "Emotional Responses": {
      "subcategories": [
        "Sentiment Analysis",
        "Satisfaction Levels",
        "Brand Loyalty"
      ]
    },
    "Common Failures": {
      "subcategories": [
        "Recurring Bugs",
        "System Downtimes",
        "Feature Limitations"
      ]
    },
    "Frequent Issues": {
      "subcategories": [
        "Payment Failures",
        "Account Issues",
        "Update Related Issues"
      ]
    }
  }
}
}

Please provide your analysis directly in JSON format, without employing Markdown code blocks or any other formatting.
Ensure that each response includes a confidence score with a two-decimal value ranging from 0 to 1, based on the analysis result.
The JSON schema should be consistent with the provided key names and include below format:
{
"review": {
    "text": "original_Review",
  },
  "sentiment_analysis": {
    "name": "positive",
    "score": 0.9
  },
  "issue_in_one_word": {
    "name": "payment method",
  },
  "suggested_improvement_in_one_word": {
    "name": "add debit card "
  },
  "positive_feedback_in_one_word": {
    "name": "Good App"
  },
"negative_feedback_in_one_word": {
    "name": "less payment method"
  },
    "topic_extraction": {
    "top1": {
      "name": "Payment Ease",
      "score": 0.9
    },
    "top2": {
      "name": "Customer Support",
      "score": 0.85
    },
    "top3": {
      "name": "Security Features",
      "score": 0.8
    }
  },
  "emotion_detection": {
    "top1": {
      "name": "satisfied",
      "score": 0.95
    },
    "top2": {
      "name": "happy",
      "score": 0.9
    },
    "top3": {
      "name": "anxious",
      "score": 0.85
    }
  },
  "categories": {
    "top1": {
      "name": "Ease of Use",
      "subcategory": {
        "name": "Navigation and Usability",
        "score": 0.95,
        "emotion_name": "happy",
        "emotion_confidence": 0.9
      }
    },
    "top2": {
      "name": "Payment Features",
      "subcategory": {
        "name": "Contactless Payments",
        "score": 0.9,
        "emotion_name": "satisfied",
        "emotion_confidence": 0.88
      }
    },
    "top3": {
      "name": "Security Measures",
      "subcategory": {
        "name": "Data Privacy",
        "score": 0.85,
        "emotion_name": "secure",
        "emotion_confidence": 0.92
      }
    }
  }
}
'''
