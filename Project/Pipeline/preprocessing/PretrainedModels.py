from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch

from Pipeline.Lyrics_Scraping.GeniusLyricsExtraction import GeniusSongs

MODELS = {
    "Sentiment": "oliverguhr/german-sentiment-bert",
    "Toxicity": "EIStakovskii/german_toxicity_classifier_plus_v2"
}


def get_huggingface_model(model_name: str):
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    classifier = pipeline(task="sentiment-analysis", model=model, tokenizer=tokenizer)
    return classifier


def calc_sentiment_bert(songs: GeniusSongs) -> float:
    """
    Calculates the normalized avergage of the lines of the song with respect to the number of lines in a song.
    This method uses the lemmatized version of the text, which is given in a list of lines.
    Each probability of positive lines will be multiplied with value +1, each negative line with value -1, neutral
    lines take value 0 and aren't considered during calculation.

    @param songs:
    @return: normalized average of sentiment of the song
    """

    topic = "Sentiment"
    model_name = MODELS[topic]
    classifier = get_huggingface_model(model_name)
    for song in songs.song_list:
        results = [{"classifier": classifier(line)[0], "text": line} for line in song.processed_lyrics_text]
        results_filtered_pos = list(filter(lambda line: line["classifier"]["label"] == "positive", results))
        results_filtered_neg = list(filter(lambda line: line["classifier"]["label"] == "negative", results))

        avg_results_filtered_pos = sum(map(lambda x: x["classifier"]["score"], results_filtered_pos))
        avg_results_filtered_neg = sum(map(lambda x: x["classifier"]["score"], results_filtered_neg))

        return (avg_results_filtered_pos - avg_results_filtered_neg) / len(results)


def calc_sentiment_bert(songs: GeniusSongs) -> float:
    """
    Calculates the normalized avergage of the lines of the song with respect to the number of lines in a song.
    This method uses the lemmatized version of the text, which is given in a list of lines.
    Each probability of positive lines will be multiplied with value +1, each negative line with value -1, neutral
    lines take value 0 and aren't considered during calculation.

    @param songs:
    @return: normalized average of sentiment of the song
    """

    topic = "Sentiment"
    model_name = MODELS[topic]
    classifier = get_huggingface_model(model_name)
    for song in songs.song_list:
        results = [{"classifier": classifier(line)[0], "text": line} for line in song.processed_lyrics_text]
        results_filtered_pos = list(filter(lambda line: line["classifier"]["label"] == "positive", results))
        results_filtered_neg = list(filter(lambda line: line["classifier"]["label"] == "negative", results))

        avg_results_filtered_pos = sum(map(lambda x: x["classifier"]["score"], results_filtered_pos))
        avg_results_filtered_neg = sum(map(lambda x: x["classifier"]["score"], results_filtered_neg))

        song.sentiment_value = (avg_results_filtered_pos - avg_results_filtered_neg) / len(results)


def calc_toxicity(songs: GeniusSongs) -> float:
    """
    @param songs:
    @return: normalized average of sentiment of the song
    """

    topic = "Toxicity"
    model_name = MODELS[topic]
    classifier = get_huggingface_model(model_name)
    for song in songs.song_list:
        results = [{"classifier": classifier(line)[0], "text": line} for line in song.processed_lyrics_text]
        song.toxicity_value = sum(map(get_toxicity_score, results))/len(results)


def get_toxicity_score(classifier_entry):
    if classifier_entry["classifier"]["label"] == "neutral":
        return -classifier_entry["classifier"]["score"]
    else:
        return classifier_entry["classifier"]["score"]