from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="distilgpt2"
)


def generate_answer(prompt):

    result = pipe(
        prompt,
        max_new_tokens=100
    )

    return result[0]["generated_text"]
