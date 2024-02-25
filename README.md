## Video_Summarizer

# Process Architecture

## 1. Audio Transcription from YouTube Video
- **Input**: YouTube video link
- **Output**: Transcribed text from the video
- **Steps**:
  - Import the necessary libraries (`whisper` and `pytube`).
  - Download the audio from the YouTube video.
  - Load the pre-trained `whisper` model.
  - Transcribe the audio into text using the `whisper` model.

## 2. Text Summarization
- **Input**: Transcribed text from the video
- **Output**: Summarized text highlighting important points
- **Steps**:
  - Import the `sumy` library for text summarization.
  - Tokenize the text.
  - Utilize Latent Semantic Analysis (LSA) for summarization.
  - Extract a summary of the text with a specified number of sentences.

## 3. Sentence Embedding and Clustering
- **Input**: Summarized text
- **Output**: Bullet points representing clustered similar sentences
- **Steps**:
  - Utilize `sentence_transformers` for sentence embedding.
  - Cluster the sentence embeddings using KMeans.
  - Group similar sentences together based on cluster labels.
  - Generate bullet points with appropriate indentation for each group.

## 4. File Output
- **Output**: Generated bullet points and transcription text
- **Steps**:
  - Write the generated bullet points to a text file.
  - Write the transcription text to a separate file for reference.

### Additional Requirement:
- **FFmpeg Installation**: 
  - Ensure FFmpeg is installed on the system for audio processing, which is necessary for extracting audio from the YouTube video before transcription.

# Helpful Articles

[6 Useful Text Summarization Algorithm in Python](https://medium.com/@sarowar.saurav10/6-useful-text-summarization-algorithm-in-python-dfc8a9d33074)

[Extractive Text Summarization Techniques with Sumy](https://medium.com/@ondenyi.eric/extractive-text-summarization-techniques-with-sumy-3d3b127a0a32)
