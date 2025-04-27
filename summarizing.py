from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization")

# Example text (your research paper or text to summarize)
text = """
DrylabNews for investors & friends · May 2017 Welcome to our first newsletter of 2017! It's been a while since the last one, and a lot has happened. We promise to keep them coming every two months hereafter, and permit ourselves to make this one rather long. The big news is the beginnings of our launch in the American market, but there are also interesting updates on sales, development, mentors and (of course) the investment round that closed in January.
New capital: The investment round was successful. We raised 2.13 MNOK to match the 2.05 MNOK loan from Innovation Norway. Including the development agreement with Filmlance International, the total new capital is 5 MNOK, partly tied to the successful completion of milestones. All formalities associated with this process are now finalized.
"""

# Get the summary (you can adjust the 'max_length' for longer summaries)
summary = summarizer(text, max_length=150, min_length=50, do_sample=False)

# Print the summary
print("Summary:")
print(summary[0]['summary_text'])
