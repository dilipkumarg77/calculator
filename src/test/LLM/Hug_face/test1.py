from transformers import pipeline

classifier = pipeline("sentiment-analysis")

res = classifier("I have no strong feelings about the movie")

print (res)