import os
import logging
import numpy as np
from glob import glob
from tqdm import tqdm
from sklearn.cluster import DBSCAN
from sentence_transformers import SentenceTransformer

logging.basicConfig(level=logging.INFO)

def main(seed_file):

    files = glob("/dataset/*")

    # read files
    logging.info("Read files ...")
    corpus_sentences = []
    for file in tqdm(files):
        with open(file, "r", encoding="utf-8") as f:
            text = f.read()
            corpus_sentences.append(text)

    # embedding
    logging.info("Encode the sentences ...")
    model = SentenceTransformer("sentence-transformers/average_word_embeddings_glove.6B.300d")
    corpus_embeddings = model.encode(corpus_sentences, batch_size=1024, show_progress_bar=True, convert_to_tensor=True)

    # clustering
    logging.info("Clustering ...")
    dbscan = DBSCAN(eps=0.65, min_samples=100)
    labels = dbscan.fit_predict(corpus_embeddings)

    # the first index of each unique value in labels
    unique, counts = np.unique(labels, return_counts=True)
    label_indexes = [np.where(labels == label)[0][0] for label in unique]

    # write seed list file
    logging.info("Write seed files ...")
    seed_files = np.array(files)[label_indexes]
    with open(seed_file, "w") as f:
        for file, count in zip(seed_files, counts):
            f.write(f"{os.path.basename(file)}, {count}\n")

    logging.info("Process success!")

if __name__ == "__main__":
    try:
        main(seed_file="/workspace/seed_file.txt")
    except Exception as e:
        logging.error(f"Process failed. {e}")