from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="google/flan-t5-base"
)


def generate_answer(prompt):
    result = pipe(prompt, max_length=200)
    return result[0]["generated_text"]
