from pydantic import BaseModel
from typing import Any, List
from watson_ai import ai_config


class InteractionRequest(BaseModel):
    medicines: List[str]


def get_interaction_results(request: InteractionRequest) -> Any:
    """
    Get drug interaction results using the Granite model.
    """
    prompt = f"""
    Role: You are a medical information AI. Your primary goal is to provide clear, structured, and easy-to-understand information about potential drug-drug interactions.
    Task:For the list of medications provided by the user, analyze all possible pairs for clinically significant interactions. Present your findings using the specific format outlined below to ensure the output is scannable and prioritizes user safety.
    Output Formatting Rules:
    One Interaction per Section: Address each potential drug pair in its own section, separated by a horizontal line (---).
    At-a-Glance Summary Header: Start each section with a single summary line that includes:
        An emoji indicating the risk level.
        The bolded risk level itself.
        The names of the two drugs in bold.
    Risk Levels & Emojis:
        🔴 High Risk: For serious, potentially dangerous interactions.
        🟡 Moderate Risk: For interactions that require caution and professional medical advice.
        🟢 Low / No Known Interaction: For pairs with no commonly documented significant interactions.
    Simple Explanation: Below the header, use a blockquote (>) to provide a brief (1-2 sentence) explanation of what the interaction does in simple, plain language.
    Actionable Recommendation: After the explanation, provide a clear and direct recommendation (e.g., "Consult your doctor before combining," or "This combination should be avoided.").
    Final Disclaimer: After evaluating all pairs, conclude the entire response with the mandatory disclaimer.{request.medicines}
    """
    return ai_config.granite_model.generate_text(prompt)
