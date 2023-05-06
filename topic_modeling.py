import os
import csv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from textblob import TextBlob

nltk.download('stopwords')


def load_transcripts(path):
    transcripts = []
    for filename in os.listdir(path):
        if filename.endswith('.txt'):
            with open(os.path.join(path, filename), 'r') as file:
                transcripts.append(file.read())
    return transcripts


def preprocess_transcripts(transcripts):
    preprocessed = []
    stop_words = set(stopwords.words('english'))
    for transcript in transcripts:
        tokens = word_tokenize(transcript)
        filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
        preprocessed.append(filtered_tokens)
    return preprocessed


def topic_modeling(preprocessed_transcripts, n_topics=5, n_words=10):
    pass  # Implement topic modeling using nltk


def sentiment_analysis(transcripts):
    sentiment_data = []
    for transcript in transcripts:
        blob = TextBlob(transcript)
        sentiment_data.append({'polarity': blob.sentiment.polarity, 'subjectivity': blob.sentiment.subjectivity})
    return sentiment_data


def save_to_csv(topics, sentiment_data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['topic', 'word', 'sentiment', 'subjectivity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i, topic in enumerate(topics):
            for word in topic:
                writer.writerow({'topic': i, 'word': word, 'sentiment': sentiment_data[i]['polarity'], 'subjectivity': sentiment_data[i]['subjectivity']})


def main():
    transcripts_path = 'transcripts'
    transcripts = load_transcripts(transcripts_path)
    preprocessed_transcripts = preprocess_transcripts(transcripts)
    topics = topic_modeling(preprocessed_transcripts)
    sentiment_data = sentiment_analysis(transcripts)
    output_file = 'results.csv'
    save_to_csv(topics, sentiment_data, output_file)


if __name__ == '__main__':
    main()